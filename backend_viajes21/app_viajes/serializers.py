from rest_framework import serializers
from .models import (
    Destino, Paquete_Turistico, Cliente_Viajes, Reserva_Viaje, 
    Vuelo, Alojamiento, Agente_Viajes
)

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

class Paquete_TuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete_Turistico
        fields = '__all__'

class Cliente_ViajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente_Viajes
        fields = '__all__'

class Reserva_ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva_Viaje
        fields = '__all__'

class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = '__all__'

class AlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alojamiento
        fields = '__all__'

class Agente_ViajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente_Viajes
        fields = '__all__'
