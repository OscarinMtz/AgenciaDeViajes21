from django.urls import path
from .views import (
    index,
    # Destino
    destino_list, destino_create, destino_update, destino_delete,
    # Paquete
    paquete_list, paquete_create, paquete_update, paquete_delete,
    # Cliente
    cliente_list, cliente_create, cliente_update, cliente_delete,
    # Reserva
    reserva_list, reserva_create, reserva_update, reserva_delete,
    # Vuelo
    vuelo_list, vuelo_create, vuelo_update, vuelo_delete,
    # Alojamiento
    alojamiento_list, alojamiento_create, alojamiento_update, alojamiento_delete,
    # Agente
    agente_list, agente_create, agente_update, agente_delete
)

# Rutas del sitio web
urlpatterns = [
    path('', index, name='index'),
    
    # Rutas para Destinos
    path('destinos/', destino_list, name='destino_list'),
    path('destinos/nuevo/', destino_create, name='destino_create'),
    path('destinos/<int:pk>/editar/', destino_update, name='destino_update'),
    path('destinos/<int:pk>/eliminar/', destino_delete, name='destino_delete'),

    # Rutas para Paquetes Turísticos
    path('paquetes/', paquete_list, name='paquete_list'),
    path('paquetes/nuevo/', paquete_create, name='paquete_create'),
    path('paquetes/<int:pk>/editar/', paquete_update, name='paquete_update'),
    path('paquetes/<int:pk>/eliminar/', paquete_delete, name='paquete_delete'),

    # Rutas para Clientes
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/nuevo/', cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', cliente_delete, name='cliente_delete'),

    # Rutas para Reservas
    path('reservas/', reserva_list, name='reserva_list'),
    path('reservas/nuevo/', reserva_create, name='reserva_create'),
    path('reservas/<int:pk>/editar/', reserva_update, name='reserva_update'),
    path('reservas/<int:pk>/eliminar/', reserva_delete, name='reserva_delete'),

    # Rutas para Vuelos
    path('vuelos/', vuelo_list, name='vuelo_list'),
    path('vuelos/nuevo/', vuelo_create, name='vuelo_create'),
    path('vuelos/<int:pk>/editar/', vuelo_update, name='vuelo_update'),
    path('vuelos/<int:pk>/eliminar/', vuelo_delete, name='vuelo_delete'),

    # Rutas para Alojamientos
    path('alojamientos/', alojamiento_list, name='alojamiento_list'),
    path('alojamientos/nuevo/', alojamiento_create, name='alojamiento_create'),
    path('alojamientos/<int:pk>/editar/', alojamiento_update, name='alojamiento_update'),
    path('alojamientos/<int:pk>/eliminar/', alojamiento_delete, name='alojamiento_delete'),

    # Rutas para Agentes
    path('agentes/', agente_list, name='agente_list'),
    path('agentes/nuevo/', agente_create, name='agente_create'),
    path('agentes/<int:pk>/editar/', agente_update, name='agente_update'),
    path('agentes/<int:pk>/eliminar/', agente_delete, name='agente_delete'),
]
