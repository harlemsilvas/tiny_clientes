# TODO

Checklist curta para retomar a execucao do projeto.

## Antes de qualquer coisa

- [ ] Ler `CONTINUATION.md`
- [ ] Ler `CLAUDE.md`
- [ ] Conferir `git status`

## Publicacao imediata

- [ ] Criar a release `v0.1.0` no GitHub:

```bash
gh release create v0.1.0 --title "v0.1.0" --notes-file docs/releases/v0.1.0.md
```

## Melhorias de UX

- [ ] Adicionar mensagens de sucesso e erro apos salvar
- [ ] Adicionar confirmacao visual apos excluir
- [ ] Aplicar mascaras em CPF/CNPJ, CEP e telefone
- [ ] Melhorar validacoes de campos obrigatorios

## Melhorias funcionais

- [ ] Exportar resultados filtrados para CSV
- [ ] Criar aba real de cobranca separada do endereco principal
- [ ] Permitir ordenacao por colunas na listagem
- [ ] Adicionar filtros por status, segmento e vendedor

## Operacao e manutencao

- [ ] Melhorar documentacao de PostgreSQL local
- [ ] Considerar `Makefile` para facilitar comandos
- [ ] Criar fluxo seguro para reimportacao do CSV

## Ao finalizar uma proxima rodada

- [ ] Atualizar `CHANGELOG.md`
- [ ] Atualizar `CONTINUATION.md`
- [ ] Criar commit local
- [ ] Fazer `git push`
