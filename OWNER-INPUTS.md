# OWNER-INPUTS — kissimmeeconcrete.com

Atualizado em 2026-09-11. Tudo abaixo bloqueia **publicação** ou **precisão**, não o build: o site está construído, auditado e pronto para preview. Os itens estão em ordem de urgência.

---

## A. Bloqueiam a publicação (sem isso o site não vai ao ar)

### A1. Entidade legal e nome fictício
| Campo | Estado | O que preciso |
|---|---|---|
| `{{LEGAL_ENTITY}}` | **pendente** | Nome legal exato e nº Sunbiz da entidade que executa e fatura: GCM Best Services Corp, ou uma LLC própria. Aparece no contrato, na About e no rodapé. |
| `{{FICTITIOUS_NAME_STATUS}}` | **pendente** | "Kissimmee Concrete" registrado como nome fictício (DBA) na Sunbiz? **Recomendo registrar.** Sem DBA o nome público não pode se apresentar como empresa, e existe um concorrente usando "Kissimmee Concrete" como nome de exibição em `kissimmeeconcrete.net`. O DBA também protege o nome. |
| `{{INSURANCE_PROOF}}` | **pendente** | Seguradora, nº de apólice, limites e vigência. O site diz "Insured" em vários lugares; preciso da COI para manter a palavra. Se não houver apólice ativa, removo a palavra do site inteiro em uma rodada. |

Sunbiz respondeu 403 às consultas automatizadas nesta sessão; a verificação tem de ser manual em `search.sunbiz.org`.

### A2. Telefone Twilio
| Campo | Estado |
|---|---|
| `{{KISSIMMEE_TWILIO_NUMBER}}` | **pendente** |

O site hoje roda **sem telefone**: todos os CTAs são o formulário e o e-mail, e não há placeholder falso em lugar nenhum. Assim que o número existir, é uma linha em `site/_data.py` (`PHONE_DISPLAY` e `PHONE_E164`) e o build reintroduz o botão de ligar, o `tel:` no rodapé, o CTA móvel e o `telephone` no schema `Organization`.

Passo a passo, seguindo o padrão já usado na sua conta Twilio:
1. Comprar um número local 407 ou 321.
2. Criar o serviço Functions `kissimmee-voice` (mesmo modelo dos outros sites).
3. Definir `FORWARD_TO` = seu telefone.
4. Apontar o Voice webhook do número para a função.
5. Testar ligando do celular e confirmando o encaminhamento.

### A3. DNS, e-mail e Cloudflare
| Item | Estado | Ação |
|---|---|---|
| Nameservers | **Afternic** | Mover `kissimmeeconcrete.com` para a Cloudflare (a zona precisa existir na conta para Pages + Email Routing). O domínio está registrado desde 2026-01-01 na GoDaddy e foi comprado por você em 2026-09-10. |
| `hello@kissimmeeconcrete.com` | **pendente** | Cloudflare Email Routing → `{{MAIN_DESTINATION_EMAIL}}`. O e-mail já está publicado no site como canal principal de contato. |
| `{{MAIN_DESTINATION_EMAIL}}` | **pendente** | Para onde os leads vão. Vai como secret `CONTACT_DESTINATION` no Worker. |
| Turnstile | **pendente** | Criar um widget Turnstile para o domínio. A chave pública vai em `_data.TURNSTILE_SITE_KEY`, a secreta como `TURNSTILE_SECRET_KEY` na Pages Function. Sem ela o formulário funciona, mas só com honeypot e rate limit. |
| Repositório GitHub | **pendente** | `gh` não está autenticado nesta máquina. Enquanto isso o deploy é por `wrangler pages deploy`. |

### A4. Google Business Profile e Yelp — decisão de negócio nº 1
`{{GBP_DECISION}}` — **pendente e urgente.**

Este é o item com maior impacto e o único que nenhuma quantidade de conteúdo substitui. Os estudos de 2026 citados no prompt mostram que Google Business Profile é a fonte nº 1 para AI Overviews em buscas locais e Yelp a nº 1 para ChatGPT. Sem perfil verdadeiro, este hub não é citado por IA em consulta local, por melhor que seja o texto.

Três caminhos, e preciso que você escolha um:
1. **GBP próprio para Kissimmee Concrete** — exige endereço real verificável ou service-area business com endereço de verificação. Não crie NAP inventado.
2. **Usar o perfil da GCM** — legítimo, e então o site exibe os depoimentos como citações atribuídas ao perfil da GCM, com link, sem `AggregateRating` no schema.
3. **Adiar** — é a situação atual, e significa aceitar que a citação local por IA fica fora de alcance por enquanto.

`{{REVIEWS_SOURCE}}`: relacionado. As 59 avaliações 4,9 da GCM só podem aparecer aqui se a entidade for a mesma e a página deixar claro de qual perfil vêm. **Hoje o site não exibe nenhuma avaliação, nota, contagem de projetos ou anos de atuação**, exatamente porque nada disso está documentado para esta marca.

---

## B. Afetam a precisão do conteúdo (o site já trata cada um honestamente)

### B1. Catálogo de serviços — confirmar ou remover
O prompt pediu a união dos catálogos de Ocoee, Lakewood Ranch e GCM. Publiquei o que você já anuncia publicamente; confirme cada linha:

