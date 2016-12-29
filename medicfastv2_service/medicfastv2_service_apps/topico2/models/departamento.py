from django.db import models


class Departamento(models.Model):

    codigo = models.CharField(max_length=25)
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        permissions = (
            ('list_departamento', 'Can list departamento'),
            ('get_departamento', 'Can get departamento'),
        )

    def __str__(self):
        return self.nombre
