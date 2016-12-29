from django.db import models
from medicfastv2_service_apps.auths.models.user import User
from .diagnostico import Diagnostico
from .historia import Historia
from .funcionvital import Funcionvital


class Consulta(models.Model):

    historia = models.ForeignKey(Historia)
    enfermedadactual = models.CharField(max_length=60)
    examenfisico = models.CharField(max_length=60)
    diagnostico = models.ManyToManyField(Diagnostico, blank=True)
    funcionvital = models.ForeignKey(
        Funcionvital, null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)
    suministrar = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

        permissions = (
            ('list_consulta', 'Can list consulta'),
            ('get_consulta', 'Can get consulta'),
        )

    def __str__(self):
        return self.enfermedadactual
