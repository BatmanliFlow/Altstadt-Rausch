# Altstadt Rausch (18+)

Open-World-Spiel im Browser: die echte Düsseldorfer Altstadt bei Nacht, mit Rhein, Brauhäusern,
Clubs, Shisha-Lounge, Büdchen und Kalle am Rheinufer. Trinken, kiffen, rauchen, so viel du willst,
und die Wirkung wird von Glas zu Glas und von Zug zu Zug stärker.

## Starten

1. Den Ordner `altstadt-rausch` auf deinen Rechner holen (ganzen Ordner, nicht nur die HTML-Datei).
2. `index.html` doppelklicken. Am besten in **Chrome** oder **Edge**.
3. Häkchen bei „Ich bin mindestens 18“, optional Musik-Ordner wählen, dann **Los geht's**.

Beim ersten Start braucht der Browser kurz Internet, weil die 3D-Engine (three.js) aus dem Netz geladen wird.

## Steuerung

| Taste | Aktion |
|---|---|
| W A S D | Laufen (Shift = rennen) |
| Maus | Umschauen |
| E | Reingehen, bestellen, mit Leuten quatschen |
| 1–9 / Mausrad + Klick | Im Menü auswählen (bestell so oft du willst) |
| J | Zug vom Joint (gibt's bei Kalle unten am Rhein) |
| K | Zug von der Kippe |
| F | Zug von der Shisha (Habibi Cloud) / Alt vom Köbes nehmen |
| M / N | Kopfhörer-Musik an/aus / nächster Track |
| H | Tasten-Hinweis ein/aus |
| Esc | Pause |

## Was drin ist (Phase 1 bis 3)

- **Echte Karte:** 2.223 Gebäude, alle Straßen, der Rhein mit beiden Ufern und 1.278 Bäume aus OpenStreetMap.
  Dazu Schlossturm, St. Lambertus, Rheinturm mit Lichtzeitpegel, Oberkasseler Brücke und Oberkassel als Kulisse.
- **Nacht-Look:** beleuchtete Fenster und Schaufenster, Laternen, Neonschilder an allen echten Kneipen-Standorten,
  spiegelnder Rhein, Glow-Effekte.
- **Belebte Altstadt:** 240 Leute laufen über das echte Wegenetz, Grüppchen stehen vor den Kneipen, Türsteher vor den Clubs.
- **8 begehbare Locations** mit eigener Einrichtung, eigenem Licht, eigener Musik und eigenem Barkeeper:

  | Location | Art | Musik |
  |---|---|---|
  | Brauhaus Zum Durstigen Köbes | Brauhaus (Heinz stellt ungefragt nach) | Kneipen-Stimmung |
  | Bunker 211 | Deutschrap-Club mit Lasern | Deutschrap / Trap |
  | Neonlicht | 80er-Kneipe mit Leuchtboden + Discokugel | 80er-Synthpop |
  | Keller 47 | Techno-Keller mit Stroboskop | Techno |
  | Schlagerhölle | Schlager-Bar mit Polonaise | Discofox |
  | Wolke 7 | Chill-Lounge | Lo-Fi Deutschrap |
  | Habibi Cloud | Shisha-Lounge (5 Sorten) | Arabic Chill |
  | Blue Lagoon | Cocktailbar mit Lara | Bar Jazz-Hop |

  Dazu das **Büdchen am Burgplatz** (Bier, Kippen, Chips gegen den Fressflash) und **Kalle** auf der Bank am Rhein.
- **Rausch-System:** Alkohol, THC und Nikotin fluten verzögert an und bauen langsam ab.
  - Alkohol: Schwanken, Wellen, Doppeltsehen, Torkeln und Stolpern, Augen fallen zu, Kotzen, Filmriss (du wachst am Rhein auf).
  - Joint: Farben glühen, Bild „atmet“, Welt und Musik werden langsamer, Lachflash-Gedanken, Fressflash, ab „komplett weg“ Paranoia mit Herzklopfen.
  - Kippe/Shisha: Kopf-Kick, Rauchwolken, Husten.
  - Die Leute im Spiel reagieren: Barkeeper sprechen dich je nach Pegel anders an, Türsteher lassen dich ab „Vollrausch“ nicht mehr rein.
- **Musik-System:** Draußen hörst du aus jeder Kneipentür gedämpft die Musik von drinnen, drinnen wird sie laut und klar.
  Besoffen klingt alles dumpf, bekifft langsamer. Ohne eigene Songs laufen live generierte Beats im passenden Stil.

## Eigene Musik

Lege deine Songs in die Unterordner von `musik/` (siehe `musik/LIESMICH.txt`) und wähle im Startbildschirm
den Ordner `musik` aus. Die Songs bleiben nur auf deinem Rechner und werden nicht ins Git hochgeladen.

## Nächste Phasen

- **Phase 4:** Mikrofon. NPCs reagieren auf deine Lautstärke (Flüstern, Reden, Schreien).
  Dafür muss das Spiel über einen kleinen lokalen Server laufen (`http://localhost`), weil der Browser das Mikro bei Doppelklick-Dateien nicht immer freigibt.
- **Phase 5:** Mehr Ausbau der Locations und Straßen.
- **Phase 6:** Freie KI-Gespräche mit Köbes, Lara, Emre, Kalle und den anderen über Sprache. Braucht einen eigenen API-Key (z. B. Claude API).
- **Phase 7:** Magic Mushrooms und weitere Substanzen, Kombi-Effekte.
- **Später:** Google Photorealistic 3D Tiles (Maps-Key) als echte Kulisse, Spotify als Musikquelle (Premium + Developer-App).

## Technik

- Eine einzige Datei `index.html` mit [three.js](https://threejs.org) 0.160 (über unpkg), Web Audio API für Musik und Sounds.
- `data/altstadt.js` entsteht mit `tools/osm_to_game.py` aus einem OpenStreetMap-Export (Befehl steht im Skript).

Kartendaten © OpenStreetMap-Mitwirkende, Lizenz [ODbL](https://opendatacommons.org/licenses/odbl/).
Alle Bars, Clubs und Personen im Spiel sind erfunden. Nur ein Spiel: Die Wirkungen sind übertrieben dargestellt und keine echten Dosierungsangaben.
