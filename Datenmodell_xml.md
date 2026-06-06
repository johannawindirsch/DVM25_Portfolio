# Task4

# Ziel:
Das primäre Ziel des XML-Exports ist es, den aktuellen Datenbestand des DMS (Aktenstrukturen, Dokumente und die in Level 3 erzeugten JSON-Metadaten) in ein standardisiertes, plattformunabhängiges Format zu überführen. Dies ermöglicht den verlässlichen Datenaustausch mit anderen Systemen, die langfristige Archivierung und die Validierung der Datenintegrität über ein strukturiertes XSD-Schema.

| Testfall-ID | Anforderungs-ID | Übergeordnetes Element | XML-Element (Tag) | Datentyp | Status | 4. Begründung für den Export |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| — | AF12 | Wurzelelement | `dms_export` | — | **Pflichtelement** | Bildet die oberste Klammer (Wurzel) des gesamten Export-Baums. |
| T14 | AF14 | `dms_export` | `export_datum` | `xs:dateTime` | **Pflichtelement** | Speichert den genauen Zeitstempel des Exports zur Absicherung der Revisionssicherheit. |
| — | AF12 | `dms_export` | `akte` | — | **Pflichtelement** | Repräsentiert einen Aktenordner im System, mehrfach vorkommen möglich |
| T14 | AF14| `akte` | `akten_name` | `xs:string` | **Pflichtelement** |  Name des Aktenordners (z. B. "Gehaltsnachweise_2026"). Unverzichtbar für die Zuordnung. |
| — | AF12 | `akte` | `dokument` | — | **Optional** | Umschließt ein einzelnes im DMS registriertes Dokument. |
| T14 | AF14 | `dokument` | `dateiname` | `xs:string` | **Pflichtelement** | Der Name der ursprünglichen PDF-Datei, um den Bezug zur Datei zu behalten. |
| — | AF12 | `dokument` | `metadaten` | — | **Pflichtelement** | Umschließt die strukturierten Metadaten-Elemente aus Level 3. |
| T11 | AF9 | `metadaten` | `dokumenten_typ`| `xs:string` | **Pflichtelement** | Typ des Dokuments (z. B. "Rechnung") für administrative Filterung. |
| T11 | AF9 | `metadaten` | `registrierungs_datum`| `xs:date` | **Pflichtelement** | Das exakte Datum an dem das Dokument im DMS erfasst wurde (Format: YYYY-MM-DD). |
| T12 | AF10 | `metadaten` | `aufbewahrung_bis`| `xs:date` | **Pflichtelement** | Ablaufdatum der gesetzlichen Löschfristen. Bildet **US2 (Perspektive A)** ab. |
| T13 | AF11 | `metadaten` | `vertraulichkeit` | `xs:string` | **Pflichtelement** | Schutzstatus des Dokuments für den Datenschutz. Bildet **US3 (Perspektive B)** ab. |

---
## Bewusst nicht exportierte Informationen und Begründung
*  binäre Inhalt der PDF-Dateien: Die eigentlichen Inhalte der PDF-Dokumente werden nicht in das XML eingebettet, weil ein Einbetten würde die XML-Datei enorm vergrößern und die Verarbeitungsgeschwindigkeit (Performance) stark drosseln. Das XML fungiert als strukturierter Metadaten-Index. Die Verknüpfung zur Datei erfolgt über das Element `dateiname`.

* Lokale, absolute Systempfade:** Absolute Pfade des Entwicklungssystems werden weggelassen, weil diese Pfade besitzen auf einem anderen Zielsystem keine Gültigkeit und würden die Interoperabilität des Exports verhindern.