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

Phase 5 fertig, Teil 1: Irish Pub, Karaoke-Bar (`KARAOKE`, `SONGS` mit eigenen Texten), Imbiss; Locations können statt `at` (lat/lon) auch `xz` haben.
Straßenmusiker (`BUSKER`, Genre `busker`), Polizei (`o.police`), Rosenverkäufer (`o.rose`, `roseSeller`), JGA (`o.jga`), Gesimse in `buildCity`, `hangingSign`.
Teil 2: Kasematten (`KASE`, als Gebäude in `prepBuildings`), Rheinturm Sky Lounge (Innenraum mit `ox/oy/oz`, `round`, `view` = Stadt bleibt sichtbar),
Schiffe (`SHIPS`, `shipCrowd`, Partyschiff-Musik über `SHIP_POS`), Verkehr (`roadChains`, `CARS`, `tram`), Rock-Kneipe mit Band (`act` drum/guitar, `makeGuitar`),
Kleinkram + Straßenschilder in `buildStreetProps`, Fenster-Silhouetten im Fassaden-Shader, Uhrzeit (`TOD`: ab 3 Uhr weniger Leute, ab 5 Uhr `DAWN`), Einstellungen `Q.crowd` + Pixelratio.

Phase 6 fertig: `AI` – T halten = Web Speech API (de-DE), Enter = Texteingabe → `aiTalk` → `@anthropic-ai/sdk@0.133.0` per Importmap (jsDelivr, erst beim ersten Gespräch geladen),
`dangerouslyAllowBrowser`, Modell `claude-opus-5-5`, effort low, `fallbacks: 'default'` (Beta `server-side-fallback-2026-07-01`), strukturierte Antwort (`AI_SCHEMA`: say/mood/action/serve).
`persona(o)` baut die Rolle, `situation()` den Zustand des Spielers; Verlauf je NPC in `o.chat` (nur anhängen, nie kürzen; nach 12 Wechseln neu). Key in localStorage `altstadt-ai-key`.
Sprachausgabe mit `speechSynthesis`. Ohne Key bleibt alles bei den festen Sätzen.

Phase 7 fertig: neue `SUB`-Einträge psi/lsd/mdma/coke/n2o (+ `FX`, Stufen, `SUBDEF` für die HUD-Balken), Tasche `GAME.inv` + `STUFF`/`consume`/`inventoryMenu` (Taste I),
Quellen: Kalle (Pilze), `RONNY` in der Mertensgasse (`ronnyMenu`), Büdchen (Lachgas). Effekte im `RauschShader` (uPsi/uLsd/uMdma/uCoke/uN2o/uDown,
Kaleidoskop, Kantenleuchten), `AfterimagePass` für Spuren, `TRIP` färbt Menschen und Himmel, Ton: `Sound.shelf` (Bass), `echoWet` (Echo), Wah über `lp`.
Kombis: `FX.load` → Herzrasen/Paranoia, ab 2,75 Absturz mit Sanitätern; `GAME.down` = Runterkommen (Essen/Wasser helfen). KI-Aktionen pilze/pappe/teil/koks_geben.

Musik: Internetradio je Genre (`RADIO`, `RADIO_TAGS`/`RADIO_HINT`, `radioSource`/`radioTry`): radio-browser.info-API, nur https-Sender mit CORS (sonst automatisch nächster),
eine Quelle pro Genre für alle Kanäle, Groove läuft, bis das Radio spielt. Reihenfolge: eigene MP3s > Radio > Groove.

Stimmen + Gratis-KI fertig: `PIPER` (onnxruntime-web 1.18 von cdnjs, Phonemizer aus `@mintplex-labs/piper-tts-web@1.0.5`, Modelle von huggingface
`diffusionstudio/piper-voices`: `de_DE-mls-medium` mit `VOICE_F`/`VOICE_M` = per Tonhöhe sortierte Sprecher-IDs, `de_DE-thorsten_emotional-medium` für
drunk/angry/whisper/sleepy/amused). Cache API (`altstadt-piper`), braucht localhost/https. `voiceOf`, `voiceSay` (PannerNode → `Sound.voice`), `updateVoices` (duckt Musik).
`LOCAL` = WebLLM `@mlc-ai/web-llm@0.2.85` (Qwen2.5 1.5B/3B, WebGPU), `aiMode()` in localStorage `altstadt-ai-mode` (local-s/local-l/claude/off),
`aiTalk` → `claudeTalk`/`localTalk`/`talkTo`, `aiReady()`. Gruppengespräche `TALKS`/`updateGroupTalks` (max. 3, Pausen in Echtzeit), `DIALOGS` als Vorrat, `groupScript` per LLM.
Headless: Piper geht (NET=1 + http://localhost:8047), WebLLM nicht (kein WebGPU).

Echte Menschen fertig: `HQ` (vor „Bewegungen“) = Pool aus Quaternius-Modellen (`assets/people/`: male/female.glb, anims.glb mit 13 UAL-Clips, Hair_*.glb),
GLTFLoader + SkeletonUtils per Importmap. `People.pose` ruft `hqWant(o, d2)`: Kandidaten bis `HQ.R` (21 m) vom Spieler, nächste zuerst, Avatar `ME` immer;
wer einen Slot hat (`o.hq`), wird nicht als Figur gezeichnet (Schatten bleibt). `hqUpdate` verteilt die Slots (getrennt nach Mann/Frau), `hqDress` setzt
Kleidung über Shader-Uniforms (`uCut` = Saum/Ärmel/Hosenbein/Jacke, Bereiche nach T-Pose-Position `vBind`), `hqClip` wählt die Animation, Laufen läuft synchron zu `o.phase`.
Körper schlanker über Knochen-Skalierung, Requisiten folgen `hand_r` aufrecht. Nur über http (nicht file://), sonst bleiben die Figuren. Lab: Aufstellung per eigener Testseite.

Offen:
- Als Nächstes: Foto-Texturen (ambientCG CC0) für Boden/Fassaden, Lampen-Schatten/AO; Kopf-Blick und Trink-Bewegung für `HQ`
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
KI testen: jsDelivr-Dateien lokal spiegeln und `https://api.anthropic.com/**` per `page.route` mit einer erfundenen Antwort beantworten (kein echter Key).

Kartendaten © OpenStreetMap-Mitwirkende (ODbL).
