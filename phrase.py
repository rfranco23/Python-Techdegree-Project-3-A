from character import Character


# Create your Phrase class logic here.
class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase
        
        self.characters = []
        for character in self.phrase:
            self.characters.append(Character(character))
            
    def __str__(self):
        return self.phrase
    
    def __repr__(self):
        return self.phrase
            
    def guessed(self, guess):
        for i in self.characters:
            i.char_match(guess)
        
    def check_guess(self):
        current_phrase = []
        for i in self.characters:
            current_phrase.append(i.show())
        return current_phrase

    def show_guess(self):
        for i in self.characters:
            print(i.show(), end= " ")
        print('\n')