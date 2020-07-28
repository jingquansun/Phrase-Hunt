
class Character:
  def __init__(self, original):
    if type(original) != str or len(original) != 1:
      raise ValueError("This must be a one letter character.")
    self.original = original
    self.was_guessed = False
    
  def update(self, guess):
    if guess.upper() == self.original.upper():
      self.was_guessed = True
    return self.was_guessed
      
  def show(self):
    if self.was_guessed:
      return self.original
    elif self.original == " ":
      return " "
    else:
      return "_" 

  def set_guess(self):
    self.was_guessed = True 
  
  def reset_guess(self):
    self.was_guessed = False
    
  def equal(self, guess):
    return self.original.upper() == guess.upper()
  
  def show_everything(self):
    return self.original
    
