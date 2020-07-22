from character import Character


# Create your Phrase class logic here.
class Phrase:
    
    def __init__(self, phrase):
        self.phrase = []
        self.characters = list(phrase)
        
        for letter in phrase:
            self.phrase.append(Character(letter))
            
    def __str__(self):
        return self.phrase
    
    def __repr__(self):
        return self.phrase
            
    def guessed(self, guess):
        for i in self.phrase:
            i.char_match(guess)
        
    def check_guess(self):
        unguessed_phrase = []
        for i in self.phrase:
            unguessed_phrase.append(i.show())
        print(unguessed_phrase)
        if '_' in unguessed_phrase:
            return False
        return True

    def show_guess(self):
        for i in self.phrase:
            print(i.show(), end= " ")
        print('\n')
        
    def already_guessed(self, guess):
        if guess.lower() in self.phrase.already_guessed:
            print('You have already guessed that letter. Please pick another letter.')
            
            
    
#    def guess_letter(self, guess):