from django import forms
from .models import Tarefa, Categoria

class TarefaForm(forms.ModelForm):
  class Meta:
    model = Tarefa
    fields = ['titulo', 'descricao', 'categoria', 'prioridade', 'data_criacao', 'concluida']
    widgets = {
      'data_vencimento': forms.DateInput(attrs={'type': 'date'})
    }
