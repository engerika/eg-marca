# eg-marca

Identidade visual da **EG Engenharia** e da marca pessoal **EB — Erika
Barros**, num lugar só, cada uma na sua pasta.

| Pasta | Marca | O que tem |
|---|---|---|
| [`eg/`](eg/) | **EG Engenharia** — a empresa e o sistema (site, portal do cliente, app) | `DESIGN.md`, `tokens.css`, componentes de referência |
| [`eb/`](eb/) | **EB — Erika Barros** — marca pessoal da engenheira (Alegria Design, 2022) | `DESIGN.md` (resumo do manual), símbolo, marca tipográfica, padronagem, elementos (PNG e PDF vetor) |

A paleta da EG **veio da EB** e foi ampliada. As duas não se confundem:
peça da empresa leva EG, peça pessoal da engenheira leva EB.

## `eg/DESIGN.md`

Segue o formato aberto [DESIGN.md](https://github.com/google-labs-code/design.md)
(Google Labs, versão *alpha*): tokens em YAML no topo, explicação em
Markdown embaixo. Ferramentas de IA de design (Claude Design, Stitch e
outras) leem esse arquivo direto. Títulos de seção em inglês, porque o
formato os reconhece por nome; o texto é em português.

Conferir o arquivo (formato, referências e contraste WCAG):

```bash
npx @google/design.md lint eg/DESIGN.md
```

```bash
npx @google/design.md lint eb/DESIGN.md
```

Os avisos `orphaned-tokens` (cor que nenhum componente usa) são
esperados: subtons e cinzas existem para quem desenha, não só para os
componentes declarados.

## Manter EG em sincronia

O mesmo valor mora em três lugares, de propósito: `DESIGN.md` (para
ferramentas de IA), `tokens.css` (para código) e o bloco repetido em cada
preview de `componentes/` (para renderizar isolado). Depois de mexer em
qualquer cor ou canto:

```bash
python3 eg/sincronizar-tokens.py              # reescreve os previews
python3 eg/sincronizar-tokens.py --verificar  # só confere, sai 1 se divergir
```

O `DESIGN.md` é editado à mão; o script só aponta a diferença.

## Quem usa

- [`eg-site`](https://github.com/engerika/eg-site) — `egenharia.com.br`
- `eg-app` — portal do cliente e app financeiro (Flutter)

## Licença

Código (`.css`, `.py`, `.html`) livre para consulta. **Marcas, nomes e
logos são de propriedade da EG Engenharia e da Erika Barros** — não
podem ser usados por terceiros.
