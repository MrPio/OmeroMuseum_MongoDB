# TODO

### 1. Analisi dei requisiti
- [ ] Definire il contesto d’uso specifico per il Museo Omero  
- [ ] Identificare i requisiti funzionali (prenotazioni, catalogo opere, tour guidati, ecc.)  
- [ ] Identificare i requisiti non funzionali (scalabilità, disponibilità, sicurezza, ecc.)  
- [ ] Definire i volumi attesi di dati (utenti, opere, interazioni)  
- [ ] Definire i casi d’uso principali  

---

### 2. Modellazione dei dati  
- [ ] Modellazione concettuale (diagramma UML o ER semplificato)  
- [ ] Identificare aggregati e radici degli aggregati  
- [ ] Decidere le entità da denormalizzare e aggregare per ridurre le query complesse  
- [ ] Stabilire le politiche di partizionamento (orizzontale per messaggi/feedback, se necessario)  

---

### 3. Progettazione NoSQL (MongoDB)  
- [ ] Tradurre il modello concettuale in documenti MongoDB  
- [ ] Scegliere la strategia di rappresentazione (ETF o EAO)  
- [ ] Definire la struttura JSON dei documenti principali (utenti, opere, eventi, gruppi, ecc.)  
- [ ] Definire gli indici per ottimizzare le query  

---

### 4. Popolamento del database  
- [ ] Creare script per il popolamento iniziale
- [ ] Generare dati per:  
    - [ ] Utenti (visitatori, guide, amministratori)  
    - [ ] Opere e collezioni  
    - [ ] Prenotazioni e visite  
    - [ ] Commenti e recensioni  

---

### 5. Definizione delle query principali  
- [ ] Creare query per:  
    - [ ] Creazione/aggiornamento/eliminazione di utenti  
    - [ ] Consultazione delle opere e delle schede descrittive  
    - [ ] Prenotazione di visite e tour tattili  
    - [ ] Gestione eventi e laboratori  
    - [ ] Statistiche su visite e feedback  

---

### 6. Deployment e documentazione  
- [ ] Creare un README con istruzioni per avviare il progetto  
- [ ] Documentare le scelte progettuali  
- [ ] Preparare una presentazione per l’esposizione del progetto  
