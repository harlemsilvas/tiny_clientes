# Continuacao do Projeto

Este documento serve para retomar o trabalho do projeto com contexto rapido, estado atual e proximos passos recomendados.

## Leitura obrigatoria na retomada

Ao reiniciar o trabalho neste projeto:

1. Ler este arquivo `CONTINUATION.md`
2. Ler `CLAUDE.md`

O `CLAUDE.md` registra a metodologia e a forma esperada de conduzir o trabalho.

## Estado atual

Data desta anotacao: `2026-08-03`

Projeto pronto com:

- importacao de CSV para banco local;
- uso de `SQLite` por padrao;
- opcao de `PostgreSQL` via `DATABASE_URL`;
- listagem com busca, filtros e paginacao;
- tela de detalhe do cliente;
- criacao, edicao e exclusao de cadastro;
- `run.sh` para execucao local;
- `README.md` melhorado para GitHub;
- previews em `docs/images/`;
- changelog e nota de release inicial.

## Git e GitHub

Repositorio remoto:

- `git@github.com:harlemsilvas/tiny_clientes.git`

Branch principal:

- `main`

Tags:

- `v0.1.0`

Ultimos commits relevantes:

- `5114a4f` - Criacao inicial da aplicacao com CRUD
- `892df6c` - Melhora da documentacao e preparacao da release inicial

## Arquivos importantes

- `README.md`
- `run.sh`
- `app.py`
- `csv_importer.py`
- `models.py`
- `templates/`
- `static/`
- `docs/releases/v0.1.0.md`
- `CHANGELOG.md`

## Proximos passos sugeridos

1. Criar a release no GitHub com:

```bash
gh release create v0.1.0 --title "v0.1.0" --notes-file docs/releases/v0.1.0.md
```

2. Melhorar a UX do formulario:

- mensagens de sucesso e erro apos salvar ou excluir;
- mascaras para CPF/CNPJ, CEP e telefone;
- validacoes de campos obrigatorios;
- refinamento visual da tela de detalhe.

3. Evoluir a parte funcional:

- exportacao de resultados filtrados para CSV;
- aba real de cobranca separada do endereco principal;
- ordenacao por colunas;
- filtros mais ricos por status, segmento e vendedor.

4. Melhorar a operacao local:

- opcionalmente criar `Makefile`;
- opcionalmente adicionar comando para reimportar o CSV com seguranca;
- documentar melhor o fluxo com PostgreSQL local.

## Observacoes importantes

- `assets/`, `csv/`, `*.csv`, `.env` e `clientes.db` estao fora do versionamento;
- os previews em `docs/images/` sao ilustracoes limpas para o GitHub;
- no ambiente de sandbox do agente, o servidor Flask pode falhar ao abrir porta mesmo com o projeto correto;
- para retomar bem o trabalho, comecar sempre por `CONTINUATION.md` e `CLAUDE.md`.
