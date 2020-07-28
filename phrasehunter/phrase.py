from phrasehunter.character import Character

class Phrase:
  def __init__(self, phrase):
    letters = list(phrase)
    self.characters = [Character(letter) for letter in letters]
    
  def guess_complete(self):
    guessed_phrase = []
    for letter in self.characters:
      guessed_phrase.append(letter.show())
    return "_" not in guessed_phrase
  
  def entire_phrase(self):
    for letter in self.characters:
      print(letter.show(), end="")
    
  def correct_guess(self, guess):
    count = 0
    for letter in self.characters:
      if letter.equal(guess):
        count += 1
        letter.set_guess()
    return count >= 1
  
  def show_everything(self):
    for letter in self.characters:
      print(letter.show_everything(), end="")

