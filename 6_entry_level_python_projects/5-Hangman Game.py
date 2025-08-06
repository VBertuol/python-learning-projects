from random import choice

words = ["mountain", "balance", "diamond", "library", "justice", "animals", "dolphin", "freedom", "kingdom", "factory", "biology", "silence", "rainbow", "blanket", "fishing", "sunshine", "texture", "airport", "history", "concept"]
word = choice(words)
attempts = len(word) 
guess = ['_'] * len(word)
guesses = []


def is_game_over(word, attempts, guess):
    if attempts == 0:
        print("no attempts left, you lost...")
        print(f"the word was: {word}")
        return True
    if ''.join(guess) == word:
        print(f"Congratulations! You guessed the word: {word}")
        return True
    return False

def new_guess(word, guess, guesses):
    while True:
        a = input("Enter a single letter: ").lower()
        if len(a) == 1 and a.isalpha():
            if a in guesses:
                print("You've already guessed this letter. Try again.")
            else:
                guesses.append(a)
                for i, char in enumerate(word):
                    if char == a:
                        guess[i] = a
                return
        else:
            print("Invalid input. Please enter a single letter.")

while True:
    if is_game_over(word, attempts, guess):
        break
    print("\nTry to guess a letter of the word:")
    print(' '.join(guess))
    print(f"Attempts left: {attempts}")
    print(f"Already guessed letters: {', '.join(sorted(guesses))}")
    new_guess(word, guess, guesses)
    attempts -= 1