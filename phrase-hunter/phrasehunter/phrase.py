from .character import Character


class Phrase:
    
    def __init__(self, phrase):
        self.phrase = []
        
        for letter in phrase:
            self.phrase.append(Character(letter))
            
    def guessed(self, guess):
        for i in self.phrase:
            i.char_match(guess)
            
    def letter_in_phrase(self, guess):
        for letter in self.phrase:
            if letter.character.lower() == guess.lower():
                return True
        return False

    def phrase_complete(self):
        for char in self.phrase:
            if char.was_guessed == False:
                return False
        return True

    def show_guess(self):
        for i in self.phrase:
            print(i.show(), end= " ")
        print('\n')
        