## KI Logbuch Level 1 

# KI gebeten, mir nochmal zu erklären, wie ich Git verknüpfe (10.April) | hat semi funktioniert 
# KI nochmal gefragt, wie ich es in Git hochlade --> habe es dann aus Versehen 3 mal hochgeladen, weil ichs nicht richtig gesehen habe (10.April) | KI semi hilfreich, aber auch teilweise meine eigene Schuld/"Dummheit"
# KI gebeten mir bei der Testumgebung zu helfen (10.April),weil ich if/for/else falsch eingerückt hatte | KI war hierbei sehr hilfreich! | hat funktioniert
# KI gebeten zu erklären, wie ich die touch-Funktion verwende (10.April) | hilfreich | hat funktioniert
# KI mir Aufgabe 5 erklären lassen, was ich vereinfacht tun soll und was ich in die test_run.log kopieren soll | KI war hierbei ebenfalls sehr hilfreich (11.April) | hat (hoffentlich) funktioniert

## Level 2
# KI gebeten mir zu erklären, warum auf einmal keine Dateien mehr in VisualCode zu sehen waren (2. Mai) | KI semi hilfreich | ich habe selbst herausgefunden, dass ich die einzelnen Dateien nochmal hochladen musste, den Fehler wieso das passiert ist, habe ich nicht gefunden

# (Allgemein) Ki gebeten, mir alle Aufgaben so einfach wie möglich zu erklärem | KI sehr hilfreich und sehr geduldig | ich habe mir insgesamt über 1,5h die Aufgaben Schritt für Schritt erklären lassen mit verschiedenen Ansätzen und Ideen | sehr hilfreich, da ich dadurch einen Durchblick bekommen habe 

# KI gebeten mir step by step, so feingliedrig wie möglich zu erklären, wie ich TASK 2 erledigen soll, weil ich es nicht verstanden habe | KI teilweise hilfreich, teilweise halluziniert | Ich habe sehr sehr lange für diese Aufgabe gebraucht und war mir zeitweise auch nicht sicher, ob das richtig ist | unsicher, ob es gut funktioniert hat 

# bei Task 3: siehe vorheriges 

# Task4: KI wieder gebeten, es mir so feingliedrig wie möglich zu erklären, ohne mir Dinge vorzukauen | KI sehr hilfreich, aber wieder das Problem der Halluzination | ebenfalls unsicher, ob es die Anforderungen erfüllt hat 

# Task5: Habe ich mir von der KI komplett erklären lassen für "DUMME", weil ich es nicht kapiert habe, was ich machen muss und wie ich es machen muss | sehr hilfreich, dennoch unsicher, ob mein Outcome richtig ist, da er mir relativ kurz erscheint | 

# Allgemein: Ich habe mir teilweise von der KI meinen Code kontrollieren lassen, um zu schauen, wo der Fehler in meiner Logik ist | hierbei KI SEHR hilfreich, da er Fehler schneller ausfindig macht als ich | 

# Allgemein: Ich habe mir nochmal die Commits erklären lassen, da ich es bei Level 1 falsch gemacht habe | diese Mal hat es besser geklappt (hoffentlich) | 

# Allgemein: ich habe mir das .gitignore erklären lassen, aber nachdem ich es gemacht habe, sind alle meine Dateien verschwunden, weshalb ich es dann doch aus Sicherheitsgründen nicht umgesetzt habe | KI also semi hilfreich 

# Allgemein: Ich habe mir Level 2 öfter die kleinen Schritte sowie die Anforderungen erklären lassen müssen, weil mir teilweise der Durchblick gefehlt hat und ich gar nicht wusste, was raus kommen soll (das hat bei Level 1 besser für mich geklappt) | insofern KI als Erklärbuddy sehr sinnvoll und hilfreich 

# Allgemein: Ich habe ebenso aus spielerischen Gründen oft auf TAB gedrückt, um zu schauen, was der COPilot so macht | Fazit: Cool zum Experimentieren. Manchmal sind die Dinge, die er für Print vorschlägt komisch formuliert, aber ich habe es dennoch so gelassen | Fazit: sehr cool! Aber man muss aufpassen WAS er genau macht und was sein Ziel ist!


## Level 3
## Reflexion zu Level 3 (Task 4 & Task 5)

# Bei der Umsetzung der Metadatenerstellung habe ich die KI schrittweise mit den in Task 2 definierten funktionalen Anforderungen gefüttert. Da ich so viel wie möglich verstehen will, aber gleichzeitig auch auf die Hilfe angewiesen bin, beinhalten meine Prompts immer "bitte schlüssel es mir schritt für schritt auf und halte dich exakt an die vorgaben"! KI ist zwar in der Hinsicht ein guter Lehrer, aber man muss vorallem drauf achten, dass er sich auch WIRKLICH daran hält, was man will. So hilft es mir beispielsweise jede Aufgabe ganz exakt und langsam durchzugehen und nicht wahllos einzukopieren. Wenn ich etwas nicht verstehe, frage ich zur Not 10 Mal nach oder verwendet den Prompt, dass Sie es so erklären soll, dass es Menschen ohne Vorkenntnisse verstehen sollen - das hilft!

