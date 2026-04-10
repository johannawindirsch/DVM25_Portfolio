# Task2
#Prüfen, ob die Ordner "test_posteingang/" und "test_isolierstation/" existieren
#Wenn nicht, dann sollen sie erstellt werden 

import os 
from pathlib import Path 

def setup_tests(): # Pfade definieren 
    posteingang = Path("test_posteingang")
    isolierstation = Path("test_isolierstation")

    for ordner in [posteingang, isolierstation]:
        if ordner.exists(): # wenn JA, dann leeren!
            print(f"Der Ordner '{ordner}' existiert bereits und wird geleert.")
            for datei in ordner.iterdir():
                if datei.is_file():
                    datei.unlink() # Dateien werden gelöscht
        else: # wenn NEIN, dann erstellen!
            print(f"Der Ordner '{ordner}' existiert nicht und wird erstellt.")
            ordner.mkdir() # erstellt den Ordner!  

# 2. Erzeugen von testdateien 

    print("--- Erstelle Testdateien! ---")

# Testdateien nach der Tabelle erzeugen
# AF1: Dateien mit Inhalt,T01a bis T01d (> 0 Byte)

    (posteingang / "antrag_normal.pdf").write_text("Testinhalt")
    (posteingang / "notiz.txt").write_text("Testinhalt")
    (posteingang / "bild.jpg").write_text("Testinhalt")
    (posteingang / "datei_groß.PDF").write_text("Testinhalt")

#AF2 Dateien für die Isolierstation: von T02a bis T03 (> 0 Byte)

    (posteingang / "virus.exe").write_text("böser Code")
    (posteingang / "update.zip").write_text("App")
    (posteingang / "datei_ohne-endung").write_text("Testinhalt")

#AF3 Leere Dateien (0 Byte) : T04 bis T05 ( 0 Byte)
    (posteingang / "leerdatei.pdf").touch() # erstellt eine leere Datei
    (posteingang / "keine_endung").touch() # erstellt eine leere Datei

    print("--- Testumgebung erfolgreich eingerichtet! ---")

if __name__ == "__main__":
    setup_tests()