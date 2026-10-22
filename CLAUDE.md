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

Phase 1 bis 4 fertig:
1. Laufen durch die Altstadt aus OSM-Daten, Nacht, Rhein, Wahrzeichen
2. Rausch-System Alkohol, THC, Nikotin mit Post-Processing-Effekten
3. Musik-System (eigene MP3s je Ordner in `musik/` oder generierte Beats), 8 begehbare Locations, Büdchen, Kalle
4. Mikrofon (`MIC`): Pegel relativ zum gelernten Grundrauschen → still/flüstern/reden/schreien; Satzende → `onUtterance`, Schreien → `onShout`.
   Start-Skripte `start-windows.bat` (PowerShell-Server `tools/server.ps1`), `start-mac.command`, `start-linux.sh`, alle auf Port 8047.

Dazu „Altstadt am Wochenende“: ~1.500 NPCs, Third-Person-Kamera (V wechselt), GTA-Farblook, Karte (Tab) mit A*-Navigation,
Sprechblasen, Anrempeln, NPCs ansprechen (E), Lichterketten, Fässer/Stehtische, Sitzstufen am Rhein, nasses Pflaster.

Offen:
- **Phase 5:** Locations/Straßen ausbauen
- **Phase 6:** freie KI-Gespräche (Spracherkennung → Claude API mit eigenem Key des Nutzers → Sprachausgabe), NPC kennt den Pegel des Spielers
- **Phase 7:** Magic Mushrooms + weitere Substanzen, Kombi-Effekte
- Später: Google 3D Tiles, Spotify, bessere NPC-Modelle, echtes Lallen über Mikro

## Aufbau

- `index.html`: das ganze Spiel in einem `<script type="module">`, weil lokale ES-Module bei `file://` wegen CORS nicht laden.
  three.js 0.160 kommt per Importmap von unpkg. Abschnitte: Texturen → Fassaden-Shader → Stadt → Boden/Rhein → Wahrzeichen →
  Laternen/Bäume → Locations/Straßen-Deko (`buildStreetProps`) → Innenräume → NPCs (`People`) → Rauch/Hand → Musik (`Synth`, `GEN`/`PATTERN`, `Groove`, `Channel`, `Sound`) →
  Rausch (`SUB`, `FX`, `RauschShader`, `GradeShader`) → Spieler/Kamera (`CAM`, Avatar `ME`) → Menüs/Interaktion → Sprechblasen (`CHAT`) → Mikro (`MIC`) →
  Events → HUD/Minikarte → Navigation/Karte (`RG`, `findPath`, `NAV`) → Eingabe → Spielschleife.
- NPCs (`People`): ein Körper-Mesh aus Grundformen mit `aInfo` = (Gelenk, Farbslot, Variante). JS rechnet pro Person 16 Gelenkwinkel
  (`animate`, Modi walk/idle/sit/dance/polo, `act` = talk/cross/laugh/cheer/film/…, `prop` = Flasche/Glas/Kippe/Handy),
  der Vertex-Shader biegt die Glieder. Nah = detailliertes Mesh (`hi`), fern = einfaches (`lo`), hinter der Kamera wird nichts gezeichnet.
- Boden: `wetMaterial` legt Pfützen/Nässe per Rauschen in Weltkoordinaten drüber, Spiegelungen kommen aus `ENV` (generierte Nacht-Umgebung).
- `data/altstadt.js`: erzeugt mit `tools/osm_to_game.py` aus einem OSM-Export (Befehl im Skript). Koordinaten in Metern,
  x = Osten, z = Süden, Ursprung bei 51.2266 / 6.7735. Die Bolkerstraße liegt bei z ≈ 15 bis 65.
- `window.__game` stellt Spielzustand fürs Testen bereit; `GAME.noLock = true` lässt das Rausch-System ohne Pointer-Lock laufen.

## Testen

Headless Chromium mit Playwright (`/opt/node-tools/node_modules/playwright`, Browser `/opt/pw-browsers/chromium-1194`),
Flags `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`. three.js-Dateien vorher per curl lokal holen und
Anfragen an unpkg mit `page.route` aus den lokalen Dateien beantworten. Software-Rendering läuft nur mit ca. 1 bis 2 FPS,
also für Screenshots Zustände direkt über `__game` setzen. Echte Performance und Sound lassen sich so nicht beurteilen.
Abblenden (z. B. `enterVenue`) dauert dort 30 bis 50 Sekunden, weil `dt` pro Frame auf 0,05 begrenzt ist.
Mikro testen: über `python3 -m http.server 8047` laden, Chromium mit `--use-fake-device-for-media-stream --use-fake-ui-for-media-stream`,
Pegel simulieren durch Überschreiben von `__game.MIC.an.getFloatTimeDomainData`.

Kartendaten © OpenStreetMap-Mitwirkende (ODbL).
