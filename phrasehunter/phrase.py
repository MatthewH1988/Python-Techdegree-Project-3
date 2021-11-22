class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def display(self, guesses):
        for character in self.phrase:
            if character in guesses:
                print(f'{character}', end=' ')
            else:
                print("_", end=" ")
                
    def check_guess(self, guesses):
        return guesses in self.phrase
    
    def check_complete(self, guesses):
        for character in self.phrase:
            if character not in guesses:
                return False
        return True