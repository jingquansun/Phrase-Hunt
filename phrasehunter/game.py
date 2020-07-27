import random
from phrasehunter.phrase import Phrase

class Game:
  def __init__(self, phrases):
    self.phrase = [Phrase(item) for item in phrases]
    self.current = random.choice(self.phrase)
    self.lives = 5
    self.guessed_char = []
    
  def start_game(self):
    intro = "\nWelcome to the Phrase Hunters Challenge!\n"
    print(intro)
    print("-" * len(intro))
    print("\nYou have {} lives, please guess the following phrase:\n".format(str(self.lives)))
    self.current.entire_phrase()
    
    while not self.current.guess_complete():
      guess = self.get_input()
      if isinstance(guess, type(None)):
        self.lost_game()
        self.end_game()
      else:  
        self.guessed_char.append(guess)
        if self.current.correct_guess(guess):
          print("\nGood guess! That is correct!\n")
          self.print_current()
          continue
        else:
          self.lives -= 1
          print("\nSorry, this letter is not in the phrase, please guess again. You now have {} lives.".format(self.lives))
          continue
          
    self.complete()
    self.end_game()
        
  def get_input(self):
    while self.lives >= 1:
      try:
        guess = input("\nPlease enter a letter:    ")
      except ValueError as err:
        self.lives -= 1
        print("\nThis is invalid, {}. You now have {} lives.".format(err, self.lives))
        continue
      if not guess.isalpha() or len(guess) != 1:
        self.lives -= 1
        print("\nThis is invalid. You now have {} lives".format(self.lives))
        continue
      elif guess in self.guessed_char:
        self.lives -= 1
        print("\nYou've already guessed this letter. You now have {} lives.".format(self.lives))
        continue
      else:
        return guess
  
  def complete(self):
    if self.current.guess_complete():
      print("\nCongratulations! You guessed the phrase!")
    else:
      self.lost_game()
      
  def end_game(self):
    choice = input("Would you like to play again? (Yes/No):  ")
    if choice.lower() == "yes":
      self.__init__(phrases)
      self.start_game()
    else:
      print("\nThanks for playing!")
  
  def lost_game(self):
      print("\nSorry, you're out of lives. Better luck next time!")
      print("The correct phrase was: ")
      print(self.current.show_everything())
                   
  def print_current(self):
      print(self.current.entire_phrase())
     