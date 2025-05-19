from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DeleteView
from .models import Tarefa
from .forms import TarefaForm
from django.contrib import messages
from django.conf import settings

class ListaTarefasView(LoginRequiredMixin, ListView):
  login_url = settings.LOGIN_URL
  model = Tarefa
  template_name = 'tarefas/lista_tarefas.html'
  context_object_name = 'tarefas'

  def get_queryset(self):
    status = self.request.GET.get('status')
    qs = Tarefa.objects.filter(usuario=self.request.user)
    if status == 'concluidas':
      qs = qs.filter(concluida=False)
    elif status == 'pendentes':
      qs = qs.filter(concluida=True)
    return qs.order_by('data_vencimento', 'prioridade')
  
class CriarTarefaView(LoginRequiredMixin, CreateView):
  login_url = settings.LOGIN_URL
  model = Tarefa
  form_class = TarefaForm
  template_name = 'tarefas/form_tarefa.html'
  success_url = reverse_lazy('lista_tarefas')

  def form_valid(self, form):
    form.instance.usuario = self.request.user
    messages.success(self.request, 'Tarefa criada com sucesso!')
    return super().form_valid(form)
  
class EditarTarefaView(LoginRequiredMixin, UpdateView):
  login_url = settings.LOGIN_URL
  model = Tarefa
  form_class = TarefaForm
  template_name = 'tarefas/form_tarefa.html'
  success_url = reverse_lazy('lista_tarefas')

class ExcluirTarefaView(LoginRequiredMixin, DeleteView):
  login_url = settings.LOGIN_URL
  model = Tarefa
  template_name = 'tarefas/excluir_tarefa.html'
  success_url = reverse_lazy('lista_tarefas')

  def delete(self, request, *args, **kwargs):
    messages.success(self.request, 'Tarefa excluída com sucesso!')
    return super().delete(request, *args, **kwargs)
