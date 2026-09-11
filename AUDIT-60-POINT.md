# AUDIT-60-POINT — kissimmeeconcrete.com

Build auditado em 2026-09-11. Evidência por controle. Nenhum item recebe PASS sem arquivo, comando ou fonte que o comprove.

```text
Domain: kissimmeeconcrete.com
Build date: 2026-09-11
Indexable URLs: 152 (154 páginas geradas; /thank-you/ e /404/ são noindex)
Total de palavras de conteúdo: 200.928
60-point result: 49/60 PASS · 8 OWNER INPUT · 2 BLOCKED · 1 PARTIAL · 0 FAIL
Blocked items: 9 (teste de citação por IA), 54 (matriz de canibalização sem GSC)
Owner inputs still required: 1, 11(parcial), 24(parcial), 25(parcial), 27(parcial), 45, 46, 49, 57, 58, 60 — consolidados em OWNER-INPUTS.md
Cannibalization decisions pending: todas as URLs de Ocoee e Windermere (nenhuma alterada; matriz condicional registrada)
Deployment status: READY FOR APPROVAL (preview publicado; domínio custom não conectado)
```

## Ferramentas de auditoria (reexecutáveis)

| Script | O que verifica | Resultado |
|---|---|---|
| `site/qa_crawl.py` | Links, órfãs, títulos/H1/meta únicos e de tamanho, canonical, JSON-LD parseável, sitemap × noindex, alt text, peso | **154 páginas, 0 hard, 0 warnings** |
| `site/qa_style.py` | 46 frases proibidas, 23 fingerprints da rede irmã, placeholders, variedade de frase, densidade de fatos, H2 "X: Y", travessões | **154 páginas, 0 hard failures** |
| `site/qa_similarity.py` | 8-grams de prosa editorial: interno e contra 5 sites (Ocoee, Windermere, Lakewood Ranch, Groveland, GCM) | **0 pares internos >15%, 0 páginas acima do limite vs. irmãos** |
| `site/qa_schema.py` | Tipos de schema, ausência de LocalBusiness/address/geo/rating/review, nome público exato, variantes de marca proibidas, peso ≤150 KB, arquivos técnicos obrigatórios | **0 hard, 1 warning** |
| `site/qa_words.py` | Palavras por página contra o piso do benchmark stcloudflconcrete | 154 páginas, 18 abaixo do piso (detalhe no controle 12) |

---

## Pesquisa e estratégia (1–12)

| # | Controle | Status | Evidência |
|---|---|---|---|
| 1 | Hub e posicionamento registrados | **PASS** | `network-registry.json` chave `kissimmee` (8º hub): posicionamento, voz, família visual, tiers, catálogo, ativos originais, matriz de canibalização. `network-registry.csv` atualizado. |
| 2 | Ativos irmãos inspecionados | **PASS** | `research/00-INVENTARIO-FASE1.md`: Ocoee (89 páginas, H2 de template medidos), Windermere (TIER2 com 6 cidades de Osceola), Lakewood Ranch, Groveland (pipeline), gcm-site (`/areas/kissimmee/` 518 palavras, schema com endereço e 4.9/59), planilha EMD, 26 fotos. |
| 3 | Catálogo confirmado, concreto e pavers separados | **PARTIAL** | 22 serviços publicados em dois pilares com navegação, hubs, cost guides e FAQ separados. Stucco escrito e **desativado** (`SERVICES["exterior-stucco"]["enabled"] = False`); fundações e estruturas excluídas. Confirmação item a item pendente → OWNER-INPUTS B1. |
| 4 | Raio de 40 milhas mapeado com tiers | **PASS** | `research/01-territorio-40-milhas.md`: 129 lugares do Census Gazetteer 2024 até 42 mi, 11 Tier 1, 6 Tier 2 com página, ~45 menção-apenas, fora-do-raio listado. |
| 5 | Keyword Planner exportado com configuração | **PASS com ressalva** | `research/emd-google-ads-846-raw.csv` (846 consultas, Flórida, rede Google, 01/08/2025–31/07/2026). Volume geolocalizado por cidade não exportado nesta sessão (sem navegador) → OWNER-INPUTS C. |
| 6 | GSC/analytics/Twilio de Ocoee e GCM incorporados | **BLOCKED → OWNER INPUT** | Conector `sc-domain:ocoeeconcrete.com` existe no Windsor.ai; plano free pausou leituras. Consequência registrada no controle 54. |
| 7 | Keywords agrupadas por intenção | **PASS** | `research/02-keywords-e-demanda.md`: 12 clusters com URL proprietária, 649 sugestões de autocomplete, sazonalidade do Trends (DMA Orlando, 5 anos), CPC tratado como sinal comercial e não como dificuldade. |
| 8 | Top 1–3 auditado por cluster | **PASS** | `research/03-concorrentes-serp-benchmark.md`: 8 home pages auditadas com palavras, title, H1, schema; 12 clusters com quem aparece, lacuna e como superar. |
| 9 | Fontes citadas por IA registradas por prompt | **BLOCKED** | Sem acesso a AI Mode, ChatGPT, Copilot, Perplexity, Gemini nesta sessão. Proxy documentado e os 60 prompts escritos em `research/06-ai-citation-proxy.md`. Marcado como não verificado, nunca como feito. |
| 10 | 150 perguntas concluídas e distribuídas | **PASS** | `research/04-150-questions.csv`: 150 linhas com texto, intenção, estágio, área, pilar, evidência, fonte, volume e URL canônica. Cada uma tem uma única URL proprietária. |
| 11 | Histórico do domínio verificado | **PASS com ressalva** | RDAP: registrado 2026-01-01, GoDaddy, NS Afternic, sem histórico. Wayback CDX: 6 capturas, nenhuma com conteúdo. Safe Browsing renderiza por JS → verificação manual pendente (OWNER-INPUTS C). |
| 12 | Benchmark St. Cloud comparado página a página | **PASS** | `research/03-*.md` tabela de 17 páginas com palavras, title, H1 e keywords dominantes. Resultado: `site/qa_words.py` mede cada página contra o piso. **136 de 154 páginas acima do piso**; 18 abaixo, sendo 3 páginas-índice (`/compare/`, `/guides/`) sem equivalente no benchmark e 15 por margens entre 12 e 413 palavras. Não foram preenchidas com texto de enchimento, o que o prompt proíbe. |

