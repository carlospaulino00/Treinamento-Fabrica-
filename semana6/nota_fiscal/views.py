from django.shortcuts import render
from rest_framework import viewsets
from .models import PostoAtendimento 
from .serializers import PostoAtendimentoSerializer
# Create your views here

class PostoAtendimentoViewSet(viewsets.ModelViewSet):
    queryset = PostoAtendimento .objects.all()
    serializer_class = PostoAtendimentoSerializer




