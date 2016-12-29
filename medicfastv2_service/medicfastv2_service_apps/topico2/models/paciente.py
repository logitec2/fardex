from django.db import models
from .departamento import Departamento
from medicfastv2_service_apps.auths.models.person import Person
from medicfastv2_service_apps.auths.models.hierarchy import Hierarchy

# Create your models here.


class Paciente(models.Model):

    codigo = models.CharField(max_length=12)
    persona = models.ForeignKey(Person)
    jerarquia = models.ForeignKey(Hierarchy)
    departamento = models.ForeignKey(Departamento, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

        permissions = (
            ('list_paciente', 'Can list paciente'),
            ('get_paciente', 'Can get paciente'),
        )

    def __str__(self):
        return self.codigo
