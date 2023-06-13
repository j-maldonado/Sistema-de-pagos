from django.db import models

class Usuario(models.Model):
    usuario= models.CharField(max_length=100)
    contrasenia= models.CharField(max_length=100)
    def __str__(self):
        return self.usuario+self.contrasenia
        
    