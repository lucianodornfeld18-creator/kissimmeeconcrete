# Keywords e demanda — kissimmeeconcrete.com

## Fontes e configuração

| Fonte | Configuração | Arquivo | Data |
|---|---|---|---|
| Google Ads Keyword Planner (plano autenticado, exportado pela sessão EMD) | Localização Florida, rede Google, inglês, 01/08/2025–31/07/2026, média mensal | `emd-google-ads-846-raw.csv` (846 consultas, 88 mercados) | 2026-09-07 |
| Google autocomplete (suggestqueries, hl=en, gl=us) + Bing autosuggest (en-US) | 46 seeds × 2 motores | `autocomplete-google-bing-2026-09-10.csv` (731 sugestões, 649 únicas, 375 com forma de pergunta/intenção) | 2026-09-10 |
| Google Trends (pytrends) | geo US-FL-534 (DMA Orlando–Daytona–Melbourne), 5 anos, interesse relativo + related queries | `trends-orlando-dma-5y*.csv`, `trends-related-*.csv` | 2026-09-10 |
| Search Console do Ocoee | **BLOCKED** (Windsor.ai free plan pausou leituras) | — | — |
| Twilio/formulários Ocoee e GCM | **OWNER INPUT** (sem acesso) | — | — |

Regras aplicadas: célula vazia = "sem volume mensurável", nunca zero; `Avg. monthly searches` agrega variantes próximas e é arredondado; CPC/competição = sinal comercial, nunca dificuldade orgânica.

## O que o Keyword Planner mostra para o território (Florida, 12 meses)

| Consulta | Média mensal | Competição | CPC baixo–alto (US$) |
|---|---|---|---|
| concrete kissimmee | 50 | High (77) | 6,21–14,14 |
| kissimmee concrete / contractor / company / driveway / repair / patio | — | — | — |
| st cloud concrete | 50 | Medium (43) | — |
| davenport concrete | 50 | Low (14) | — |
| four corners concrete | 50 | Low (7) | — |
| osceola county concrete (todas as variantes) | — | — | — |
| orlando concrete / contractor / company | 500 cada | High/Medium | 4,61–26,70 |
| orlando concrete driveway / repair / patio | 50 cada | High/Medium | 8,67–56,49 |
| lakeland concrete / concrete lakeland | 50 / 50 | Low / High (98) | 8,33–20,35 |
| clermont concrete / concrete clermont / clermont concrete contractors | 50 / 50 / 50 | Low/Medium | 7,85–19,14 |
| sanford, oviedo, lake mary, windermere (core) | 50 | — | — |
| apopka, winter garden, winter park (reverse contractor) | 50 | Low | — |

Conclusão (mantida do prompt): o volume da região **não** está nas strings com cidade. Está nas consultas genéricas geolocalizadas. Evidência complementar do Trends (DMA Orlando, 5 anos, related queries "top"): `concrete contractor near me` (100), `concrete driveway contractor` (50), `pavers near me` (66), `pavers orlando` (60), `pool pavers` (59), `seal pavers` (34), `concrete driveway cost` (100), `driveway repair` (70), `concrete driveway repair` (69), `paver sealing near me` (100), `stamped concrete patio` (100), `pool deck paint` (100), `concrete pool deck` (85), `pool deck pavers` (40), `pool deck resurfacing` (39), `travertine pool deck` (30), `polyaspartic vs epoxy` (rising +75.250%), `how much does it cost to epoxy a garage floor` (rising), `stucco repair orlando` (69), `concrete repair orlando` (38).

## Sazonalidade (Trends, média mensal do índice, 5 anos, DMA Orlando)

| Tema | Pico | Vale | Leitura |
|---|---|---|---|
| pavers | abr (80) – mai (79) | dez (46) | primavera = temporada de pavers; planejar conteúdo e anúncios fev–mai |
| concrete driveway | mai (10,2) | dez (2,9) | pico antes da estação chuvosa |
| pool deck | mai (57) | dez (21) | decks decididos abr–jun |
| travertine | abr (33) | dez (9) | idem |
| epoxy garage floor | fev (12) | jan (4) | pós-festas/"garage reset" |
| stucco repair | abr (8) | dez–jan (1) | baixa demanda, sazonal |
| concrete repair | abr–mai (7,7) | dez (0) | após chuvas de primavera |
| paver sealing | ago (4,6) | dez (0,3) | verão = manutenção pós-chuva |

## Clusters e URL proprietária (resumo; a lista completa de perguntas está em `04-150-questions.csv`)

