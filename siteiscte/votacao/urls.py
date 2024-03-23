from django.urls import include, path
from . import views
app_name = 'votacao'

urlpatterns = [
    path("", views.index, name='index'),
    # ex: votacao/1
    path("<int:questao_id>", views.detalhe,
         name='detalhe'),
    path('<int:questao_id>/resultados', views.resultados,
         name='resultados'),

    path('<int:questao_id>/voto', views.voto,
         name='voto'),
    path('votacao/criarquestao/', views.criar_questao, name='criarquestao'),

    path('<int:questao_id>/criaropcao/', views.criar_opcao, name='criaropcao'),

    path('<int:questao_id>/remover/', views.remover_questao, name='remover_questao'),


]