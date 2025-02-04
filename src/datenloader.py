import json
import os

def lade_maschinendaten():
    """Lädt die Maschinendaten aus der JSON-Datei im Hauptverzeichnis."""
    json_pfad = os.path.join(os.path.dirname(__file__), "..", "maschinendaten.json")

    with open(json_pfad, "r", encoding="utf-8") as file:
        return json.load(file)

# Direkt laden, damit alle Module es nutzen können
daten = lade_maschinendaten()