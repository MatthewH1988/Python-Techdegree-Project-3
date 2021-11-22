import random
import sys
from phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("de opresso liber"), 
            Phrase("semper paratus"), 
            Phrase("semper fidelis"), 
            Phrase("non sibi sed patriae"),
            Phrase("semper fortis")
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        
    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("WELCOME TO PHRASE HUNTER!\n")
        
    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f'Number of missed attempts: {self.missed}')
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                print("Incorrect!")
                self.missed += 1
        else:
            self.game_over()
        
    def get_guess(self):
        while True:
            try:
                guess_try = input("Guess a letter: ").lower()
                if len(guess_try) != 1:
                    print("Please guess one letter")
                    continue
                elif not guess_try.isalpha():
                    raise ValueError("Please guess letters only")
                elif guess_try.lower() in self.guesses:
                    print("You have already guessed that letter")
            except ValueError:
                print("Please guess letters only")
                continue
            else:
                return guess_try
            
    def game_over(self):
        if self.missed == 5:
            print("Game Over! You Lost!")
            self.play_again()
        else:
            print("You Won!")
            self.play_again()
        
    def play_again(self):
        play_again_input = input("Would you like to play again? Please press 'Y' to play again and any other button to quit ").upper()
        if play_again_input == 'Y':
            self.__init__()
            self.start()
        else:
            print("Thank you for playing!")
            sys.exit()