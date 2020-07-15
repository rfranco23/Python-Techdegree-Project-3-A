# Create your Character class logic in here.
class Character:
    
    def __init__(self, character, was_guessed=False):
        if not len(character) == 1:
            raise ValueError("Please enter a single letter.")
        if not isinstance(character, str):
            raise ValueError("Value must be a letter, not an integer.")
        if character == ' ':
            self.was_guessed = True
        else:
            self.was_guessed = was_guessed
        self.character = character
        
    def __str__(self):
        return self.character
        
    def __repr__(self):
        return self.character
        
    def char_match(self, guess):
        if guess.lower() == self.character.lower():
            self.was_guessed = True
        
    def show(self):
        if self.was_guessed == True:
            return self.character   
        return '_'
       