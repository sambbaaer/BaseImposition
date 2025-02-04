# --- Variabelnberechnung ---

# Endformat (Ef)
EfBreite = 297  # in Millimeter
EfHohe = 210    # in Millimeter
EfLaufrichtung = "Breitbahn"  # "Breitbahn" oder "Schmalbahn"
EfAnschnitt = 3  # in Millimeter

# Rohbogen (Rb)
RbBreite = 700  # in Millimeter
RbHohe = 500    # in Millimeter

# Endformat Aufbereitung - Rechnungsendformat (REf)
REfLaufrichtung = 1  # 1 = BB | 2 = SB (Standard BB)
REfBreite = 0        # Breite inklusive 2x Anschnitt
REfHohe = 0          # Höhe inklusive 2x Anschnitt

def REfAufbereitung():
    """Berechnet Rechnungsendformat und Laufrichtung."""
    global REfLaufrichtung, REfBreite, REfHohe
    if EfLaufrichtung == "Breitbahn":  # Laufrichtungsstring zu einer Zahl umwandeln
        REfLaufrichtung = 1
    else:
        REfLaufrichtung = 2
    # Masse inklusive Anschnitt berechnen
    REfBreite = EfBreite + (2 * EfAnschnitt)
    REfHohe = EfHohe + (2 * EfAnschnitt)

#Hauptprogramm
REfAufbereitung()