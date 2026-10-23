---
version: alpha
name: EG Engenharia
description: >-
  Identidade visual do sistema da EG Engenharia — site egenharia.com.br,
  portal do cliente e app financeiro. Derivada da marca pessoal Erika
  Barros. Terracota sobre bege, superfícies brancas que flutuam com sombra
  quente, números sempre tabulares.
colors:
  # Terracotas — a mesma cor da marca em três papéis (ver "Colors")
  primary: "#CD6543"
  primary-button: "#B8532F"
  primary-text: "#A84A28"
  on-primary: "#FFFFFF"
  secondary: "#E6A87D"
  tertiary: "#E2BCA8"
  # Fundos e superfícies
  background: "#E6DCCE"
  background-light: "#F4EFE9"
  surface: "#FFFFFF"
  on-surface: "#2A1B14"
  on-surface-muted: "#6B5E55"
  border-subtle: "#E9E2D8"
  # Subtons — terracota misturada ao branco
  subtone-50: "#FCF6F4"
  subtone-100: "#F9EDE8"
  subtone-200: "#F4DDD6"
  subtone-300: "#ECC4B8"
  # Neutros (R=G=B)
  white: "#FFFFFF"
  neutral-50: "#FAFAFA"
  neutral-100: "#F4F4F4"
  neutral-200: "#E8E8E8"
  neutral-300: "#D4D4D4"
  neutral-400: "#A3A3A3"
  neutral-500: "#737373"
  neutral-600: "#525252"
  neutral-700: "#3A3A3A"
  neutral-800: "#262626"
  neutral-900: "#171717"
  black: "#0A0A0A"
typography:
  headline-display:
    fontFamily: Plus Jakarta Sans
    fontSize: 46px
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: -0.025em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.06em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
  button-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
  button-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 19px
    fontWeight: 700
    lineHeight: 1.25
  data-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    fontFeature: '"tnum"'
  data-md:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    fontFeature: '"tnum"'
rounded:
  sm: 10px
  icon: 14px
  md: 16px
  lg: 24px
  xl: 32px
  full: 9999px
spacing:
  card-padding: 32px
  touch-target: 44px
  artboard-mobile: 390px
components:
  button-primary:
    backgroundColor: "{colors.primary-button}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 26px
    height: 44px
  button-tonal:
    backgroundColor: "{colors.subtone-100}"
    textColor: "{colors.primary-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 26px
    height: 44px
  button-tonal-hover:
    backgroundColor: "{colors.subtone-100}"
    textColor: "{colors.primary-text}"
  button-light:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-surface}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    height: 44px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: 32px
  chip:
    backgroundColor: "{colors.subtone-100}"
    textColor: "{colors.primary-text}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    height: 44px
  list-row-selected:
    backgroundColor: "{colors.subtone-50}"
    textColor: "{colors.on-surface}"
---

# EG Engenharia

Fonte única da identidade visual do sistema da EG. Os valores do bloco YAML acima são a
norma; o texto abaixo diz **por que** são esses e **quando** usar cada um.
Os mesmos valores, como variáveis CSS (`--eb-*`), estão em `tokens.css`;
`sincronizar-tokens.py --verificar` falha se os dois divergirem.

## Overview

**Engenharia de precisão com calor humano.** A marca junta o rigor técnico
da construção civil (obra, orçamento, prazo, número que tem de bater) à
fluidez de um software bem feito. Público: clientes de obra e reforma,
construtoras parceiras e a equipe que lança o financeiro no dia a dia.

A sensação buscada é a de um **instrumento confiável**: claro, calmo,
legível no sol da obra, sem enfeite gratuito. A terracota dá a assinatura;
o bege e o branco dão o ar. Imagens: arquitetura moderna, concreto
aparente, madeira e aço, canteiro organizado, maquete 3D.

Superfícies: site institucional (`egenharia.com.br`), portal do cliente e
app financeiro (Flutter, `portal.egenharia.com.br`), documentos e PDFs.

### EG e EB — duas marcas

- **EG Engenharia** — a empresa (sociedade da Erika com o marido) e o
  sistema que ela opera: site, portal do cliente, app financeiro. É a
  marca **deste arquivo**.
- **EB — Erika Barros** — a marca pessoal da engenheira, criada pela
  **Alegria Design** (2022, contratada pela Erika). Fica em `../eb/`.

A EG não nasceu do zero: **a paleta, a terracota e o tom vieram da EB** e
foram ampliados aqui (subtons, neutros, elevação, regras de contraste).
A Erika é engenheira da EG, então a EB aparece dentro da EG — na
assinatura técnica, no "Sobre", no CREA —, mas as duas não se confundem:
peça da empresa leva a marca EG; peça pessoal da engenheira leva a EB.

**Logo da EG: ainda não existe.** Até existir, site e app usam o
**símbolo EB como provisório** (`../eb/logos/`). Ao criar o logo da EG,
trocar nos dois e registrar aqui.

## Colors

