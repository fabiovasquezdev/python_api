# Python API - Portfolio Project

API RESTful, desenvolvida com FastAPI e PostgreSQL.

## Requisitos do Sistema

- Python 3.8+
- Docker e Docker Compose
- PostgreSQL (via Docker)

## Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd python-api
```

2. Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o ambiente:

   1. Crie um arquivo `.env` na raiz do projeto:
   ```bash
   touch .env
   ```

   2. Adicione as variáveis de ambiente:
   ```env
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/python_api
   ```

   3. Configure o banco de dados:
   ```bash
   docker-compose up -d
   ```

5. Execute a aplicação:

   1. Ative o ambiente virtual (se ainda não estiver ativo):
   ```bash
   source venv/bin/activate  # Linux/Mac
   # ou
   .\venv\Scripts\activate  # Windows
   ```

   2. Inicie o servidor de desenvolvimento:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

A API estará disponível em:
- Local: `http://localhost:8000`
- Rede: `http://seu-ip:8000`

## Documentação da API

A documentação interativa da API está disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Estrutura do Projeto

```
python-api/
├── app/
│   ├── database/
│   │   └── session.py
│   │   
│   ├── models/
│   │   └── user.py
│   │   
│   ├── repository/
│   │   └── user.py
│   │   
│   ├── routers/
│   │   └── user.py
│   │   
│   ├── schemas/
│   │   └── user.py
│   │   
│   ├── services/
│   │   └── user.py
│   │   
│   └── main.py
│   
├── docker-compose.yml
│   
├── requirements.txt
│   
└── README.md
```


## Comandos Úteis

### Gerenciamento do Ambiente Virtual
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Desativar ambiente virtual
deactivate
```

### Docker
```bash
# Iniciar containers
docker-compose up -d

# Parar containers
docker-compose down

# Ver logs
docker-compose logs -f
```

### Desenvolvimento
```bash
# Instalar dependências
pip install -r requirements.txt

# Atualizar dependências
pip freeze > requirements.txt

# Executar testes
pytest
``` 