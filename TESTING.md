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

| ID | AF | Datei / Eingabe | Eigenschaft | Erwartetes Ergebnis |
|:---|:---|:---|:---|:---|
| T06 | AF4 | rechnung_hannah.pdf | neue PDF Datei | wird zu 2024-11-20_001_rechnung_hannah.pdf |
| T07 | AF5 | Start bei leeren Ordner | /tagespost ist leer | Start Sequenznummer bei 001 |
| T07a | AF5 | /tagespost hat Inhalt | enthält Sequenznummer 001 | neue datei erhält Sequenznummer 002 |
| T07b | AF5 | Nummer Extraktion | mit Split-Funktion | Nummer 001 wird erkannt und korrekt um 001 erhöht | 
| T08 | AF6 | Gehaltsnachweise_2026 | Aktenzeichen | Erstellen Unterverzeichnis akten/Gehaltsnachweise_2026/ wird erstellt | 
| T08a | AF6 | Akte wird verschoben | Abschluss Aktion | Datei wird erfolgreich von /tagespost zu akten/Gehaltsnachweise_2026/ verschoben | 
| T08b | AF6 | Projekt_NEU | Zweite Akte | Erstellen neuer Aktenordner und Dateien werden dorthin verschoben | 
| T09 | AF7 | 2 Dateien im Posteingang | Interaktive Abfrage | Skript wird bei der Abfrage gestoppt und fragt nach Aktenzeichen | 

# Level 3: Testdefinitionen festlegen 

| ID | AF | Testbedingungen | Erwartetes Ergebnis |
|:---|:---|:---|:---|
| T10 | AF8 | führt Skript aus und ordnet eine Datei einer Akte zu | Im Zielordner der Akte erscheint eine neue .json-Datei mit dem gleichen Namen wie das Dokument |
| T11 | AF9 |  .json-Datei existiert | Datei enthält die Keys  dokumenten_typ (initial: "Unbekannt") und erstellungsdatum |
| T12 | AF10 |  .json-Datei existiert | Datei enthält key "aufbewahrung_bis" |
| T13 | AF11 | .json-Datei existiert | Datei enthält key vertraulichkeit | 



# Level 4: Testdef. festlegen-->  XML-Export und Validierung

| ID | AF | Testbedingungen | Erwartetes Ergebnis |
|:---|:---|:---|:---|
| T14 | AF12/13 | Überprüfung der XSD-Struktur und Datenmodell-Konformität | XML-Struktur entspricht exakt den Vorgaben aus `dms_export.xsd` (Pflichtfelder/Typen). |
| T15 | AF14 | Export aus aktuellem DMS-Datenbestand | XML-Datei wird erstellt, enthält alle notwendigen Akten- und Dokumenteninformationen. |
| T16 | AF15 | Validierung der XML-Datei gegen das XSD-Schema | Validierung erfolgreich ("Valid XML"), Schema-Konformität bestätigt. |
| T17 | AF15 | Validierung einer manipulierten/fehlerhaften XML-Datei | Validierung schlägt fehl ("Invalid XML"), Fehler wird in Konsole/Log ausgegeben. |

# Level 5 Testfallerweiterung 

| ID | AF | Testbedingungen | Erwartetes Ergebnis |
|:---|:---|:---|:---|
| T18 | AF17 |  Datei mit erlaubter Endung .png liegt im Posteingang (z. B. bild_neu.png) | bleibt im posteingang/ |
| T19 | AF17 | Regressionstest (kein neuer Code nötig, siehe WARTUNG.md) | T02a/T02b/T03 bestätigen weiterhin korrekte Isolierung |

**AF18 – Feldumbenennung:** Das Metadatenfeld `erstellungsdatum` wird zu `registrierungsdatum` umbenannt. Der bisherige Name war fachlich ungenau, da das Feld nie das tatsächliche Erstellungsdatum eines Dokuments speichert, sondern das Datum seiner Registrierung im DM. Der neue Name ist präziser und stimmt zudem mit ### 1. Systemanalyse & Entscheidungen

**Wo wird der Feldname im Code erzeugt oder gelesen?**
- Erzeugt: in `akten_management.py`, Funktion `ordne_akte_zu()`, wo das Python-Dictionary für die JSON-Metadaten befüllt und per `json.dump()` geschrieben wird.
- Gelesen: in `xml_export.py`, Funktion `exportiere_dms_als_xml()`, wo die JSON-Dateien eingelesen werden, um die XML-Struktur zu generieren.

**Was passiert mit alten JSON-Metadaten-Dateien, die noch den bisherigen Feldnamen enthalten?**
Sie werden nicht ignoriert. Der Code in `xml_export.py` prüft beim Einlesen zuerst, ob der neue Key `registrierungsdatum` vorhanden ist. Fehlt er, wird auf den alten Key `erstellungsdatum` zurückgegriffen.

**Muss der XML-Export angepasst werden?**
Die XML-Struktur bleibt unverändert – das Element heißt weiterhin `registrierungs_datum`. Der Code in `xml_export.py` muss aber angepasst werden, um den neuen JSON-Key zu lesen und die Fallback-Logik für alte Dateien umzusetzen.

**Muss das XSD-Schema angepasst werden?**
Nein. Da sich das XML-Element nicht ändert, bleibt `dms_export.xsd` unverändert und weiterhin gültig.

**Welche Tests müssen geändert oder ergänzt werden?**
- T11 wird auf den neuen Feldnamen `registrierungsdatum` umgestellt.
- Neuer Testfall --> eine JSON-Datei mit dem alten Key `erstellungsdatum` wird angelegt und geprüft, dass sie trotzdem korrekt verarbeitet und exportiert wird.

---

### 2. Strategie für den Umgang mit bestehenden Daten

NEUE Dokumente  → akten_management.py schreibt "registrierungsdatum"
ALTE Dokumente  → liegen schon mit "erstellungsdatum" auf der Platte, bleiben so
                       ↓
        xml_export.py liest BEIDE Varianten beim Exportdem bereits bestehenden XML-Element `registrierungs_datum` überein.

