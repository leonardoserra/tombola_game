# Create at least a Cartella Object and pass in a name param, 
# pass the list of players to the start_game() function
# the first that found all the 15 numbers on its card will win

# start the program and see who will win!

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
