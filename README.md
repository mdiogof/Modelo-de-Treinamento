# 📚 API de Trilhas de Aprendizado

Este projeto é uma **API em Django + Django REST Framework** para gerenciar **trilhas de aprendizado**, suas **etapas** e as **ligações** relacionadas.  
O sistema permite criar, visualizar, atualizar e excluir informações (CRUD), além de algumas funcionalidades extras como marcar etapas como assistidas.

---

## 🚀 Funcionalidades

- **Trilhas**:
  - Criar novas trilhas
  - Listar todas as trilhas
  - Visualizar detalhes de uma trilha específica (incluindo etapas vinculadas)
  - Atualizar ou excluir trilhas existentes

- **Etapas**:
  - Criar etapas vinculadas a uma trilha
  - Listar todas as etapas
  - Visualizar detalhes de uma etapa específica
  - Atualizar ou excluir etapas
  - Marcar etapa como **assistida**

- **Ligações**:
  - Criar ligações associadas a uma etapa
  - Listar todas as ligações
  - Visualizar detalhes de uma ligação específica
  - Atualizar ou excluir ligações

---

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Swagger](https://swagger.io/) (para documentação interativa)
- [VS Code](https://code.visualstudio.com/)

---

## 📦 Estrutura da API

A API segue o padrão REST, com endpoints disponíveis para **Trilhas**, **Etapas** e **Ligações**.

### 🔹 Endpoints principais

#### Trilhas (`/api/trilhas/`)
- `POST /trilhas/` → Criar uma trilha
- `GET /trilhas/` → Listar todas as trilhas
- `GET /trilhas/{id}/` → Visualizar uma trilha
- `PUT/PATCH /trilhas/{id}/` → Atualizar uma trilha
- `DELETE /trilhas/{id}/` → Deletar uma trilha

#### Etapas (`/api/etapas/`)
- `POST /etapas/` → Criar uma etapa vinculada a uma trilha
- `GET /etapas/` → Listar todas as etapas
- `GET /etapas/{id}/` → Visualizar uma etapa
- `PUT/PATCH /etapas/{id}/` → Atualizar uma etapa
- `DELETE /etapas/{id}/` → Deletar uma etapa
- `POST /etapas/{id}/marcar_assistido/` → Marcar uma etapa como assistida 

#### Ligações (`/api/ligacoes/`)
- `POST /ligacoes/` → Criar uma ligação associada a uma etapa
- `GET /ligacoes/` → Listar todas as ligações
- `GET /ligacoes/{id}/` → Visualizar uma ligação
- `PUT/PATCH /ligacoes/{id}/` → Atualizar uma ligação
- `DELETE /ligacoes/{id}/` → Deletar uma ligação

---

## ▶️ Como executar o projeto

1. Clone o repositório:
   ```
   git clone https://github.com/mdiogof/Modelo-de-Treinamento.git
   cd Modelo-de-Treinamento
   ```
2. Crie e ative um ambiente virtual
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências
   ```
   pip install -r requirements.txt
   ```
4. Execute as migrações
   ```
   python manage.py migrate
   ```
5. Inicie o servidor
   ```
   python manage.py runserver
   ```
6. Acesse o link gerado no navegador:  
    - http://127.0.0.1:8000/ -> página inicial
    - http://127.0.0.1:8000/swagger/ -> documentação swagger
    - http://127.0.0.1:8000/api/ -> API root

---

### 📌 Observações

- Os dados cadastrados ficam apenas em memória (SQLite local).
Sempre que reiniciar o servidor, os dados serão resetados caso não esteja usando um banco persistente.
- A documentação Swagger facilita o uso da API sem precisar de ferramentas externas como Postman.  

---

#### 📖 Veja exemplos de requisições no arquivo [API_EXAMPLES.md](API_EXAMPLES.md).