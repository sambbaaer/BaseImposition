# --- Basisrechnung ---

from config import REfBreite, REfHohe, RbBreite, RbHohe, EfBreite, EfHohe, EfAnschnitt, EfLaufrichtung


def BasisNutzenberechnung():
    """Berechnet die Basisanzahl der Nutzen."""
    global BasisAnzNutzen, BasisRechnung
    # Nutzenanzahl berechnen für beide Laufrichtungen
    if REfBreite > 0 and REfHohe > 0:  # Verhindert Division durch Null
        AnzNutzen1 = (int(RbBreite / REfBreite)) * (int(RbHohe / REfHohe))
        AnzNutzen2 = (int(RbBreite / REfHohe)) * (int(RbHohe / REfBreite))
        # Größere Nutzenanzahl auswählen
        BasisAnzNutzen = max(AnzNutzen1, AnzNutzen2)
        if AnzNutzen1 > AnzNutzen2:
            BasisAnzNutzen = int(AnzNutzen1)
            BasisRechnung = 1
        else:
            BasisAnzNutzen = int(AnzNutzen2)
            BasisRechnung = 2
    else:
        BasisAnzNutzen = 0  # Fehlerfall: Kein Nutzen berechenbar
        print("Fehler: Überprüfe deine Eingabe und nutze nur positive Zahlen.")

def LaufrichtungDB():
    """Berechnet, welche Laufrichtung beim Rohbogen/Druckbogen benötigt wird."""
    global LaufrichtungRB
    if BasisRechnung == 1:
        LaufrichtungRB = "Breitbahn"
    else:
        LaufrichtungRB = "Schmalbahn"

def Papiernutzung():
    """Berechnet, wie hoch die Nutzung vom Papier ist."""
    global PapierNutzung
    PapierNutzung = round((BasisAnzNutzen*REfBreite*REfHohe)/(RbBreite*RbHohe)*100, 2)

# Hauptprogramm
BasisAnzNutzen = 0  # Anzahl Nutzen über die Basisrechnung
BasisRechnung = 1  # welcher der beiden Rechnungswege verwendet wurde
LaufrichtungRB = "unbekannt"  # Initialwert für die Laufrichtung
PapierNutzung = 0 # Wie viel Prozent des Papieres wird ausgenutzt

# Funktionen aufrufen
BasisNutzenberechnung()
LaufrichtungDB()
Papiernutzung()

# Ergebnisse anzeigen
print("Rohbogenformat:", RbBreite, "x", RbHohe, "mm")
print("Endformat:", EfBreite, "x", EfHohe, "mm mit", EfAnschnitt, "mm Anschnitt")
print("Es können", BasisAnzNutzen, "Nutzen herausgeschnitten werden. Es werden", PapierNutzung, "Prozent des Rohbogens genutzt.")
print("Der Rohbogen muss", LaufrichtungRB, "haben, um die gewünschte Laufrichtung (", EfLaufrichtung, ") im Endformat zu erreichen.")