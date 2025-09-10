from rest_framework import serializers
from .models import Trilha, Etapa, Ligacao

class LigacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligacao
        fields = ['id', 'etapa', 'nome', 'telefone', 'duracao']

class EtapaSerializer(serializers.ModelSerializer):
    ligacoes = LigacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Etapa
        fields = ['id', 'trilha', 'titulo', 'descricao', 'links', 'assistido', 'ordem', 'ligacoes']

class TrilhaSerializer(serializers.ModelSerializer):
    etapas = EtapaSerializer(many=True, read_only=True)

    class Meta:
        model = Trilha
        fields = ['id', 'titulo', 'descricao', 'etapas']