## Level 4
## Reflexionsfragen zu Level 4

## Wie haben Sie die KI beim Entwurf des Datenmodells genutzt?

# Ich habe die KI als Unterstützung genutzt, um die Ordnerstruktur und die JSON-Metadaten unseres DMS in eine saubere XML-Baumstruktur zu bringen. Gemeinsam haben wir entschieden, das Modell komplett über verschachtelte Elemente (Tags) statt über Attribute aufzubauen. So fängt alles beim Hauptelement `<dms_export>` an, geht über `<akte>` und `<dokument>` und packt die eigentlichen Werte ordentlich in einen `<metadaten>`-Container.Die KI hat mir außerdem dabei geholfen, die Felder aus den JSON-Dateien richtig zuzuordnen. Mein Python-Code nimmt zum Beispiel das `"erstellungsdatum"` aus der JSON und schreibt es im XML in das Tag `<registrierungs_datum>`, damit es genau zu unserem XSD-Schema passt. Wichtig war auch die Entscheidung, die echten PDFs nicht in das XML zu packen, um das System nicht zu bremsen oder unnötig zu belasten. Zuletzt hat sie mir geholfen, den Code mit der `.get()`-Methode abzusichern. So läuft das Skript stabil und stürzt nicht ab, falls in einer JSON-Datei mal ein Feld fehlt.

---

## Wie haben Sie geprüft, dass das XSD wirklich zu Ihrem Modell passt?

# Weil die exportierte Datei fehlerfrei durchging und mein Skript die Meldung `ERFOLG: XML ist valide!` ausgegeben hat, war der Beweis erbracht, dass das Schema exakt zu unserem exportierten Modell passt. Ich hatte aus den vorherigen Leveln auch einen Fehler, wodurch auch mal nicht valide kam. So habe ich germekrt, dass ich mehr oder weniger funktioniert. 

---
### Welche Teile mussten Sie selbst verstehen, um das Schema mündlich begründen zu können?

# Alles tatsächlich. Sobald man etwas nicht versteht, kommen die Fehler und eben wenn man davor mehrere Level gemact hat, MUSS man zumindest ein wenig Verständnis dafür aufbringen. Zu 100prozent habe ich es dennoch nicht verstanden bzw teile nicht richtig verstandne, dass gebe ich zu! Aber ein Grundverständnis habe ich mir erarbeitet!



## Level 5

**Welche Teile meines bisherigen Codes waren KI-generiert?**
Viele Teile waren mit KI-Unterstützung entstanden, aber immer unter meiner Kontrolle. Ich habe geprüft, ob der Code Sinn ergibt, und bei Unklarheiten nachrecherchiert oder nachgefragt, statt es einfach zu übernehmen. 

**Wie habe ich überprüft, dass ich den Code wirklich verstehe?**
Ich bin den Code über mehrere Stunden immer wieder durchgegangen, habe mir einzelne Bedingungen Schritt für Schritt selbst durchgerechnet und bei Fehlern (NameError, Tippfehler, falsche Ordnerstruktur) so lange nachgeforscht, bis ich die Ursache wirklich verstanden hatte, statt nur die Fehlermeldung wegzuklicken.

**Wo hat KI bei der Wartung geholfen?**
Die KI hat mir geholfen, indem sie Fehler gefunden hat, die ich selbst übersehen hatte (z. B. doppelt vergebene Test-IDs), und mir Zusammenhänge erklärt hat, die mir vorher nicht klar waren – das hat die Arbeit insgesamt leichter und schneller gemacht, ohne dass mir die Entscheidungen abgenommen wurden.

**Wo war KI gefährlich / hat etwas übersehen?**
KI ist grundsätzlich dann gefährlich, wenn man kein eigenes Konzept hat und ihr blind vertraut, statt die Vorschläge zu hinterfragen. Auch in meinem Fall sind sicher nicht alle Vorschläge auf Anhieb perfekt gewesen – ich habe versucht, so genau und präzise wie möglich zu bleiben und alles selbst zu kontrollieren, statt mich blind zu verlassen.

**Wie habe ich nachgewiesen, dass meine Änderungen keine Regressionen erzeugt haben?**
Ich habe nach jeder Änderung alle drei bestehenden Testskripte (`main.py`, `test_setup_reg.py`, `test_xml_export.py`) erneut nacheinander ausgeführt und die Ergebnisse mit dem Stand vor der Änderung verglichen. Alle Ergebnisse wurden im `regression_test_run.log` dokumentiert.