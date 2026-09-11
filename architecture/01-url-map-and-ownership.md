# Arquitetura, mapa de URLs e propriedade de intenções — kissimmeeconcrete.com

Data: 2026-09-10. Estático, uma intenção por URL, trailing slash, minúsculas, sem datas/parâmetros, breadcrumbs em toda página interna, profundidade ≤ 3 cliques.

## Decisões de escopo (e por quê)

1. **Serviços publicados** (23): concreto (driveways, patios, pool decks, stamped & decorative, slabs & pads, sidewalks & walkways, repair, resurfacing & overlays, architectural, commercial) + pavers & hardscape (driveways, patios, pool decks, travertine, marble & porcelain, walkways & steps, sealing & cleaning, repair, retaining walls & outdoor living, artificial turf, outdoor lighting) + coatings (epoxy/polyaspartic garage floors). Epoxy, sidewalks e commercial já são anunciados publicamente pelo próprio proprietário em ocoeeconcrete.com; architectural/turf/lighting/retaining walls decorativas/travertine/marble estão no catálogo real da GCM.
2. **Não publicados**: stucco (registry `not_confirmed_do_not_use`; conteúdo escrito e desativado em `content_services_coatings.py` até confirmação), foundations/footings/muros estruturais (exigem licença não confirmada), pool shells, room additions.
3. **Kissimmee é a âncora das páginas de serviço**; por isso não existe `/concrete/driveways/kissimmee/` (seria duplicata). O city hub `/areas/kissimmee/` cobre bairros e jurisdição.
4. **City×service Tier 1 (44 URLs)** só para combinações com sinal de demanda (Trends/autocomplete/tipo de estoque de casas) e com bloco local verificável. Tier 2 (Polk: 6 city hubs) cobre os 4 serviços de maior demanda em seções da própria página; URLs city×service Tier 2 ficam adiadas até 90 dias de GSC (controle 22, doorway policy).
5. **Cidades de Orange/Lake/Seminole** só como texto em `/areas/` e no hub `/areas/orange-county-south/` (nenhuma liberação registrada no registry pelos hubs vizinhos).
6. **/es/** adiado (sem volume mensurável e sem confirmação de atendimento em espanhol); o formulário oferece idioma preferido.
7. **/reviews/, /directories/, /projects/** ficam fora do build até haver perfis, avaliações e projetos reais com fonte (OWNER INPUT). **/warranty/** publica como funciona a garantia de mão de obra por escrito (modelo aprovado pelo proprietário para o Groveland em 2026-09-09), sem prazos até `{{WARRANTY_TERMS}}`.
8. **Autor**: sem pessoa real confirmada, artigos levam `author` = Organization (Kissimmee Concrete) e "Reviewed by the Kissimmee Concrete estimating desk" **não** é usado (seria uma equipe inventada). O campo `{{AUTHOR}}` está no OWNER-INPUTS; quando vier, `_data.py` passa a emitir `Person` com `sameAs`.

## Mapa de URLs (156 rotas indexáveis + 2 noindex)

```
/                                   Home
/concrete/                          Pilar concreto
/concrete/driveways/ /concrete/patios/ /concrete/pool-decks/ /concrete/stamped/ /concrete/slabs/
/concrete/sidewalks-walkways/ /concrete/repair/ /concrete/resurfacing/ /concrete/architectural/ /concrete/commercial/
/pavers/                            Pilar pavers & hardscape
/pavers/driveways/ /pavers/patios/ /pavers/pool-decks/ /pavers/travertine/ /pavers/marble-porcelain/
/pavers/walkways-steps/ /pavers/sealing/ /pavers/repair/ /pavers/retaining-walls-outdoor-living/
/pavers/artificial-turf/ /pavers/outdoor-lighting/
/coatings/garage-floors/
/concrete/<service>/<city>/ e /pavers/<service>/<city>/   44 city×service (lista abaixo)
/areas/                             Área de atendimento (tiers, 70+ localidades, tempos estimados)
/areas/osceola-county/ /areas/polk-county/ /areas/orange-county-south/
/areas/kissimmee/ /areas/st-cloud/ /areas/celebration/ /areas/poinciana/ /areas/buenaventura-lakes/
/areas/four-corners/ /areas/champions-gate/ /areas/reunion/ /areas/davenport/ /areas/haines-city/ /areas/harmony/
/areas/winter-haven/ /areas/auburndale/ /areas/lake-alfred/ /areas/dundee/ /areas/lake-wales/ /areas/polk-city/
/pricing/ /pricing/concrete/ /pricing/pavers/ /pricing/kissimmee-concrete-cost-index/
/permits/ /permits/city-of-kissimmee/ /permits/osceola-county/ /permits/city-of-st-cloud/ /permits/polk-county/ /permits/orange-county/
/hoa/ /hoa/poinciana-apv/ /hoa/solivita/ /hoa/celebration/ /hoa/bellalago/ /hoa/solterra/
/compare/ + concrete-vs-pavers, travertine-vs-concrete-pavers, stamped-vs-pavers, resurface-vs-replace,
           4-inch-vs-6-inch, rebar-vs-fiber-vs-mesh, cool-deck-vs-pavers, sealer-types
/tools/ + permit-finder, concrete-paver-calculator, concrete-vs-pavers, hoa-packet-checklist, pour-calendar,
          ask-the-estimator, project-brief
/faq/ /faq/concrete/ /faq/pavers/ /faq/permits-hoa/ /faq/cost/
/guides/ + 14 guias (lista em content_guides.py)
/gallery/ /about/ /editorial-standards/ /data-and-methods/ /warranty/ /contact/
/privacy/ /terms/ /accessibility/ /404/
/thank-you/ (noindex)
/sitemap.xml /robots.txt /llms.txt /llms-full.txt /feed.xml /api/cost-index.json /api/cost-index.csv /site.webmanifest
```

City×service (44): st-cloud ×6 (concrete/driveways, concrete/slabs, concrete/repair, pavers/driveways, pavers/pool-decks, pavers/sealing); celebration ×5 (pavers/driveways, pavers/pool-decks, pavers/sealing, pavers/walkways-steps, concrete/repair); poinciana ×4 (concrete/driveways, concrete/patios, concrete/repair, pavers/driveways); buenaventura-lakes ×4 (concrete/driveways, concrete/repair, concrete/resurfacing, pavers/driveways); four-corners ×4 (pavers/pool-decks, pavers/sealing, pavers/driveways, concrete/repair); champions-gate ×4 (pavers/pool-decks, pavers/sealing, pavers/driveways, concrete/repair); reunion ×4 (pavers/pool-decks, pavers/travertine, pavers/sealing, pavers/driveways); davenport ×5 (concrete/driveways, pavers/driveways, pavers/pool-decks, concrete/repair, concrete/slabs); haines-city ×4 (concrete/driveways, concrete/patios, concrete/repair, pavers/driveways); harmony ×4 (concrete/driveways, concrete/slabs, pavers/driveways, pavers/pool-decks).

## Matriz de canibalização (seção 2.1) — decisão por URL conflitante

Regra: sem GSC (bloqueado nesta sessão), **nenhuma URL irmã é redirecionada ou alterada agora**. A tabela fixa a decisão condicional que será executada quando a exportação de 16 meses chegar e este hub estiver indexado.

| URL irmã | Intenção | URL proprietária neste hub | Decisão condicional |
|---|---|---|---|
| ocoeeconcrete.com/concrete/kissimmee/ | concrete × Kissimmee | `/concrete/` + `/areas/kissimmee/` | < 50 impressões/mês e sem lead → 301 para `/areas/kissimmee/` após indexação; senão manter 90 dias com intro "serving Kissimmee from West Orange", remover seção de preços/FAQ, canonical autorreferente, reavaliar |
| ocoeeconcrete.com/pavers/kissimmee/ | pavers × Kissimmee | `/pavers/` + `/areas/kissimmee/` | idem |
| ocoeeconcrete.com/blog/concrete-cost-kissimmee/ | custo concreto × Kissimmee | `/pricing/concrete/` | 301 na mesma janela |
| ocoeeconcrete.com/blog/paver-cost-kissimmee/ | custo pavers × Kissimmee | `/pricing/pavers/` | 301 na mesma janela |
| ocoeeconcrete.com/concrete|pavers/celebration/ + blogs | Celebration | `/areas/celebration/`, `/pavers/driveways/celebration/`… | idem matriz |
| ocoeeconcrete.com/concrete|pavers/davenport/ + blogs | Davenport | `/areas/davenport/`, city×service | idem (o Ocoee **rankeia** hoje em "concrete contractor davenport" → tratar como URL com tráfego: manter 90 dias) |
| ocoeeconcrete.com/concrete|pavers/four-corners/ + blogs | Four Corners | `/areas/four-corners/` | idem |
| windermereconcrete.com/kissimmee/, /st-cloud/, /celebration/, /champions-gate/, /davenport/ | city hubs | `/areas/<cidade>/` | não indexadas (set/2026) → 301 para `/areas/<cidade>/` assim que este hub indexar; até lá ficam vivas |
| windermereconcrete.com/lake-nona/ | Lake Nona | — (Orange) | mantém no Windermere |
| gcmbestservicescorp.com/areas/kissimmee/, /blog/hardscape-costs-kissimmee/ | marca-mãe | — | permanecem; cost guide deste hub tem escopo/dados/público diferentes |
| stcloudflconcrete.com/* | terceiro | — | concorrente; benchmark |

Títulos, H1 e primeiras frases deste hub foram escritos do zero e checados contra as 4 pastas irmãs (`site/qa_similarity.py`).

## Interlinks

Home → pilares, Tier 1, ferramentas, cost guides. Pilar → serviços + hubs de condado. Serviço → suas city×service + comparações + cost guide + FAQ do pilar. City hub → serviços com demanda na cidade + city×service + permit da jurisdição + HOA. City×service → serviço, cidade, 2–4 recursos. Guia → próxima etapa comercial + fontes. Sem links para domínios irmãos.

## Fórmulas de title/H1 (aplicadas em `_seo.py`)

Home `Kissimmee Concrete | Concrete & Paver Contractor, Kissimmee FL`; pilar `Concrete Contractor in Kissimmee, FL – Driveways, Patios, Slabs`; serviço `Concrete Driveways in Kissimmee, FL – Cost, Thickness, Permits`; city×service `Concrete Driveways in St. Cloud, FL – Osceola Permits & Cost`; city hub `Concrete & Pavers in St. Cloud, FL – Local Contractor Guide`; cost guide `Concrete Cost in Kissimmee, FL (2026): Per Sq Ft & By Project`; permit `Do You Need a Permit for a Driveway in Osceola County? (2026)`; comparação `Pavers vs. Concrete Driveway in Central Florida: Cost & Heat`; FAQ `Concrete Questions Kissimmee Homeowners Ask (Answered)`. Sem "Best/#1/Top-Rated", sem ano em páginas comerciais permanentes.
