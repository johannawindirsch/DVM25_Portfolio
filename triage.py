from pathlib import Path

def run_triage(test_posteingang, test_isolierstation):
    posteingang = Path(test_posteingang)
    isolierstation = Path(test_isolierstation)

    gefaehrliche_endungen = [".exe", ".zip"]

    for datei in posteingang.iterdir(): 
        if datei.is_file():
            #AF3 leere Dateien prüfen und löschen!
            if datei.stat().st_size == 0: # wenn die Dateigröße = 0 Byte ist, dann löschen!
               datei.unlink()
               print(f"Die leere Datei '{datei.name}' wurde gelöscht.")
               

            #Af2 Dateien für Isolierstation prüfen und ggf verschieben!
           
            elif datei.suffix.lower() in gefaehrliche_endungen or not datei.suffix: # wenn die Dateiendung gefährlich ist oder keine Endung hat, dann verschieben!
                zielpfad = isolierstation / datei.name
                datei.rename(zielpfad) # verschiebt die Datei in die Isolierstation
                print(f"Die Datei '{datei.name}' wurde in die Isolierstation verschoben.")

                #AF1
            else:
                print(f"Die Datei '{datei.name}' ist unbedenklich.")
            
if __name__ == "__main__":
    run_triage("test_posteingang", "test_isolierstation")
