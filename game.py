import random

from phrase import Phrase


# Create your Game class logic in here.
class Game:
    
    def __init__(self, phrases):
        self.phrases = [Phrase(item) for item in phrases]
        self.active_phrase = random.choice(self.phrases)
        self.lives = 5
        
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
        phrase = self.active_phrase
        phrase.show_guess()
        
        while self.lives > 0 and not self.active_phrase.phrase_complete():
            guess = self.get_letter()
            hit = phrase.guess_letter(guess)
            print('\n')
            if hit == True:
                phrase.show_guess()
#            if hit != True:
#                self.lives -= 1
#                print("You have {} out of 5 lives remaining!\n".format(self.lives))
#            phrase.show_guess()
                    