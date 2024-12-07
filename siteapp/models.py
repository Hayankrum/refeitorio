from django.db import models
from PIL import Image
import os

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome_aluno = models.CharField(max_length=255, null=False)
    matricula_aluno = models.CharField(max_length=255, null=False)
    foto_aluno = models.ImageField(upload_to='alunos/', blank=True, null=True)  # Imagens de alunos vão para a pasta 'alunos/'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.foto_aluno:  # Verifica se há uma foto antes de tentar abrir
            im = Image.open(self.foto_aluno.path)
            novo_tamanho = (40, 40)  # Tamanho para o qual a imagem será redimensionada
            im.thumbnail(novo_tamanho)
            im.save(self.foto_aluno.path)  # Salva a imagem redimensionada

    def foto_url(self):
        if self.foto_aluno and hasattr(self.foto_aluno, 'url'):
            return self.foto_aluno.url
        else:
            return self.nome_aluno

    def __str__(self):
        return self.nome_aluno

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nome_evento = models.CharField(max_length=255, null=False)
    foto_evento = models.ImageField(upload_to='eventos/', blank=True, null=True)  # Imagens de eventos vão para a pasta 'eventos/'
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column="id_aluno")

    def __str__(self):
        return self.nome_evento
