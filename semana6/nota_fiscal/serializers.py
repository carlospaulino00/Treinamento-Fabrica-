from rest_framework import serializers
from .models import PostoAtendimento 


class PostoAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostoAtendimento 
        fields = ['id', 'nome','cpf', 'combustivel','quantidade','valorPago']