A paleta nasce de uma cor só, a **terracota**, e se abre em três papéis,
porque branco sobre `#CD6543` dá só 3,79:1 e reprova texto normal (AA
pede 4,5:1).

| Token | Valor | Papel | Contraste |
|---|---|---|---|
| `primary` | `#CD6543` | a marca: ícone, borda, gradiente, gráfico. **Nunca leva texto** | branco 3,79 ✗ |
| `primary-button` | `#B8532F` | superfície com **texto branco** em cima (botão, badge) | branco 4,87 ✓ |
| `primary-text` | `#A84A28` | terracota como **letra**: link, botão tonal, secundário | branco 5,71 · subtone-100 4,98 ✓ |
| `secondary` | `#E6A87D` | acento: ícone, ponta do gradiente, anel de foco | — |
| `tertiary` | `#E2BCA8` | hover, superfície secundária, botão claro do app | `on-surface` 9,48 ✓ |

**Fundos e texto.** `background` (`#E6DCCE`, bege) é o chão do app;
`background-light` para telas densas e listas; `surface` (branco) nos
cards. O texto do produto é o marrom `on-surface` (`#2A1B14`, ~10,5:1 no
bege) e o secundário `on-surface-muted` (`#6B5E55`, ~4,6:1).

**Subtons** (`subtone-50` a `300`): terracota misturada ao branco, para
superfície clara com identidade — fundo de ícone, chip, botão tonal,
linha selecionada. 50–200 aceitam os dois textos; **300 só aceita
`on-surface`** (o muted dá 3,92) — use como borda ou enfeite.

**Neutros** (`neutral-50` a `900`, `white`, `black`): cinza de verdade
(R=G=B) para o que não deve ter cor — tabela de dados, divisória, ícone
neutro, desabilitado, documento. Como texto: **500+ no branco, 600+ no
bege** (o 500 dá 4,74 no branco e 3,50 no bege). Cinza é frio: rende
melhor sobre card branco do que direto no bege.

**Gradientes** (em `tokens.css`; o formato não tem token de gradiente):

| Variável | Valor | Aceita texto? |
|---|---|---|
| `--eb-gradiente` (vivo) | `#CD6543 → #E6A87D`, 120° | **não** — nenhuma cor passa nas duas pontas |
| `--eb-gradiente-botao` | `#BD5733 → #A84A28`, 180° | **branco** (4,59 → 5,71) |
| `--eb-gradiente-suave` / `-card` / `-fundo` | subtons e bege | **escuro** (`on-surface`) |

Badge com texto ("Premium", "Mais solicitado") usa o gradiente do botão,
nunca o vivo.

### Preset B — Industrial

Alternativa escura escolhida **por projeto** (reformas de alto padrão,
peças institucionais), não o modo escuro do Preset A. Ativada com
`data-preset="industrial"` no `<html>`; valores completos em `tokens.css`.
Fundo `#2A1B14`, card `#3A2820`, texto `#FAF8F5`, muted `#A89F91`,
terracota como texto `#E08A64` (5,31 no card). Subtons misturados ao card,
não ao branco. Dados em IBM Plex Mono. **Medido por script, ainda não
conferido em tela.**

## Typography

Duas famílias, com papéis que não se misturam:

- **Plus Jakarta Sans** (alternativa: Outfit) — títulos, texto, rótulos,
  botões. Geométrica, firme, com bom desenho em peso alto.
- **Inter com `tabular-nums`** — **todo número**: valor, porcentagem,
  m², data, saldo, simulador. Sem algarismo tabular os dígitos dançam
  quando o valor muda, e este produto é número mudando na tela.

No título de abertura, a frase de efeito pode ir em **serifa itálica**
(Georgia ou equivalente, peso 400): "Engenharia de precisão para
*transformar sua obra*." É o único uso de serifa.

| Token | Uso |
|---|---|
| `headline-display` | título de abertura (hero), 1 por tela |
| `headline-lg` | título de seção ou de tela |
| `headline-md` | título de card |
| `body-md` | texto corrido, 52 a 70 caracteres por linha |
| `body-sm` | apoio, legenda |
| `label-md` | rótulo em caixa alta (sobrelinha de seção, chip) |
| `label-sm` | rótulo de campo, nota de rodapé |
| `button-md` / `button-lg` | botão padrão / CTA grande |
| `data-lg` / `data-md` | número em destaque / número em tabela |

## Layout

**Mobile-first.** Desenha-se em 390 pt de largura (prancheta do app) e
expande-se. Alvo de toque mínimo de **44 × 44** — todos os botões e
campos têm 44 de altura mínima. Card com 32 de folga interna (24 no
celular). Grade em **Bento**: cards de tamanhos diferentes que se
encaixam, com o mesmo canto e o mesmo espaço entre eles.

A escala de espaçamento completa **ainda não está decidida** — espera o
canvas do app mostrar o que se repete. Até lá, múltiplos de 4.

## Elevation & Depth

