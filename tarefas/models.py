from django.db import models
from django.contrib.auth.models import User

PRIORIDADES = [
  ('A', 'Alta'),
  ('M', 'Média'),
  ('B', 'Baixa'),
]

class Categoria(models.Model):
  nome = models.CharField(max_length=50)
  cor = models.CharField(max_length=7, default='#000000')

  def __str__(self):
    return self.nome

class Tarefa(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField(blank=True)
  categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
  prioridade =  models.CharField(max_length=1, choices=PRIORIDADES, default='M')
  data_criacao = models.DateTimeField(null=True, blank=True)
  data_vencimento = models.DateField(null=True, blank=True)
  concluida = models.BooleanField(default=False)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.titulo

