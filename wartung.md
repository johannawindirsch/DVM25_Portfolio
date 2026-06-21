# level 5 - task 1 - Wartungsvorlage!

## Änderungsanfrage für : 


| Punkt | Frage | Antwort |
|---|---|---|
| 1. Ziel | Was soll sich fachlich ändern? | ... |
| 2. Fundstellen | In welchen Dateien/Funktionen wird das aktuelle Verhalten vermutlich umgesetzt? | ... |
| 3. Risiko | Welche bestehende Funktion könnte durch die Änderung kaputtgehen? | ... |
| 4. Test vor Code | Welcher Test muss vor der Umsetzung ergänzt oder angepasst werden? | ... |
| 5. Entscheidung | Gibt es eine fachliche oder technische Entscheidung, die vor dem Coding getroffen werden muss? | ... | 


## Änderungsanfrage: AF17 – PNG als Eingangsformat

| Punkt | Frage | Antwort |
|---|---|---|
| 1. Ziel | Was soll sich fachlich ändern? | Das DMS muss künftig `.png`-Dateien (Screenshots/Scans) als erlaubtes Format im Posteingang akzeptieren und verarbeiten. Unerlaubte Formate (`.exe`, `.zip` etc.) müssen weiterhin isoliert werden. |
| 2. Fundstellen | In welchen Dateien/Funktionen wird das aktuelle Verhalten vermutlich umgesetzt? | `triage.py`, Funktion `run_triage`. |
| 3. Risiko | Welche bestehende Funktion könnte durch die Änderung kaputtgehen? | Eine fehlerhafte Anpassung könnte dazu führen, dass schädliche Dateien (wie `.exe`) fälschlicherweise durchgelassen werden oder harmlose Dateitypen blockiert werden. |
| 4. Test vor Code | Welcher Test muss vor der Umsetzung ergänzt oder angepasst werden? | In TESTING.md wird Testfall T18 für eine valide `.png`-Datei angelegt. Als Regressionsnachweis dienen die bestehenden Tests T02a/T02b/T03 aus Level 1 |
| 5. Entscheidung | Gibt es eine fachliche oder technische Entscheidung, die vor dem Coding getroffen werden muss? | Die Endungs-Prüfung in run_triage wird umgebaut- Statt nur verbotene Endungen zu listen, wird künftig geprüft, ob die Endung auf einer Liste erlaubter Formate (.pdf, .txt, .jpg, .png) steht – alles andere landet automatisch in der Isolierstation. So sind auch künftig unbekannte Dateitypen automatisch sicher abgedeckt.|

# Anmerkungen: 
# Regressionstest ist durch T02a/T02b/T03 abgedeckt, deshalb keiner zusätzlich nötig
# Einfügen von Code in Triage statt "verbotene Endungen" in "nur die sind erlaubt- Endungen"! Hätte man es nur bei den unerlaubten Endungen gelassen, hätten da immer wieder welche die unbekannt sind durchrutschen können!
# Dokumentation in test_run.log


## Änderungsanfrage: AF18 – Feldname umbenennen

| Punkt | Frage | Antwort |
|---|---|---|
| 1. Ziel | Was soll sich fachlich ändern? | Das JSON-Metadatenfeld `erstellungsdatum` soll in `registrierungsdatum` umbenannt werden, da der gespeicherte Wert nie das echte Erstellungsdatum des Dokuments ist, sondern das Datum, an dem es im DMS registriert wurde. Der neue Name passt außerdem zum bereits bestehenden XML-Element `registrierungs_datum`. |
| 2. Fundstellen | In welchen Dateien/Funktionen wird das aktuelle Verhalten vermutlich umgesetzt? | `akten_management.py` (Funktion `ordne_akte_zu`, wo das Feld geschrieben wird); `xml_export.py` (Funktion `exportiere_dms_als_xml`, wo das Feld per `data.get("erstellungsdatum", ...)` ausgelesen wird) und `test_setup_reg.py`. |
| 3. Risiko | Welche bestehende Funktion könnte durch die Änderung kaputtgehen? | Altdaten (bereits existierende JSON-Dateien mit dem alten Key `erstellungsdatum`) könnten beim Lesen ignoriert werden – in `xml_export.py` würde `.get()` dann lautlos auf den Standardwert zurückfallen, statt das echte Datum zu exportieren. |
| 4. Test vor Code | Welcher Test muss vor der Umsetzung ergänzt oder angepasst werden? | T11 wird auf den neuen Feldnamen `registrierungsdatum` angepasst. T14/T16 (XML-Struktur-Validierung) werden erneut geprüft, da das Feld in die XML-Datei einfließt. Zusätzlich neuer Testfall: eine JSON-Datei mit dem altem Feldnamen `erstellungsdatum` wird weiterhin korrekt gelesen. |
| 5. Entscheidung | Gibt es eine fachliche oder technische Entscheidung, die vor dem Coding getroffen werden muss? |  System schreibt neue Dateien mit dem Key `registrierungsdatum`. Beim Lesen einer alten JSON-Datei wird geprüft, ob der alte Key `erstellungsdatum` existiert; falls ja, wird er auf den neuen Key gemappt, damit der XML-Export reibungslos funktioniert. |

