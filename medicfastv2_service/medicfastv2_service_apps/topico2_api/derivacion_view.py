from rest_framework import serializers, viewsets
#from django.db.models import Q
#from operator import __or__ as OR
#from functools import reduce

from medicfastv2_service_apps.topico2.models.derivacion import Derivacion


class DerivacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Derivacion
        fields = '__all__'
        # fields = ('id', 'codigo', 'nombre', 'estado',)
        # read_only_fields = ('id',)
        # exclude = ('users',)


class DerivacionViewSet(viewsets.ModelViewSet):
    queryset = Derivacion.objects.all()
    serializer_class = DerivacionSerializer
