# Altstadt Rausch (18+)

Open-World-Spiel im Browser: die echte Düsseldorfer Altstadt bei Nacht, mit Rhein, Brauhäusern,
Clubs, Shisha-Lounge, Büdchen und Kalle am Rheinufer. Trinken, kiffen, rauchen, so viel du willst,
und die Wirkung wird von Glas zu Glas und von Zug zu Zug stärker.

## Starten

1. Den Ordner `altstadt-rausch` auf deinen Rechner holen (ganzen Ordner, nicht nur die HTML-Datei).
2. Starten:
   - **Mit Mikrofon (empfohlen):** Windows: `start-windows.bat` doppelklicken. Mac: Rechtsklick auf `start-mac.command` → **Öffnen**
     (beim ersten Mal muss man das so machen). Das kleine schwarze Fenster offen lassen, solange du spielst.
   - **Ohne Mikrofon:** einfach `index.html` doppelklicken.
   Am besten in **Chrome** oder **Edge**.
3. Häkchen bei „Ich bin mindestens 18“, optional Häkchen bei 🎤 Mikrofon und Musik-Ordner wählen, dann **Los geht's**.
   Wenn der Browser fragt, ob er das Mikro benutzen darf: **Erlauben**. Kopfhörer sind besser, sonst hört das Mikro die Musik mit.

Beim ersten Start braucht der Browser kurz Internet, weil die 3D-Engine (three.js) aus dem Netz geladen wird.

## Steuerung

