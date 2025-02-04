from datenloader import daten
from config import RbBreite, RbHohe, REfBreite, REfHohe

def dbcalculation(maschinenname):
    """Berechnet Parameter für eine gegebene Maschine."""
    maschine = daten.get(maschinenname, None)
    if maschine is None:
        raise ValueError(f"Maschine '{maschinenname}' nicht gefunden.")
    
    # Maximal- und Minimalformat aus JSON auslesen
    max_breite, max_hohe = maschine.get("Maximalformat", [float('inf'), float('inf')])
    min_breite, min_hohe = maschine.get("Minimalformat", [0, 0])

    # Prüfen, ob der Rohbogen innerhalb der erlaubten Formate liegt
    if not (min_breite <= RbBreite <= max_breite and min_hohe <= RbHohe <= max_hohe):
        AnzNutzen1 = (max_breite // REfBreite) * (max_hohe // REfHohe)  # Hochkant
        AnzNutzen2 = (max_breite // REfHohe) * (max_hohe // REfBreite)  # Quer

        # Größere Nutzenanzahl auswählen
        BasisAnzNutzen = max(AnzNutzen1, AnzNutzen2)
        
        # Randberechnung (Druckrand und optional Greiferrand)
        druckrand = maschine.get("Druckrand", 0)
        greiferrand = maschine.get("Greiferrand", 0)
        randHohe = (druckrand * 2) if greiferrand == 0 else (druckrand + greiferrand)

        # Berechnung der optimalen Breite und Höhe basierend auf der besten Nutzenanzahl
        if BasisAnzNutzen == AnzNutzen1:
            optimalBreite = ((max_breite // REfBreite) * REfBreite) + (2 * druckrand)
            optimalHohe = ((max_hohe // REfHohe) * REfHohe) + randHohe
        else:
            optimalBreite = ((max_breite // REfHohe) * REfHohe) + (2 * druckrand)
            optimalHohe = ((max_hohe // REfBreite) * REfBreite) + randHohe
        
        print(f"⚠️ Rohbogen passt nicht optimal, aber bestmöglich nutzbare Fläche: {optimalBreite} x {optimalHohe} mm")
    
    else:
        print(f"✅ Rohbogen passt in {maschinenname}. Größe: {RbBreite} x {RbHohe} mm")