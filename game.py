from phrase import Phrase


# Create your Game class logic in here.
class Game:
    
    def __init__(self, phrases):
        self.phrases = phrases
        
        self.get_phrase = []
        for phrase in self.phrases:
            self.get_phrase.append(Phrase(phrase))
        