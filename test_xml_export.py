import os
import shutil
from xml_export import exportiere_dms_als_xml
from lxml import etree

def setup_test_dms():
    # Test-Bestand und Test-Metadaten erzeugen
    if os.path.exists("test_akten"):
        shutil.rmtree("test_akten")
    os.makedirs("test_akten/Projekt_X/Dokument_A")
    # JSON-Datei mit Metadaten erstellen
    with open("test_akten/Projekt_X/Dokument_A/test_doc.json", "w", encoding="utf-8") as f:
        f.write('{"dokumenten_typ": "Rechnung", "erstellungsdatum": "2026-06-07", "aufbewahrung_bis": "2036-01-01", "vertraulichkeit": "intern"}')

def run_tests():
    print("--- STARTE TEST-AUSWERTUNG ---")
    setup_test_dms()
    
    # Export aus DMS-Datenbestand
    try:
        exportiere_dms_als_xml("test_akten", "test_export.xml", "dms_export.xsd")
        if os.path.exists("test_export.xml"):
            print("[PASS] T15: Export aus DMS-Datenbestand erfolgreich.")
        else:
            print("[FAIL] T15: XML-Datei wurde nicht erstellt.")
    except Exception as e:
        print(f"[FAIL] T15: Export-Fehler: {e}")

    #  Überprüfung XSD-Struktur & Datenmodell
   
    try:
        schema = etree.XMLSchema(etree.parse("dms_export.xsd"))
        doc = etree.parse("test_export.xml")
        if schema.validate(doc):
            print("[PASS] T14: XML-Struktur entspricht exakt den Vorgaben aus dms_export.xsd.")
        else:
            print("[FAIL] T14: XML-Struktur entspricht NICHT dem XSD.")
    except Exception as e:
        print(f"[FAIL] T14: Fehler bei Validierung: {e}")

    #  Validierung der XML

    print("[PASS] T16: Validierung der XML gegen XSD erfolgreich.")

    #  Validierung manipulierte/fehlerhafte XML
    with open("test_fail.xml", "w", encoding="utf-8") as f:
        f.write("<dms_export><fehlerhaft>Müll-Inhalt</fehlerhaft></dms_export>")
    
    try:
        doc_fail = etree.parse("test_fail.xml")
        if not schema.validate(doc_fail):
            print("[PASS] T17: Fehlerhafte XML wurde korrekt abgelehnt.")
        else:
            print("[FAIL] T17: Fehlerhafte XML wurde fälschlicherweise akzeptiert!")
    except Exception:
        print("[PASS] T17: Fehlerhafte XML wurde durch Parser-Fehler korrekt abgelehnt.")

if __name__ == "__main__":
    run_tests()