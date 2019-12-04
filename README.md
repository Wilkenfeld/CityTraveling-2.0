# City Traveling 2.0 - A new way to experience your city!

## Funzionamento del software di simulazione

La simulazione software si presenta con due aree principali:

- la rappresentazione grafica della città (vedi la sezione apposita);
- il menù di controllo

### Rappresentazione grafica

La città viene rappresentata come un grafo, dove i nodi rappresentano incroci
e passaggi a livello (distinti da colori differenti), mentre gli archi
rappresentano strade e binari (anch'essi distinti da colori differenti).

I vari veicoli vengono identificati da dei rettangoli che percorrono gli archi.
Per dettagli riguardo al loro funzionamento, vedi sezione apposita.

#### Colori

Per i **nodi** i colori sono:

- Incroci "normali" -> grigio scuro
- Passaggi a livello -> grigio chiaro
- Semafori -> verde nelle direzioni in cui è consentito il transito, rosso
    in quelle in cui è negato

Per gli **archi** i colori sono:

- Strade normali -> grigio chiaro
- Binari -> grigio scuro