--- 

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

## Outcome1 --> als test das datum von 07.06.26 zu 08.06.26 geändert --> funktioneirt!!

## <?xml version='1.0' encoding='utf-8'?>
<dms_export>
    <export_datum>2026-06-21T10:46:13.731775</export_datum>
    <akte>
        <akten_name>Projekt_X</akten_name>
        <dokument>
            <dateiname>test_doc</dateiname>
            <metadaten>
                <dokumenten_typ>Rechnung</dokumenten_typ>
                <registrierungs_datum>2026-06-08</registrierungs_datum>
                <aufbewahrung_bis>2036-01-01</aufbewahrung_bis>
                <vertraulichkeit>intern</vertraulichkeit>
            </metadaten>
        </dokument>
    </akte>
</dms_export>


### Begründung der Strategie & Folgen für alte/neue Metadaten

**Warum diese Strategie zum DMS passt:** In der öffentlichen Verwaltung gilt der
Grundsatz der Revisionssicherheit – bereits archivierte Akten und deren Metadaten
dürfen nicht nachträglich automatisiert massenhaft überschrieben werden. Eine
Migration aller bestehenden JSON-Dateien wäre also unpassend. Die Fallback-Strategie
löst das rein softwareseitig, ohne die archivierten Daten selbst anzufassen.

**Folgen für neue Metadaten:** Werden ab sofort direkt mit dem fachlich korrekten
Feldnamen `registrierungsdatum` geschrieben (`akten_management.py`). Kein
Unterschied im Verhalten für nachgelagerte Systeme wie den XML-Export.

**Folgen für alte Metadaten:** Bleiben unverändert mit dem Feldnamen
`erstellungsdatum` auf der Festplatte liegen – keine Migration, keine
nachträgliche Bearbeitung. Beim XML-Export werden sie automatisch über die
Fallback-Logik in `xml_export.py` erkannt und korrekt verarbeitet.

# Alle 22 bestehenden Tests laufen nach der Änderung weiterhin auf PASS – keine Regression festgestellt (vollständiges Protokoll siehe test_run.log).



### Level 5 - Task 4 -- AF20 - Wartbarkeit

**Gewählte Stelle:** `triage.py`, Funktion `run_triage()` – die Liste `erlaubte_endungen` ist aktuell lokal innerhalb der Funktion definiert.

**Begründung & Ziele:** Eine Liste mit fachlichen Regeln (welche Dateiformate sind erlaubt) sollte als gut sichtbare, benannte Konstante am Dateianfang stehen statt in einer Funktion versteckt zu sein. Das bringt drei Vorteile:
1. **Sichtbarkeit:** Die fachliche Regel ist sofort erkennbar, ohne erst in die Funktion schauen zu müssen.
2. **Wiederverwendbarkeit:** Andere Funktionen in der Datei könnten künftig ebenfalls auf dieselbe Liste zugreifen, statt sie zu duplizieren.
3. **Wartungsfreundlichkeit:** Künftige Änderungen (z. B. ein weiteres erlaubtes Format) lassen sich an einer klar erkennbaren Stelle vornehmen, statt im Funktionskörper danach zu suchen.

**Ist-Zustand (was der Code aktuell macht):** In `triage.py`, Funktion `run_triage()`, wird die Liste `erlaubte_endungen` (`.pdf`, `.txt`, `.jpg`, `.png`) bei jedem Aufruf der Funktion neu lokal erzeugt. Die `elif`-Bedingung prüft für jede Datei im Posteingang, ob ihre Endung NICHT in dieser Liste enthalten ist – falls ja, wird die Datei in die Isolierstation verschoben, andernfalls bleibt sie im Posteingang. Die Liste ist aktuell nur innerhalb der Funktion sichtbar und nicht zentral wiederverwendbar.

**Nachweis:** Tests vor und nach der Umstellung liefern identische Ergebnisse (alle 10 Tests PASS, gleiche Dateizuordnung). Das fachliche Verhalten ist unverändert, nur die Codestruktur wurde verbessert. Siehe test_run_log

-