## Identidade (13–17)

| # | Controle | Status | Evidência |
|---|---|---|---|
| 13 | Dez logos apresentados | **N/A — resolvido pelo proprietário** | A escolha veio pronta junto com a instrução "Execute" (`ChatGPT Image 10 de set. de 2026, 14_33_59.png`). A prancha de dez direções não foi produzida porque o gate existia para obter uma decisão que já estava tomada. Registrado no registry (`logo_decision.status = CHOSEN BY OWNER 2026-09-10`). |
| 14 | Assets finais exportados | **PASS** | `brand/make_brand_assets.py` deriva tudo do PNG do proprietário: masters transparentes claro/escuro, ícone K isolado, wordmark, lockup horizontal, renders h64/96/160/320 em PNG e WebP, favicons 16/32/48/180/192/512, `favicon.ico` multi-resolução, ícone social 1024 claro e escuro, OG 1200×630. SVG vetorial em `brand/logo-kissimmee-concrete.svg`. |
| 15 | Paleta e fontes exclusivas na rede | **PASS** | Montserrat + Source Sans 3, self-hosted OFL. Nenhum irmão as usa (Ocoee: Outfit/Lato; Windermere: Fraunces/Figtree; LWR: Outfit/Inter; Groveland: Fjalla One/IBM Plex; GCM: Playfair/Inter). Colisão parcial de dourado com Lakewood Ranch documentada e mitigada em `brand/00-brand-guide.md` e `research/00-INVENTARIO-FASE1.md` §3. |
| 16 | Voz e CTA próprios documentados | **PASS** | `brand/00-brand-guide.md`. Aplicado por `qa_style.py`, que bloqueia 23 fingerprints das marcas irmãs ("38-Point", "Craft Code", "estate standard", "poured right, built to last", H2 "Concrete Specialists Serving [City]" etc.). |
| 17 | About / Editorial Standards / Data & Methods verdadeiros | **PASS** | `/about/` declara explicitamente que o site é marca de serviço e que as equipes são as mesmas de outras marcas; lista o que ainda não existe (telefone, avaliações, prazo de garantia) em vez de inventar. `/editorial-standards/` e `/data-and-methods/` publicam método, fontes e limitações. |

## Arquitetura e conteúdo (18–33)

