import os 

from akten_management import run_registration, ordne_akte_zu

print("=== STARTE INTERAKTIVE AUSWERTUNG ===")

# Registrierung 
run_registration("posteingang", "tagespost")

# Auslesen!
dateien = os.listdir("tagespost")

# for Schleife 
for datei in dateien:
  
    if not datei.startswith("."):
        
        # Interaktive Abfrage: Aktenzeichen eingeben
        eingabe = input(f"Bitte Aktenzeichen für '{datei}' eingeben: ")

        # Akte zuordnen
        ordne_akte_zu("tagespost/" + datei, eingabe, "akten")
        
        print(f"Datei wurde erfolgreich in Akte '{eingabe}' einsortiert.")

print("\n=== ALLE DATEIEN VERARBEITET ===")