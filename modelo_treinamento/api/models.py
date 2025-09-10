from django.db import models

#create your models here
class Trilha(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class Etapa(models.Model):
    trilha = models.ForeignKey(Trilha, related_name='etapas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    links = models.JSONField(default=list)  # lista de URLs
    assistido = models.BooleanField(default=False)
    ordem = models.PositiveIntegerField()  # ordem sequencial da etapa

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return f"{self.titulo} - {self.trilha.titulo}"


class Ligacao(models.Model):
    etapa = models.ForeignKey(Etapa, related_name='ligacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    duracao = models.DurationField()  # duração da ligação

    def __str__(self):
        return f"{self.nome} - {self.etapa.titulo}"