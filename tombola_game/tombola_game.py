# Modellare estrazione di numeri (tombola).

# Ho una classe Cartella che contiene 15 numeri diversi tra loro e casuali tra 1 e 90. → Meglio il set causa unicità

# Creo tre oggetti Cartella.

# Ho un elenco di numeri che rappresenta l'estrazione (che immaginiamo fatta da un altro) e per noi di fatto sarà una costante.
#  → Faccio una lista (a livello globale) di 90 numeri tutti diversi (posso riusare l'approccio del passo precedente)

# Scorro l'elenco di numeri simulando l'estrazione:
# - Ad ogni passo stampo la situazione delle mie tre cartelle.
# - In particolare voglio che mi venga detto quanti numeri mi
#   mancano per vincere (in ciascuna cartella)
# - Quando vinco produco un messaggio "Ho vinto in n passi"

from tombola import Tombola
from cartella import Cartella

players:list = [
  Cartella('Leonardo'),
  Cartella('Fabio'),
  Cartella('Federico'),
  Cartella('Enrico'),
  Cartella('Sara'),
]

Tombola.start_game(players)
