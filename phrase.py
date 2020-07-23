from character import Character


# Create your Phrase class logic here.
class Phrase:
    
    def __init__(self, phrase):
        self.phrase = []
        
        for letter in phrase:
            self.phrase.append(Character(letter))
            
    def guess_letter(self, guess):
        for i in self.phrase:
            i.char_match(guess)
            
#    def guess_letter(self, guess):
#        if guess.lower() in self.phrase:
#            return True
#        return False

    def phrase_complete(self):
        for char in self.phrase:
            if char.was_guessed == False:
                return False
        return True

    def show_guess(self):
        for i in self.phrase:
            print(i.show(), end= " ")
        print('\n')
        