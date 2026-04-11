import os

def verify_tests():
    print("--- STARTE TEST-AUSWERTUNG ---")
    # Check für T01 (AF1)
    if os.path.exists("test_posteingang/antrag_normal.pdf"):
        print("[PASS] T01 (AF1): antrag_normal.pdf ist weiterhin im Posteingang.")
    else:
        print("[FAIL] T01 (AF1): antrag_normal.pdf fehlt im Posteingang!")

    # Check für AF2 - wurde die gefährliche Datei in die Isolierstation verschoben?
    if os.path.exists("test_isolierstation/virus.exe"):
        print("[PASS] T02 (AF2): virus.exe ist in der Isolierstation.")
    else:
        print("[FAIL] T02 (AF2): virus.exe fehlt in der Isolierstation.")

    # Check für AF3 - wurden die leeren Dateien gelöscht?
    if not os.path.exists("test_posteingang/leerdatei.pdf") and not os.path.exists("test_posteingang/keine_endung"):
        print("[PASS] T03 (AF3): Leere Dateien wurden gelöscht.")
    else:
        print("[FAIL] T03 (AF3): Leere Dateien sind noch im Posteingang!")

    print("--- ENDE TEST-AUSWERTUNG ---")


if __name__ == "__main__":
    verify_tests()