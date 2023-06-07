from django.db import models


class PostoAtendimento(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()
    combustivel = models.CharField(max_length=50)
    quantidade = models.FloatField()
    valorPago = models.FloatField()

    def __str__(self):
        return self.nome
