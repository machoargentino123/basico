from django.db import models

# Create your models here.


class Prueba(models.Model):
    Luz = models.IntegerField(primary_key=True)
    encendido = models.BooleanField(default=False)
    Ip = models.GenericIPAddressField(protocol='IPv4',default='0.0.0.0')
    descripcion = models.CharField(max_length=100,default='A determinar')
    def __str___(self):
        return self.title


class Logger(models.Model):
    luz = models.CharField(max_length=20,default='0')
    df = models.CharField(max_length=20,default='0')
    ram = models.CharField(max_length=20,default='0')
    wifi_ip = models.CharField(max_length=20,default='0')
    created_on = models.DateTimeField(auto_now_add=True)

