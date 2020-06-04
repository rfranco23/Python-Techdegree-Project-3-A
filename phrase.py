from character import Character


# Create your Phrase class logic here.
class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase
        
        self.characters = []
        for character in self.phrase:
            self.characters.append(Character(character))
        
    def guessed(self):
        if '_' in self.phrase:
            return "The phrase is not completely guessed."
        return "The phrase is completely guessed."
        
    def check_guess(self):
        show_phrase = []
        for i in self.characters:
            show_phrase.append(i.show())
        return show_phrase