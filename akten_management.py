import os 
import json
from datetime import date 

def run_registration(eingang_ordner, tagespost_ordner):
    heute = date.today()

    # Datum erstellen!
    datum_string = heute.isoformat()
    
    dateien_im_eingang = os.listdir(eingang_ordner)
    
    for dateiname in dateien_im_eingang:
    
        alle_tagespost_dateien = os.listdir(tagespost_ordner)
        hoechste_nummer = 0
        
        for t_datei in alle_tagespost_dateien:
            if datum_string in t_datei:
                teile = t_datei.split("_")
                if len(teile) >= 2:
                    nummer_als_zahl = int(teile[1])
                    if nummer_als_zahl > hoechste_nummer:
                        hoechste_nummer = nummer_als_zahl
        
        neue_nummer = hoechste_nummer + 1
        
        # Nummer formatieren!
        if neue_nummer < 10:
            nummer_text = "00" + str(neue_nummer)
        elif neue_nummer < 100:
            nummer_text = "0" + str(neue_nummer)
        else:
            nummer_text = str(neue_nummer)

        # Neuen Namen bauen
        neuer_name = datum_string + "_" + nummer_text + "_" + dateiname
        
        quelle = eingang_ordner + "/" + dateiname
        ziel = tagespost_ordner + "/" + neuer_name
        os.rename(quelle, ziel)


# 2. 
def ordne_akte_zu(dateipfad_quelle, aktenzeichen, akten_basis_ordner):
    #  Ordner erstellen
    ziel_ordner = akten_basis_ordner + "/" + aktenzeichen
    os.makedirs(ziel_ordner, exist_ok=True)
    
    # Dateiname isolieren!
    dateiname = dateipfad_quelle.split("/")[-1]
    
    # Datei verschieben und umbenennen!
    ziel_pfad = ziel_ordner + "/" + dateiname
    os.rename(dateipfad_quelle, ziel_pfad)

    # Datum aus dem Dateinamen extrahieren 
    datum_aus_name = dateiname.split("_")[0]

    # Metadaten erstellen! 
    metadaten = {
        "dokumenten_typ": "Unbekannt",       
        "registrierungsdatum": datum_aus_name,  
        "aufbewahrung_bis": "2036-01-01",     
        "vertraulichkeit": "intern"           
    }

    # Json - Endungen festlegen! 

    name_ohne_endung = dateiname.rsplit(".", 1)[0]
    json_pfad = ziel_ordner + "/" + name_ohne_endung + ".json"

    with open(json_pfad, "w") as json_datei:
        json.dump(metadaten, json_datei, indent=4)