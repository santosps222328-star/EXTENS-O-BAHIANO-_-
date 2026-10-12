# Central de idiomas — BAHIANO UI

Este pacote prepara o repositório de traduções para integração futura com a extensão. **Ainda não conecta nem altera a extensão.**

## Idiomas
- `pt-BR` Português (Brasil), idioma-base
- `en-US` Inglês (Estados Unidos)
- `pt-PT` Português (Portugal)
- `ru` Russo
- `zh-CN` Chinês simplificado
- `ja` Japonês
- `id` Indonésio
- `de` Alemão

## Arquivos
- `languages-index.json`: catálogo dos idiomas.
- `languages-<código>.json`: traduções por idioma.
- `languages-template.json`: modelo de referência.
- `scripts/validate-translations.py`: verifica chaves, placeholders e traduções pendentes.
- `.github/workflows/validate-translations.yml`: executa o verificador no GitHub Actions.

## Como atualizar
1. Adicione a nova chave ao arquivo `languages-pt-BR.json`.
2. Adicione a mesma chave aos outros idiomas.
3. Envie os arquivos para o GitHub.
4. Abra a aba **Actions** para ver o relatório.

As strings com `[NEEDS TRANSLATION]` são avisos explícitos e farão a validação falhar até serem traduzidas. Isso evita marcar traduções incompletas como prontas.

## Segurança e limitações
Os JSON contêm texto, não código para executar. Na integração, valide o formato e insira as strings como texto; não use `innerHTML` para conteúdo remoto. O verificador detecta inconsistências estruturais, não garante qualidade linguística. As traduções deste pacote são um ponto de partida e ainda precisam ser revistas.
