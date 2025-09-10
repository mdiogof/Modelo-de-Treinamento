from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Trilha, Etapa, Ligacao
from .serializers import TrilhaSerializer, EtapaSerializer, LigacaoSerializer

class TrilhaViewSet(viewsets.ModelViewSet):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer


class EtapaViewSet(viewsets.ModelViewSet):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer

    @action(detail=True, methods=['post'])
    def marcar_assistido(self, request, pk=None):
        etapa = self.get_object()
        etapa.assistido = True
        etapa.save()
        return Response({'status': 'conteúdo marcado como assistido'}, status=status.HTTP_200_OK)


class LigacaoViewSet(viewsets.ModelViewSet):
    queryset = Ligacao.objects.all()
    serializer_class = LigacaoSerializer