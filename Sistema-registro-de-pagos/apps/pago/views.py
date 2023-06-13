from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Pago
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from apps.cliente.models import Cliente

@method_decorator(login_required, name='dispatch')
class PagosList(ListView):
    model = Cliente
    template_name = 'cliente_pagos.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        id_pago = self.kwargs['id']
        return super().get_queryset().filter(id=id_pago)
    
    success_url = reverse_lazy('clientes')

@method_decorator(login_required, name='dispatch')
class PagosIngresar(CreateView):
    model = Pago
    template_name = 'pago_form.html'
    fields = ['fecha_pago', 'mes_pago', 'id_cliente']
    success_url = reverse_lazy('clientes')
