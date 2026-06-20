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