| Cluster | Keywords representativas (fonte) | Intenção | URL proprietária |
|---|---|---|---|
| Concrete contractor (genérico geolocalizado) | concrete contractors near me, concrete contractor kissimmee fl, concrete near me contractor, how much do concrete contractors charge (AUTOCOMPLETE/TRENDS) | comercial | `/` e `/concrete/` |
| Concrete driveway | concrete driveway cost, cost to have a concrete driveway poured, how much does a 2 car concrete driveway cost, how thick should a concrete driveway be in florida, concrete driveway replacement cost, cement driveway contractors near me (AUTOCOMPLETE/TRENDS) | comercial + custo | `/concrete/driveways/`, `/pricing/concrete/` |
| Paver driveway | paver driveway cost florida, how much does a paver driveway cost, driveway pavers cost per square foot, is a paver driveway cheaper than concrete (AUTOCOMPLETE) | comercial + custo | `/pavers/driveways/`, `/pricing/pavers/` |
| Pool decks | pool deck pavers near me, travertine vs pavers pool deck, travertine vs concrete pavers pool deck, is travertine good for pool decks, cool deck vs pavers, pool deck resurfacing (AUTOCOMPLETE/TRENDS) | comercial + comparação | `/pavers/pool-decks/`, `/concrete/pool-decks/`, `/compare/travertine-vs-concrete-pavers/`, `/compare/cool-deck-vs-pavers/` |
| Permits | do you need a permit for a driveway in florida, do i need a permit for a concrete patio in florida, do i need a permit for a concrete slab in florida, osceola county driveway permit, osceola county right of way permit, do you need a license to pour concrete in florida (AUTOCOMPLETE) | informacional | `/permits/*`, `/tools/permit-finder/` |
| Concrete vs pavers | pavers vs concrete driveway florida, which is cheaper pavers or concrete driveway, is a paver driveway better than concrete, stamped concrete vs pavers cost/pros and cons/for pool deck (AUTOCOMPLETE) | comparação | `/compare/concrete-vs-pavers/`, `/compare/stamped-vs-pavers/`, `/tools/concrete-vs-pavers/` |
| Sealing / maintenance | paver sealing near me, paver sealing cost, should you seal pavers in florida, polymeric sand vs paver sand, what causes rust stains on concrete driveway, how to remove rust from concrete driveway (AUTOCOMPLETE/TRENDS) | comercial + how-to | `/pavers/sealing/`, `/guides/rust-stains-irrigation/`, `/faq/pavers/` |
| Repair | why does concrete crack, why do concrete driveways crack, concrete driveway repair cost, paver driveway repair cost, driveway repair (AUTOCOMPLETE/TRENDS) | comercial + diagnóstico | `/concrete/repair/`, `/pavers/repair/`, `/guides/why-concrete-cracks-osceola/` |
| Garage floors | epoxy garage floor orlando fl, how much does a garage epoxy floor cost, polyaspartic vs epoxy (AUTOCOMPLETE/TRENDS) | comercial | `/coatings/garage-floors/` |
| Stucco | stucco repair near me, stucco repair cost, are stucco cracks normal (AUTOCOMPLETE) | comercial | **não publicado** até confirmação de capacidade (registry `not_confirmed_do_not_use`) |
| Slabs | concrete slab for shed cost, do i need a permit for a concrete slab (AUTOCOMPLETE) | comercial | `/concrete/slabs/`, `/tools/concrete-paver-calculator/` |
| Espanhol | concreto kissimmee, contratista de concreto orlando, adoquines kissimmee → sem sugestões relevantes | — | `/es/` adiado |

Exclusões aplicadas: ready-mix supplier/delivery, jobs/salary, DIY sem valor comercial, precast, pumping, equipment rental, e o ruído do autocomplete (driving permit, St. Louis, Oregon, Wisconsin etc.).

## Pendências para fechar o controle 5 com localização por cidade

Exportar do Keyword Planner (Chrome autenticado) as famílias abaixo com localização = Kissimmee, Osceola County, cada cidade Tier 1/2 e Orlando metro, salvando CSV com data: `[service]` / `near me` / `contractor(s)` / `company` / `installation` / `cost` / `price per square foot` / `estimate` / `repair` / `replacement` / `resurfacing` / `sealing` / `cleaning` / `leveling` / `removal`, mais as comparações e os termos técnicos listados na seção 5.1 do prompt. Sem isso, o volume geolocalizado por cidade permanece "não mensurado" e o site usa apenas as evidências acima.
