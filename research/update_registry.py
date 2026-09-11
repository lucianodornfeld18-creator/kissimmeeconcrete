# -*- coding: utf-8 -*-
"""Add/refresh the `kissimmee` hub in the network registry without touching other hubs."""
import json, csv, datetime, os

REG_DIR = r"C:\Users\luana\Documents\Codex\2026-09-03\pr\outputs\concrete-leadgen-network"
J = os.path.join(REG_DIR, "network-registry.json")
C = os.path.join(REG_DIR, "network-registry.csv")
today = datetime.date.today().isoformat()

reg = json.load(open(J, encoding="utf-8"))
hub = {
    "domain": "kissimmeeconcrete.com",
    "hub_id": "kissimmee",
    "public_name": "Kissimmee Concrete",
    "status_existing_or_new": "novo",
    "local_path": r"C:\Users\luana\Projetos\kissimmeeconcrete",
    "positioning": "Hub de concreto, pavers e hardscape para Kissimmee, Osceola County e o corredor US-27/I-4 de Polk (raio de 40 mi). Diferenciais: permits por jurisdição (Kissimmee/St. Cloud/Osceola/Polk), HOA/ARC verificadas (APV, Solivita, Celebration, Bellalago, Solterra), solos nomeados (Smyrna/Myakka/Candler), clima NOAA Kissimmee 2, Cost Index com metodologia e dataset, Permit Finder por endereço, Pour Calendar, calculadora concreto+pavers, casas de férias/STR.",
    "voice_rules": "Voz de prestador local, contrações, frases de tamanho variado, um fato verificável a cada 120-150 palavras, cápsulas de resposta de 40-70 palavras sob H2 em forma de pergunta, fontes primárias linkadas, nada de 'licensed' sem número, nada de N-Point checklist, nada de 'Why Choose Us' genérico. Lista de frases proibidas em site/qa_style.py.",
    "visual_family": {"display_font": "Montserrat (700/800, self-hosted OFL)", "body_font": "Source Sans 3 (variable, self-hosted OFL)", "palette": {"gold": "#B07828", "gold_light": "#D3A64A", "ink": "#1A1A1A", "surface": "#F2F2EF", "surface_2": "#E7E6E0", "line": "#D4D2CA", "text": "#202020", "muted": "#5C5B55", "focus": "#0B63C6", "dark_bg": "#161616", "dark_surface": "#1F1F1F", "dark_text": "#EDEAE2"}, "logo": "Owner-supplied stacked K mark (gold/charcoal) + KISSIMMEE / CONCRETE wordmark; horizontal lockup derived; brand/00-brand-guide.md", "collision_note": "Dourado colide parcialmente com Lakewood Ranch (#FFC84A/creme); diferenciado por tom (ouro escovado), fundo (branco/cinza-concreto), tipografia (Montserrat+Source Sans 3), hero com foto real e faixa de dados, sem tagline em rima."},
    "anchor_city": "Kissimmee",
    "radius_miles": 40,
    "cities_tier1": ["Kissimmee", "St. Cloud", "Celebration", "Poinciana", "Buenaventura Lakes", "Four Corners", "ChampionsGate", "Reunion", "Davenport", "Haines City", "Harmony/Narcoossee", "Loughman/Campbell/Intercession City (blocos)"],
    "cities_tier2_pages": ["Winter Haven", "Auburndale", "Lake Alfred", "Dundee", "Lake Wales", "Polk City"],
    "cities_mention_only": ["Lake Nona", "Hunters Creek", "Meadow Woods", "Southchase", "Williamsburg", "Taft", "Pine Castle", "Dr. Phillips", "Horizon West", "Windermere", "Orlando", "Winter Garden", "Ocoee", "Winter Park", "Belle Isle", "Edgewood", "Conway", "Oak Ridge", "Azalea Park", "Union Park", "Wedgefield", "Bithlo", "Pine Hills", "Gotha", "Oakland", "Maitland", "Altamonte Springs", "Casselberry", "Clermont", "Minneola", "Montverde", "Apopka", "Longwood", "Winter Springs", "Oviedo", "Groveland", "Mascotte", "Lake Mary", "Sanford", "Lakeland", "Mount Dora", "Bartow", "Frostproof", "Kenansville", "Holopaw"],
    "counties_owned": ["Osceola (todas as intenções)", "Polk norte / Ridge (Davenport, Haines City, Loughman, Poinciana-Polk, Winter Haven, Auburndale, Lake Alfred, Dundee, Lake Wales, Polk City)"],
    "counties_not_owned": ["Orange (Orlando/Ocoee/Windermere)", "Lake (Groveland/Windermere)", "Seminole (Orlando)"],
    "city_service_intent_owner": "44 city×service listadas em architecture/01-url-map-and-ownership.md; Kissimmee é a âncora das páginas de serviço (sem /<service>/kissimmee/).",
    "cannibalization_matrix": {
        "status": "condicional — GSC do Ocoee bloqueado nesta sessão (Windsor.ai free plan); nenhuma URL irmã alterada",
        "ocoeeconcrete.com": ["/concrete/kissimmee/", "/pavers/kissimmee/", "/blog/concrete-cost-kissimmee/", "/blog/paver-cost-kissimmee/", "/concrete|pavers/celebration/", "/concrete|pavers/davenport/", "/concrete|pavers/four-corners/", "+ blogs de custo dessas cidades"],
        "windermereconcrete.com": ["/kissimmee/", "/st-cloud/", "/celebration/", "/champions-gate/", "/davenport/"],
        "rule": "<50 impressões/mês e sem lead → 301 para a URL equivalente deste hub após indexação; com tráfego → manter 90 dias, reescrever intro, remover preços/FAQ, canonical autorreferente, reavaliar",
    },
    "service_catalog_published": ["concrete-driveways", "concrete-patios", "concrete-pool-decks", "concrete-stamped", "concrete-slabs", "concrete-sidewalks-walkways", "concrete-repair", "concrete-resurfacing", "concrete-architectural", "concrete-commercial", "paver-driveways", "paver-patios", "paver-pool-decks", "paver-travertine", "paver-marble-porcelain", "paver-walkways-steps", "paver-sealing", "paver-repair", "paver-retaining-walls-outdoor-living", "paver-artificial-turf", "paver-outdoor-lighting", "coatings-garage-floors"],
    "service_catalog_written_but_disabled": ["stucco (registry not_confirmed_do_not_use; aguarda confirmação do proprietário)"],
    "services_excluded": ["foundations/footings", "structural retaining walls", "pool shells", "room additions"],
    "primary_keyword_by_url": "architecture/02-titles-metas.csv (gerado no build)",
    "owned_questions": "research/04-150-questions.csv (150; cada uma com URL canônica única nesta rede)",
    "original_assets": ["Kissimmee Concrete Cost Index (/pricing/kissimmee-concrete-cost-index/ + /api/cost-index.json|csv, Dataset schema, CC BY 4.0)", "Permit & Jurisdiction Finder (/tools/permit-finder/, TIGERweb boundaries)", "Concrete & Paver Calculator", "Concrete vs Pavers Decision Tool", "HOA/ARC Packet Checklist", "Pour Calendar (NOAA Kissimmee 2 normals)", "Ask the Estimator (+ feed.xml)", "Project Brief generator"],
    "cta_offer": "Free on-site estimate; written proposal; call/text/form; EN/ES language preference on the form",
    "twilio_number": "{{KISSIMMEE_TWILIO_NUMBER}}",
    "email_alias": "hello@kissimmeeconcrete.com → {{MAIN_DESTINATION_EMAIL}}",
    "logo_decision": {"status": "CHOSEN BY OWNER 2026-09-10 (delivered with the Execute instruction)", "source_file": r"C:\Users\luana\Downloads\ChatGPT Image 10 de set. de 2026, 14_33_59.png", "note": "Prancha de 10 direções não produzida porque a escolha já veio pronta; registrado no AUDIT-60-POINT controle 13"},
    "domain_history": "Registrado 2026-01-01 (GoDaddy), comprado pelo proprietário 2026-09-10, sem histórico de conteúdo no Wayback, sem sinais tóxicos; nameservers ainda Afternic",
    "research_status": "complete_with_blocks (GSC, AI-citation test, Keyword Planner geolocalizado, ACS por cidade)",
    "writing_status": "in_progress",
    "qa_status": "in_progress",
    "publish_status": "not_started",
    "content_hash": "site/dist/CONTENT-HASHES.json (gerado no build)",
    "similarity_result": "site/audit/similarity-report.md (gerado no QA)",
    "updated": today,
}
hubs = [h for h in reg["hubs"] if h.get("hub_id") != "kissimmee"]
hubs.append(hub)
reg["hubs"] = hubs
reg["_meta"]["updated"] = today
reg["_meta"]["updated_by"] = "Claude (execução do 08-PROMPT-KISSIMMEE-CONCRETE.md)"
reg["_meta"]["real_provider_confirmed"].setdefault("catalog_notes", []).append({
    "date": today, "hub": "kissimmee",
    "note": "Prompt 08 pediu a união dos catálogos (Ocoee + LWR + GCM). Publicados neste hub além do catálogo GCM: epoxy/polyaspartic garage floors, sidewalks/walkways, commercial flatwork e parking lots (já anunciados publicamente pelo proprietário em ocoeeconcrete.com). Stucco continua em not_confirmed_do_not_use (conteúdo escrito e desativado). Foundations/estruturas continuam excluídas.",
})
json.dump(reg, open(J, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

rows = list(csv.DictReader(open(C, encoding="utf-8")))
rows = [r for r in rows if r["hub_id"] != "kissimmee"]
rows.append({"domain": "kissimmeeconcrete.com", "hub_id": "kissimmee", "public_name": "Kissimmee Concrete", "status": "novo", "local_path": r"C:\Users\luana\Projetos\kissimmeeconcrete", "anchor_city": "Kissimmee", "research_status": hub["research_status"], "writing_status": hub["writing_status"], "qa_status": hub["qa_status"], "publish_status": hub["publish_status"]})
with open(C, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print("registry updated:", len(reg["hubs"]), "hubs")
