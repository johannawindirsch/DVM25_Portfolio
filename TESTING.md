# Task 1 : testdefinitionen festlegen 

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
