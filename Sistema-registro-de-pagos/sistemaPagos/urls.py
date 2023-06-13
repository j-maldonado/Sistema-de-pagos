"""
URL configuration for sistemaPagos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, user_login, user_signup, user_logout
from apps.cliente.views import ClienteList, ClienteCreate, ClienteDelete, ClienteDetail, ClienteUpdate
from apps.pago.views import PagosList,PagosIngresar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ingresar/', user_login, name='login'),
    path('registrar/', user_signup, name='signup'),
    path('salir/', user_logout, name='logout'),
    path('clientes/', ClienteList.as_view(), name='clientes'),
    path('cliente/create/', ClienteCreate.as_view(), name='create'),
    path('cliente/<int:pk>/detail/',ClienteDetail.as_view(), name='detail'),
    path('cliente/<int:pk>/update/', ClienteUpdate.as_view(), name='update'),
    path('cliente/<int:pk>/delete/', ClienteDelete.as_view(), name='delete'),
    path('cliente/<int:id>/pagos/', PagosList.as_view(), name='pagos'),
    path('pagos/ingresar/', PagosIngresar.as_view(), name='pagosIngresar'),
]
