#!/usr/bin/env python3
"""Wandelt einen OpenStreetMap-Export (.osm XML) in die Spieldaten data/altstadt.js um.

Kartendaten holen (Altstadt + Rheinufer + Kö):
    curl -o altstadt.osm "https://api.openstreetmap.org/api/0.6/map?bbox=6.7650,51.2210,6.7840,51.2320"
Umwandeln:
    python3 tools/osm_to_game.py altstadt.osm data/altstadt.js

Koordinaten im Spiel: Meter, x = Osten, z = Süden (Three.js: -z ist Norden),
Ursprung an der Ecke Bolkerstraße / Kurze Straße.
Kartendaten (c) OpenStreetMap-Mitwirkende, Lizenz ODbL.
"""
import json
import math
import sys
import xml.etree.ElementTree as ET

LAT0, LON0 = 51.2266, 6.7735
KX = math.cos(math.radians(LAT0)) * 111320.0
KZ = 110540.0
# Ausschnitt (Meter um den Ursprung), in dem der Rhein ins Spiel kommt
RIVER_BOX = 1400.0
# Rheinufer-Wege der Rhein-Wasserfläche (Relation 13897550)
EAST_BANK, WEST_BANK = "147532933", "979866285"

ROAD_TYPES = {"trunk": 3, "primary": 3, "secondary": 2, "tertiary": 2, "residential": 1,
              "living_street": 1, "service": 1, "unclassified": 1}
WALK_TYPES = {"pedestrian": 4, "footway": 5, "path": 5, "steps": 6, "cycleway": 5, "platform": 5,
              "corridor": 5}
POI_TYPES = {"bar": 0, "pub": 1, "nightclub": 2, "biergarten": 1}


def xz(lat, lon):
    return (round((lon - LON0) * KX, 1), round(-(lat - LAT0) * KZ, 1))


def hash_id(s):
    h = 2166136261
    for c in s:
        h = ((h ^ ord(c)) * 16777619) & 0xFFFFFFFF
    return h


def levels_height(tags, wid):
    try:
        if "height" in tags:
            return max(3.0, float(tags["height"].split()[0].replace(",", ".")))
    except ValueError:
        pass
    try:
        if "building:levels" in tags:
            lv = float(tags["building:levels"].replace(",", "."))
            return lv * 3.3 + 1.5
    except ValueError:
        pass
    b = tags.get("building", "yes")
    if b in ("garage", "garages", "shed", "kiosk", "roof", "hut", "service"):
        return 3.5
    if b == "church":
        return 22.0
    # Altstadthäuser: 3-5 Geschosse
    return (3 + hash_id(wid) % 3) * 3.3 + 1.5


def flat(pts):
    out = []
    for p in pts:
        out += [p[0], p[1]]
    return out


def main(src, dst):
    root = ET.parse(src).getroot()
    nodes = {}
    trees = []
    pois = []
    for n in root.iter("node"):
        lat, lon = float(n.get("lat")), float(n.get("lon"))
        nodes[n.get("id")] = (lat, lon)
        tags = {t.get("k"): t.get("v") for t in n.iter("tag")}
        if tags.get("natural") == "tree":
            trees += list(xz(lat, lon))
        a = tags.get("amenity")
        if a in POI_TYPES:
            x, z = xz(lat, lon)
            pois.append([POI_TYPES[a], x, z])

    buildings, roads, walks, greens, waters, bridges = [], [], [], [], [], []
    names, name_idx = [], {}
    landmarks = {}

    def name_id(nm):
        if not nm:
            return -1
        if nm not in name_idx:
            name_idx[nm] = len(names)
            names.append(nm)
        return name_idx[nm]

    raw_ways = {}
    for w in root.iter("way"):
        wid = w.get("id")
        refs = [nd.get("ref") for nd in w.iter("nd")]
        raw_ways[wid] = refs
        if any(r not in nodes for r in refs):
            continue
        pts = [xz(*nodes[r]) for r in refs]
        tags = {t.get("k"): t.get("v") for t in w.iter("tag")}
        closed = len(refs) > 3 and refs[0] == refs[-1]

        if tags.get("man_made") == "tower" and tags.get("name") == "Schlossturm":
            cx = sum(p[0] for p in pts[:-1]) / (len(pts) - 1)
            cz = sum(p[1] for p in pts[:-1]) / (len(pts) - 1)
            landmarks["schlossturm"] = [round(cx, 1), round(cz, 1)]
            continue
        if "building" in tags and closed:
            if tags.get("location") == "underground" or tags.get("layer", "0").startswith("-"):
                continue
            if tags.get("building") == "roof":
                continue
            h = round(levels_height(tags, wid), 1)
            roof = 1 if tags.get("roof:shape") in ("gabled", "hipped") else 0
            buildings.append([h, roof] + flat(pts[:-1]))
            continue
        hw = tags.get("highway")
        if hw and tags.get("tunnel") not in ("yes", "building_passage") and tags.get("layer", "0") in ("0", "1"):
            if hw in ROAD_TYPES and tags.get("bridge") != "yes":
                roads.append([ROAD_TYPES[hw], name_id(tags.get("name"))] + flat(pts))
            elif hw in WALK_TYPES:
                walks.append([WALK_TYPES[hw], name_id(tags.get("name"))] + flat(pts))
            continue
        if tags.get("man_made") == "bridge" and closed:
            bridges.append([name_id(tags.get("name"))] + flat(pts[:-1]))
            continue
        if closed and (tags.get("landuse") in ("grass", "village_green", "meadow", "flowerbed", "recreation_ground")
                       or tags.get("leisure") in ("park", "garden", "playground")
                       or tags.get("natural") in ("grass", "scrub", "wood")):
            greens.append(flat(pts[:-1]))
            continue
        if closed and tags.get("natural") == "water" and tags.get("water") in ("pond", None):
            waters.append(flat(pts[:-1]))

    def bank(wid):
        # zusammenhängendes Uferstück im Ausschnitt, das am nächsten an der Altstadt liegt
        pts = [xz(*nodes[r]) for r in raw_ways[wid] if r in nodes]
        runs, cur = [], []
        for p in pts:
            if abs(p[0]) < RIVER_BOX and abs(p[1]) < RIVER_BOX:
                cur.append(p)
            elif cur:
                runs.append(cur)
                cur = []
        if cur:
            runs.append(cur)
        sel = min(runs, key=lambda r: min(math.hypot(*p) for p in r))
        if sel[0][1] < sel[-1][1]:  # Süd -> Nord sortieren
            sel.reverse()
        return sel

    east, west = bank(EAST_BANK), bank(WEST_BANK)
    river = east + list(reversed(west))

    data = {
        "origin": [LAT0, LON0],
        "attribution": "Kartendaten (c) OpenStreetMap-Mitwirkende, ODbL",
        "names": names,
        "buildings": buildings,
        "roads": roads,
        "walks": walks,
        "greens": greens,
        "waters": waters,
        "bridges": bridges,
        "river": flat(river),
        "eastBank": flat(east),
        "trees": trees,
        "pois": pois,
        "landmarks": landmarks,
    }
    with open(dst, "w", encoding="utf-8") as f:
        f.write("// Automatisch erzeugt von tools/osm_to_game.py. " + data["attribution"] + "\n")
        f.write("window.ALTSTADT=")
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")
    print(f"{len(buildings)} Gebäude, {len(roads)} Straßen, {len(walks)} Wege, {len(pois)} Kneipen/Clubs, "
          f"{len(trees) // 2} Bäume, Rhein {len(river)} Punkte -> {dst}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
