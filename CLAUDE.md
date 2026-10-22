# Altstadt Rausch: Projektkontext

Open-World-Browserspiel (18+) in der echten Düsseldorfer Altstadt bei Nacht. Der Spieler läuft frei herum,
geht in Brauhäuser, Clubs, Bars und eine Shisha-Lounge, trinkt, kifft und raucht unbegrenzt und spürt
die Wirkung Schluck für Schluck bzw. Zug für Zug. Die Welt reagiert darauf.

Mit dem Nutzer auf **Deutsch** reden, locker und direkt. Er ist kein Entwickler: erklären, was er tun muss, in einfachen Schritten.

## Wünsche des Nutzers

- Grafik **möglichst realistisch** (aktuell: Browser-Version mit three.js; später evtl. Godot/Unreal).
- **Freie KI-Gespräche** mit NPCs über Mikrofon (Barkeeper, Köbes, Kalle usw.), NPCs sollen auf Lautstärke reagieren.
- **Musik ist zentral:** draußen Deutschrap-Chill, viele Clubs in der Altstadt, 80er-Hits in Kneipen, passende Musik je Location.
- Spotify als Musikquelle wäre cool (geht nur mit Premium + Developer-App, und ohne Rausch-Audioeffekte wegen DRM).
- Google-Maps-Key (Photorealistic 3D Tiles) rüstet er später nach.
- Alle Substanzen inkl. Magic Mushrooms. Wirkungen bleiben spielerisch übertrieben, keine echten Dosierungsangaben.
- Bars, Clubs und Personen sind erfunden; echte Kneipen-Standorte aus OSM dienen nur als Positionen.

## Stand

Phase 1 bis 3 fertig:
1. Laufen durch die Altstadt aus OSM-Daten, Nacht, Rhein, Wahrzeichen
2. Rausch-System Alkohol, THC, Nikotin mit Post-Processing-Effekten
3. Musik-System (eigene MP3s je Ordner in `musik/` oder generierte Beats), 8 begehbare Locations, Büdchen, Kalle

Offen:
- **Phase 4:** Mikrofon-Lautstärke steuert NPC-Reaktionen (braucht `http://localhost`, ggf. Start-Skript mit lokalem Server)
- **Phase 5:** Locations/Straßen ausbauen
- **Phase 6:** freie KI-Gespräche (Spracherkennung → Claude API mit eigenem Key des Nutzers → Sprachausgabe), NPC kennt den Pegel des Spielers
- **Phase 7:** Magic Mushrooms + weitere Substanzen, Kombi-Effekte
- Später: Google 3D Tiles, Spotify, bessere NPC-Modelle, echtes Lallen über Mikro

## Aufbau

- `index.html`: das ganze Spiel in einem `<script type="module">`, weil lokale ES-Module bei `file://` wegen CORS nicht laden.
  three.js 0.160 kommt per Importmap von unpkg. Abschnitte: Texturen → Fassaden-Shader → Stadt → Boden/Rhein → Wahrzeichen →
  Laternen/Bäume → Locations/Innenräume → NPCs (`Crowd`, instanziert) → Rauch/Hand → Musik (`Synth`, `GEN`/`PATTERN`, `Groove`, `Channel`, `Sound`) →
  Rausch (`SUB`, `FX`, `RauschShader`) → Spieler → Menüs/Interaktion → Events → HUD/Minikarte → Spielschleife.
- `data/altstadt.js`: erzeugt mit `tools/osm_to_game.py` aus einem OSM-Export (Befehl im Skript). Koordinaten in Metern,
  x = Osten, z = Süden, Ursprung bei 51.2266 / 6.7735. Die Bolkerstraße liegt bei z ≈ 15 bis 65.
- `window.__game` stellt Spielzustand fürs Testen bereit; `GAME.noLock = true` lässt das Rausch-System ohne Pointer-Lock laufen.

## Testen

Headless Chromium mit Playwright (`/opt/node-tools/node_modules/playwright`, Browser `/opt/pw-browsers/chromium-1194`),
Flags `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`. three.js-Dateien vorher per curl lokal holen und
Anfragen an unpkg mit `page.route` aus den lokalen Dateien beantworten. Software-Rendering läuft nur mit ca. 1 bis 2 FPS,
also für Screenshots Zustände direkt über `__game` setzen. Echte Performance und Sound lassen sich so nicht beurteilen.

Kartendaten © OpenStreetMap-Mitwirkende (ODbL).
