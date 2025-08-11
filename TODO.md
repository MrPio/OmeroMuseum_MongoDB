# TODO

### 1. Analisi dei requisiti
- [X] Definire il contesto d’uso specifico per il Museo Omero -> Vale
- [ ] Descrivere le tabelle del dataset -> Ems
- [X] Schema dei processi interni revisionato -> Vale
- [ ] Identificare i requisiti funzionali (prenotazioni, catalogo opere, tour guidati, ecc.) -> Federico
- [ ] Identificare i requisiti non funzionali (scalabilità, disponibilità, sicurezza, ecc.)
- [X] Modellazione concettuale (ER semplificato) -> Vale
---

### 2. Modellazione dei dati   
- [ ] Progettazione aggregati con costi e operazioni (rosso e blu -> vale, verdi -> fede) 
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
