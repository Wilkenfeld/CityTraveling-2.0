# City Traveling 2.0 - A new way to experience your city!

## Introduzione

CityTraveling è una piattaforma cittadina che permette di abbattere le
emissioni causate dal traffico senza creare ZTL, oltre a facilitare l'arrivo
di mezzi di soccorso.

## Feature

- Calcolo del percorso meno inquinante e più veloce
- Calcolo del percorso più veloce (per i mezzi di soccorso)

## Esempi

Nella cartella *samples* è presente un eseguibile per effettuare
una simulazione su un modello prefatto.

## Funzionamento dell'algoritmo per il calcolo del percorso

Il percorso viene calcolato seguendo i seguenti passi:

1. La centralina presente nell'auto invia le informazioni necessarie
    alla centralina fissa più vicina;

2. La centralina fissa reindirizza il messaggio a tutte le altre centraline
    vicine a lei, memorizzando momentaneamente il mittente. Questo processo
    viene ripetuto finché il messaggio non raggiunge la destinazione;

3. Quando il messaggio raggiunge la destinazione viene rispedito indietro
    verso l'origine, il cui contenuto rappresenta il percorso migliore fino
    a quel momento;

4. La centralina fissa di partenza restituisce all'auto il percorso migliore.

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

- **Grigio scuro** per gli **incroci "normali"**
- **Grigio chiaro** per i **passaggi a livello**
- **Verde** nelle direzioni in cui è consentito il transito, **rosso**
    in quelle in cui è negato

Per gli **archi** i colori sono:

- **Grigio chiaro** per le **strade normali**
- **Grigio scuro** per i **binari**

Per i **veicoli** i colori sono:

- **Bianco** per le **automobili**
- **Rosso** per **veicoli di emergenza (ambulanze, pompieri...)**
- **Blu** per **forze dell'ordine (Polizia, Carabinieri)**
- **Rosso scuro** per i **treni**

### Schema della struttura

Sia i grafi che i veicoli vengono salvati sotto forma di file JSON.

Il file JSON contenente la città (il grafo) contiene una lista popolata da
una serie di oggetti, che rappresentano i nodi.

Ogni nodo contiene:

- un **id**, che identifica il nodo
- una lista chiamata **closeTo**, dentro alla quale sono contenute tante liste
quanti sono i nodi raggiungibili. Ogni sottolista è composta
dall'ID del nodo, la distanza da esso, il grado dell'angolo che si forma rispetto alle sue coordinate,
l'inquinamento massimo che quella strada può sostenere.
- **nodeType**, che specifica il tipo di nodo
(specifica se è un semaforo, un incrocio o un passaggio a livello).
