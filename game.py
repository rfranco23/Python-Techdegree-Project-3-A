import random

from phrase import Phrase


# Create your Game class logic in here.
class Game:
    
    def __init__(self, phrases):
        self.phrases = [Phrase(item) for item in phrases]
        self.active_phrase = random.choice(self.phrases)
        self.lives = 5
        
#        self.get_phrase = []
#        for phrase in self.phrases:
#            self.get_phrase.append(Phrase(phrase))

    def __str__(self):
        return self.phrases
    
    def __repr__(self):
        return self.phrases
    
#    def verify_phrase(self, guess):
#        self.active_phrase.guessed(guess)
#        return self.active_phrase.check_guess()

    def get_letter(self):
        guess_letter = True
        
        while guess_letter:
            try:
                guess = input('\nGuess a letter: ')
                if guess.lower() == 'exit':
                    return guess.lower()
                if not guess.isalpha() or len(guess) != 1:
                    raise ValueError
                return guess.lower()
            except ValueError:
                print('Please select a single letter.')
    
    def start_game(self):
        welcome = print("\nWelcome to the Phrase Hunters Challenge!\n")
        phrase = self.active_phrase.characters
        guessed_letters = []
        check_phrase = self.active_phrase.check_guess()
        
        while self.lives > 0 and '_' in check_phrase:
            guess = self.get_letter()