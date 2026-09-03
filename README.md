# API de Usuários

API simples em Python com FastAPI, sem orientação a objetos e sem banco de dados.
Os dados são representados por dicionários/listas e persistidos em `usuarios.json`.

## Estrutura

```text
api_usuarios/
├── main.py
├── controller.py
├── service.py
├── usuarios.json
├── requirements.txt
└── README.md
```

O `main.py` cria a aplicação e registra o `router` do controller.
O `controller.py` concentra as rotas HTTP.
O `service.py` contém a lógica e a persistência no arquivo JSON.

## Instalação

```bash
python -m venv .venv
```

Windows:

```bash
.venv\\Scripts\\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Subir o servidor

```bash
uvicorn main:app --reload
```

API:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

## Endpoints

### POST `/usuarios`

```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "idade": 30
}
```

### GET `/usuarios`

Lista todos os usuários.

### GET `/usuarios/{id}`

Busca um usuário pelo ID.

### PUT `/usuarios/{id}`

Atualiza os dados do usuário.

```json
{
  "nome": "João Santos",
  "email": "joao.santos@email.com",
  "idade": 31
}
```

### DELETE `/usuarios/{id}`

Exclui o usuário pelo ID.
