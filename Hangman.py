import random

class Hangman:
    def __init__(self):
        self.words = ["python", "hangman", "game", "code", "fun"]
        self.word = random.choice(self.words)
        self.guessed = "_" * len(self.word)
        self.incorrect_guesses = 0
        self.max_incorrect = 6
        self.guessed_letters = []

    def display_word(self):
        print( "Word:",self.guessed)

    def get_guess(self):
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            return None
        return guess

    def update_guessed(self, guess):
        new_guessed = ""
        for i in range(len(self.word)):
            if self.word[i] == guess:
                new_guessed += guess
            else:
                new_guessed += self.guessed[i]
        self.guessed = new_guessed

    def play(self):
        print("Welcome to Hangman!")

        while self.incorrect_guesses < self.max_incorrect and "_" in self.guessed:
            self.display_word()
            guess = self.get_guess()

            if guess is None:
                continue

            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            self.guessed_letters.append(guess)

            if guess in self.word:
                self.update_guessed(guess)
            else:
                self.incorrect_guesses += 1
                print("Wrong guess! You have ",self.max_incorrect - self.incorrect_guesses ,"tries left.")

        if "_" not in self.guessed:
            print("\nCongratulations! You guessed the word:",self.word)
        else:
            print("\nGame over! The word was:",self.word)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            new=Hangman()
        else:
            print("Thanks for playing!")

p=Hangman()
p.play()
