import os 
from datetime import date 

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
