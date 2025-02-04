from datenloader import daten
from config import RbBreite, RbHohe, REfBreite, REfHohe

AnzNutzen1 = 0
AnzNutzen2 = 0
optiNzRb1 = 0
optiNzRb2 = 0
optimalBreite = 0
optimalHohe = 0


def dbcalculation(maschinenname):
    """Berechnet, ob der gegebene Rohbogen in die Maschine passt oder eine Optimierung nötig ist."""
    global AnzNutzen1, AnzNutzen2, optimalBreite, optimalHohe

    maschine = daten.get(maschinenname, None)
    if maschine is None:
        raise ValueError(f"Maschine '{maschinenname}' nicht gefunden.")
    
    # Maschinenformate aus JSON laden
    max_breite, max_hohe = maschine.get("Maximalformat", [float('inf'), float('inf')])
    min_breite, min_hohe = maschine.get("Minimalformat", [0, 0])

    # Druckrand und Greiferrand
    druckrand = maschine.get("Druckrand", 0)
    greiferrand = maschine.get("Greiferrand", 0)
    randHohe = druckrand * 2 if greiferrand == 0 else druckrand + greiferrand

    # Prüfen, ob der Rohbogen direkt in die Maschine passt
    if min_breite <= RbBreite <= max_breite and min_hohe <= RbHohe <= max_hohe:
        print(f"✅ Rohbogen passt in {maschinenname}. Größe: {RbBreite} x {RbHohe} mm")
        return
    
    # Falls nicht passend: Beste Möglichkeit berechnen
    AnzNutzen1 = (max_breite // REfBreite) * (max_hohe // REfHohe)  # Hochkant
    AnzNutzen2 = (max_breite // REfHohe) * (max_hohe // REfBreite)  # Quer

    # Optimale Nutzung bestimmen
    if AnzNutzen1 >= AnzNutzen2:
        optimalBreite = (max_breite // REfBreite) * REfBreite + (2 * druckrand)
        optimalHohe = (max_hohe // REfHohe) * REfHohe + randHohe
    else:
        optimalBreite = (max_breite // REfHohe) * REfHohe + (2 * druckrand)
        optimalHohe = (max_hohe // REfBreite) * REfBreite + randHohe

    print(f"⚠️ Rohbogen passt nicht optimal. Bestmögliche nutzbare Fläche: {optimalBreite} x {optimalHohe} mm")

def optimalformat():
    """Berechnet, wie viele optimale Druckbogen aus dem Rohbogen geschnitten werden können."""
    global optiNzRb1, optiNzRb2, optimalBreite, optimalHohe

    optiNzRb1 = (RbBreite // optimalBreite) * (RbHohe // optimalHohe)
    optiNzRb1 = (RbBreite // optimalHohe) * (RbHohe // optimalBreite)

    # Sind mehr als 1 optimal Druckbogen möglich aus einem Rohbogen?
    if optiNzRb1 > 1
        print(f"ℹ️ Es können {optiNzRb1} Druckbogen im Format {optimalBreite} x {optimalHohe} mm aus dem Rohbogen geschnitten werden.")
    else if optiNzRb2 > 1
        print(f"ℹ️ Es können {optiNzRb2} Druckbogen im Format {optimalBreite} x {optimalHohe} mm aus dem Rohbogen geschnitten werden.")
    else
        print(f"ℹ️ Das Druckformat {optimalBreite} x {optimalHohe} mm wird nicht empfohlen, da nur ein Druckbogen aus einem Rohbogen geschnitten werden kann.")
