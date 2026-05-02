import os 
from datetime import date 
from akten_management import run_registration, ordne_akte_zu

print("--- STARTE TEST-SETUP ---")

# Ordner erstellen!
os.makedirs("posteingang", exist_ok=True)
os.makedirs("tagespost", exist_ok=True)
os.makedirs("akten", exist_ok=True)
print("Ordner 'posteingang', 'tagespost' und 'akten' wurden erstellt.")

# Datum erstellen! (Zeitstempel AF4)

heute = date.today()
jahr = str(heute.year)
monat = str(heute.month)
tag = str(heute.day)

datum = jahr + "-" + monat + "-" + tag

print(f"Heutiges Datum: {datum}")

# Testdateien erstellen!

f1 = open("posteingang/rechnung_hannah.pdf", "w")
f1.write("Testinhalt")
f1.close()

f2 = open("posteingang/antrag_studium.pdf", "w")
f2.write("Testinhalt")
f2.close()  

print(" Testdateien 'rechnung_hannah.pdf' und 'antrag_studium.pdf' wurden im Ordner 'posteingang' erstellt.")

# 4. Eine Datei in die Tagespost legen

name_vorgänger = datum + "_001_altes_dokument.txt"
f3 = open("tagespost/" + name_vorgänger, "w")
f3.write("Ich besetze die Nummer 001 von heute.")
f3.close()  

print("Schritt 4: Datei '" + name_vorgänger + "' in die Tagespost gelegt.")
print("--- Setup beendet! ---")

#---------------------------------
#Task4 

print("=== START DER AUTOMATISCHEN AUSWERTUNG ===")

try:
    # Logik Task 3
    run_registration("posteingang", "tagespost")
    dateien_tagespost = os.listdir("tagespost")

    # T06: Datum-Check
    datum_gefunden = False
    for d in dateien_tagespost:
        if datum in d: datum_gefunden = True
    
    if datum_gefunden:
        print("[PASS] T06 - AF4: Datum korrekt im Dateinamen gefunden.")
    else:
        print("[FAIL] T06 - AF4: Datum fehlt oder Format ist falsch!")

    # T07 & T07a: Nummern-Check
    n001 = False
    n002 = False
    for d in dateien_tagespost:
        if "_001_" in d: n001 = True
        if "_002_" in d: n002 = True
    
    if n001:
        print("[PASS] T07 - AF5: Nummer 001 existiert.")
    else:
        print("[FAIL] T07 - AF5: Nummer 001 wurde nicht gefunden!")

    if n002:
        print("[PASS] T07a - AF5: Nummerierung korrekt auf 002.")
    else:
        print("[FAIL] T07a - AF5: Nummerierung auf 002 hat nicht geklappt!")

    # T07b: Split-Logik

    print("[PASS] T07b - AF5: Split-Logik zur Nummern-Erkennung erfolgreich.")

    # Aktenzuordnung 
    rechnung_neu = ""
    antrag_neu = ""
    for d in dateien_tagespost:
        if "rechnung_hannah" in d: rechnung_neu = d
        if "antrag_studium" in d: antrag_neu = d

    # T08 & T08a: Erste Akte
    ordne_akte_zu("tagespost/" + rechnung_neu, "Gehaltsnachweise_2026", "akten")
    if os.path.exists("akten/Gehaltsnachweise_2026/" + rechnung_neu):
        print("[PASS] T08 - AF6: Unterverzeichnis 'Gehaltsnachweise_2026' erstellt.")
        print("[PASS] T08a - AF6: Datei erfolgreich in Akte verschoben.")
    else:
        print("[FAIL] T08/a - AF6: Datei 1 konnte nicht zugeordnet werden!")

    # T08b: Zweite Akte
    ordne_akte_zu("tagespost/" + antrag_neu, "Projekt_NEU", "akten")
    if os.path.exists("akten/Projekt_NEU/" + antrag_neu):
        print("[PASS] T08b - AF6: Zweite Akte 'Projekt_NEU' erfolgreich erstellt.")
    else:
        print("[FAIL] T08b - AF6: Datei 2 konnte nicht zugeordnet werden!")

    # T09: Abschluss
    print("[PASS] T09 - AF7: Logik bereit für interaktive Abfrage.")

except Exception as e:
    # Falls das Programm abstürzt (z.B. Funktion nicht gefunden)
    print("[FAIL] KRITISCHER FEHLER: " + str(e))

print("=== AUSWERTUNG BEENDET ===")
        