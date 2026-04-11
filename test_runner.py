import os

def verify_tests():
    print("--- STARTE TEST-AUSWERTUNG ---")
    # Check für T01 (AF1)
    if os.path.exists("test_posteingang/antrag_normal.pdf"):
        print("[PASS] T01a (AF1): antrag_normal.pdf ist weiterhin im Posteingang.")
    else:
        print("[FAIL] T01a (AF1): antrag_normal.pdf fehlt im Posteingang!")

    if os.path.exists("test_posteingang/notiz.txt"):
        print("[PASS] T01b (AF1): notiz.txt ist weiterhin im Posteingang.")
    else:
        print("[FAIL] T01b (AF1): notiz.txt fehlt im Posteingang!")

    if os.path.exists("test_posteingang/bild.jpg"):
        print("[PASS] T01c (AF1): bild.jpg ist weiterhin im Posteingang.")
    else:
        print("[FAIL] T01c (AF1): bild.jpg fehlt im Posteingang!")
    
    if os.path.exists("test_posteingang/datei_groß.PDF"):
        print("[PASS] T01d (AF1): datei_groß.PDF ist weiterhin im Posteingang.")
    else:
        print("[FAIL] T01d (AF1): datei_groß.PDF fehlt im Posteingang!") 

    # Check für AF2 - wurde die gefährliche Datei in die Isolierstation verschoben?
    if os.path.exists("test_isolierstation/virus.exe"):
        print("[PASS] T02a (AF2): virus.exe ist in der Isolierstation.")
    else:
        print("[FAIL] T02a (AF2): virus.exe fehlt in der Isolierstation.")

    if os.path.exists("test_isolierstation/update.zip"):
        print("[PASS] T02b (AF2): update.zip ist in der Isolierstation.")
    else:
        print("[FAIL] T02b (AF2): update.zip fehlt in der Isolierstation.")  

    if os.path.exists("test_isolierstation/datei_ohne-endung"):
        print("[PASS] T03 (AF2): datei_ohne-endung ist in der Isolierstation.")
    else:
        print("[FAIL] T03 (AF2): datei_ohne-endung fehlt in der Isolierstation!")

    # Check für AF3 - wurden die leeren Dateien gelöscht?
    if not os.path.exists("test_posteingang/leerdatei.pdf") and not os.path.exists("test_posteingang/keine_endung"):
        print("[PASS] T04 (AF3): Leere Dateien wurden gelöscht.")
    else:
        print("[FAIL] T04 (AF3): Leere Dateien sind noch im Posteingang!")

    if not os.path.exists("test_posteingang/keine_endung") and not os.path.exists("test_posteingang/leerdatei.pdf"):
        print("[PASS] T05 (AF3): Leere Dateien wurden gelöscht.")
    else:        
        print("[FAIL] T05 (AF3): Leere Dateien sind noch im Posteingang!")

    print("--- ENDE TEST-AUSWERTUNG ---")


if __name__ == "__main__":
    verify_tests()