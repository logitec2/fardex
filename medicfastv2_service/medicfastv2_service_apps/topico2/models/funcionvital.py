from django.db import models


class Funcionvital(models.Model):

    frecuenciacardiaca = models.CharField(max_length=3)
    frecuenciarespiratoria = models.FloatField()
    imc = models.CharField(max_length=60)
    masacorporal = models.FloatField()
    peso = models.FloatField()
    presionarterial = models.FloatField()
    talla = models.FloatField()
    temperatura = models.FloatField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Funcionvital"
        verbose_name_plural = "Funcionvitals"
        permissions = (
            ('list_funcionvital', 'Can list funcionvital'),
            ('get_funcionvital', 'Can get funcionvital'),
        )

    def __str__(self):
        return self.frecuenciacardiaca
