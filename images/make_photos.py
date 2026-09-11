# -*- coding: utf-8 -*-
"""Photo pipeline for kissimmeeconcrete.com.

Reads the owner's library (C:/Users/luana/Projetos/Concreto Fotos), applies EXIF
orientation, privacy crops/blurs (address overlays, third-party signage, license
plates, house numbers), strips metadata by re-encoding, and writes
site/static/images/<slug>-{1600,960,480}.webp plus images/photos.json.

kind = "real"      provider job photo (Central Florida; not asserted as Kissimmee)
kind = "rendering" AI concept image; labelled "Concept rendering" on the page.
The real/rendering classification matches the review done for the Groveland hub
on 2026-09-09 (images/MANIFEST.md there), re-checked visually on 2026-09-10.
"""
from PIL import Image, ImageOps, ImageFilter
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "C:/Users/luana/Projetos/Concreto Fotos/"
OUT = os.path.join(HERE, "..", "site", "static", "images")
os.makedirs(OUT, exist_ok=True)

# (source, slug, kind, services, alt, ops)
P = [
    ("6BAF8FC5-7847-4205-9DB7-6987FBE91485.png", "marble-pool-deck-under-screen-enclosure", "real",
     ["paver-pool-decks", "paver-marble-porcelain", "paver-travertine"],
     "Polished marble pavers on a pool deck inside a screened lanai, with the pool step and coping visible in the background", {}),
    ("73e2a25b-5b8e-46ff-bde0-1d8f71df2bb7.jpeg", "front-entry-steps-porcelain-treads-new-build", "real",
     ["paver-walkways-steps", "concrete-sidewalks-walkways", "concrete-architectural"],
     "Front entry steps on a new build, poured in concrete and capped with large-format porcelain treads between stucco cheek walls", {"crop_bottom": 0.21}),
    ("CONCRETE PATIO DAVENPORT.jpeg", "square-concrete-paver-patio-gravel-joints-backyard", "real",
     ["paver-patios", "concrete-patios"],
     "Backyard patio of large square concrete pavers laid on a compacted base with open gravel joints, fenced yard behind", {}),
    ("CONCRETE SERVICE IN KISSIMMEE.png", "curved-raised-terrace-stone-wall-cedar-pergola", "real",
     ["paver-retaining-walls-outdoor-living", "paver-patios", "concrete-patios"],
     "Curved raised terrace with a stone-veneer wall face and a cedar pergola, built off the rear of a lakefront home during construction", {}),
    ("IMG_1966.jpeg", "charcoal-slate-texture-paver-detail-border", "real",
     ["paver-driveways", "paver-repair", "paver-sealing"],
     "Close view of charcoal slate-textured pavers with a soldier-course border, joints sanded and aligned", {}),
    ("IMG_2877.jpeg", "wide-gray-paver-driveway-charcoal-grid-street-view", "real",
     ["paver-driveways"],
     "Wide gray paver driveway with charcoal grid banding and border, looking from the garage toward the street and the paver entry pillar", {}),
    ("IMG_2879.jpeg", "paver-clad-entry-pillar-wall-light-driveway", "real",
     ["paver-driveways", "paver-outdoor-lighting", "paver-retaining-walls-outdoor-living"],
     "Paver-clad entry pillar with a mounted light fixture at the edge of a gray and charcoal paver driveway", {"blur": [(2600, 1300, 2900, 1450)]}),
    ("IMG_2882.jpeg", "gray-paver-driveway-charcoal-bands-two-car-garage", "real",
     ["paver-driveways", "paver-walkways-steps"],
     "Gray paver driveway with charcoal cross bands running up to a dark two-car garage, with a matching side walkway along the hedge", {"blur": [(720, 1480, 940, 1580)]}),
    ("IMG_4183.jpeg", "bullnose-marble-pool-coping-curved-edge", "real",
     ["paver-pool-decks", "paver-marble-porcelain"],
     "Bullnose marble coping following the curve of a pool edge, with matching marble field pavers on the deck", {}),
    ("IMG_4204.jpeg", "marble-paver-lanai-pool-deck-drain-channel", "real",
     ["paver-pool-decks", "paver-marble-porcelain", "paver-outdoor-lighting"],
     "Full marble paver pool deck inside a screened lanai, with a linear drain channel and a freeform pool with rock waterfall", {}),
    ("IMG_4455.jpeg", "paver-driveway-install-in-progress-staged-stacks", "real",
     ["paver-driveways", "paver-repair"],
     "Paver driveway installation in progress: stacks of gray pavers staged on the screeded bedding sand while the crew sets the field", {"crop_right": 0.16}),
    ("IMG_4457.jpeg", "paver-stacks-along-driveway-edge-bedding-sand", "real",
     ["paver-driveways"],
     "Stacks of pavers lined up along the lawn edge of a driveway during installation, showing the screeded bedding layer", {}),
    ("IMG_5036.jpeg", "tumbled-travertine-look-pool-deck-drain-oaks", "real",
     ["paver-pool-decks", "paver-travertine"],
     "Tumbled travertine-look paver pool deck with a drain channel around a rectangular pool, shaded by mature oaks", {}),
    ("PAVER DECK WINDERMERE.jpeg", "tan-tumbled-paver-patio-under-dark-pergola", "real",
     ["paver-patios", "paver-retaining-walls-outdoor-living"],
     "Tumbled tan-blend paver patio under a dark-stained wood pergola behind a single-story stucco home", {}),
    ("PAVER DRIVEWAY OCOEE.jpeg", "mixed-gray-tan-terracotta-paver-driveway-garage", "real",
     ["paver-driveways"],
     "Random-ashlar paver driveway in mixed gray, tan and terracotta tones in front of a two-car garage", {"blur": [(465, 220, 525, 252), (455, 350, 515, 375)]}),
    ("PAVER DRIVEWAY WINTER GARDEN.jpeg", "tan-blend-paver-driveway-color-option-concept", "rendering",
     ["paver-driveways"],
     "Color concept rendering of the same driveway in a tan blend, meeting a poured concrete apron at the street", {"blur": [(465, 220, 525, 252), (455, 350, 515, 375)]}),
    ("PAVER PATIO DAVENPORT.jpeg", "multi-level-paver-patio-raised-pool-terrace-construction", "real",
     ["paver-patios", "paver-retaining-walls-outdoor-living", "paver-pool-decks"],
     "Multi-level paver patio under construction, with a raised pool terrace, paver-faced step risers and a wet saw on site", {}),
    ("PAVER CONCRETE OCOEE.jpeg", "tan-paver-front-walkway-soldier-border-concept", "rendering",
     ["paver-walkways-steps"],
     "Concept rendering of a tan paver front walkway with a soldier-course border toward a covered entry", {}),
    ("PAVER DRIVEWAY FOUR CORNERS.jpeg", "curved-tan-paver-driveway-charcoal-border-concept", "rendering",
     ["paver-driveways"],
     "Concept rendering of a curved tan paver driveway edged in charcoal in front of a tile-roof home", {}),
    ("PAVER DRIVEWAY KISSIMMEE.jpeg", "aerial-curved-paver-driveway-oaks-concept", "rendering",
     ["paver-driveways"],
     "Aerial concept rendering of a curved paver driveway with a dark border between two live oaks", {}),
    ("PAVER DRIVEWAY WINTER GARDEN (2).jpeg", "brick-tone-paver-walkway-running-bond-concept", "rendering",
     ["paver-walkways-steps"],
     "Concept rendering of a brick-tone paver walkway in running bond with a border course leading to a front door", {"crop_top": 0.15}),
    ("PAVER IN APOPKA.jpeg", "small-tan-paver-patio-bistro-fence-concept", "rendering",
     ["paver-patios"],
     "Concept rendering of a compact tan paver patio with a bistro set beside a wood privacy fence", {}),
    ("PAVER RENOVATION OCOEE.jpeg", "paver-entry-courtyard-planting-beds-concept", "rendering",
     ["paver-walkways-steps", "paver-patios"],
     "Concept rendering of a paver entry courtyard with planting beds cut into the field", {}),
    ("PAVERS WALKWAY WINTER GARDEN.jpeg", "gray-paver-walkway-entry-step-dusk-lights-concept", "rendering",
     ["paver-walkways-steps", "paver-outdoor-lighting"],
     "Concept rendering of a gray paver walkway and entry step with recessed lights at dusk", {}),
    ("PAVERS WITH LIGHT WINDERMERE.jpeg", "curved-paver-steps-riser-lighting-concept", "rendering",
     ["paver-walkways-steps", "paver-outdoor-lighting"],
     "Concept rendering of curved paver entry steps with integrated riser lighting and a winding walkway", {}),
]

