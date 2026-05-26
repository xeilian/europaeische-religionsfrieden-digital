# Finding a new ontology for Eured

The goal of this exercise was to find ideas for a possible CIDOC-based ontology for Eured via NotebookLM. This encompassed the scraping of all texts from Eured of the first three modules. The [script](https://github.com/xeilian/europaeische-religionsfrieden-digital/blob/main/a4%2C%20find_ontology/extract_text_contents.py) was done in Python. The scraped texts, all 52 of them, are also in this [repository](https://github.com/xeilian/europaeische-religionsfrieden-digital/blob/main/a4%2C%20find_ontology/).

The first prompt for NotebookLM was the following:
>As sources, you'll find 50 sources of early-modern European peace treatments. Scour through the texts and find a possible ontology for a online edition adhering to the CIDOC Conceptual Reference Model (CIDOC). This ontology should help to link data to certain classes and properties that are relevant to the texts in questions. Please list all the individual elements of the ontology and explain its relevance in a few words.

This was the answer of NotebookLM. It sadly only allowed a maximum capacity of 50 sources, that's why two sources were not taken into account. It was answered in German.[^1]

>Ein auf dem CIDOC Conceptual Reference Model (CRM) basierendes Ontologie-Modell für eine Online-Edition frühneuzeitlicher Friedensverträge (wie sie in den Quellen vorliegen) ermöglicht eine strukturierte semantische Erfassung der komplexen politischen, religiösen und rechtlichen Verhältnisse jener Zeit.
>Hier ist eine Auflistung der relevanten CIDOC-CRM-Klassen und -Eigenschaften für eine solche Edition, basierend auf den bereitgestellten Dokumenten:

>Zentrale Klassen (Classes)
>* E31 Document (Dokument): Dies ist die grundlegende Klasse für die Texte selbst, wie etwa das Wormser Edikt, den Augsburger Religionsfrieden oder den Prager Frieden. Sie dient zur Erfassung des physischen und intellektuellen Objekts der Edition.
>* E5 Event (Ereignis): Repräsentiert die diplomatischen Akte, aus denen die Dokumente hervorgingen, insbesondere den „Reichstag“ (z. B. zu Speyer 1526, Augsburg 1530 oder Augsburg 1555).
>* E39 Actor (Akteur) / E74 Group (Gruppe): Erfasst die handelnden Personen und Institutionen. Dazu gehören Kaiser wie Karl V. oder Ferdinand II., aber auch Gruppen wie die „Churfürsten, Fürsten und Stände“ oder die „Augspurgische Confessionsverwandten“.
>* E53 Place (Ort): Zur Lokalisierung der Ereignisse und Geltungsbereiche, wie „Speyer“, „Passau“, „Augspurg“ oder „Prag“.
>* E52 Time-Span (Zeitspanne): Definiert die präzisen Daten der Unterzeichnung (z. B. der 23. September 1555) oder die Gültigkeitsdauer von Bestimmungen, wie die „viertzig Jahre“ im Prager Frieden.
>* E29 Design or Procedure (Entwurf oder Verfahren): Repräsentiert normative Vorgaben und Bekenntnisse, die in den Texten referenziert werden, wie die „Augspurgische Confession“ oder spezifische „Kirchenordnungen“.
>* E55 Type (Typ): Ermöglicht die Kategorisierung der Dokumente nach ihrer Rechtsform, zum Beispiel als „Edict“, „Abschied“, „Vertrag“, „Patent“ oder „Privilegium“.
>* E73 Information Object (Informationsobjekt): Für spezifische rechtliche Konzepte innerhalb der Verträge, wie den „Geistlichen Vorbehalt“ (Reservatum Ecclesiasticum) oder die „Amnistia“.

>Relevante Eigenschaften (Properties)
>* P14 carried out by (ausgeführt von): Verknüpft das Ereignis (z. B. den Abschluss des Frankfurter Anstands) mit den verantwortlichen Akteuren oder deren „Commissarien“.
>* P11 had participant (hatte Teilnehmer): Zur Erfassung der anwesenden Zeugen, Räte und Gesandten, die in den Unterschriftenlisten detailliert aufgeführt sind.
>* P7 took place at (fand statt in): Verbindet die Verhandlungen oder den Reichstag mit dem geografischen Ort.
>* P4 has time-span (hat Zeitspanne): Ordnet den Dokumenten ihre spezifischen Daten zu.
>* P129 is about (ist über): Verknüpft das Dokument oder einzelne Artikel mit den behandelten Themen, wie „Religion“, „Landfrieden“ oder den Widerstand gegen den „Türcken“.
>* P67 refers to (verweist auf): Wichtig für die in den Texten häufigen Verweise auf frühere Verträge, wie den „Passauer Vertrag“ oder das „Wormser Edikt“.
>* P105 right held by (Recht innegehabt von): Zur Abbildung von Besitzverhältnissen und Restitutionsansprüchen an „Stifftern, Klöstern und Gütern“.

>Diese Struktur erlaubt es, die Online-Edition so aufzubereiten, dass Nutzer gezielt nach Akteuren, Orten oder spezifischen Rechtsnormen über das gesamte Korpus von 50 Quellen hinweg suchen und diese in Beziehung setzen können.
>Möchten Sie, dass ich für eines dieser Dokumente beispielhaft eine detaillierte semantische Erfassung nach diesem Modell erstelle?


To dig a bit deeper, a second prompt was writting that in the end should hand out the classes and properties in a table.

>You are working with a collection of 50 early modern European peace treaties. Please analyse the content of the texts and identify semantic patterns, before proposing a CIDOC-CRM-based ontology model for a digital edition.

>You shall do this in three steps:
>Firstly, you should identify main entity types, events, concepts, actors, places and temporal references that recur across the sources.
>Then, you should derive from this a CIDOC-CRM-based ontology. Please explain for each element,
>* what source phenomenon it models and
>* why it is necessary for the edition.

>Finally, present the result as a table with the columns CIDOC class/property, source relevance, function in the edition, possible priority and an example from the corpus. Please explain in an paragraph which questions the model can and cannot capture and where additional ontologies would be helpful.

Since it did not capture everything, a reponse prompt was necessary, but it did eventually hand out a table. It also explained in a paragraph which questions the model can capture and where additional ontologies would be helpful:

>Hier ist der vervollständigte Entwurf der CIDOC-CRM-basierten Ontologie für eine digitale Edition der 50 frühneuzeitlichen Friedensverträge. Diese Tabelle führt nun alle in der Analyse identifizierten Klassen und Eigenschaften zusammen.

| CIDOC Klasse/Eigenschaft | Quellenrelevanz | Funktion in der Edition | Priorität | Beispiel aus dem Korpus |
| :--- | :--- | :--- | :--- | :--- |
| **E31 Document** | Das physische/digitale Vertragsobjekt. | Primäre Dateneinheit der Edition. | Hoch | *Wormser Edikt* |
| **E5 Event** | Formale Akte der Diplomatie (Reichstage). | Kontextualisierung der Entstehung. | Hoch | *Reichstag zu Speyer* |
| **E39 Actor** | Handelnde Einzelpersonen (Kaiser, Fürsten). | Identifikation der Unterzeichner. | Hoch | *Karl V.*, *Ferdinand II.* |
| **E74 Group** | Kollektive Akteure (Stände, Konfessionen). | Abbildung politischer/religiöser Lager. | Hoch | *Augspurgische Confessionsverwandte* |
| **E53 Place** | Geografische Verortung. | Räumliche Indizierung (Verhandlungsorte). | Mittel | *Speyer*, *Passau*, *Prag* |
| **E52 Time-Span** | Spezifische Zeitpunkte und Zeiträume. | Chronologische Einordnung. | Hoch | *23. September 1555*, *40 Jahre* |
| **E29 Design or Procedure** | Normative Vorlagen (Kirchenordnungen). | Vergleich rechtlicher/religiöser Vorgaben. | Mittel | *Augspurgische Confession* |
| **E55 Type** | Kategorisierung der Textsorten. | Formale Klassifikation der Dokumente. | Mittel | *Edict*, *Abschied*, *Patent* |
| **E73 Information Object** | Abstrakte rechtliche Konzepte. | Erfassung ideeller Vertragskonstrukte. | Mittel | *Amnistia*, *Geistlicher Vorbehalt* |
| **P14 carried out by** | Urheberschaft von Handlungen. | Verknüpfung von Event und Hauptakteur. | Hoch | Reichstag ausgeführt durch *Karl V.* |
| **P11 had participant** | Anwesenheit von Zeugen/Gesandten. | Erfassung des diplomatischen Netzwerks. | Mittel | Teilnahme von *Mauritz zu Eichstedt* |
| **P7 took place at** | Örtliche Bindung von Ereignissen. | Verbindung von Handlung und Ort. | Mittel | Reichstag fand statt in *Augsburg* |
| **P4 has time-span** | Zeitliche Bindung von Ereignissen. | Verknüpfung von Event und Datum. | Hoch | Passauer Vertrag vom *2. August 1552* |
| **P129 is about** | Inhaltliche Themenbereiche. | Thematische Erschließung der Artikel. | Mittel | Vertragsteil über den *„Türcken“* |
| **P67 refers to** | Intertextuelle Verweise. | Abbildung der Vertragshierarchien. | Hoch | Passau verweist auf *Wormser Edikt* |
| **P105 right held by** | Besitz- und Jurisdiktionsrechte. | Abbildung von Restitutionsansprüchen. | Hoch | Recht an *„Stifftern und Klöstern“* |

>Reichweite und Grenzen des Modells
>Dieses Modell kann komplexe Fragen zu politischen Netzwerken und rechtlichen Abhängigkeiten beantworten (z. B.: „Welche Akteure waren an allen Verträgen beteiligt, die sich auf den Religionsfrieden beziehen?“ oder „Welche Orte waren Zentren für die Aushandlung von Restitutionsrechten?“). Es ermöglicht eine präzise Suche nach Rechtsdokumenten basierend auf ihrer Form (E55) und ihrem Entstehungskontext (E5). 

>Das Modell stößt jedoch an seine Grenzen, wenn es um die inhaltliche Exegese theologischer Argumente oder die rhetorische Analyse der Texte geht. CIDOC CRM ist ereignisorientiert und weniger geeignet, um den logischen Aufbau einer theologischen Beweisführung innerhalb eines Traktats (wie im Augsburger Interim) im Detail abzubilden. Hierfür wäre die Integration einer spezialisierten Ontologie für Argumentationsstrukturen oder eine feinere Taxonomie für konfessionelle Begrifflichkeiten als Ergänzung sinnvoll.

>Möchten Sie, dass ich für eines der Dokumente (z. B. den Prager Frieden) eine beispielhafte Instanziierung nach diesem Modell durchführe?






[^1]: Link to the notebook: https://notebooklm.google.com/notebook/1550cc3b-fab0-49e9-bf62-3331a9ee05fe