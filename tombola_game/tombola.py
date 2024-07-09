import random
class Tombola:
  winner:bool = False
  all_numbers = list(range(1,91))

  # This starts the game, and print all the players steps till someone win
  @staticmethod
  def start_game(cartelle:list)->None:
    print("------------ BENVENUTI AL GIOCO DELLA TOMBOLA ------------")
    if not len(cartelle): print("Non Ci sono cartelle"); exit(); 
    
    while not Tombola.winner or Tombola.all_numbers:
      
      index:int = random.randint(0, len(Tombola.all_numbers)-1)
      extracted = Tombola.all_numbers.pop(index)
      for cartella in cartelle:
        
        cartella.count += 1

        if extracted in cartella.numbers:
          cartella.numbers.discard(extracted)
          print(F"{cartella.name} -> Trovato numero!:", extracted)
          print(F"Mancano {15 - len(cartella.numbers)} numeri per vincere!")
          print(F"Numeri rimanenti: {list(cartella.numbers)}")
          print(F"{cartella.count} estrazioni effettuate.")
          print("---------------------------------------")

        if len(cartella.numbers) == 0: Tombola.winner = True 
        if Tombola.winner: print(F"{cartella.name} ha vinto! Estrazioni effettuate: {cartella.count}"); exit()
        random.seed(None)
