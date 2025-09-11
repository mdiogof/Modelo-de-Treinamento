# Create your tests here
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import timedelta
from .models import Trilha, Etapa, Ligacao

# -----------------------------
# Testes para Trilhas
# -----------------------------
class TrilhaAPITest(APITestCase):
    def test_criar_trilha(self):
        data = {"titulo": "Trilha de Python", "descricao": "Aprendendo do básico ao avançado"}
        response = self.client.post("/api/trilhas/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["titulo"], "Trilha de Python")

    def test_listar_trilhas(self):
        Trilha.objects.create(titulo="Trilha de Django", descricao="Framework web")
        response = self.client.get("/api/trilhas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_trilha(self):
        trilha = Trilha.objects.create(titulo="Trilha Antiga", descricao="Descricao antiga")
        data = {"titulo": "Trilha Atualizada", "descricao": "Descricao atualizada"}
        response = self.client.put(f"/api/trilhas/{trilha.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["titulo"], "Trilha Atualizada")

    def test_deletar_trilha(self):
        trilha = Trilha.objects.create(titulo="Trilha Teste", descricao="Descricao teste")
        response = self.client.delete(f"/api/trilhas/{trilha.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# -----------------------------
# Testes para Etapas
# -----------------------------
class EtapaAPITest(APITestCase):
    def setUp(self):
        self.trilha = Trilha.objects.create(titulo="Trilha JS", descricao="Frontend e Backend")

    def test_criar_etapa(self):
        data = {
            "titulo": "Introdução ao JS",
            "descricao": "Conceitos básicos",
            "ordem": 1,
            "trilha": self.trilha.id,
            "links": []
        }
        response = self.client.post("/api/etapas/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["trilha"], self.trilha.id)

    def test_atualizar_etapa(self):
        etapa = Etapa.objects.create(
            titulo="Etapa Antiga",
            descricao="Descricao antiga",
            ordem=1,
            trilha=self.trilha
        )
        data = {
            "titulo": "Etapa Atualizada",
            "descricao": "Descricao atualizada",
            "ordem": 2,
            "trilha": self.trilha.id,
            "links": []
        }
        response = self.client.put(f"/api/etapas/{etapa.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["titulo"], "Etapa Atualizada")

    def test_deletar_etapa(self):
        etapa = Etapa.objects.create(titulo="Etapa Teste", descricao="Descricao teste", ordem=1, trilha=self.trilha)
        response = self.client.delete(f"/api/etapas/{etapa.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_marcar_assistido(self):
        etapa = Etapa.objects.create(titulo="Etapa Assistir", descricao="Descricao", ordem=1, trilha=self.trilha, assistido=False)
        data = {"assistido": True}
        response = self.client.patch(f"/api/etapas/{etapa.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["assistido"])


# -----------------------------
# Testes para Ligações
# -----------------------------
class LigacaoAPITest(APITestCase):
    def setUp(self):
        self.trilha = Trilha.objects.create(titulo="Trilha Redes", descricao="Conceitos de redes")
        self.etapa = Etapa.objects.create(
            titulo="Camada de Aplicação",
            descricao="HTTP, DNS",
            ordem=1,
            trilha=self.trilha
        )

    def test_criar_ligacao(self):
        data = {"nome": "Ligação 1", "telefone": "123456789", "duracao": timedelta(minutes=30), "etapa": self.etapa.id}
        response = self.client.post("/api/ligacoes/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["etapa"], self.etapa.id)

    def test_atualizar_ligacao(self):
        ligacao = Ligacao.objects.create(nome="Ligação Antiga", telefone="111111111", duracao=timedelta(minutes=15), etapa=self.etapa)
        data = {
            "nome": "Ligação Atualizada",
            "telefone": "222222222",
            "duracao": timedelta(minutes=20),
            "etapa": self.etapa.id  # <- corrigido
        }
        response = self.client.put(f"/api/ligacoes/{ligacao.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], "Ligação Atualizada")

    def test_deletar_ligacao(self):
        ligacao = Ligacao.objects.create(nome="Ligação Teste", telefone="333333333", duracao=timedelta(minutes=10), etapa=self.etapa)
        response = self.client.delete(f"/api/ligacoes/{ligacao.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
