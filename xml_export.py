import os
import json
import datetime
import xml.etree.ElementTree as ET

try:
    from lxml import etree
    LXML_VORHANDEN = True
except ImportError:
    LXML_VORHANDEN = False
    print("ACHTUNG: 'lxml' ist nicht installiert. Validierung wird übersprungen.")

def exportiere_dms_als_xml(akten_basis_ordner, ziel_xml_pfad, schema_pfad):
    print(f"--- Starte Export ---")
    
    # Root-Element erstellen
    root = ET.Element("dms_export")
    
    # Datum
    datum_element = ET.SubElement(root, "export_datum")
    datum_element.text = datetime.datetime.now().isoformat()
    
    #  Akten durchsuchen 
    if not os.path.exists(akten_basis_ordner):
        print(f"FEHLER: Ordner '{akten_basis_ordner}' nicht gefunden!")
        return

    for akten_name in os.listdir(akten_basis_ordner):
        pfad_zur_akte = os.path.join(akten_basis_ordner, akten_name)
        
        if os.path.isdir(pfad_zur_akte):
            akte_node = ET.SubElement(root, "akte")
            ET.SubElement(akte_node, "akten_name").text = akten_name
            
            for dateiname in os.listdir(pfad_zur_akte):
                if dateiname.endswith(".json"):
                    pfad_json = os.path.join(pfad_zur_akte, dateiname)
                    
                    with open(pfad_json, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    dok_node = ET.SubElement(akte_node, "dokument")
                    ET.SubElement(dok_node, "dateiname").text = dateiname.replace(".json", "")
                    
                    meta_node = ET.SubElement(dok_node, "metadaten")
                    ET.SubElement(meta_node, "dokumenten_typ").text = data.get("dokumenten_typ", "Unbekannt")
                    
                   
                    ET.SubElement(meta_node, "registrierungs_datum").text = data.get("erstellungsdatum", "2026-06-07")
                    ET.SubElement(meta_node, "aufbewahrung_bis").text = data.get("aufbewahrung_bis", "2036-01-01")
                    ET.SubElement(meta_node, "vertraulichkeit").text = data.get("vertraulichkeit", "intern")

 
    tree = ET.ElementTree(root)

    ET.indent(tree, space="    ", level=0)
    tree.write(ziel_xml_pfad, encoding="utf-8", xml_declaration=True)
    print(f"XML-Datei erfolgreich unter '{ziel_xml_pfad}' erstellt.")

    #  XSD-Validierung
    if LXML_VORHANDEN:
        print("Starte XSD-Validierung...")
        if os.path.exists(schema_pfad):
            try:
                xml_schema_doc = etree.parse(schema_pfad)
                xml_schema = etree.XMLSchema(xml_schema_doc)
                xml_doc = etree.parse(ziel_xml_pfad)
                
                if xml_schema.validate(xml_doc):
                    print("ERFOLG: XML ist valide!")
                else:
                    print("FEHLER: XML ist NICHT valide!")
                    print(xml_schema.error_log)
            except Exception as e:
                print(f"Technischer Fehler bei Validierung: {e}")
        else:
            print(f"FEHLER: Schema-Datei '{schema_pfad}' nicht gefunden.")

if __name__ == "__main__":
    exportiere_dms_als_xml("akten", "dms_export.xml", "dms_export.xsd")
    print("--- Programm beendet ---")