from django.db import models
from .consulta import Consulta
from ..enumstiposeguro import SEGURO_TIPO_CHOICES, CLINICA


class Derivacion(models.Model):

    consulta = models.OneToOneField(Consulta)
    destino = models.CharField(max_length=30, null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now=True)
    tipo = models.CharField(
        max_length=50, choices=SEGURO_TIPO_CHOICES, default=CLINICA)

    class Meta:
        verbose_name = "Derivacion"
        verbose_name_plural = "Derivacions"
        permissions = (
            ('list_derivacion', 'Can list derivacion'),
            ('get_derivacion', 'Can get derivacion'),
        )

    def __str__(self):
        return self.destino