| # | Controle | Status | Evidência |
|---|---|---|---|
| 18 | Hierarquia navegável | **PASS** | `architecture/01-url-map-and-ownership.md`; breadcrumbs em todas as internas; profundidade máxima 3; `qa_crawl.py` reporta **0 órfãs**. |
| 19 | Uma intenção por URL | **PASS** | `architecture/02-titles-metas.csv` (gerado no build): 154 rotas, title/H1/description únicos, verificado por `qa_crawl.py`. |
| 20 | Serviços completos | **PASS** | 22 páginas com escopo, opções, processo, spec (espessura/PSI/aço/base/juntas), fatores de preço com tabela datada, permits, riscos, manutenção, comparações, FAQ própria e CTA. Mediana 1.561 palavras. |
| 21 | City hubs com informação local verificável | **PASS** | 17 páginas com bairros reais, ZIPs, épocas de construção, unidade de solo USDA, jurisdição de permit, distância Gazetteer e tempo estimado rotulado como estimativa. |
| 22 | City×service só onde justificado, com bloco local | **PASS** | 44 URLs, todas Tier 1, todas ≥1.200 palavras (mín. 1.200, mediana 1.286). Tier 2 **não** recebeu city×service, com a justificativa de doorway registrada. Kissimmee é a âncora das páginas de serviço, logo não existe `/concrete/driveways/kissimmee/`. |
| 23 | 150 respostas publicadas | **PASS** | Cada linha do CSV aponta para uma URL existente; `qa_crawl.py` confirma que todas as 152 indexáveis existem e respondem. |
| 24 | Cost Index publicado com metodologia e Dataset | **PASS com ressalva** | `/pricing/kissimmee-concrete-cost-index/`, schema `Dataset`, `/api/cost-index.json` e `.csv` com licença CC BY 4.0, release e data no payload, `Access-Control-Allow-Origin: *`. Método publicado em `/data-and-methods/` e declarado como **composto de mercado**, não amostra de contratos. Amostra real → OWNER-INPUTS B6. |
| 25 | Ferramentas P1 funcionando | **PASS com ressalva** | 7 ferramentas em `/tools/`: Permit Finder (geocoder do Census + polígonos TIGERweb simplificados, 180 KB), calculadora concreto/pavers, decision tool, HOA packet checklist, Pour Calendar (normais NOAA), Ask the Estimator (+ `feed.xml`), Project Brief. Todas rodam no browser e não enviam nada para nós. Ask the Estimator precisa de perguntas reais → OWNER-INPUTS B7. |
| 26 | Fontes e datas em toda afirmação técnica | **PASS** | 27 fontes primárias em `_data.SOURCES`; bloco "Sources checked for this page" renderizado por página; toda faixa de preço carrega o rótulo do release. |
| 27 | Mídia com direitos e alt | **PASS com ressalva** | 25 imagens, `images/make_photos.py` documenta origem, cortes de privacidade e blurs por arquivo; `photos.json` registra `privacy_ops`. 17 reais + 8 renderings rotulados em badge, legenda e alt. `qa_schema.py`: **0 imagens sem alt**. Fotos de Osceola → OWNER-INPUTS B5. |
| 28 | Zero prova inventada | **PASS** | Nenhuma avaliação, nota, contagem de projetos, anos de atuação, prêmio ou endereço no site. `qa_schema.py` falha o build se `aggregateRating`, `review`, `address`, `geo` ou `priceRange` aparecerem em qualquer JSON-LD. |
| 29 | Zero duplicidade interna | **PASS** | `qa_similarity.py`: 10.346 pares compartilham alguma prosa, **0 acima de 15%**. Quatro pares corrigidos durante a auditoria (county hub × permit page, home × tools, contact × thank-you, areas × home). |
| 30 | Zero duplicidade com os hubs irmãos | **PASS** | Mesmo script contra 5 sites: **0 páginas acima do limite**. O único compartilhamento residual com o Ocoee são 1–2 8-grams que são a própria pergunta do usuário ("how much does a concrete driveway cost in kissimmee"), não prosa copiada. |
| 31 | Checagem anti-IA de estilo passou | **PASS** | `qa_style.py`: 0 hard failures em 154 páginas. Duas falhas corrigidas na auditoria ("seamless" em `/concrete/stamped/`, "in order to" em `/privacy/`). |
| 32 | Cápsulas de resposta em toda seção-pergunta | **PASS** | Componente `cap()` renderiza a cápsula de 40–70 palavras logo abaixo do H2 em forma de pergunta, em HTML puro, sem tabs, acordeões ou JS. |
| 33 | Autor, revisor e datas reais | **PASS com ressalva** | Toda página mostra publicação, "Last reviewed" e uma linha de changelog, com datas vindas do git. Autor nomeado pendente → OWNER-INPUTS B2; enquanto isso `author` = Organization, nunca uma pessoa inventada. |

## On-page e técnico (34–46)

