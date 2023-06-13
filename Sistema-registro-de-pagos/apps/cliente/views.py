from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Cliente
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente.html'
    context_object_name = 'clientes'
    success_url = reverse_lazy('clientes')

@method_decorator(login_required, name='dispatch') 
class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'client_form.html'
    fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento','email']
    success_url = reverse_lazy('clientes')

@method_decorator(login_required, name='dispatch')
class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'cliente_detalle.html'
    context_object_name = 'clientes'
    success_url = reverse_lazy('clientes')

@method_decorator(login_required, name='dispatch')
class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'client_form.html'
    fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento','email']
    success_url = reverse_lazy('clientes')

@method_decorator(login_required, name='dispatch')
class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('clientes')