out = []
for src, slug, kind, services, alt, ops in P:
    im = ImageOps.exif_transpose(Image.open(SRC + src)).convert("RGB")
    w, h = im.size
    if "crop_bottom" in ops:
        im = im.crop((0, 0, w, int(h * (1 - ops["crop_bottom"]))))
    if "crop_top" in ops:
        im = im.crop((0, int(h * ops["crop_top"]), w, h))
    if "crop_right" in ops:
        im = im.crop((0, 0, int(w * (1 - ops["crop_right"])), h))
    for box in ops.get("blur", []):
        reg = im.crop(box).filter(ImageFilter.GaussianBlur(18))
        im.paste(reg, box[:2])
    m = im.copy(); m.thumbnail((2400, 2400), Image.LANCZOS)
    m.save(os.path.join(HERE, slug + ".jpg"), quality=90)  # re-encode = metadata stripped
    sizes = {}
    for W in (1600, 960, 480):
        r = im.copy(); r.thumbnail((W, W), Image.LANCZOS)
        r.save(os.path.join(OUT, f"{slug}-{W}.webp"), quality=80 if W == 1600 else 82, method=6)
        sizes[W] = r.size
    out.append({"slug": slug, "kind": kind, "services": services, "alt": alt, "source": src,
                "w": sizes[1600][0], "h": sizes[1600][1], "privacy_ops": sorted(ops.keys())})
    print(kind.ljust(9), slug, sizes[1600], os.path.getsize(os.path.join(OUT, f"{slug}-1600.webp")) // 1024, "KB")

json.dump(out, open(os.path.join(HERE, "photos.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# Home hero: IMG_2882 (gray paver driveway to garage) cropped 16:9, plate blurred.
im = ImageOps.exif_transpose(Image.open(SRC + "IMG_2882.jpeg")).convert("RGB")
reg = im.crop((720, 1480, 940, 1580)).filter(ImageFilter.GaussianBlur(18)); im.paste(reg, (720, 1480))
w, h = im.size
ch = int(w * 9 / 16); top = int(h * 0.40)
hero = im.crop((0, top, w, top + ch))
for W in (1600, 1200, 800):
    r = hero.copy(); r.thumbnail((W, W)); r.save(os.path.join(OUT, f"hero-paver-driveway-{W}.webp"), quality=76, method=6)
    print("hero", W, r.size, os.path.getsize(os.path.join(OUT, f"hero-paver-driveway-{W}.webp")) // 1024, "KB")
t = hero.copy(); t.thumbnail((40, 40)); t.save(os.path.join(OUT, "hero-lqip.webp"), quality=35, method=6)
print("lqip bytes", os.path.getsize(os.path.join(OUT, "hero-lqip.webp")))
print(len(out), "photos written")