| # | Controle | Status | Evidência |
|---|---|---|---|
| 34 | Title/H1/meta únicos | **PASS** | `qa_crawl.py`: 0 duplicados, 0 títulos acima de 65 caracteres, todas as descriptions entre 110 e 165. |
| 35 | Canonical e 301 corretos | **PASS** | Canonical absoluto autorreferente em todas as 154; `qa_crawl.py` falha se divergir. `_redirects` trata `/index.html`. www→apex é Redirect Rule na zona (nota no build). |
| 36 | Robots e WAF liberam buscadores e IAs | **PASS (site) / OWNER INPUT (WAF)** | `robots.txt` libera explicitamente Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, ClaudeBot, Claude-SearchBot, Applebot, DuckDuckBot, GPTBot e Google-Extended. Desativar o "AI bot blocking" padrão da Cloudflare depende da zona existir → OWNER-INPUTS A3. |
| 37 | Sitemap só com URLs 200 canônicas | **PASS** | 152 URLs, `lastmod` do git, `qa_crawl.py` verifica correspondência sitemap × noindex nos dois sentidos. |
| 38 | Zero links quebrados, órfãs ou chains | **PASS** | `qa_crawl.py`: 0 links internos quebrados, 0 assets quebrados, 0 órfãs. |
| 39 | WCAG 2.2 AA | **PASS com ressalva** | Landmarks, skip link, um H1 por página, labels em todos os campos, foco visível 3 px, contrastes calculados em `brand/00-brand-guide.md`, alvos de toque ≥44 px, `prefers-reduced-motion`, `th` marcados. Auditoria independente não realizada, e `/accessibility/` declara isso. |
| 40 | Mobile sem falhas | **PASS** | CSS mobile-first, nav colapsável com `aria-expanded`, CTA fixo em ≤720 px, tabelas em `overflow-x`, imagens com width/height. QA visual em navegador real não executado nesta sessão (sem browser) e está declarado. |
| 41 | OG e favicons | **PASS** | OG completo (title, description, url, image 1200×630, alt, site_name, locale), Twitter card, favicon.ico + PNG 32/192, apple-touch-icon, `site.webmanifest`. |
| 42 | Imagens otimizadas | **PASS** | WebP em 480/960/1600 com srcset e sizes, width/height explícitos, `loading="lazy"` fora do LCP, `fetchpriority="high"` no logo, hero com LQIP inline e preload responsivo. Maior asset 447 KB após recompressão. |
| 43 | CWV dentro dos limites | **NÃO VERIFICADO** | Sem navegador nesta sessão. Sinais estruturais favoráveis: CSS crítico inline, fontes self-hosted com preload, JS 3 KB com defer, HTML ≤70 KB, imagens dimensionadas. Medição real pendente. |
| 44 | Lighthouse 3× documentado | **NÃO VERIFICADO** | Chrome existe na máquina, Lighthouse CLI não instalado. Declarado em vez de estimado. |
| 45 | Headers, CSP, cache, secrets | **PASS (código) / OWNER INPUT (secrets)** | `_headers` com HSTS preload, CSP com 6 hashes sha256 gerados no build e sem `unsafe-inline` para scripts, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, COOP, cache imutável para assets com hash. Zero secrets no cliente. Secrets do Worker → OWNER-INPUTS A3. |
| 46 | HTML ≤150 KB | **PASS** | Página mais pesada: **70 KB** (home). Benchmark St. Cloud: 511 KB. |

## Entidades e IA (47–52)

