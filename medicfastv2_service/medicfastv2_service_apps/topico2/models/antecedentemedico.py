from django.db import models


class Antecedentemedico(models.Model):

    archivo = models.FileField(upload_to='media/')
    estado = models.BooleanField(default=True)
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Antecedentemedico"
        verbose_name_plural = "Antecedentemedicos"
        permissions = (
            ('list_antecedentemedico', 'Can list antecedentemedico'),
            ('get_antecedentemedico', 'Can get antecedentemedico'),
        )

    def __str__(self):
        return self.nombre
