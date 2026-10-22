#!/bin/bash
# Startet Altstadt Rausch über einen lokalen Server (nötig fürs Mikrofon).
# Erster Start: Rechtsklick auf die Datei -> Öffnen. Terminal-Fenster offen lassen, solange du spielst.
cd "$(dirname "$0")"
PORT=8047
( sleep 1; open "http://localhost:$PORT/" ) &
if command -v python3 >/dev/null 2>&1; then
  python3 -m http.server $PORT --bind 127.0.0.1
elif command -v ruby >/dev/null 2>&1; then
  ruby -run -e httpd . -p $PORT -b 127.0.0.1
else
  echo "Weder python3 noch ruby gefunden. Bitte Python von python.org installieren und nochmal starten."
  read -r
fi
