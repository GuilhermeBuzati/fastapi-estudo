Instale o fastpi no pip

-   pip install fastapi

Instale o  ASGI server

-   pip install "uvicorn[standard]"


Crie um arquivo inicial na raiz do projeto. De exemplo, irei utilizar o "main.py"

Execute a aplicação

-   uvicorn main:app --reload

Detalhado

-   uvicorn NOME_ARQUIVO_INICIAL:NOME_VARIAVEL_FAST_API --reload


Documentação automatica criada com SWAGGER em "localhost:8000/docs/"