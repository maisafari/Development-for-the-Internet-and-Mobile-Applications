from datetime import timezone, datetime

from django.contrib.auth.models import User
from django.db import models


from django.db import models

class Questao(models.Model):
    questao_texto = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.questao_texto

    def foi_publicada_recentemente(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)
class Opcao(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    opcao_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcao_texto

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curso = models.CharField(max_length=50)
    votos = models.IntegerField(max_length=20, default=0)
    limite = models.IntegerField(max_length=20, default=0)
    grupo = models.CharField(max_length=20)




    def __str__(self):
        return self.user.username


class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    votos = models.IntegerField(max_length=20, default=0)

    limite = models.IntegerField(max_length=20, default=100)
    grupo = models.CharField(max_length=20, default='admin')



    def __str__(self):
         return self.user.username