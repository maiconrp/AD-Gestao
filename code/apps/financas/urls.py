from django.urls import path
from .views import *

urlpatterns = [
    path('saidas/adicionar/', adicionar_saida, name='adicionar_saida'),
    path('saidas/gerar_relatorio/', gerar_relatorio, name='gerar_relatorio'),
    path('saidas/excluir/<uuid:saida_id>/', excluir_saida, name='excluir_saida'),
    path('saidas/listar/', listar_saida, name='listar_saida'),
    path('saidas/detalhar/<uuid:saida_id>/', detalhar_saida, name='detalhar_saida'),
    path('saidas/editar/<uuid:saida_id>/', editar_saida, name='editar_saida'),
    path('entradas/dizimos/adicionar/', adicionar_dizimo, name='adicionar_dizimo'),
    path('entradas/gerar_relatorio/', gerar_relatorio, name='gerar_relatorio'),
    path('entradas/dizimos/excluir/<uuid:dizimo_id>/', excluir_dizimo, name='excluir_dizimo'),
    path('entradas/dizimos/listar/', listar_dizimos, name='listar_dizimos'),
    path('entradas/dizimos/detalhar/<uuid:dizimo_id>/', detalhar_dizimo, name='detalhar_dizimo'),
    path('entradas/dizimos/editar/<uuid:dizimo_id>/', editar_dizimo, name='editar_dizimo'),
]