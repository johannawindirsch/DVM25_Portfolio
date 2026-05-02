# Level 1 : testdefinitionen festlegen 

| ID | AF | Datei | Eigenschaft | Erwartetes Ergebnis 
|:---|:---|:---|:---|:---|
| T01a | AF1 | antrag_normal.pdf (Inhalt: "Test") | > 0 Byte | bleibt in posteingang/ |
| T01b | AF1 | notiz.txt (Inhalt: "Test")| > 0 Byte | bleibt posteingang/ |
| T01c | AF1 | bild.jpg (Inhalt: "Test") | > 0 Byte | bleibt in posteingang/ |
| T01d | AF1 | datei_groß.PDF (Inhalt: "Test") | > 0 Byte | bleibt in posteingang/ |
| T02a | AF2 | virus.exe (Inhalt: "böser Code") | > 0 Byte | wird in isolierstation/ verschoben |
| T02b | AF2 | update.zip (Inhalt: App) | > 0 Byte | wird in isolierstation/ verschoben |
| T03 | AF2 | datei_ohne_endung (Inhalt: "Test")| > 0 Byte | wird in isolierstation/ verschoben |
| T04 | AF3 | leerdatei.pdf | 0 Byte | Datei wird gelöscht, Konsole zeigt an "Gelöscht (0 Byte): [Dateiname]" |
| T5 | AF3 | keine_endung | | 0 Byte | Datei wird gelöscht, Konsole zeigt an "Gelöscht (0 Byte): [Dateiname]" |

# Level 2 : Registrierung und Aktenanforderung 

| T06 | AF4 | rechnung_hannah.pdf | neue PDF Datei | wird zu 2024-11-20_001_rechnung_hannah.pdf |
| T07 | AF5 | Start bei leeren Ordner | /tagespost ist leer | Start Sequenznummer bei 001 |
| T07a | AF5 | /tagespost hat Inhalt | enthält Sequenznummer 001 | neue datei erhält Sequenznummer 002 |
| T07b | AF5 | Nummer Extraktion | mit Split-Funktion | Nummer 001 wird erkannt und korrekt um 001 erhöht | 
| T08 | AF6 | Gehaltsnachweise_2026 | Aktenzeichen | Erstellen Unterverzeichnis akten/Gehaltsnachweise_2026/ wird erstellt | 
| T08a | AF6 | Akte wird verschoben | Abschluss Aktion | Datei wird erfolgreich von /tagespost zu akten/Gehaltsnachweise_2026/ verschoben | 
| T08b | AF6 | Projekt_NEU | Zweite Akte | Erstellen neuer Aktenordner und Dateien werden dorthin verschoben | 
| T09 | AF7 | 2 Dateien im Posteingang | Interaktive Abfrage | Skript wird bei der Abfrage gestoppt und fragt nach Aktenzeichen | 