| Taste | Aktion |
|---|---|
| W A S D | Laufen (Shift = rennen) |
| Maus | Umschauen / Kamera drehen |
| Tab | Große Karte: Ziel anklicken, dann wirst du hingeführt |
| V | Kamera: hinter der Figur (GTA) oder Ego-Sicht |
| E | Reingehen, bestellen, Leute ansprechen |
| T (halten) | Mit der Person vor dir reden (Mikro, Gratis-KI oder Claude-Key) |
| Enter | Der Person vor dir was schreiben |
| I | Tasche: Pilze, LSD-Pappe, Ecstasy, Koks, Lachgas nehmen |
| 1–9 / Mausrad + Klick | Im Menü auswählen (bestell so oft du willst) |
| J | Zug vom Joint (gibt's bei Kalle unten am Rhein) |
| K | Zug von der Kippe |
| F | Zug von der Shisha (Habibi Cloud) / Alt vom Köbes nehmen |
| M / N | Kopfhörer-Musik an/aus / nächster Track |
| H | Tasten-Hinweis ein/aus |
| Esc | Pause |

## Neu: echte 3D-Menschen

- Die Leute in deiner Nähe (bis ca. 20 m) sind jetzt **richtige 3D-Menschen** mit Skelett-Animationen: laufen, quatschen, sitzen, tanzen.
  Jeder hat eigene Kleidung (T-Shirt, Pulli, Jacke, Jeans, Shorts, Rock), Hautfarbe, Frisur oder Bart, und Flasche, Altbier-Glas, Kippe oder Handy in der Hand.
- Deine eigene Figur (Taste V) ist auch ein echtes Modell.
- Weiter weg bleiben die schnellen, einfachen Figuren, damit das Spiel flüssig läuft. Bei „Grafik: schnell“ gibt es weniger echte Menschen.
- Klappt nur mit den Start-Skripten (nicht per Doppelklick auf `index.html`). Abschalten im Startbildschirm: „🧍 Echte 3D-Menschen“.
- Modelle und Animationen: [Quaternius](https://quaternius.com) (CC0), siehe `assets/people/LIZENZ.txt`.

## Neu: echte Stimmen und Gratis-KI

- **Alle Leute haben jetzt echte Stimmen**, gratis und ohne Konto: über 170 verschiedene deutsche Stimmen (Frauen und Männer),
  dazu betrunkene, wütende, flüsternde und müde Varianten. Kalle klingt verpeilt, Betrunkene lallen.
  Die Stimmen kommen räumlich aus der Richtung der Person und werden leiser, je weiter weg sie ist.
- **Grüppchen auf der Straße unterhalten sich hörbar miteinander**, bis zu drei Gespräche gleichzeitig.
- **Gratis-KI-Gehirn:** Ohne API-Key kannst du jetzt trotzdem frei mit allen reden. Ein kleines Sprachmodell läuft direkt auf
  deinem Rechner (Grafikkarte). Es ist nicht so schlau wie Claude, kostet aber nichts. Wenn es geladen ist,
  schreibt es auch die Gespräche der Grüppchen.
- Beim ersten Spielen wird einmalig heruntergeladen: Stimmen ca. 150 MB, KI ca. 1 GB (groß: ca. 2 GB). Danach bleibt alles gespeichert.
  Dafür das Spiel mit `start-windows.bat` / `start-mac.command` starten (nicht per Doppelklick auf `index.html`) und **Chrome oder Edge** benutzen.
- Im Startbildschirm unter **„🧠 KI-Gespräche und echte Stimmen“** kannst du das Gehirn wählen (Gratis klein, Gratis groß, Claude, aus)
  und die Stimmen ausschalten. Unten rechts siehst du, wie weit das Laden ist.

## Neu in Phase 7: mehr Substanzen

Alles erfunden und bewusst übertrieben, nur ein Spiel, keine echten Infos oder Dosierungen.

- **Wo du was bekommst:** Kalle am Rhein hat jetzt endlich **Pilze**. Für **LSD-Pappe**, **Ecstasy** und **Koks** schickt er dich zu
  **Ronny**, der im Kapuzenpulli in der **Mertensgasse** an der Wand lehnt. **Lachgas-Ballons** gibt's am **Büdchen**.
  Mit KI-Key kannst du Kalle und Ronny auch einfach danach fragen.
- **Taste I** öffnet deine Tasche, daraus nimmst du die Sachen.
- **Pilze:** kommen langsam, dann atmen die Wände, Farben fließen ins Lila-Pink, Leute und Himmel schimmern bunt, die Musik hallt nach,
  die Welt wird langsamer.
- **LSD:** hält ewig. Farben wandern durchs ganze Spektrum, Kanten leuchten, Muster auf dunklen Flächen, alles zieht Spuren.
  Zusammen mit Pilzen wird's ein Kaleidoskop.
- **Ecstasy:** alles warm und glänzend, mehr Bass, du liebst alle. Bleibst du stehen, fängt deine Figur an zu tanzen.
  Danach kommt das **Runterkommen**: alles grau, bis Essen, Wasser oder Zeit helfen.
- **Koks:** kurz und heftig. Du läufst schneller, alles wird hart und klar, Tunnelblick, Herzrasen, große Gedanken.
  Man fühlt sich nüchterner, als man ist (der Alkohol ist trotzdem da).
- **Lachgas:** 30 Sekunden wah-wah-wah im Bild und im Ton.
- **Kombis:** Gras verstärkt Pilze und LSD, Ecstasy mit Alkohol macht Durst, wer zu viel durcheinander nimmt, kriegt Herzrasen
  und Paranoia, und ab einem Punkt ist **Absturz**: Die Sanitäter setzen dich an den Rhein und geben dir Wasser.
- **Die Welt merkt's:** Leute lästern („Der streichelt die Hauswand“), die Polizei spricht dich an, die Türsteher lassen dich
  nicht rein, wenn du zu drüber bist, und im KI-Gespräch wissen die Leute genau, was mit dir los ist.

## Neu in Phase 6: freie KI-Gespräche

Mit einem eigenen **Claude-API-Key** kannst du mit jeder Person im Spiel frei reden: mit Kalle, dem Köbes, Lara,
den Türstehern, der Polizei, dem JGA, irgendwem auf der Straße.

1. Auf **console.anthropic.com** ein Konto anlegen, Guthaben aufladen (ein paar Euro reichen lange, pro Antwort etwa ein Cent)
   und unter „API Keys“ einen Key erstellen.
2. Im Startbildschirm auf **„🧠 KI-Gespräche“** klicken, den Key einfügen, **Speichern**. Er bleibt nur in deinem Browser.
3. Im Spiel vor jemanden stellen und **T gedrückt halten**, sprechen, loslassen. Oder **Enter** drücken und tippen.

Die Person antwortet als Sprechblase und mit Stimme. Sie weiß, wie spät es ist, wo sie ist und wie voll oder bekifft du bist,
und merkt, ob du schreist oder flüsterst. Gespräche können was auslösen: Kalle gibt dir Joints, der Türsteher lässt dich rein
(oder nicht), der Köbes bringt dir dein Alt, der JGA gibt einen aus. Spracherkennung klappt in Chrome/Edge und am besten mit
`start-windows.bat` / `start-mac.command`. Ohne Key gibt es jetzt die Gratis-KI (siehe oben).

## Neu in Phase 5 (Teil 2): Rhein, Verkehr, Ratinger Straße

- **Kasematten** am Rheinufer: Bar-Reihe mit Terrassen, Bierbänken und Heizpilzen. **Kasematte 7** ist begehbar (Backstein-Gewölbe).
- **Rheinturm Sky Lounge:** Unten rein, Aufzug hoch, und auf 168 m über die Lichter von Düsseldorf schauen.
- **Schiffe:** Ein beleuchtetes Partyschiff mit Musik und Leuten an Deck fährt den Rhein rauf und runter, dazu ein Frachter.
- **Verkehr am Rand der Altstadt:** Autos mit Scheinwerfern, Taxis (mit Taxistand an der Heinrich-Heine-Allee) und eine Straßenbahn.
  Sie bremsen, wenn du vor ihnen stehst, und hupen bzw. klingeln.
- **Ratinger Straße** mit Lichterketten und der Rock-Kneipe **Zum Schrägen Vogel** mit Live-Band.
- **Details:** Mülleimer, Fahrräder, Bierkästen, leere Flaschen, blaue Straßenschilder, Leute als Silhouetten in den Fenstern.
- **Die Nacht vergeht:** Ab 3 Uhr wird es leerer und mehr Leute torkeln heim, ab 5 Uhr dämmert es über dem Rhein.
- **Einstellungen im Startbildschirm:** Menge an Leuten (wenig/mittel/viel) und Grafik (schnell/schön) für schwächere Rechner.

## Neu in Phase 5: mehr Altstadt

- **Drei neue Locations:**
  - **O'Rheily's Irish Pub** (Bolkerstraße): Stout, Cider, Whiskey, Lederbänke, Fässer, Dartscheibe, Irish-Folk.
  - **Kehlkopf Karaoke:** Geh auf die Bühne (E am Mikroständer) und sing. Der Text läuft auf der Leinwand und unten im Bild.
    Mit Mikro wird bewertet, wie viel du wirklich singst, am Ende gibt's Punkte und Applaus, ab 85 Punkten einen Shot aufs Haus.
  - **Pommes Paradies** (Imbiss): Pommes rot-weiß, Currywurst, Döner. Hilft gegen den Fressflash.
- **Straßenmusiker** auf der Bolkerstraße mit Gitarre, um ihn herum bleiben Leute stehen und filmen.
- **Polizeistreife** läuft durch die Altstadt und spricht dich an, wenn du zu voll bist.
- **Rosenverkäufer** kommen auf dich zu („Rose? Für die Freundin?“), mit E kaufst du eine.
- **Junggesellenabschied:** Braut in Weiß mit Mädels in Pink, sie grölen „JGA! JGA!“ und geben dir einen aus, wenn du sie ansprichst.
- **Schönere Fassaden:** Dachgesimse, Stockwerksbänder über dem Erdgeschoss, Ausleger-Schilder, die quer in die Gasse ragen.
- Die Kamera geht in engen Gassen automatisch über die Schulter, statt in deine Figur zu fahren.

## Neu: Altstadt am Wochenende

- **Rappelvoll:** rund 1.500 Leute auf der Straße. Grüppchen vor jeder Kneipe um Altbierfässer und Stehtische,
  Schlangen vor den Clubs, Leute auf den Sitzstufen am Rhein (eine Gruppe hat eine Musikbox dabei), Spaziergänger in Grüppchen.
- **Echtere Menschen:** Körper mit Knien, Ellbogen, Gesicht, Frisuren (kurz, lang, Dutt, Cap, Bart), Röcke, kurze Hosen, Turnschuhe.
  Sie trinken Bier aus der Flasche oder Altbier aus dem Glas, rauchen (Glut leuchtet), gucken aufs Handy, filmen, lachen, tanzen,
  gestikulieren beim Reden, torkeln, sitzen. Wer in deiner Nähe steht, guckt dich auch mal an.
- **Sprechblasen:** Die Leute quatschen („Noch ein Alt?“, „Wer kommt mit ins Bunker?“), lästern, wenn du hacke bist,
  und meckern, wenn du sie anrempelst. Mit **E** kannst du jeden ansprechen, manchmal gibt dir jemand einen Schluck aus.
- **GTA-Look:** Kamera hinter deiner Figur, kräftige Farben, warme Laternen, lila Schatten, leichtes Filmkorn.
- **Echterer Boden:** kleines Kopfsteinpflaster mit Fugen, Rinne in der Mitte der Gassen, nasse Stellen und Pfützen, in denen sich Lichter spiegeln.
- **Lichterketten** quer über den Gassen, Markisen über den Kneipentüren.
- **Karte mit Navigation:** **Tab** öffnet die große Karte mit Straßennamen. Ort aus der Liste wählen oder irgendwo hinklicken,
  dann zeigen leuchtende Punkte auf dem Boden, ein Lichtstrahl am Ziel und die Linie auf der Minikarte den Weg.
- **Mehr Musik draußen:** aus bis zu acht Kneipentüren gleichzeitig, das Stimmengewirr wird lauter, je voller es ist.
- **Neue Wahrzeichen:** der verdrehte Turm von St. Lambertus, Jan-Wellem-Reiterstandbild am Marktplatz, Radschläger-Brunnen am Burgplatz.
- **Mikrofon (Phase 4):** Stell dich vor jemanden und rede einfach, dann antwortet die Person. Flüstern versteht keiner.
  Schreien fällt auf: Die Leute drehen sich um und kommentieren, Türsteher lassen dich danach eine halbe Stunde nicht rein,
  im Club jubeln alle mit, im Brauhaus schimpft der Köbes.

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

  Seit Phase 5 außerdem: O'Rheily's Irish Pub, Kehlkopf Karaoke und Pommes Paradies (siehe oben).

  Dazu das **Büdchen am Burgplatz** (Bier, Kippen, Chips gegen den Fressflash) und **Kalle** auf der Bank am Rhein.
- **Rausch-System:** Alkohol, THC und Nikotin fluten verzögert an und bauen langsam ab.
  - Alkohol: Schwanken, Wellen, Doppeltsehen, Torkeln und Stolpern, Augen fallen zu, Kotzen, Filmriss (du wachst am Rhein auf).
  - Joint: Farben glühen, Bild „atmet“, Welt und Musik werden langsamer, Lachflash-Gedanken, Fressflash, ab „komplett weg“ Paranoia mit Herzklopfen.
  - Kippe/Shisha: Kopf-Kick, Rauchwolken, Husten.
  - Die Leute im Spiel reagieren: Barkeeper sprechen dich je nach Pegel anders an, Türsteher lassen dich ab „Vollrausch“ nicht mehr rein.
- **Musik-System:** Draußen hörst du aus jeder Kneipentür gedämpft die Musik von drinnen, drinnen wird sie laut und klar.
  Besoffen klingt alles dumpf, bekifft langsamer. Ohne eigene Songs laufen live generierte Beats im passenden Stil.

## Musik: Internetradio

Ohne eigene MP3s spielt jede Location automatisch einen passenden **Internetradio-Sender**: Deutschrap auf der Straße und im Bunker,
80er im Neonlicht, Karneval/Stimmung im Brauhaus, Techno im Keller, Schlager in der Schlagerhölle, Irish Folk im Pub usw.
Die Senderliste kommt von radio-browser.info, das Spiel nimmt nur Sender, die gerade erreichbar sind. Mit **N** springst du zum nächsten Sender.
Braucht Internet; ohne Internet laufen die eingebauten Beats. Abschalten: Häkchen „📻 Echte Musik über Internetradio“ im Startbildschirm.

## Eigene Musik

Lege deine Songs in die Unterordner von `musik/` (siehe `musik/LIESMICH.txt`) und wähle im Startbildschirm
den Ordner `musik` aus. Die Songs bleiben nur auf deinem Rechner und werden nicht ins Git hochgeladen.

## Nächste Phasen

- ~~Phase 4: Mikrofon~~ erledigt.
- ~~Phase 5: Locations und Straßen~~ erledigt.
- ~~Phase 6: freie KI-Gespräche~~ erledigt.
- ~~Phase 7: weitere Substanzen~~ erledigt.
- ~~Echte Stimmen + Gratis-KI~~ erledigt.
- ~~Echte 3D-Menschen~~ erledigt.
- ~~Foto-Texturen für Pflaster, Gehwege, Putz~~ erledigt (ambientCG, CC0, `assets/tex/`).
- **Als Nächstes:** Kopf-Blick und Trink-Bewegung der echten Menschen, bessere Schatten.
- **Später:** Google Photorealistic 3D Tiles (Maps-Key) als echte Kulisse, Spotify als Musikquelle (Premium + Developer-App).

## Technik

- Eine einzige Datei `index.html` mit [three.js](https://threejs.org) 0.160 (über unpkg), Web Audio API für Musik und Sounds.
- Stimmen: [Piper](https://github.com/rhasspy/piper) (Stimmen `de_DE-mls` und `de_DE-thorsten_emotional`) über onnxruntime-web.
  Gratis-KI: [WebLLM](https://webllm.mlc.ai) mit Qwen2.5 (1,5B/3B), braucht WebGPU.
- `data/altstadt.js` entsteht mit `tools/osm_to_game.py` aus einem OpenStreetMap-Export (Befehl steht im Skript).

Kartendaten © OpenStreetMap-Mitwirkende, Lizenz [ODbL](https://opendatacommons.org/licenses/odbl/).
Alle Bars, Clubs und Personen im Spiel sind erfunden. Nur ein Spiel: Die Wirkungen sind übertrieben dargestellt und keine echten Dosierungsangaben.
