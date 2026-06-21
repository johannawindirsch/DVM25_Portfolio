# DVM25 Portfolio – Dokumentenmanagementsystem (DMS)

Kurze Übergabe-Dokumentation für eine nachfolgende Entwicklergruppe.

## Wie man das Projekt startet

- Es gibt drei unabhängige Einstiegspunkte, je nach Anwendungsfall:
  - `python3 main.py` – Vorsortierung des Posteingangs (Level 1)
  - `python3 main_interaktiv.py` – Registrierung & interaktive Aktenzuordnung auf den echten Ordnern `posteingang/`, `tagespost/`, `akten/` (Level 2)
  - `python3 xml_export.py` – Export des aktuellen Aktenbestands als `dms_export.xml`, inkl. Validierung gegen `dms_export.xsd` (Level 4)

## Welche Dateien zentral sind

| Datei | Zweck |
|---|---|
| `triage.py` | Vorsortierung des Posteingangs: erlaubte Formate, Isolierung gefährlicher/unbekannter Dateien, Löschen leerer Dateien (AF1–AF3, AF17) |
| `akten_management.py` | Eingangsstempel & Tages-Sequenz (`run_registration`), Aktenzuordnung & JSON-Metadaten (`ordne_akte_zu`) (AF4–AF11, AF18) |
| `xml_export.py` | Export des Aktenbestands als XML, XSD-Validierung (AF12–AF15) |
| `dms_export.xsd` | Formales Schema für den XML-Export |
| `main.py` / `main_interaktiv.py` | Einstiegspunkte, die die obigen Module orchestrieren |
| `WARTUNG.md` | Vorlage und Historie aller Änderungsanfragen |
| `TESTING.md` / `ANFORDERUNGEN.md` / `USER_STORIES.md` | Anforderungs- und Testdokumentation |

## Wie man die Tests ausführt

Drei Testskripte, unabhängig voneinander, jeweils mit eigener Testumgebung:

python3 main.py            # Level 1 - Tests T01-T05, T18
python3 test_setup_reg.py  # Level 2-3 - Tests T06-T13
python3 test_xml_export.py # Level 4 - Tests T14-T17

Alle drei geben `[PASS]`/`[FAIL]` pro Testfall auf der Konsole aus. Ein
zusammenfassender Nachweis aller Tests nach den Level-5-Änderungen steht in
`regression_test_run.log`.

## Bekannte Schwächen

- **Teilstring-Datumsvergleich in `run_registration()`:** Die Erkennung "gehört
  diese Datei zu heute?" prüft per `if datum_string in t_datei`. Bei sehr
  ähnlichen Daten kann das zu falschen Treffern führen (z. B. ist `"2026-5-1"`
  auch Teilstring von `"2026-5-10"`).
- **Feste Platzhalterwerte:** `aufbewahrung_bis` und `vertraulichkeit` erhalten
  aktuell für jede Datei denselben festen Wert, nicht dokumenten- oder
  aktenspezifisch.
- **Dauerhafte Fallback-Logik (AF18):** Die Abwärtskompatibilität für den
  Feldnamen `erstellungsdatum` → `registrierungsdatum` muss im Code bleiben,
  solange alte JSON-Dateien existieren könnten – es gibt keine automatische
  Migration.
- **Separate Datumsberechnung in `test_setup_reg.py`:** Nutzt eine eigene,
  nicht mit `akten_management.py` geteilte Berechnung des heutigen Datums
  (ohne führende Nullen bei einstelligen Monaten/Tagen) – rein für die Testumgebung,
   ohne Auswirkung auf die produktive Logik.

   

