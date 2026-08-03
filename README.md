# Tiny Clientes

Projeto simples para:

- ler um arquivo CSV de clientes;
- importar os dados para um banco local;
- abrir uma pagina web para pesquisa e visualizacao.

## Stack

- `Flask`
- `SQLAlchemy`
- `SQLite` por padrao
- `PostgreSQL` opcional via `DATABASE_URL`

## Como rodar

1. Criar um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Importar o CSV para o banco:

```bash
python csv_importer.py
```

4. Subir a aplicacao:

```bash
flask --app app run --debug
```

Abra `http://127.0.0.1:5000`.

## Banco padrao

Sem configurar nada, o projeto cria o arquivo local `clientes.db`.

## PostgreSQL opcional

Se quiser usar PostgreSQL local no WSL, crie um arquivo `.env` com algo assim:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/clientes
CSV_FILE=/mnt/c/Projetos/tiny_clientes/contatos_unificado.csv
```

Depois rode novamente:

```bash
python csv_importer.py
flask --app app run --debug
```

## Filtros da tela

- busca por nome, fantasia, documento, email e telefone;
- filtro por estado;
- filtro por cidade;
- paginacao de resultados;
- resumo com totais e ranking por estado.
