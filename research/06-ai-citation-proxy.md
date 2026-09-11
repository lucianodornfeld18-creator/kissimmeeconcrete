# Teste de citação por IA — status: BLOCKED (proxy documentado)

Nesta sessão não há acesso a Google AI Mode/AI Overviews, ChatGPT Search, Bing Copilot, Perplexity, Gemini ou Claude com busca. O controle 9 do `AUDIT-60-POINT.md` fica **BLOCKED** até que o proprietário (ou uma sessão com navegador) rode os 60 prompts abaixo e registre resposta, fontes citadas e formato.

## Proxy usado agora

Para cada pergunta, a ferramenta de busca desta sessão devolveu as páginas que respondem hoje (são as candidatas naturais a citação). Padrão observado em 2026-09-10:

| Pergunta (prompt de teste) | Páginas que respondem hoje | O que elas têm | O que este hub entrega a mais |
|---|---|---|---|
| How much does a concrete driveway cost in Kissimmee/Orlando? | concretenetwork.com, angi.com/orlando, ocoeeconcrete.com/blog/concrete-cost-orlando, linkedconcrete.com, homeblue.com, homeadvisor | faixas por sq ft (US$ 6–10 broom, 12–18 stamped; demolição 2–4) | Cost Index por serviço e por cidade com data, metodologia, CSV/JSON e `Dataset` |
| How much does a paver driveway cost in Kissimmee? | homeyou, thumbtack, ksbrickpavers ("$12–26/sq ft"), jaxtellerbrickpavers, manta | faixas sem método | idem + fatores locais (Polk Paver Release, HOA) |
| Do I need a permit for a driveway in Osceola County? | osceola.org (aplicações), allcitypermits.com, um PDF de Osceola County **Michigan** (erro de entidade) | quase nada útil | `/permits/osceola-county/` com §22-50.6 citado, Permit Finder por endereço |
| Do I need a permit for a concrete patio/slab in Florida? | permitsguide.com, govcodex.com, miamidade.gov, broward.org | respostas de outros condados | páginas por jurisdição real (Kissimmee, St. Cloud, Osceola, Polk, Orange) |
| Pavers vs concrete driveway in Florida? | alliancepavers.com, ocoeeconcrete.com/blog/concrete-vs-pavers-driveway | comparação genérica | comparação com calor de superfície, HOA, custo por ciclo de vida, decision tool |
| Travertine vs concrete pavers pool deck (heat)? | localpaversllc.com (Orlando), american-outdoorliving.com, ntpavers.com, outercle.com, backbaypools.com | temperaturas "20–30 °F cooler", "130–140 °F vs 110–120 °F" sem método | tabela de temperatura com fonte citada e método de medição própria a executar em julho (Data & Methods) |
| Why does concrete crack in Florida? | luxcandoflorida.com, ynlconcrete.com, gcmbestservicescorp.com, alliancepavers.com | "sandy soil, high water table" genérico | solos nomeados (Smyrna/Myakka), lençol 12", juntas ACI 332, cura |
| Rust stains on driveway from irrigation? | larust.com, rustdoctorsfl.com, spraytekservices.com, ctigerclean.com, cascadianwater.com | causa (ferro do poço), remoção, prevenção | guia interativo de identificação de mancha |
| Best concrete contractor in Kissimmee FL? | thumbtack, houzz, yelp, angi (diretórios) | listas | não competimos com diretórios; entramos via GBP/Yelp reais (decisão do proprietário) |
| Paver sealing Kissimmee? | trtcleans, elitepaversealingfl, normile, jrpaversealing | serviços | sealer types compare + cronograma |
| Epoxy garage floor cost Kissimmee? | garageexperts, orlandoepoxyflooring, epoxycreations | franquias | polyaspartic vs epoxy + teste de umidade |

Observação de fundo (estudos citados no prompt e confirmados em busca de 2026-09-10): o uso de IA para achar negócios locais subiu de 6% para 45% em um ano; ~77% das fontes citadas sobre uma marca são off-page (diretórios, reviews, fóruns, vídeo); ChatGPT cruza GBP, Yelp, BBB, Bing Places e Foursquare e reduz a confiança quando o NAP diverge. Portanto, sem GBP e Yelp reais este hub não será citado por IA em buscas locais, por melhor que seja o conteúdo — é a decisão de negócio nº 1 no OWNER-INPUTS.

## Os 60 prompts a rodar (3 formatos × 20 temas)

Formato A "how much does X cost in Kissimmee": concrete driveway; paver driveway; 12×12 concrete patio; paver patio; 600 sq ft pool deck pavers; travertine pool deck; stamped concrete patio; concrete slab for a shed; driveway extension; concrete driveway replacement; paver sealing; paver repair (sinking); concrete repair (crack); concrete resurfacing; epoxy garage floor; retaining wall (decorative); walkway pavers; artificial turf; outdoor lighting; concrete pad for AC/generator.

Formato B "best concrete contractor in Kissimmee FL" / "best paver company in St. Cloud FL" / Celebration / Poinciana / Davenport / ChampionsGate / Haines City / Four Corners / Buenaventura Lakes / Harmony + "who installs travertine pool decks near Reunion FL" + 9 variações "near me" com cidade.

Formato C "do I need a permit for X in Osceola County": driveway; driveway widening; patio slab; shed pad; pavers; pool deck; sidewalk in the right-of-way; in the City of Kissimmee; in St. Cloud; in Polk County (Davenport); + "does my HOA in Poinciana/Celebration/Solterra/Bellalago/Solivita need to approve pavers"; + "how thick should a driveway be in Florida", "3000 or 4000 psi for a driveway", "rebar or wire mesh", "how long before I can drive on new concrete", "can you pour concrete in the rain in Florida", "why does my driveway have rust stains", "when should I seal pavers in Florida", "polymeric sand or regular sand".

Registrar para cada: motor, data, resposta resumida, fontes citadas (URL), formato (tabela/lista/parágrafo), o que a fonte citada tem que ainda não temos.
