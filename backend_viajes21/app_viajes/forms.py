
from django import forms
from .models import (
    Vuelo, Alojamiento, Paquete_Turistico, Cliente_Viajes, 
    Agente_Viajes, Reserva_Viaje, Destino
)

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'

class VueloForm(forms.ModelForm):
    fecha_salida = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_llegada = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Vuelo
        fields = '__all__'

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = '__all__'

class PaqueteForm(forms.ModelForm):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Paquete_Turistico
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    fecha_registro = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Cliente_Viajes
        fields = '__all__'

class AgenteForm(forms.ModelForm):
    fecha_contratacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Agente_Viajes
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    fecha_reserva = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_vencimiento_pago = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reserva_Viaje
        fields = '__all__'

