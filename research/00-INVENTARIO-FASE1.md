# Fase 1 — Inventário, ativos irmãos, domínio e restrições (kissimmeeconcrete.com)

Data: 2026-09-10. Sessão de execução do `08-PROMPT-KISSIMMEE-CONCRETE.md`. Relatório em português; tudo o que é público no site sai em inglês.

## 1. Ativos inspecionados

| Ativo | Caminho | O que foi verificado | Uso neste hub |
|---|---|---|---|
| Registry da rede | `Documents\Codex\2026-09-03\pr\outputs\concrete-leadgen-network\network-registry.json` + `.csv` | 7 hubs, entidade real (GCM Best Services Corp), catálogo confirmado, lista `not_confirmed_do_not_use` (foundation-installation, stucco, room additions, pool shells, muros estruturais) | Atualizado com o hub `kissimmee` (ver `network-registry.json`, chave `hubs[7]`) |
| Prompt mestre | `PROMPT-MESTRE-7-HUBS-CONCRETO.md` | Política central: verdade, sem NAP fictício, schema só com fatos, city×service só justificado, 50 controles | Base dos 60 controles do `AUDIT-60-POINT.md` |
| Groveland (pipeline) | `Documents\Codex\2026-09-07\groveland-concrete\site` | `build.py` → `dist/`, `_seo.py`, `_photos.py`, `templates.py`, `functions/api/contact.js`, `workers/contact-email`, CSP com hashes, fontes self-hosted, `_headers`, `llms.txt` | Base **técnica** reescrita para este hub (nenhum texto, paleta, fonte ou layout reaproveitado) |
| Ocoee Concrete | `SSD-Antigo-Lucia\Projetos\ocoeeconcrete` | 89 páginas; `/concrete/kissimmee/` (1.844 palavras), `/pavers/kissimmee/` (1.877), `/blog/concrete-cost-kissimmee/` (1.931), `/blog/paver-cost-kissimmee/` (2.013) e equivalentes de Celebration, Davenport e Four Corners com os **mesmos H2** (template com cidade trocada). Telefone (689) 356-6292. Fontes Outfit + Lato; paleta laranja/marrom (#D05A1E, #7C2D12, #FCD34D) | Matriz de canibalização (seção 2.1 do prompt) — ver `architecture/01-url-map-and-ownership.md` |
| Windermere Concrete | `SSD-Antigo-Lucia\Projetos\windermereconcrete` e `Documents\Codex\2026-08-20\co\work\windermereconcrete` | TIER2 com `/kissimmee/` (2.247 palavras), `/st-cloud/` (2.288), `/celebration/`, `/champions-gate/`, `/davenport/`, `/lake-nona/`, todas com H2 idênticos ("Every service we bring to X", "The Windermere Craft Code", "X homeowners ask us"). Fontes Fraunces + Figtree; paleta verde-sálvia (#9FC3B2) | Idem |
| Lakewood Ranch Concrete | `SSD-Antigo-Lucia\Projetos\lakewoodranchconcretefl` | Fora do raio. Fontes Outfit + Inter; paleta dourado/creme (#FFC84A, #9A7C32, #FBF7EF); "42-Point Install Standard"; tagline "Poured right. Built to last." Telefone (941) 263-0948 | Só para checagem de colisão de paleta/fingerprints |
| GCM Best Services (site real) | `SSD-Antigo-Lucia\gcm-site` | `/areas/kissimmee/` (518 palavras, posicionamento luxo: Reunion, Bellalago, Bella Trae, Formosa Gardens), `/blog/hardscape-costs-kissimmee/` (533 palavras, tabela de faixas), schema `Organization` + `LocalBusiness` com endereço 7914 Tumblestone Dr, Orlando FL 32819, telefone (407) 250-1948, e-mail gcmrenovationsservices@gmail.com, `aggregateRating` 4.9/59 (autodeclarado), `sameAs` Instagram/Facebook/TikTok. `llms.txt` lista Kissimmee e St. Cloud como áreas. Fontes Playfair Display + Inter | Marca-mãe permanece; o cost guide deste hub é diferente em escopo (por serviço, por cidade, por metodologia, com dataset) |
| Planilha EMD | `Documents\Codex\2026-09-03\pr\outputs\emd-concreto-fl\pesquisa_emd_concreto_florida_google_ads_2026-09-07.xlsx` | 846 consultas, Keyword Planner autenticado, Flórida, 01/08/2025–31/07/2026. Extraído para `research/emd-google-ads-846-raw.csv` | Base de volume por cidade (seção 5.1) |
| Fotos | `Projetos\Concreto Fotos` (26 arquivos) | 18 fotos reais do prestador + 8 renderings (classificação idêntica à revisão feita para o Groveland em 2026-09-09, reconferida visualmente). Achados de privacidade tratados no pipeline: overlay com endereço em Windermere (crop), logo GCM em rendering (crop), placa de obra de terceiro com telefone (crop), placas de carro e número de casa (blur). Ver `images/photos.json` | Galeria, páginas de serviço, hero |
| Logo | `Downloads\ChatGPT Image 10 de set. de 2026, 14_33_59.png` → `brand/logo-source-owner-2026-09-10.png` | Escolha do proprietário entregue junto com o "Execute" (K dourado/chumbo + KISSIMMEE / CONCRETE + DRIVEWAYS · PATIOS · WALKWAYS · MORE). Obs.: o arquivo 14_34_09 é o logo de **Sarasota**, não usar aqui | Gate de logo considerado **resolvido pelo proprietário**; a prancha de 10 direções não foi produzida porque a escolha já veio pronta (registrado no registry e no `AUDIT-60-POINT.md`, controle 13) |

Auditoria anterior do Ocoee (`Downloads\AUDITORIA_OCOEECONCRETE_v1.md`) **não foi encontrada** em Downloads/Documents nesta máquina; o registry preserva o resumo (7 problemas: GBP×site, reviewCount falso, sameAs quebrado…).

## 2. Domínio kissimmeeconcrete.com (seção 5.6)

| Verificação | Resultado (2026-09-10) | Fonte |
|---|---|---|
| RDAP | Registrado em 2026-01-01, expira 2028-01-01, registrar GoDaddy.com LLC, último update 2026-09-10 (compra pelo proprietário), status client{Delete,Renew,Transfer,Update}Prohibited (locks padrão), nameservers `NS1/NS2.AFTERNIC.COM` (ainda parqueado) | `https://rdap.verisign.com/com/v1/domain/kissimmeeconcrete.com` |
| Wayback (CDX) | 6 capturas: 2021-12 (301), 2022-01 (favicon/robots 200), 2023-03 (sem status), 2025-07 (302). Nenhum conteúdo real capturado → sem histórico de site, sem spam/farmácia/cassino observável | `web.archive.org/cdx/search/cdx?url=kissimmeeconcrete.com/*` (via curl; o WebFetch é bloqueado para archive.org) |
| Estado atual | `http://kissimmeeconcrete.com/` responde 200 (página de parking Afternic) | curl |
| Safe Browsing | Página do Transparency Report responde 200; o veredito é renderizado por JS e não pôde ser lido nesta sessão → **verificar manualmente** em `transparencyreport.google.com/safe-browsing/search?url=kissimmeeconcrete.com` (controle 11 fica PASS com ressalva) | — |
| Backlinks | Bing Webmaster/Ahrefs exigem login → OWNER INPUT (esperado: zero, dado o histórico vazio) | — |

Conclusão: domínio limpo, sem legado. Ação do proprietário: trocar os nameservers de Afternic para Cloudflare (a zona precisa existir na conta Cloudflare para Pages + Email Routing).

## 3. Fingerprints da rede — lista de proibições aplicada (seção 2.2)

Frases/estruturas encontradas nos irmãos e bloqueadas no checador de estilo (`site/qa_style.py`):
`38-Point`, `42-Point`, `N-Point` como marca, `Our Four Promises`, `Straight answers before you spend a dollar`, `in plain English`, `Built Local Since`, `poured right, built to last`, `Craft Code`, `estate standard`, `outlasts the mortgage`, `Every service we bring to`, `homeowners ask us`, H2 `Concrete Specialists Serving`, `Concrete Services We Offer in`, `[Service] Prices in [City], FL (2026)`, `Neighborhoods & ZIP Codes We Serve`, URL `/concrete/<cidade>/` e `/pavers/<cidade>/` no nível 2, blog `concrete-cost-<cidade>` / `paver-cost-<cidade>`, fontes Outfit, Lato, Inter, Fraunces, Figtree, Fjalla One, IBM Plex, Playfair Display; paletas laranja/marrom (Ocoee), sálvia (Windermere), dourado #FFC84A/creme (LWR), argila/ocre (Groveland).

Colisão parcial inevitável: o logo escolhido pelo proprietário é dourado + chumbo, e o Lakewood Ranch usa dourado (#FFC84A) + creme. Diferenciação aplicada: tons (ouro escovado #B07828 vs. amarelo #FFC84A), fundo (branco/cinza-concreto #F2F2EF vs. creme #FBF7EF), tipografia (Montserrat + Source Sans 3 — nenhum irmão usa), layout (hero com foto + faixa de dados, não hero com textura), sem checklist "N-Point", sem tagline em rima. Registrado no registry e no controle 15.

## 4. Acessos e bloqueios encontrados nesta sessão

| Recurso | Estado | Consequência |
|---|---|---|
| Google Ads Keyword Planner (Chrome autenticado) | Sem navegador nesta sessão | Usada a exportação autenticada de 2026-09-07 (846 consultas) + autocomplete Google/Bing (649 sugestões únicas, `research/autocomplete-google-bing-2026-09-10.csv`) + Google Trends DMA Orlando 5 anos (`research/trends-*.csv`). Controle 5 = PASS com base na exportação existente; famílias geolocalizadas por cidade ficam como OWNER INPUT (exportar do Planner com localização = Kissimmee/Osceola) |
| Search Console do Ocoee | Conector Windsor.ai existe (`sc-domain:ocoeeconcrete.com`) mas o plano free pausou leituras (13 contas conectadas, limite 1) | Matriz 2.1 aplicada com regra conservadora (nenhuma URL do Ocoee é redirecionada agora); decisão final por URL fica pendente da exportação GSC de 16 meses → OWNER INPUT (desconectar contas no Windsor ou exportar CSV do GSC) |
| Twilio | CLI instalada, sem perfil configurado; MCP Twilio só documenta | Número exclusivo, serviço `kissimmee-voice` e `FORWARD_TO` = OWNER INPUT com passo a passo |
| Cloudflare | `wrangler` autenticado (permissões pages, email_routing, kv, workers). Projetos existentes: gcmbestservices, ocoeeconcrete3, sarasotaflooringcompany… | Projeto Pages `kissimmeeconcrete` pode ser criado e receber preview em `*.pages.dev` (com `X-Robots-Tag: noindex` só no host de preview). Zona DNS do domínio ainda não está no Cloudflare → Email Routing e domínio custom = OWNER INPUT |
| GitHub CLI | Não autenticado | Repositório `kissimmeeconcrete` no GitHub = OWNER INPUT; enquanto isso o deploy é por upload direto do `wrangler pages deploy` |
| Census API / Census Reporter | API pede chave; Census Reporter devolveu 403 para o script | Idade do estoque de casas (ACS B25034) não pôde ser extraída por cidade nesta sessão; textos usam somente fatos de época de desenvolvimento documentados (BVL anos 1980, Poinciana anos 1970–, Celebration 1996–, resorts 2004–) e marcam o resto como faixa. OWNER INPUT: chave gratuita do Census (api.census.gov/data/key_signup) para completar a coluna |
| Yelp / kissimmeeconcretecontractors.com | 403 / desafio anti-bot | Auditoria desses dois só via SERP e fontes secundárias (Thumbtack, Houzz) |
| Google AI Mode / ChatGPT / Perplexity / Gemini / Copilot | Sem acesso nesta sessão | Teste de 60 prompts = BLOCKED; substituído por proxy (fontes que aparecem nas buscas por pergunta) em `research/06-ai-citation-proxy.md`, marcado como não verificado |
| Sunbiz | Busca por entidade devolveu 403 (anti-bot); busca por nome fictício 500 | `{{LEGAL_ENTITY}}`, `{{FICTITIOUS_NAME_STATUS}}` = OWNER INPUT |
