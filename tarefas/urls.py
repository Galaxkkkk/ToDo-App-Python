from django.urls import path
from .views import ListaTarefasView, CriarTarefaView, EditarTarefaView, ExcluirTarefaView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', ListaTarefasView.as_view(), name='lista_tarefas'),
    path('nova/', CriarTarefaView.as_view(), name='criar_tarefa'),
    path('editar/<int:pk>/', EditarTarefaView.as_view(), name='editar_tarefa'),
    path('excluir/<int:pk>/', ExcluirTarefaView.as_view(), name='excluir_tarefa'),
]
