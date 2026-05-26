# Improving the Eured ontology with NotebookLM 

This dossier presents the results of a NotebookLM analysis of 50 early modern peace treaties and their annotations. It shows how a CIDOC CRM-based model can organize recurring entities, relations, and editorial patterns into structured metadata for a digital edition. It also highlights where the current model works well and where it may need to be expanded.


## Proceedings
First, all texts from Eured of the first three modules were scraped. The annotations were left in. The [script](https://github.com/xeilian/europaeische-religionsfrieden-digital/blob/main/a4%2C%20improving%20the%20ontology%20with%20notebooklm/extract_text_contents_v2.py) was done in Python. The scraped texts, all 52 of them, are also in this [repository](https://github.com/xeilian/europaeische-religionsfrieden-digital/blob/main/a4%2C%20improving%20the%20ontology%20with%20notebooklm/). It was tried to use only the .xml-files (converted to .txt files), but those were rejected by NotebookLM. That's why the HTML was used.


## First draft
The following prompt didn't harvest sufficiently detailed result, so it was divided in six parts by Perplexity. These prompts serve as the basis for the following dossier.

```text
I am working with a corpus of 50 early modern peace treaties and their annotations. Based on these sources, I want to identify possible use cases, relationships, and research questions for an ontology for a digital edition of early modern peace treaties. The ontology is based on CIDOC CRM and currently includes the following classes and properties:

Classes
* Historical Documents (E31 Document): Written or recorded artifacts that contain historical or legal information.
* Identifiers (E42 Identifier): Unique codes or references assigned to documents for identification purposes.
* Events (E5 Event): Significant occurrences, such as treaties, wars, or legal agreements, described or recorded in documents.
* People (E21 Person): Individuals who participated in or are mentioned in historical documents.
* Places (E53 Place): Geographical locations mentioned in or relevant to the documents.

Properties
* Has Identifier (P1 is identified by): Links a document to an identifier, such as a catalog number or a unique reference.
* Valid In (P6 valid in): Indicates the place where a document is considered valid or relevant.
* Had Participant (P11 had participant): Links a document to people who were involved in its creation, negotiation, or signing.
* Refers To (P67 refers to): Indicates places mentioned or relevant in the document.
* Documents Event (P70i documents): Links a document to an event it describes or records.
* Brought into Existence (P92 brought into existence): Specifies the creation data.

Please analyze the sources and look for:
* Expected connections that clearly appear in the texts and annotations
* Unexpected connections that may be present but are not immediately obvious
* Missing connections that one might expect in such treaties, but that do not appear in the corpus
* Potential use cases for the ontology in a digital edition
* Gaps or limitations of the current model based on the sources
* Additional classes or properties that might be needed if the corpus requires more precise modeling

Please answer in a structured way and include:
* A list of recurring entities, events, and relationships found in the sources
* A list of possible queries that the ontology should support
* A list of connections that are present in some treaties but absent in others
* A list of uncertain or ambiguous cases where interpretation is needed
* A short conclusion on how the ontology could be improved for the edition

If possible, also identify:
* references to earlier treaties
* references to persons, places, institutions, or other actors
* references to legal norms, obligations, or validity
* temporal expressions and dating variants
* editorial annotations that suggest additional metadata relations

Focus on what the sources actually support, not only on what would be theoretically expected.
```


## Part 1: Corpus overview

### Prompt
```text
I am working with a corpus of 50 early modern peace treaties and their annotations. First, please give me a detailed corpus overview. Identify the recurring entities, events, and relationships that appear across the sources.

Please focus on:
- treaty titles and title variants,
- document identifiers,
- dates and dating formulas,
- signing, ratification, proclamation, or publication events,
- persons and collective actors,
- places of issue, negotiation, or validity,
- references to earlier treaties or related agreements,
- editorial annotations that suggest metadata relations,
- legal formulas, obligations, guarantees, exceptions, and validity clauses.

For each recurring element, explain:
- what it is,
- how it appears in the sources,
- how often or in what kind of texts it appears,
- and why it matters for an ontology.

Please present the results in a structured list or table.
```

### Result
The following detailed corpus overview identifies the recurring entities, events, and relationships found across the 50 early modern peace treaties and annotations. This structure provides a foundation for a CIDOC CRM-based ontology.

**Corpus Overview: Entities, Events, and Relationships**<br>

| Element | Description & Appearance | Frequency / Text Type | Ontological Significance |
| :--- | :--- | :--- | :--- |
| **Treaty Titles & Variants** | Formal names (e.g., *Wormser Edikt*, *Augsburger Religionsfrieden*) and descriptive variants found in headers (e.g., *Abschiet des Reichstags zu Speyer*). | Found in all documents, often at the start or in archival headers. | Essential for **E31 Document** labeling and linking related documents. |
| **Document Identifiers** | Unique archival codes (e.g., *pa000008-0110*) or internal references to original vs. copy status (*Original*, *Copei*). | Present in metadata headers and editorial annotations for every source. | Maps to **E42 Identifier** and **P1 is identified by**. |
| **Dating Formulas** | Complex temporal expressions: calendar dates (e.g., *27. Augusti 1526*), Saints' days (*Dinstag nach Marie Magdalene*), and regnal years. | Universal across the corpus; legal validity often depends on specific start dates. | Requires **E52 Time-Span**; crucial for modeling temporal validity of legal norms. |
| **Issue & Signing Events** | The formal creation of the document (*Geben und geschehen*) involving high-ranking participants and their seals. | Found at the end of nearly every treaty or recess. | Maps to **P92 brought into existence** and **P11 had participant**. |
| **Ratification & Proclamation** | Acts of confirming (*Ratificirt*) or publicly announcing (*publiciert unnd eröffnet*) the treaty's contents. | Recurring in Imperial Recesses and subsequent mandates. | Represents a distinct **E5 Event** that triggers legal validity in specific **E53 Places**. |
| **Monarchs & Individual Actors** | Sovereigns (e.g., *Karl V*, *Ferdinand I*, *Rudolff II*) and their commissioned representatives (*Commissarien*). | Every document names a high-level authority or authorized agents. | Maps to **E21 Person** and institutionalized roles. |
| **Collective Actors (Stände/Groups)** | Institutional groups such as *Churfürsten*, *Fürsten*, *Stände*, *Rath* (City Councils), and *Domkapitel* (Cathedral Chapters). | Extremely frequent; these groups are the primary legal subjects and participants. | Requires **E74 Group**; treaties often apply to groups rather than individuals. |
| **Places of Issue & Validity** | Locations of negotiation/signing (e.g., *Augsburg*, *Speyer*, *Prag*) and regions where norms apply (*Holy Roman Empire*). | Specific cities are named in the *Datum* line; validity regions are in the preamble. | Maps to **E53 Place**, **P6 valid in**, and **P67 refers to**. |
| **Inter-Treaty References** | Explicit mentions of previous laws (e.g., 1629 Edict referring to 1555 Peace, or 1539 Anstand referring to 1532 Nuremberg). | Common in later documents as a basis for legal continuity or revision. | Crucial for modeling **relationships between E31 Documents**. |
| **Editorial Annotations** | Notes on physical state (*Blatt*), collation (*Collationirt*), or archival provenance. | Frequent in transcripts and metadata. | Suggests metadata relations for document state and authentication. |
| **Legal Formulas & Validity** | Mandatory clauses: "Bey peen der Acht" (penalties), "Alles getrewlich und ungefehrlich" (good faith), and "until a general council" (conditional validity). | Standardized phrasing across different document types. | Defines the **modalities of relationships** between actors and norms. |

**Key Observations for Ontology Refinement**<br>

1.  **Institutional Primacy:** The corpus is dominated by **Collective Actors (E74 Group)** like the *Stände* and *Domkapitel*. Modeling these as mere "People" is insufficient; the ontology must support groups as entities capable of holding rights and obligations.
2.  **Geographic Specificity:** While many documents claim validity for the whole Empire, specific **Privileges** (e.g., for *Altona* or *Glückstadt*) are localized. The **P6 valid in** property must distinguish between broad Imperial law and specific municipal exemptions.
3.  **Cross-Document Lineage:** The sources are not isolated; they form a web of **confirmation, revocation, and re-interpretation**. An ontology should include properties like "is confirmed by" or "revises" to link these historical documents.
4.  **Conditional States:** Many treaties define a period of validity not by a date, but by an event (e.g., *until a general council*). The model must account for **event-contingent validity periods** within the **E52 Time-Span** class.
5.  **Multilingualism:** The corpus includes German, Latin, and Dutch. The ontology needs to handle **language-specific variants** of entity names (e.g., *Fredericopolis* vs. *Friedrichstadt*).

Would you like me to elaborate on the specific types of legal penalties (e.g., the Imperial Ban) found in these treaties to help define a class for legal consequences?



## Part 2: Expected and unexpected relations

### Prompt
```text
Based on the same corpus, please distinguish between different kinds of relations found in the sources.

I want you to identify:
- expected relations that clearly appear,
- unexpected relations that are present but not immediately obvious,
- missing but expected relations that seem important for treaty editions but are absent or weakly represented,
- and ambiguous relations where interpretation is uncertain.

For each case, give:
- a short description,
- an example from the corpus,
- and a note on why it matters for the ontology.

Please be precise and stay close to the actual sources.
```

### Result
Based on the corpus of 50 early modern peace treaties and annotations, the following analysis distinguishes between the different types of relations that an ontology must support to accurately model these historical documents.

**1. Expected Relations**<br>
These are connections that appear explicitly and consistently across the corpus as part of the legal and diplomatic structure of the Holy Roman Empire.

*   **Document Confirmation (E31 to E31):** Later treaties explicitly cite, confirm, or revise earlier ones to establish legal continuity.
    *   **Example:** The **Peace of Augsburg (1555)** refers back to the **Passau Treaty (1552)** as the basis for its negotiations. Similarly, the **Edict of Restitution (1629)** provides a detailed legal re-interpretation of the 1555 Peace.
    *   **Ontological Significance:** Requires a property like *P67 refers to* (or a specialized sub-property *documents_confirms*) to link historical documents in a chain of legal validity.
*   **Actor Representation (E21/E74 to E5):** Individuals acting on behalf of institutional bodies or sovereigns during specific events.
    *   **Example:** At the **Reichstag of Speyer (1526)**, King Ferdinand and various Dukes act as "verordente... Commissarien" (commissioned representatives) for Emperor Charles V.
    *   **Ontological Significance:** This requires distinguishing between the **Person (E21)** and the **Group/Institution (E74)** they represent. The ontology must model the relation *P11 had participant* through the lens of a specific role (e.g., "as Commissioner").
*   **Geographic Issuance and Validity (E31 to E53):** A document is issued in one place but valid in several others.
    *   **Example:** The **Hammelburg Treaty (1530)** was negotiated in Hammelburg but concerns the internal governance of the city of **Erfurt**.
    *   **Ontological Significance:** Supports *P6 valid in* and *P7 took place at*. It is crucial for mapping the "reach" of specific laws versus the location of their creation.

**2. Unexpected Relations**<br>
These relations are present in the corpus but are not immediately obvious without deep analysis of the legal formulas and religious contexts.

*   **Conditional Temporal Validity (E31 to E52):** Validity that is not tied to a calendar date but to a future, uncertain event.
    *   **Example:** Many treaties, such as the **Münster Treaty (1533)**, state their provisions are valid only "until a general, free, Christian council" (**biß uff ein gemein... Concilium**).
    *   **Ontological Significance:** This suggests that **Time-Spans (E52)** in the ontology cannot always be modeled as fixed date ranges. They must be linked to **Events (E5)** (e.g., "until the conclusion of Event X").
*   **Fiscal Dependency (Action to Legal Status):** The restoration of rights or territories is often conditional upon financial payment.
    *   **Example:** In the **Wolfenbüttel Treaty (1553)**, the restoration of Duke Henry's rights and the town's peace is tied to the management and repayment of a debt of 300,000 gold guilders.
    *   **Ontological Significance:** This creates a relation between a **Financial Transaction** and the **Legal Validity** of a treaty article, suggesting a need for modeling "Legal Obligations" as a class.
*   **Internal Article Hierarchy:** References within a document to its own sub-sections or to specific clauses in other documents.
    *   **Example:** The **Edict of Restitution** refers specifically to the **"Geistlicher Vorbehalt"** (Ecclesiastical Reservation) clause within the 1555 Peace.
    *   **Ontological Significance:** Using *P148 has component* to model **Articles** as separate entities under an **E31 Document** allows researchers to track the history of specific legal paragraphs across 100 years.

**3. Missing but Expected Relations**<br>
These are relations one might expect in a corpus of peace treaties that are notably absent or weakly represented in these specific texts.

*   **Voices of Non-Elite Actors:** While "the common man" or "subjects" are frequently mentioned as the *reason* for a treaty, they are almost never *participants*.
    *   **Example:** The **1526 Speyer Recess** identifies the "uprising of the common man" (Peasants' War) as a cause for the treaty, but no representatives of this group sign the document.
    *   **Ontological Significance:** Highlights the top-down nature of early modern law. The ontology should include a "Pxx subject of" relation to link non-participating groups to the events that affected them.
*   **Cross-Confessional Bi-lateralism:** Many of these documents are not "treaties" between equals but "Recesses" (imperial decrees) where the Emperor dictates to the Estates.
    *   **Example:** The **1530 Augsburg Recess** is a one-sided decree by Charles V against the Protestant minority.
    *   **Ontological Significance:** The ontology must distinguish between **Bi-lateral Agreements** (where both sides sign) and **Uni-lateral Decrees** (issued by a sovereign).

**4. Ambiguous Relations**<br>
Cases where the text supports multiple interpretations or requires significant editorial intervention to model.

*   **The "Copey" vs. "Original" Status:** Documents often describe their own physical state or the state of their sources in contradictory ways.
    *   **Example:** The **1526 Speyer Recess** is marked as "Collated against the Original" (**Gegen dem Original Collationirt**), implying the text we have is a copy, yet it is signed by the estates as if it were the act of signing itself.
    *   **Ontological Significance:** Requires modeling **Document States** (Original, Copy, Print) as specific identifiers or types for E31.
*   **Identity of Rights-Holders (Titles vs. Persons):** Rulers are referred to by an exhaustive list of titles, many of which refer to places they do not currently control or where the treaty is not valid.
    *   **Example:** Charles V's titles include "King of Jerusalem" and "King of the Indian Islands" in documents concerning internal German religious peace.
    *   **Ontological Significance:** The ontology must differentiate between the **Person (E21)**, the **Title/Office** they hold, and the **Place (E53)** where that title grants them authority.
*   **Ambiguous Intercession:** It is often unclear if an intercessor is a "participant" or merely a "reference."
    *   **Example:** Archduke Matthias intercedes for the Hungarian estates to Emperor Rudolph II.
    *   **Ontological Significance:** This requires a specific relation for **Mediation** (e.g., "Actor X mediated Event Y") that is distinct from direct participation (*P11*).


## Part 3: Ontology use cases
### Prompt

```
Now, based on the same corpus, derive concrete use cases for a CIDOC CRM-based ontology in an online edition of early modern peace treaties.

Please identify possible user questions and edition functions such as:
- finding treaties by place, person, or date,
- tracing references to earlier treaties,
- comparing legal norms or validity clauses,
- linking documents to events and actors,
- identifying repeated or unique actors across the corpus,
- and connecting editorial annotations to source metadata.

For each use case, explain:
- the user need,
- the ontology elements involved,
- whether it is a core or advanced use case,
- and whether the corpus clearly supports it.

Present the result as a table.
```

### Result
Based on the provided corpus of 50 early modern peace treaties and decrees, the following table outlines concrete use cases for a CIDOC CRM-based ontology within a digital edition.

**Use Cases for a Treaty Ontology**

| User Need / Function | Description | Ontology Elements | Core/Advanced | Corpus Support |
| :--- | :--- | :--- | :--- | :--- |
| **Search by Facet (Person, Place, Date)** | Finding documents based on historical agents (e.g., Charles V), locations of signing (e.g., Augsburg), or specific years. | **E31 Document**, **E21 Person**, **E53 Place**, **E52 Time-Span**, **P11 had participant**, **P67 refers to**. | **Core** | **Strong**: Every source provides titles, dates, and locations. |
| **Tracing Legal Lineage** | Tracking how a specific treaty (e.g., the 1555 Peace) is cited, confirmed, or reinterpreted in later documents. | **E31 Document**, **E73 Information Object**, **P67 refers to** (or sub-property *confirms*). | **Advanced** | **Very Strong**: The 1629 Edict and 1635 Peace explicitly trace back to 1555 and 1552. |
| **Prosopographical Network Analysis** | Identifying repeated actors, such as specific **Commissioners** or **Doctors**, who appear across different negotiations. | **E21 Person**, **E74 Group**, **E5 Event**, **P11 had participant**. | **Advanced** | **Strong**: Participants and their roles (e.g., *verordente Commissarien*) are meticulously listed in recesses. |
| **Validity Clause Comparison** | Filtering and comparing treaties valid only under specific conditions, such as "until a general council". | **E31 Document**, **E5 Event**, **E52 Time-Span**, **P67 refers to**. | **Advanced** | **Strong**: This temporal formula is a recurring legal standard across the corpus. |
| **Structural Granularity (Article Search)** | Navigating and citing specific sections, such as the "Ecclesiastical Reservation" or "Amnesty" clauses. | **E31 Document**, **P148 has component**, **E73 Information Object**. | **Advanced** | **Moderate**: Many documents use numbered articles (*Articuln*) that the ontology can model as components. |
| **Source Critique & State Tracking** | Distinguishing between the "Original," "Copey," or "Abtruckh" (print) status of a document. | **E31 Document**, **E42 Identifier**, **P1 is identified by**, Editorial Annotations. | **Core** | **Strong**: Annotations frequently specify the document state and collation status. |
| **Mapping Territorial Validity** | Visualizing the reach of a treaty (e.g., validity for the whole Empire vs. a single city like Altona). | **E31 Document**, **E53 Place**, **P6 valid in**. | **Core** | **Strong**: Preambles explicitly list the territories or groups subject to the law. |
| **Mandate & Penalty Tracking** | Finding documents that invoke specific legal consequences, such as the **Imperial Ban (Acht)**. | **E31 Document**, **E73 Information Object**, **P67 refers to**. | **Advanced** | **Strong**: Penal formulas like *bey peen der Acht* are standard in imperial decrees. |

**Explanation of Use Cases**

*   **Finding Treaties by Facet:** This is a basic requirement for any digital edition. Users need to filter the 50 sources to find all documents issued in **Speyer** or those involving **King Ferdinand**. The ontology links the **E31 Document** to the **E53 Place** via **P67** and to the **E21 Person** via **P11**.
*   **Tracing Legal Lineage:** Historians often need to see the "life" of a law. The **Edict of Restitution (1629)** is essentially a 40-page commentary on the **1555 Peace of Augsburg**. Modeling these as **P67 refers to** relations between **E31** entities allows users to navigate this hierarchy.
*   **Linking Documents to Events and Actors:** This use case addresses the need to understand the *context* of a treaty. For example, the **Prague Peace (1635)** is linked to negotiations in **Leithmeritz** and **Pirna**. The ontology captures this by linking the **E31 Document** to an **E5 Event** (Negotiation) via **P70i documents**.
*   **Connecting Editorial Annotations to Metadata:** The sources contain rich metadata in headers and notes, such as "Gegen dem Original Collationirt". By mapping these to **E42 Identifier** and types for **E31**, the ontology ensures that users can distinguish between a primary source and a later transcription.
*   **Validity Clauses:** Many early modern laws have a "shelf life" contingent on future events. Documents like the **Münster Treaty (1533)** define validity *biß uff ein gemein... Concilium* (until a general council). The ontology models this as a conditional **E52 Time-Span** linked to a future **E5 Event**.


## Part 4: Ontology gaps and extensions
```text
Please now evaluate the ontology model itself in light of the corpus.

The current model includes:
- E31 Document
- E42 Identifier
- E5 Event
- E21 Person
- E53 Place
- P1 is identified by
- P6 valid in
- P11 had participant
- P67 refers to
- P70i documents
- P92 brought into existence

Please analyze:
- which important source phenomena are not well captured,
- which distinctions should be made more precise,
- which classes or properties should probably be added,
- and where CIDOC CRM may be too general for the corpus.

Please explain each suggested extension briefly and tie it to a source phenomenon.
```

### Result
Based on an evaluation of the 50 early modern peace treaties and annotations, the current model requires expansion to capture the complex legal, institutional, and structural realities of the corpus.

**Source Phenomena Not Well Captured**<br>

*   **Collective and Institutional Actors:** The current model only includes **E21 Person**, but the sources are dominated by **E74 Groups** such as the Imperial Estates (**Stände**), Cathedral Chapters (**Thumb Capittel**), and City Councils (**Rath**). These groups act as legal entities that hold rights, enter into obligations, and provide representatives.
*   **Document States and Transmission:** Annotations frequently distinguish between the physical status of a text, such as **Original**, **Copey** (copy), or **Abtruckh** (print). The current model lacks a way to distinguish between the abstract legal act and its various physical or digital manifestations.
*   **Condition-Based Validity:** Many treaties are not valid for a fixed date range but until a specific future event occurs, most commonly "until a general, free, Christian council" (**biß uff ein gemein... Concilium**). The current model cannot easily link the validity of an **E31 Document** to a prospective **E5 Event**.

**Distinctions Needing More Precision**<br>

*   **Internal Document Hierarchy:** Treaties are structured into distinct **Articles** (**Articuln**) or **Paragraphs**. A researcher often needs to cite a specific clause (e.g., the "Ecclesiastical Reservation") rather than the whole document.
*   **Types of Document References:** The property **P67 refers to** is too general for this corpus. The sources show specific legal relationships: one document may **confirm**, **reivse**, **suspend**, or **revoke** the articles of an earlier treaty.
*   **Roles of Participation:** **P11 had participant** does not distinguish between different roles. In the corpus, actors participate as **Sovereigns**, **Commissioners** (**Commissarien**) with delegated power, **Mediators** (**Intercessoren**), or **Witnesses**.

**Proposed Additional Classes and Properties**<br>

| Suggested Extension | Source Phenomenon / Tie to Corpus |
| :--- | :--- |
| **E74 Group** | Essential for modeling the **Stände**, **Chapters**, and **Councils** that are the primary parties to these agreements. |
| **E73 Information Object** | To represent the conceptual "Peace of Augsburg" (1555) as a legal norm that is cited across various physical documents like the 1629 Edict. |
| **P148 has component** | To model the internal structure of **Articles** and **Paragraphs** as identifiable sub-entities of an **E31 Document**. |
| **P107 has current or former member** | To link the **E21 Persons** (like specific doctors or representatives) to the **E74 Groups** (like a City Council) they serve. |
| **E52 Time-Span (linked to E5)** | To model periods of validity that are contingent upon a future event, such as a "General Council". |
| **Pxx confirms / Pxx revokes** | Specific sub-properties of **P67** to track the legal lineage and validity chains found throughout the corpus. |

**Where CIDOC CRM Is Too General**<br>

*   **P6 valid in (Place):** In this corpus, legal validity is often social or confessional rather than purely geographical. For example, a privilege might be valid for **Mennonites** in a specific city but not for other residents. The model needs a way to express that a document is **"valid for [Group] in [Place]."**
*   **P11 had participant:** This property is too broad to capture the legal nuance of **Delegation**. The corpus distinguishes between the "Sovereign" in whose name a document is issued and the "Commissioner" who actually signs it. A specialized property for **"acting on behalf of"** would be more precise.
*   **E5 Event:** Negotiation processes in the corpus are complex, often involving multiple sub-events in different locations (e.g., negotiations moving from Leithmeritz to Pirna to Prague). Using a single **E5 Event** for a treaty signing obscures these distinct diplomatic stages.

Would you like me to focus on modeling a specific document, such as the **Peace of Augsburg (1555)**, to demonstrate how these proposed classes would capture its internal articles and external references?


## Part 4.5: Example Peace of Augsburg (1555)
To demonstrate how the proposed ontology extensions would accurately capture the complexities of the sources, I will model the **Peace of Augsburg (1555)** and its associated documents (**Augsburger Reichsabschied** and **Declaratio Ferdinandea**) using the refined CIDOC CRM-based structure.

**1. Modeling the Document as an E31 Document and E73 Information Object**<br>
The current model (E31) captures the physical artifact. However, the sources treat the "Peace" as a persistent legal norm cited across centuries.

*   **E31 Document:** The specific archival text (e.g., *pa000008-0116*).
*   **E73 Information Object:** The conceptual "Religious Peace of 1555".
*   **Relationship:** The E31 Document **carries** the E73 Information Object. This allows the 1629 Edict of Restitution to **refer to (P67)** the "Peace" as a set of rules regardless of which specific physical copy it uses.

**2. Institutional Primacy (Adding E74 Group)**<br>
The text is not an agreement between individuals, but between the **King** and the **Imperial Estates**.

*   **E21 Person:** **Ferdinand I**, Römischer König.
*   **E74 Group:** The **Stände** (Imperial Estates), including **Churfürsten** (Electors) and **Fürsten** (Princes).
*   **Role-based Participation:** Using a specialized property, we model that Ferdinand acted **on behalf of** Emperor Charles V, who gave him "absolute power" to negotiate. The Estates participated as collective bodies, representing their respective territories.

**3. Structural Granularity (Adding P148 has component)**<br>
The 1555 Peace is highly structured, and later treaties cite specific clauses. Modeling these as components is essential for precise legal tracking.

*   **E31 Document (Augsburger Reichsabschied)** **has component (P148)**:
    *   **Article 13:** General Peace between the Estates.
    *   **Article 15:** Protection for the Augsburg Confession.
    *   **Article 18:** The **Ecclesiastical Reservation (Geistlicher Vorbehalt)**.
    *   **Article 24:** The **Right of Emigration (Ius Emigrandi)**.
*   **Source Phenomenon:** The 1629 Edict specifically analyzes and reinterprets **Article 18** (the Reservation). Without this structural modeling, a query for "references to the Ecclesiastical Reservation" would only return the entire 40-page document rather than the specific relevant article.

**4. Legal Lineage and Confessional Specificity**<br>
The sources show that validity is often tied to a specific group in a specific place.

*   **P6 valid in (Place) + Valid for (Group):** The Peace is generally valid for the **Holy Roman Empire**, but specific provisions—like the **Declaratio Ferdinandea**—are explicitly valid for the **Knighthood and Cities** under spiritual lords who adhere to the Augsburg Confession.
*   **Legal Continuity:** The 1555 Peace explicitly **refers to (P67)** and builds upon the **Passau Treaty (1552)**. An ontology extension like **"Pxx confirms"** would link these two E31 Documents, allowing a researcher to trace the chain of legal validity from 1552 through 1555 to 1629.

**5. Conditional Temporal Validity (E52 Time-Span linked to E5)**<br>
A major recurring element in the 1555 Peace (and others like the 1533 Münster Treaty) is its contingent expiration date.

*   **E52 Time-Span:** The validity period of the peace.
*   **Condition:** Valid **"until a final Christian comparison/settlement"** (*biß zu endtlicher Christlicher vergleichung*).
*   **Ontological Modeling:** Instead of a fixed end-date (e.g., 1555–1599), the **E52 Time-Span** is defined as starting on **Sept 23, 1555** and ending upon the occurrence of a future **E5 Event (General Council/Settlement)**. This captures the legal reality that the treaty was intended as a permanent solution only *if* a council failed to materialize.

**Summary of Improvements for the Edition**<br>
By implementing these extensions, the edition moves from a simple digital archive to a **legal and prosopographical network**:
*   Users can query: "Which specific **Article (P148)** of the 1555 Peace does the 1635 **Prague Peace** revoke or confirm?".
*   Users can identify: "Which **Commissioners (E21)** representing **Cathedral Chapters (E74)** were active in both the 1555 and 1552 negotiations?".
*   Users can visualize: "What regions of the Empire were subject to the **Ius Emigrandi** based on their confessional group?".


## Part 5: Ambiguities and editorial issues
```text
Please identify all ambiguous or difficult cases in the corpus that may affect modeling in the ontology.

In particular, look for:
- uncertain dates,
- ambiguous places,
- collective actors,
- multiple versions of the same treaty,
- editorial interventions,
- references without a clear referent,
- and legal or normative statements that are difficult to model.

Please list these cases and explain what kind of modeling problem each creates.
```

### Result
Based on the analysis of the 50 early modern documents in the corpus, several ambiguous or difficult cases emerge that present significant challenges for modeling in a CIDOC CRM-based ontology.

**1. Uncertain and Complex Dates**
The corpus rarely relies on simple ISO-standard dates, instead using religious calendars or regnal years.
*   **Case:** Dates are frequently defined by **Saints’ days** (e.g., "Monday after Sunday Rogationum", "Tuesday after St. Michael's Day") or **regnal years** (e.g., "the 10th year of our Roman reign", "34th year of our reign").
*   **Modeling Problem:** These do not map directly to a static `E52 Time-Span`. Modeling them requires a **transformation layer** to align relative dates with the Gregorian calendar. Furthermore, legal validity is often tied to these specific, non-standard start dates, meaning errors in calculation ripple through the entire legal lineage of the ontology.

**2. Ambiguous Places and Jurisdictional Overlap**
Documents often involve multiple geographic entities with different roles.
*   **Case:** A treaty might be **issued** at Prague Castle, **negotiated** at Leithmeritz and Pirna, but be **valid** for the entire Kingdom of Bohemia. Other documents, like the **Hammelburg Treaty**, were signed in Hammelburg but concern the internal governance of Erfurt.
*   **Modeling Problem:** Using only `P7 took place at` and `P67 refers to` is insufficient. The ontology must distinguish between the **Place of Issue** (the `E53 Place` where `P92 brought into existence` happened) and the **Territorial Reach** (`P6 valid in`). Additionally, places often have **multilingual names** (e.g., Fredericopolis/Friedrichstadt), requiring the model to support multiple `E41 Appellations` for a single `E53 Place`.

**3. Collective and Institutional Actors**
The primary actors in the corpus are rarely individuals, but rather collective bodies or institutions.
*   **Case:** Agreements are made between "The Three Estates of the Crown of Bohemia", "The Cathedral Chapter", "City Councils", or "The Common Man". Individuals like **Ferdinand I** often act "on behalf of" the Emperor.
*   **Modeling Problem:** Representing these as `E21 Person` is incorrect. They require **`E74 Group`**. The difficulty lies in modeling **Delegation**: an individual (`E21`) participates in an event (`E5`) not as themselves, but as a representative of a Group (`E74`). The ontology needs a way to link the person to the group via a specific **Role** (e.g., *Commissarien*).

**4. Multiple Versions and Document States**
Annotations frequently highlight the physical or transmission status of the document.
*   **Case:** Documents are labeled as "Warhafftiger Abtruckh" (True Print), "Copei" (Copy), or "Gegen dem Original Collationirt" (Collated against the original).
*   **Modeling Problem:** There is a conflict between the **Legal Act** (the `E73 Information Object`) and its **Physical Manifestations** (the `E31 Documents`). If two documents represent the same treaty but one is an original and one is a "collated copy," the ontology must link them while preserving their distinct archival metadata. Standard CRM properties do not inherently distinguish between "Original" and "Copy" without custom extensions for **Document State**.

**5. Editorial Interventions and Placeholder Actors**
The sources contain editorial placeholders and transcriptions of missing text.
*   **Case:** Formulas such as **"N. N. N. und N."** are used when the names of ambassadors were to be inserted later. Square brackets like **"[uns]"** or **"[nit]"** indicate editorial reconstructions of damaged or missing text.
*   **Modeling Problem:** This creates **identitiy ambiguity**. A participant modeled as "N. N." cannot be linked to a known `E21 Person`. The ontology needs to support **Uncertainty Markers** or a way to model "Potential Participants" to distinguish between verified historical actors and editorial placeholders.

**6. References without a Clear Referent**
Treaties are part of a dense web of "recursive" legal language.
*   **Case:** Documents frequently refer to "the former treaty", "the aforementioned articles", or "the above-mentioned mandates". In the **1529 Speyer Recess**, one section refers specifically to "the Seven Articles" handed over by the Statthalter.
*   **Modeling Problem:** Without **Internal Hierarchy modeling** (`P148 has component`), these references remain "blind." If the ontology only models the document as a whole, it cannot resolve a reference to a specific **Article** or **Paragraph** within that document. This requires a granular structural model of the text itself.

**7. Difficult Legal and Normative Statements**
Many legal clauses define conditions that are theoretically and ontologically complex.
*   **Case:**
    *   **Conditional Validity:** "Valid until a final Christian settlement".
    *   **Amnesty with Exceptions:** General amnesties that explicitly exclude specific individuals or rebellion events (e.g., the Bohemian Rebellion).
    *   **Negative Obligations:** Provisions stating that something "shall not be done".
*   **Modeling Problem:** Standard ontologies are good at modeling *what is*, but struggle with **conditions and exceptions**. A `P6 valid in` property is binary; it cannot easily capture that a treaty is "Valid in Place X *except* for Group Y" or "Valid *until* Event Z occurs." This requires modeling **Legal Norms** as entities with their own lifecycles and conditional attributes.


## Part 6: Application on the Treaty of Münster
### Input
* this (.ttl-file)[https://github.com/WunschK/EuReD-Ontology/blob/main/muenster_vertrag.ttl]
* the source file of the Treaty of Münster

### Prompt
```text
Please apply your findings on this specific use case.
```

### Result
To apply the findings from our analysis to the **Münsterer Vertrag (1533)**, we can see how this specific document perfectly illustrates the need for the suggested ontology extensions. This treaty is a prime example of the complex institutional and conditional legal structures found throughout the corpus.

**1. Modeling Recurring Entities: Beyond Individuals**
The current model identifies several **E21 Persons** (e.g., Philipp of Hesse, Franz von Waldeck). However, the text highlights the necessity of the **E74 Group** extension:
*   **Collective Actors:** The treaty is not just between individuals but involves the "City Council, Elders, Masters, and the entire community of Münster" (*Raith, Alterleute, Meisterleute und gantze gemeyneheit*) and the **Cathedral Chapter** (*Dhumcapittel*).
*   **Delegated Authority:** Philipp of Hesse acts as a mediator (*unß yn die saichen geschlagen unnd zu guitlicher underhandelonge*), involving his own counselors (*unßere Rethe*). The ontology must distinguish his role as an **Intercessor** from the primary parties.

**2. Structural Granularity (P148 has component)**
The text is clearly organized into **19 Articles**, validating the call for a component-based model:
*   **Article 1:** Grants the city the right to preach the "Word of God" and minister sacraments in six specific parish churches (St. Lamberti, Ludgeri, etc.).
*   **Article 2:** Protects the religious practice of the Cathedral Chapter and other foundations in all other locations.
*   **Modeling Benefit:** Using **P148**, a researcher could query specific rights granted to the **Parish Churches** versus the **Cathedral**, rather than retrieving the entire 1533 document.

**3. Legal Lineage and References**
This treaty explicitly confirms the findings regarding cross-document dependencies:
*   **Reference to Earlier Norms:** Article 1 explicitly states that its provisions must follow the "Recess and Peace" established at the **Diet of Nuremberg in 1532** (*Nuremberg uffgericht... abschidts unnd friddens*).
*   **Ontological Link:** This supports the need for a property like **"confirms"** or **"refers to"** to link the 1533 Münsterer Vertrag to the 1532 Nuremberg Peace.

**4. Handling Temporal Ambiguity**
The Münsterer Vertrag provides a textbook example of **conditional validity**:
*   **The Condition:** The religious arrangements are valid only **"until a general, free, Christian council in the German nation"** (*biß uff ein gemein, frei, christlich Concilium yn deutscher Nation*).
*   **Modeling Problem:** As identified in the dossier, this cannot be modeled as a fixed end-date. The **E52 Time-Span** for this treaty’s validity must be linked to a future, uncertain **E5 Event** (the Council).

**5. Authentication and Document State**
The final articles (17–19) provide rich metadata for **P92 brought into existence**:
*   **Seals as Metadata:** The document lists the specific seals attached: the Landgrave's secret seal, the Bishop's princely seal, and the city's "great seal" (*Statt groiß Siegel*).
*   **Document Versions:** The text mentions that two identical versions were created (*zweene gleich lautend gefertigt*), one for the Bishop and one for the City Council. This supports the need for the ontology to track **multiple manifestations** of the same legal act.

**Summary of Application**
For this specific use case, the basic model (E31/E21) would capture the date and the main signatories but would miss the **institutional complexity of the Münster City Council**, the **conditional timeframe** based on a future council, and the **granular legal distinctions** between the six parish churches and the cathedral. Implementing the **E74 Group** and **P148 component** extensions is essential to make this digital edition truly research-capable.

**Improved .ttl file**
This improved `.ttl` file incorporates the findings from our analysis, specifically adding institutional groups (**E74 Group**), distinguishing the conceptual legal act (**E73 Information Object**) from the physical document, modeling the internal structure of **Articles** (**P148**), and capturing the **conditional validity** contingent on a future council.

```turtle
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

### 1. The Legal Act as a Conceptual Entity (E73 Information Object)
# This represents the "Peace of Münster" as a legal norm cited in later years.
<https://tueditions.ulb.tu-darmstadt.de/v/pa000008/inf/muensterer_vertrag_1533> a crm:E73_Information_Object ;
    rdfs:label "Münsterer Vertrag (Legal Act)" ;
    # Link to the previous legal norm it confirms
    crm:P67_refers_to <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/eve/#anstand_nuernberg_1532> ;
    # Modeling internal structure: Articles as components
    crm:P148_has_component <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/inf/muensterer_vertrag_1533/art_1> ,
                           <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/inf/muensterer_vertrag_1533/art_2> ;
    # Conditional Validity: until a general council
    crm:P16i_was_used_for <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/ts/muenster_validity_period> .

### 2. The Historical Document (E31 Document)
# This represents the specific archival object (pa000008-0207).
<http://purl.ulb.tu-darmstadt.de/vp/a000008-0207> a crm:E31_Document ;
    rdfs:label "Münsterer Vertrag (Physical Source)" ;
    crm:P1_is_identified_by "pa000008-0207" ;
    crm:P72_has_language "Deutsch" ;
    # The physical document carries the conceptual legal information
    crm:P128_carries <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/inf/muensterer_vertrag_1533> ;
    crm:P92_brought_into_existence <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/eve/signing_muenster_1533> ;
    crm:P6_valid_in <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/pla/muenster> .

### 3. Institutional Actors (E74 Group)
# Modeling the groups as the primary legal entities.
<https://tueditions.ulb.tu-darmstadt.de/v/pa000008/grp/muenster_rat> a crm:E74_Group ;
    rdfs:label "Rat, Alterleute, Meisterleute und gantze gemeyneheit der Stadt Münster" .

<https://tueditions.ulb.tu-darmstadt.de/v/pa000008/grp/muenster_domkapitel> a crm:E74_Group ;
    rdfs:label "Domkapitel zu Münster (Dhumcapittel)" .

### 4. Representation and Membership
# Linking specific persons to the groups they represent.
<https://tueditions.ulb.tu-darmstadt.de/v/pa000008/per/johann_bueren> a crm:E21_Person ;
    crm:P107i_is_current_or_former_member_of <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/grp/muenster_domkapitel> .

### 5. Conditional Validity (E52 Time-Span linked to E5 Event)
# The validity ends not with a date, but with a future event.
<https://tueditions.ulb.tu-darmstadt.de/v/pa000008/ts/muenster_validity_period> a crm:E52_Time_Span ;
    rdfs:label "Validity until a general council" ;
    crm:P82a_begin_of_the_begin "1533-02-14"^^xsd:date ;
    # The end of validity is tied to the prospective event
    crm:P4i_is_time-span_of <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/eve/prospective_general_council> .

<https://tueditions.ulb.tu-darmstadt.de/v/pa000008/eve/prospective_general_council> a crm:E5_Event ;
    rdfs:label "Gemein, frei, christlich Concilium yn deutscher Nation" .

### 6. The Signing Event
<https://tueditions.ulb.tu-darmstadt.de/v/pa000008/eve/signing_muenster_1533> a crm:E5_Event ;
    rdfs:label "Signing of the Münster Treaty" ;
    crm:P11_had_participant <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/per/philipp_hessen> , # Mediator role
                            <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/per/franz_waldeck> , # Principal role
                            <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/grp/muenster_rat> ,
                            <https://tueditions.ulb.tu-darmstadt.de/v/pa000008/grp/muenster_domkapitel> .
```

