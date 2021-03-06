import random

from .phrase import Phrase


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
        self.active_phrase.show_guess()
        
        while self.lives > 0 and not self.active_phrase.phrase_complete():
            guess = self.get_letter()
            self.active_phrase.guessed(guess)
            self.active_phrase.letter_in_phrase(guess)
            print('\n')
            if self.active_phrase.letter_in_phrase(guess) == False:
                self.lives -= 1
                print("You have {} out of 5 lives remaining!\n".format(self.lives))
            self.active_phrase.show_guess()
            
            if self.lives > 0 and self.active_phrase.phrase_complete():
                print('Congratulations!! You guessed the phrase!\n')
                play_again = input("Would you like to play again? [Y]es/[N]o: ")
                if play_again.lower() in ['y', 'yes']:
                    self.active_phrase = random.choice(self.phrases)
                    self.lives = 5
                    welcome = print("\nWelcome back to the Phrase Hunters Challenge!\n")
                    self.active_phrase.show_guess()
                    continue
                print('\nGoodbye, thank you for playing.\n')
                break
                
            elif self.lives == 0 and not self.active_phrase.phrase_complete():
                print('Game Over...You have run out of guesses\n')
                play_again = input("Would you like to play again? [Y]es/[N]o: ")
                if play_again.lower() in ['y', 'yes']:
                    self.active_phrase = random.choice(self.phrases)
                    self.lives = 5
                    welcome = print("\nWelcome back to the Phrase Hunters Challenge!\n")
                    self.active_phrase.show_guess()
                    continue
                print('\nGoodbye, thank you for playing.\n')
                break
                    