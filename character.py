# Create your Character class logic in here.
class Character:
    
    def __init__(self, character, was_guessed=False):
        if not len(character) == 1:
            raise ValueError("Please enter a single letter.")
        if not isinstance(character, str):
            raise ValueError("Value must be text, not an integer.")
        self.character = character
        self.was_guessed = was_guessed
        
    def __str__(self):
        return "{}".format(str(self.character))
        
    def char_match(self, guess):
        if guess.lower() == self.character.lower():
            self.was_guessed = True
        
    def show(self):
        if self.was_guessed == True:
            return self.character   
        return '_'
       