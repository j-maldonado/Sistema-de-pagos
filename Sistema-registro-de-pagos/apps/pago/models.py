from django.db import models

class Pago(models.Model):
    fecha_pago= models.DateField()
    mes_pago= models.CharField(max_length=7)
    id_cliente=models.ForeignKey('cliente.Cliente', on_delete=models.DO_NOTHING, verbose_name='Cliente', related_name='pagos')
    