| Serviço | Situação | Preciso |
|---|---|---|
| Concrete driveways, patios, pool decks, stamped, slabs, sidewalks, repair, resurfacing | Publicado | Confirmar |
| Architectural concrete, luxury pavers, travertine, marble/porcelain, pool decks, patios, retaining walls decorativas, artificial turf, outdoor lighting | Publicado (catálogo GCM confirmado) | Confirmar |
| **Epoxy/polyaspartic garage floors** | Publicado | Você executa (própria ou subcontratado identificado)? Está no ocoeeconcrete.com mas não no catálogo GCM. |
| **Commercial flatwork e parking lots pequenos** | Publicado, com limites de escopo declarados | Confirmar |
| **Sidewalks em right-of-way** | Publicado | Confirmar |
| **Stucco** | **Escrito e desativado** | O registry marca como `not_confirmed_do_not_use`. A página existe em `content_services_coatings.py` e liga com uma linha em `_data.py` se você confirmar. |
| Foundations, footings, muros estruturais, pool shells | **Excluídos** | Exigem licença não confirmada. Mantenho fora. |

### B2. Autor nomeado
`{{AUTHOR}}` — **pendente.** Hoje os artigos levam `author` = Organization. Com um nome real, bio e credencial verificável, passo a emitir `Person` com `sameAs`, o que é um sinal E-E-A-T relevante. Não invento um autor.

### B3. Garantia
`{{WARRANTY_TERMS}}` — **pendente.** A página `/warranty/` explica cobertura, exclusões e processo de acionamento, mas **sem prazo**, porque não foi definido. Preciso do prazo e das condições de transferência.

### B4. Financiamento
`{{FINANCING_PARTNER}}` — **pendente.** A FAQ de custo diz textualmente que ainda não há parceiro definido e manda perguntar. Não nomeio um parceiro que não existe.

### B5. Fotos e projetos reais de Osceola
Estado atual: 25 imagens processadas da sua biblioteca — 17 fotos reais do prestador e 8 renderings, todos rotulados "Concept rendering" no badge, na legenda e no alt text. As fotos reais **não são afirmadas como sendo de Kissimmee**; o alt text diz Central Florida.

Privacidade já tratada no pipeline: overlay com endereço de Windermere cortado, logo GCM em rendering cortado, placa de obra de terceiro com telefone cortada, placas de carro e número de casa borrados, metadados removidos por reencode.

Preciso de: **20–30 fotos de obras em Osceola** (Kissimmee, St. Cloud, Celebration, Poinciana, BVL, Four Corners) e **5–10 projetos documentados** com cidade, serviço, metragem, material, desafio, solução, prazo e faixa de preço. Com isso as páginas de cidade ganham prova local real e `/projects/` pode existir.

### B6. Dados para o Cost Index
O release Q3 2026 é um **composto de mercado** declarado como tal: preços de fornecedor, referências regionais publicadas e nossos próprios levantamentos. A página `/data-and-methods/` diz isso explicitamente.

Para o próximo release preciso de **orçamentos executados anonimizados**: serviço, cidade, metragem, preço, data. Sem nome, endereço ou telefone. Com cinco ou mais por item, a linha passa de composto para amostra e o índice vira um ativo genuinamente citável.

### B7. Perguntas reais recebidas
A ferramenta `/tools/ask-the-estimator/` existe e tem feed RSS. Preciso de perguntas reais recebidas por telefone e formulário (Ocoee e GCM servem), anonimizadas. É a fonte mais valiosa de conteúdo que existe e não pode ser inventada.

---

## C. Bloqueios de acesso desta sessão (não são decisões suas, são credenciais)

| Recurso | O que aconteceu | Para destravar |
|---|---|---|
| **Search Console do Ocoee** | O conector Windsor.ai tem `sc-domain:ocoeeconcrete.com` mas o plano free pausou leituras (13 contas conectadas, limite 1) | Desconectar contas no Windsor **ou** exportar CSV de 16 meses direto do Search Console. Isso destrava a matriz de canibalização (controle 54) — sem os dados **nenhuma URL do Ocoee ou do Windermere foi alterada ou redirecionada**. |
| **Keyword Planner geolocalizado** | Sem navegador nesta sessão | Exportar do Chrome autenticado com localização = Kissimmee, Osceola County e cada cidade Tier 1/2. A exportação de 2026-09-07 (846 consultas, Flórida) foi usada como base. |
| **Teste de citação por IA** | Sem acesso a AI Mode, ChatGPT, Perplexity, Gemini, Copilot | Os 60 prompts estão escritos em `research/06-ai-citation-proxy.md`, prontos para rodar. Controle 9 = BLOCKED. |
| **Census API / ACS** | API pede chave; Census Reporter devolveu 403 | Chave gratuita em `api.census.gov/data/key_signup` para completar idade do estoque de casas por cidade. Hoje o site usa só épocas de desenvolvimento documentadas. |
| **Sunbiz / Yelp / kissimmeeconcretecontractors.com** | 403 anti-bot | Verificação manual. |
| **Safe Browsing do domínio** | Página responde 200 mas o veredito é renderizado por JS | Conferir manualmente em `transparencyreport.google.com/safe-browsing/search?url=kissimmeeconcrete.com`. Wayback mostra domínio sem histórico de conteúdo, então o risco é baixo. |
| **GitHub CLI** | Não autenticado | `gh auth login` para conectar Pages ao repositório. |

---

## D. O que fazer na ordem, quando você tiver 30 minutos

1. Mover os nameservers do domínio para a Cloudflare.
2. Decidir A4 (GBP/Yelp) — é o item de maior impacto.
3. Comprar o número Twilio e montar `kissimmee-voice`.
4. Criar o Email Routing e o widget Turnstile, me passar as chaves.
5. Confirmar o catálogo (B1) e a garantia (B3).
6. Exportar o Search Console do Ocoee (C) para eu fechar a matriz de canibalização.
7. Mandar as fotos de Osceola e os projetos documentados (B5).

Com 1 a 4, o site publica. 5 a 7 melhoram precisão e diferenciação, e podem vir depois.
