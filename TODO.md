# TODO

### 1. Analisi dei requisiti
- [X] Definire il contesto d’uso specifico per il Museo Omero -> Vale
- [X] Descrivere le tabelle del dataset -> Ems
- [X] Schema dei processi interni revisionato -> Vale
- [X] Identificare i requisiti funzionali (prenotazioni, catalogo opere, tour guidati, ecc.) -> Fede, revisione Vale
- [X] Identificare i requisiti non funzionali (scalabilità, disponibilità, sicurezza, ecc.) -> Vale
---

### 2. Modellazione dei dati   
- [X] Modellazione concettuale (ER semplificato) -> Vale
- [X] Tavola volumi con giustificazione -> Fede
- [X] Tavola operazioni -> Tutti, da estendere
- [X] Partizionamento orizzontale -> Vale
- [X] Giustificazione aggregati con costi e operazioni -> Ems e Vale
- [X] NoAM e Aggregate Partitioning (EAO/ETF) -> Fede/Ems

---

### 3. Progettazione NoSQL (MongoDB)  
- [X] Definire la struttura JSON dei documenti -> Ems
- [X] Creare script per il popolamento iniziale -> Vale
- [ ] Aggiustare valori db: 
    1) referencing tra ticketIds in Event e ticket dei visitatori
    2) ref. tra id impiegato e msg di risposta in chat visitatore
    3) RD15 come farla se trade è in artwork?
    4) ref. tra department e shifts con employees per RD21/24
    5) inserire authorID in artwork per RD29
    6) controllare consistenza riferimenti msg
- [ ] Creare query -> Tutti
- [X] Appendice AI -> Fede
---

### 4. Documentazione 
- [ ] Creare un README con istruzioni per avviare il progetto  
- [ ] Preparare una presentazione per l’esposizione del progetto  
