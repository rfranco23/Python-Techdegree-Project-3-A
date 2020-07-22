import random

from phrase import Phrase
from character import Character


# Create your Game class logic in here.
class Game:
    
    def __init__(self, phrases):
        self.phrases = [Phrase(item) for item in phrases]
        self.active_phrase = random.choice(self.phrases)
        self.lives = 5
        

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
        check_phrase = phrase.phrase_guessed()
        self.active_phrase.show_guess()
        
        while self.lives > 0 and check_phrase:
            guess = self.get_letter()
            phrase.verify_phrase(guess)
            print('\n')
#            for char in phrase:
#                if char.was_guessed == False:
#                    guess = self.get_letter()
#                    check_guess = self.verify_phrase(guess)
#                    print('\n')
#                    if guess not in phrase:
#                        self.lives -= 1
#                        print("You have {} out of 5 lives remaining!\n".format(self.lives))
            self.active_phrase.show_guess()
                    
        
#        while self.lives > 0:
#            for char in phrase:
#                if char.was_guessed == False:
#                    guess = self.get_letter()
#                    self.verify_phrase(guess)
#            self.active_phrase.show_guess()
#            break