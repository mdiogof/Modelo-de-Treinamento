## 📌 Exemplos de uso da API

### 1️⃣ Criar uma Trilha

```
POST /trilhas/
{
  "titulo": "Trilha de Python",
  "descricao": "Aprenda Python do básico ao avançado"
}
```

### 2️⃣ Criar uma Etapa vinculada a uma Trilha

```
POST /etapas/
{
  "trilha": 1,
  "titulo": "Introdução ao Python",
  "descricao": "Primeiros passos com a linguagem",
  "ordem": 1,
  "links": [
      "https://docs.python.org/3/tutorial/",
      "https://www.youtube.com/watch?v=rfscVS0vtbw"
      ],
  "assistido": false
}
```

### 3️⃣ Criar uma Ligação vinculada a uma Etapa

```
POST /ligacoes/
{
  "etapa": 1,
  "nome": "Mentor João",
  "telefone": "+55 11 99999-8888",
  "duracao": "00:30:00"
}
```

### 4️⃣ Listar Trilhas

    GET /trilhas/
Resposta (exemplo):
```
[
  {
    "id": 1,
    "titulo": "Trilha de Python",
    "descricao": "Aprenda Python do básico ao avançado"
  }
]
```

### 5️⃣ Marcar Etapa como assistida

```
PATCH /etapas/1/
{
  "assistido": true
}
```