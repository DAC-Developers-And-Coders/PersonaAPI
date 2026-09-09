# API de Personas em Python + HTML/CSS/JS Front-End

API em Python com FastAPI, com orientação a objetos, banco de dados e front-end.

## Estrutura

```text
├── api-backend/
|   ├── Model/
|   |    ├── Arcana.py
|   |    ├── Database.py
|   |    ├── Elemento.py
|   |    └── Persona.py
|   ├── Routers/
|   |    ├── arcanas.py
|   |    ├── elementos.py
|   |    └── personas.py
|   ├── Utils/
|   |    └── default_values.py
|   ├── main.py
|   ├── controller.py
|   ├── service.py
|   ├── requirements.txt
|   └── personadb.db
├── front-end/
|   ├── fonts/
|   ├── images/
|   ├── script/
|   |    └── script.js
|   ├── style/
|   |    └── style.css
|   └── index.html
└── README.md
```

## Instalação da API - na pasta api-backend

```bash
python -m venv .venv
```
#### OU
```bash
py -m venv .venv
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

Front-End:

```text
http://localhost:8000/docs
```

API:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

## Endpoints - PERSONAS

### POST `/personas`

```json
{
  "nome": "string",
  "origem": "string",
  "primeira_aparicao": "string",
  "classe": "string",
  "nivel_inicial": 0,
  "arcana_id": 0,
  "elemento_id": 0
}
```

### GET `/personas`

Lista todas as personas.

### GET `/personas/{id}`

Busca uma persona pelo ID.

### PUT `/personas/{id}`

Atualiza os dados da persona.

### DELETE `/personas/{id}`

Deleta os dados da persona.

### PATCH `/personas/{id}/{attribute}`

Atualiza um atributo da persona.

### HEAD `/personas`

Verifica se existem personas.

### HEAD `/personas/{id}`

Verifica se uma persona existe.

### OPTIONS `/personas`

Verifica as opções de request HTML disponíveis.

## Endpoints - ELEMENTOS

### GET `/elementos`

Lista todos os elementos.

### GET `/elementos/{id}`

Busca um elemento pelo ID (1 - 11).

### HEAD `/elementos`

Verifica se existem elementos.

### HEAD `/elementos/{id}`

Verifica se um elemento existe.

### OPTIONS `/elementos`

Verifica as opções de request HTML disponíveis.

## Endpoints - ARCANAS

### GET `/arcanas`

Lista todas as arcanas.

### GET `/arcanas/{id}`

Busca uma arcana pelo ID (0 - 21).

### HEAD `/arcanas`

Verifica se existem arcanas.

### HEAD `/arcanas/{id}`

Verifica se uma arcana existe.

### OPTIONS `/arcanas`

Verifica as opções de request HTML disponíveis.