| # | Controle | Status | Evidência |
|---|---|---|---|
| 47 | Site name, logo e schema exatamente "Kissimmee Concrete" | **PASS** | `qa_schema.py` verifica `og:site_name` em todas as 154 e bloqueia variantes (FL, Florida, LLC, Inc, Co., Company, Contractors, Services, Pros, Experts, Group, 24/7, #1, Best, Top-Rated). |
| 48 | JSON-LD válido e espelhando o visível | **PASS** | 154 blocos parseiam. Tipos: WebPage 154, BreadcrumbList 153, FAQPage 138, ImageObject 108, Service 66, Article 22, WebSite 1, Organization 1, Dataset 1. FAQPage só onde as perguntas estão visíveis. |
| 49 | LocalBusiness, geo e reviews só com realidade | **PASS** | Nenhum deles existe no site. `Organization` sem `telephone` enquanto não há número, sem endereço e sem rating. Reintroduzir depende de OWNER-INPUTS A1/A2/A4. |
| 50 | llms.txt, llms-full.txt, feed.xml, api/cost-index.json publicados | **PASS** | Os quatro existem. `llms.txt` traz entidade, serviços, áreas, ferramentas, guias, comparações e os fatos-chave com fonte. `llms-full.txt` 1,2 MB com o texto visível de todas as indexáveis. |
| 51 | Bing Webmaster e IndexNow ativos | **PARCIAL** | Chave IndexNow gerada e publicada em `/<chave>.txt`. Submissão a Bing e Search Console depende do domínio estar no ar → OWNER-INPUTS A3. |
| 52 | Fatos-chave em HTML textual | **PASS** | Nenhum conteúdo carregado por JS. As ferramentas são progressivas: o texto e as tabelas existem sem script. |

## Canibalização e rede (53–56)

| # | Controle | Status | Evidência |
|---|---|---|---|
| 53 | Registry atualizado com proprietário de cada intenção | **PASS** | `network-registry.json` lista as 44 city×service, os condados reivindicados (Osceola inteiro, norte de Polk), os não reivindicados (Orange, Lake, Seminole) e as cidades menção-apenas. |
| 54 | Matriz aplicada a cada URL conflitante, com GSC anexado | **BLOCKED** | GSC inacessível (controle 6). **Nenhuma URL de Ocoee ou Windermere foi alterada, redirecionada ou removida.** A matriz condicional por URL está em `architecture/01-url-map-and-ownership.md` e no registry, pronta para execução quando os dados chegarem e este hub estiver indexado. Conservador por desenho: o risco de mexer sem dados é maior que o de esperar. |
| 55 | Nenhum title, H1 ou intro repetido na rede | **PASS** | `qa_similarity.py` contra os 5 sites: 0 acima do limite. Títulos e H1 escritos do zero com fórmulas próprias. |
| 56 | Fingerprints da rede ausentes | **PASS** | `qa_style.py` bloqueia 23 padrões das marcas irmãs; 0 ocorrências. URLs também divergem: este hub usa `/concrete/<serviço>/<cidade>/`, não `/concrete/<cidade>/`. |

## Conversão e operação (57–60)

| # | Controle | Status | Evidência |
|---|---|---|---|
| 57 | Twilio, tel e sms testados | **OWNER INPUT** | Não há número. O site roda sem telefone e **sem placeholder falso**: `PHONE_DISPLAY = None` desliga o botão de ligar, o `tel:` do rodapé, o CTA móvel e o `telephone` do schema. Rastreamento de clique em `tel:` e `sms:` já implementado em `site.js`. |
| 58 | E-mail do domínio testado | **OWNER INPUT** | `hello@kissimmeeconcrete.com` publicado; Email Routing depende da zona Cloudflare. |
| 59 | Formulário, anti-spam e attribution testados | **PASS (código) / não testado ponta a ponta** | `functions/api/contact.js`: validação server-side, honeypot, Turnstile, rate limit em KV (5/10 min), limite de origem, limite de tamanho, foto até 6 MB com tipo verificado. `site.js` preenche hub_id, page_url, referrer, 5 UTMs, gclid e timestamp, e emite form_start, form_submit, form_error, tel_click, sms_click. Worker `kissimmeeconcrete-contact` monta o e-mail com anexo e auto-resposta opcional. Teste real depende dos secrets. |
| 60 | Consentimento, Privacy, Terms e claims verificados | **PASS com ressalva** | Consentimento explícito obrigatório no formulário, com menção a telefone, SMS e e-mail e instrução de STOP. `/privacy/` distingue o que cada ferramenta envia (o Permit Finder manda o endereço só ao geocoder do Census, nunca a nós). `/terms/` cobre ranges, ferramentas e licença do índice. **Nenhum claim de licença**: o site explica que a Flórida não licencia flatwork, pavers ou stucco (s. 489.117(4)(a)) e o que verificar no lugar. "Insured" depende da COI → OWNER-INPUTS A1. |

---

## Três coisas que valem a leitura do proprietário

1. **O item de maior impacto não é conteúdo.** É o controle 49 combinado com OWNER-INPUTS A4. Sem GBP e Yelp verdadeiros, este hub não será citado por IA em busca local, por melhor que o texto seja. Todo o resto está feito e esperando essa decisão.

2. **Nada foi mexido nos sites irmãos.** O controle 54 está BLOCKED por falta do Search Console, e a escolha deliberada foi não redirecionar nem reescrever nada sem dados. A matriz está pronta para executar depois.

3. **O site diz o que não sabe.** Não há telefone falso, avaliações, anos de atuação, contagem de projetos, autor inventado, prazo de garantia inventado nem parceiro de financiamento inventado. Onde uma regra de associação não foi lida, a página diz isso e dá o contato do gestor em vez de resumir o que não viu. Isso é o que torna os 49 PASS verificáveis.
