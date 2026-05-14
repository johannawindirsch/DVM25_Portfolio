## Level 03 - TASK 02: Anforderungen erstellen!

| ID | Titel | Beschreibung | Bezug zu |

| AF8 | JSON-Begleitdatei | Das System muss unmittelbar bei der Zuordnung eines Dokuments zu einer Akte eine gleichnamige Datei mit der Endung `.json`im selben Akten-Ordner erzeugen. | US1 |

| Af9 | Basis-Metadaten | Die JSON-Datei muss die Keys `dokumenten_typ` und èrstellungsdatum`enthalten. | US1 |

| AF10 | Aufbewahrungs-Metadaten | In der JSON-Datei muss key `aufbewahrung_bis` enthalten sein, um die gesetzlichen Löschfristen (Perspektive A) zu dokumentieren. | US2 |

| AF11 | Sicherheits-Metadaten | In der JSON-Datei muss key `vertraulichkeit` enthalten sein, um den Schutzstatus (Perspektive B) der Datei festzulegen. | US3 |