O efeito "flutuando" é a assinatura das superfícies. Cada nível tem
**duas sombras**: uma curta e marrom (contato — onde o objeto encosta) e
uma longa e terracota (ambiente — a luz quente que ele rebate), esta com
*spread* negativo para ficar embaixo e não vazar para os lados. **Sombra
cinza ou preta apaga a marca.**

| Nível | Nome | Onde | Valor (`--eb-elevacao-N`) |
|---|---|---|---|
| 1 | repouso | cards em grade, tiles de lista, chips | `0 1px 2px rgba(42,27,20,.06), 0 4px 12px -2px rgba(205,101,67,.08)` |
| 2 | destaque | card principal, input em foco | `0 2px 4px rgba(42,27,20,.05), 0 12px 28px -6px rgba(205,101,67,.14)` |
| 3 | flutuante | botão, navbar em ilha, FAB, hover | `0 4px 8px rgba(42,27,20,.06), 0 20px 40px -10px rgba(205,101,67,.22)` |
| 4 | sobreposição | modal, folha inferior, popover, menu | `0 8px 16px rgba(42,27,20,.08), 0 32px 64px -16px rgba(205,101,67,.30)` |

- Aresta de luz no topo da superfície branca: `inset 0 1px 0 rgba(255,255,255,.7)`.
- **Vidro** (navbar, modal, menu): fundo bege translúcido,
  `backdrop-filter: blur(12px)`, borda de 1 px branca a 50%.
- **Ruído**: textura `feTurbulence` a 4% de opacidade sobre a página.
- **Movimento**: quem flutua sobe 2 px no hover e pega a sombra do nível
  seguinte; afunda no toque; desabilitado perde a sombra. Curva
  `cubic-bezier(0.25, 0.46, 0.45, 0.94)`, 220 ms.

## Shapes

Cantos suaves, nunca vivos. Escala: `sm` 10 (chip, tag) · `icon` 14
(tile de ícone 44–48, quase *squircle*) · `md` 16 (botão, input, linha) ·
`lg` 24 (card) · `xl` 32 (bloco grande, folha inferior, modal) · `full`
(pílula, avatar).

**Concentricidade:** canto de dentro = canto de fora − folga entre eles.
Card 24 com folga 8 → filho 16. Sem isso o canto "morde".

## Components

- **Botão primário** (`button-primary`): `primary-button` com texto
  branco, peso 600, altura 44, elevação 3 e halo terracota
  (`0 10px 24px -8px rgba(184,83,47,.55)`). Pode usar o gradiente do
  botão no lugar da cor chapada. Um por tela.
- **Botão tonal** (`button-tonal`): subtom com letra `primary-text`. Ação
  secundária. No hover **o fundo não muda** — no `subtone-200` a letra
  cai para 4,40:1 e reprova; o retorno é o movimento (sobe 2 px, elevação 2).
- **Botão claro** (`button-light`): `tertiary` com letra marrom — padrão
  do **app financeiro**, por preferência por tons claros (9,48:1). Nele,
  os **estados ativos** (caixa marcada, interruptor, foco, carregando)
  usam `primary`, porque o claro some no branco.
- **Card** (`card`): branco, canto 24, folga 32, elevação 1 (2 se for o
  principal).
- **Chip** (`chip`): subtom com letra terracota, canto 10.
- **Input** (`input`): branco, canto 16, altura 44; no foco, anel de 2 px
  em `secondary` e elevação 2. Rótulo flutuante.
- **Linha selecionada** (`list-row-selected`): fundo `subtone-50`.
- **Navbar em ilha**: pílula flutuante centralizada, transparente no
  topo; ao rolar vira vidro.
- **Número**: sempre `data-*`, alinhado à direita em tabela.

Peças de referência renderizadas em `componentes/` (cores, tipografia,
botões, elevação).

## Do's and Don'ts

- **Faça:** texto branco só sobre `primary-button`, `--eb-gradiente-botao`
  ou mais escuro.
- **Faça:** terracota como letra sempre em `primary-text` (`#A84A28`).
- **Faça:** `tabular-nums` em todo valor numérico.
- **Faça:** sombras com o par marrom + terracota da tabela de elevação.
- **Faça:** confira contraste (mínimo 4,5:1 para texto, 3:1 para ícone e
  borda de componente) antes de criar combinação nova.
- **Não faça:** texto sobre `primary` (`#CD6543`) — 3,79:1.
- **Não faça:** texto sobre o gradiente vivo, de cor nenhuma.
- **Não faça:** cinza 500 como texto sobre o bege (3,50:1).
- **Não faça:** sombra cinza/preta no Preset A, nem canto vivo.
- **Não faça:** tratar o Preset B como modo escuro automático.
- **Não faça:** recolorir, distorcer ou pôr sombra no símbolo.
- **Não faça:** usar a marca EB como se fosse a da empresa — o símbolo EB
  no site e no app é provisório, até a EG ter logo próprio.
