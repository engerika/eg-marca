---
version: alpha
name: EB — Erika Barros
description: >-
  Marca pessoal da engenheira Erika Barros, identidade da Alegria Design
  (2022). Símbolo das iniciais E e B entrelaçadas, paleta de quatro tons
  terrosos e tipografia Prompt.
colors:
  primary: "#CD6543"
  secondary: "#E6A87D"
  tertiary: "#E2BCA8"
  neutral: "#E6DCCE"
  ink: "#000000"
  paper: "#FFFFFF"
typography:
  display:
    fontFamily: Prompt
    fontWeight: 700
  headline:
    fontFamily: Prompt
    fontWeight: 500
  body:
    fontFamily: Prompt
    fontWeight: 400
  light:
    fontFamily: Prompt
    fontWeight: 300
omitted:
  - section: spacing
    reason: O manual da agência não define grid de página nem espaçamento.
  - section: rounded
    reason: O manual não define cantos; a forma da marca é o traço do símbolo.
  - section: components
    reason: Identidade gráfica, sem componentes de interface.
---

# EB — Erika Barros

Marca pessoal da Erika Barros como engenheira. Fonte: **manual de
identidade da Alegria Design** (2022, contratada pela Erika), resumido
aqui. O manual completo e os arquivos de trabalho (AI, EPS, fontes)
ficam guardados fora deste repositório — ver `README.md`.

A EB é a **origem** da EG Engenharia (`../eg/DESIGN.md`): as quatro cores
abaixo são exatamente a base da paleta da EG. Mas são marcas diferentes —
peça pessoal da engenheira leva EB; peça da empresa e do sistema leva EG.

## Overview

**Áreas de atuação** definidas no projeto: engenharia, mentorias e
produção de conteúdo.

**Palavras-chave:** exclusivo, único, moderno, dinâmico, destaque,
deslumbrante, respeito.

**Conceito (da agência):** identidade **atemporal**, que conversa com
públicos de todas as idades. O símbolo nasce das iniciais **E** e **B**,
entrelaçadas. Paleta elegante, de tons claros e neutros, com **um acento
cromático** para dar contraste. A padronagem é feita do próprio símbolo
e dá dinamismo.

### Versões da marca

| Versão | Cores permitidas | Arquivos |
|---|---|---|
| **Símbolo** (monograma EB) | **todas as cores da paleta**, preto e branco | `marca/simbolo/` |
| **Marca tipográfica horizontal** ("ERIKA BARROS" em uma linha) | **só preto ou branco** | `marca/tipografica/horizontal-*` |
| **Marca tipográfica vertical** ("ERIKA" sobre "BARROS") | **só preto ou branco** | `marca/tipografica/vertical-*` |

- Preto em fundo claro, branco em fundo escuro.
- **Não aplicar em cores fora da paleta.** Sempre com bom contraste com o
  fundo, seja liso, foto ou estampa.
- **Grid fixo:** não mudar espaço entre letras ou palavras, não distorcer.
- **Margem de segurança:** **1/3 da largura da marca** de cada lado e
  **1/3 da altura** em cima e embaixo, livre de outros elementos.
- Vetor em PDF (`*-vetor.pdf`); PNG sem fundo para uso digital.

### Padronagem e elementos gráficos

- **Padronagem** (`padronagem/`): o símbolo espelhado e repetido em
  grade de quatro. Pode ser aplicada em qualquer cor da paleta — em fotos
  para redes sociais, papelaria etc.
- **Símbolo em traço fino** (`elementos/`): elemento gráfico de fundo, em
  qualquer cor da paleta. No manual aparece grande, sobre foto, em
  transparência.

## Colors

Quatro cores, do mais claro ao acento (valores do manual):

| Token | Nome | HEX | CMYK |
|---|---|---|---|
| `neutral` | bege | `#E6DCCE` | 12 13 20 00 |
| `tertiary` | terracota suave | `#E2BCA8` | 11 29 33 01 |
| `secondary` | terracota clara | `#E6A87D` | 09 40 53 01 |
| `primary` | terracota (o acento) | `#CD6543` | 16 69 75 04 |

`ink` (preto) e `paper` (branco) são os das versões P&B da marca.

**Combinações do símbolo mostradas no manual**, com o contraste medido
(o mínimo para elemento gráfico é 3:1; para texto, 4,5:1):

| Fundo | Símbolo | Contraste |
|---|---|---|
| bege | terracota | 2,80 |
| terracota clara | bege | 1,51 |
| terracota suave | preto | 11,99 |
| terracota | terracota suave | 2,17 |

Três das quatro ficam abaixo de 3:1: são combinações **decorativas**, boas
para símbolo grande, padronagem e fundo. Para a marca **ser lida** —
pequena, em tela, em documento —, prefira preto ou branco com contraste.

Os PNGs da agência têm desvio de um ponto (`#E6DDCE`, `#E6A97D`,
`#CE6643`) — exportação; vale o valor do manual.

## Typography

**Prompt** (Cadson Demak, Google Fonts, licença aberta OFL), em quatro
pesos: **Light 300, Regular 400, Medium 500, Bold 700**. Pela regra da
agência, é a fonte de **todos** os textos, títulos e frases das peças da
marca — papelaria, site, folders, orçamentos, cartão de visitas.

- Instalar: [fonts.google.com/specimen/Prompt](https://fonts.google.com/specimen/Prompt).
- A marca tipográfica ("ERIKA BARROS") **não** é escrita em Prompt: é
  desenho fixo, usar sempre o arquivo. O manual não nomeia a fonte dela.
- O manual não define tamanhos — só a família e os pesos.

Nas aplicações de exemplo do manual: títulos em caixa alta e peso alto,
texto corrido em Regular/Light, e o nome com letras espaçadas
("e r i k a b a r r o s") como assinatura em redes sociais.

## Components

O manual não define componentes de interface. Os exemplos de aplicação
são peças gráficas: posts e stories (frase, pergunta, checklist, texto,
foto com título), destaques do Instagram, capa de material, papelaria,
assinatura de e-mail.

## Do's and Don'ts

- **Faça:** use o símbolo em qualquer cor da paleta; a marca tipográfica,
  só em preto ou branco.
- **Faça:** respeite a margem de 1/3 ao redor da marca.
- **Faça:** use Prompt em todo texto das peças da EB.
- **Faça:** para a marca ser lida em tamanho pequeno, preto ou branco.
- **Não faça:** recolorir a marca fora da paleta.
- **Não faça:** mudar o espaçamento das letras, distorcer, redesenhar.
- **Não faça:** reescrever "ERIKA BARROS" em outra fonte no lugar do
  arquivo da marca.
- **Não faça:** usar a EB como marca da empresa EG — no sistema EG o
  símbolo EB é provisório, até a EG ter logo próprio.
