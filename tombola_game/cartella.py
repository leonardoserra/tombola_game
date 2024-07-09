import random

class Cartella:

  def __init__(self, name) -> None:
    self.name = name
    self.numbers = self.extract_card_numbers()
    self.count = 0

  def extract_card_numbers(self)->set:
    numbers = set()
    while len(numbers) < 15:
      r:int = random.randint(1, 90)
      numbers.add(r)
    print(F"Numeri Della Cartella di {self.name} :", numbers, "\n-------------------------------------")  
    return numbers
