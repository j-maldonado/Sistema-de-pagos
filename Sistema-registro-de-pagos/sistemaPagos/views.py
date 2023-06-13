from django.shortcuts import render, redirect
from .forms import RegisterUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@login_required (login_url='login')
def home(request):
    context={
        'USER':request.user}
    return render(request=request, template_name='index.html', context=context)
    

def user_login(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('clientes')
        else:
            messages.info(request, 'Usuario o password incorrecto')

    context={'USER':request.user}
    return render(request=request, template_name='login.html', context=context)

def user_signup(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Registro exitoso para ' + username)
            return redirect('login')
    else:
        form = RegisterUser()
    context = {
        "form": form,
        "page_heading": "Registrar",
        "USER": request.user
    }
    return render(request=request, template_name='signup.html', context=context)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')



