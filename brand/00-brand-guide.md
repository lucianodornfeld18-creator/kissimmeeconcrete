# Kissimmee Concrete — guia rápido de marca (v1, 2026-09-10)

## Origem
Logo escolhido e entregue pelo proprietário em 2026-09-10 (`logo-source-owner-2026-09-10.png`, 1536×1024, fundo branco). Todos os ativos abaixo são derivados dele por `make_brand_assets.py`. Nome público fixo: **Kissimmee Concrete** (sem FL, Florida, LLC, sufixos). A linha "DRIVEWAYS · PATIOS · WALKWAYS · MORE" é descritor do logo, não faz parte do nome.

## Ativos
| Arquivo | Uso |
|---|---|
| `logo-stacked-master.png` / `logo-stacked-dark-master.png` | Versão empilhada (K + wordmark), fundo transparente, claro/escuro |
| `icon-k-master.png` / `icon-k-dark-master.png` | Símbolo isolado (favicon, ícone social, avatar) |
| `wordmark-master.png` / `wordmark-dark-master.png` | Só o texto |
| `logo-horizontal-light-master.png` / `-dark-` | Lockup horizontal para header (K à esquerda, wordmark à direita) |
| `logo-kissimmee-concrete.svg` | Interpretação vetorial limpa do lockup (geometria do K simplificada; o PNG do proprietário continua sendo a fonte de verdade para impressão) |
| `site/static/brand/png|webp/*-h64/96/160/320` | Renders para header/footer |
| `site/static/brand/png/favicon-16/32/48/180/192/512.png`, `site/static/favicon.ico` | Favicons e ícone PWA |
| `site/static/brand/png/icon-square-dark-1024.png` / `-light-` | Ícone social 1:1 (GBP, Yelp, Facebook) |
| `og-default.jpg` (1200×630) | Imagem padrão de compartilhamento |

## Paleta (extraída do logo)
| Token | HEX | Uso |
|---|---|---|
| gold | #B07828 | marca, botões primários, regras, links de destaque |
| gold-light | #D3A64A | hover, marca em fundo escuro |
| ink | #1A1A1A | wordmark, títulos, footer |
| text | #202020 | corpo |
| muted | #5C5B55 | metadados, legendas |
| surface | #F2F2EF | fundo (cinza-concreto claro) |
| surface-2 | #E7E6E0 | blocos alternados, tabelas |
| line | #D4D2CA | bordas |
| focus | #0B63C6 | foco de teclado (contraste AA sobre surface) |
| ok / warn | #2E6B3F / #A0520D | estados |
| dark: bg #161616, surface #1F1F1F, text #EDEAE2, line #3A3A36 | modo escuro |

Contrastes checados: ink sobre surface 15.9:1; gold (#B07828) sobre branco 4.6:1 (texto ≥ 18 px ou negrito; para texto pequeno usar #8A5D1C, 6.1:1); texto claro sobre dark 13.8:1.

## Tipografia (self-hosted, OFL)
- Display: **Montserrat** variável (latim), pesos 700/800, caixa alta com tracking para eyebrows; combina com a geometria do wordmark.
- Corpo: **Source Sans 3** variável (latim) + itálico; 17–18 px, line-height 1.6.
- Nenhum hub irmão usa essas famílias (Ocoee: Outfit/Lato; Windermere: Fraunces/Figtree; LWR: Outfit/Inter; Groveland: Fjalla One/IBM Plex; GCM: Playfair/Inter).

## Voz
Prestador local que explica com números: solos nomeados, jurisdição certa, chuva por mês, preço com data e método. Contrações, frases curtas e longas alternadas, uma opinião de especialista por página com justificativa. Não usa: N-Point checklist, "Why Choose Us", superlativos, "licensed" sem número, palavras da lista proibida (`site/qa_style.py`).

## Distinção
Único hub com hero fotográfico + faixa de dados regionais, K dourado, ouro escovado sobre cinza-concreto e tipografia Montserrat/Source Sans 3. Colisão parcial de cor com Lakewood Ranch (dourado #FFC84A/creme) documentada e mitigada (ver `research/00-INVENTARIO-FASE1.md`, seção 3).
