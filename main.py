import os 
#Import der anderen Funktionen 
from test_umgebung import setup_tests
from triage import run_triage
from test_runner import verify_tests

def main():
    setup_tests() #Dateien erstellen 
    run_triage("test_posteingang", "test_isolierstation") # Triage ausführen
    verify_tests() # Tests auswerten

if __name__ == "__main__":
    main()

    