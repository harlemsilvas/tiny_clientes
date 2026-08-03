# Tiny Clientes

Aplicacao web simples para importar um arquivo CSV de clientes para um banco local e consultar os dados por uma interface web.

## Preview

Painel de busca:

![Painel de clientes](docs/images/dashboard-preview.svg)

Tela de cadastro e edicao:

![Formulario de cliente](docs/images/client-form-preview.svg)

## O que o projeto faz

- importa clientes de um arquivo CSV;
- salva os dados em `SQLite` por padrao;
- permite usar `PostgreSQL` via `DATABASE_URL`;
- oferece busca, filtros e paginacao;
- permite visualizar, editar, criar e excluir cadastros.

## Stack

- `Python 3`
- `Flask`
- `SQLAlchemy`
- `SQLite`
- `PostgreSQL` opcional

## Estrutura

```text
.
|-- app.py
|-- csv_importer.py
|-- models.py
|-- config.py
|-- requirements.txt
|-- run.sh
|-- templates/
|-- static/
`-- .env.example
```

## Execucao rapida

No WSL ou Linux:

```bash
chmod +x run.sh
./run.sh
```

O script:

- cria `.venv` se necessario;
- instala dependencias se estiverem faltando;
- importa o CSV para o banco se `clientes.db` ainda nao existir;
- sobe a aplicacao em `http://127.0.0.1:5000`.

## Execucao manual

1. Criar ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Importar o CSV:

```bash
python csv_importer.py
```

4. Subir a aplicacao:

```bash
flask --app app run --debug
```

## Configuracao

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Exemplo:

```env
DATABASE_URL=sqlite:////mnt/c/Projetos/tiny_clientes/clientes.db
CSV_FILE=/mnt/c/Projetos/tiny_clientes/contatos_unificado.csv
SECRET_KEY=tiny-clientes-local
```

## Banco padrao

Sem configuracao extra, o projeto usa `SQLite` local no arquivo `clientes.db`.

Para o volume atual de cerca de `12.500` clientes, `SQLite` atende bem para uso local com filtros e CRUD simples.

## PostgreSQL opcional

Se quiser usar PostgreSQL local no WSL:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/clientes
CSV_FILE=/mnt/c/Projetos/tiny_clientes/contatos_unificado.csv
SECRET_KEY=tiny-clientes-local
```

Depois rode:

```bash
python csv_importer.py
flask --app app run --debug
```

## Funcionalidades

- busca por nome, fantasia, documento, email e telefone;
- filtro por estado;
- filtro por cidade;
- pagina de detalhe do cliente;
- criacao, edicao e exclusao de cadastro;
- resumo com totais e ranking por estado.

## Observacoes

- os arquivos CSV, banco local e assets de referencia estao fora do versionamento pelo `.gitignore`;
- o importador tenta lidar com pequenas inconsistencias de formato no CSV.
- os previews versionados em `docs/images/` sao ilustracoes limpas para o GitHub, separadas dos assets brutos locais.
