FROM python:3.12

# Instalando Poetry
RUN pip install poetry

# Copiar o código fonte da aplicação
COPY . /api_crud

# Definir diretório de trabalho
WORKDIR /api_crud

# Instalar dependências com poetry
RUN poetry install

# Expor a porta da aplicação
EXPOSE 8501

# Definir entrypoint para executar o servidor uvicorn
ENTRYPOINT [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8501"]