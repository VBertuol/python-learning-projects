from random import randrange

difficulties = {1 : 10, 2 : 100, 3 : 1000}
hot_or_cold = [(2, 5), (20, 50), (200, 500)]

print("Welcome to the Guess The Number Game!\n\n")
print("Difficulty Levels:")
print("1 - Easy (1 - 10)")
print("2 - Hard (1 - 100)")
print("3 - Impossible (1 - 1000)\n")

while True:
    try:
        difficulty = int(input("Enter the difficulty level (1, 2 or 3):"))
        if difficulty in [1, 2, 3]:
            break
        else:
            print("Please enter a valid difficulty: 1, 2 or 3")
    except: 
        print("Please enter a valid difficulty: 1, 2 or 3")


random_number = randrange(1, difficulties[difficulty])
attempts = 0
lst = []

while True:
    print(f'\ndifficulty level = {difficulty}, range to guess: 1 - {difficulties[difficulty]}')
    print(f'Total guesses: {attempts}, guessed numbers: {lst}')
    try:
        number = int(input("Guess a number: "))
        if number < 1 or number > difficulties[difficulty]:
            print(f'Number out of range, range to guess: 1 - {difficulties[difficulty]}')
        else:
            if number == random_number:
                attempts += 1
                print(f'Congratulations! You guessed right! The number was {random_number}\n You took {attempts} guesses to hit the right one')
                break
            elif number in lst:
                print(f'You already tried {number} and is not right, guess another one!')
            else:
                attempts += 1
                lst.append(number)
                if abs(number - random_number) < hot_or_cold[difficulty-1][1]:
                    if abs(number - random_number) < hot_or_cold[difficulty-1][0]:
                        print('You guessed it wrong, but it is very hot..')
                    else:
                        print('You guessed it wrong, but it is hot..')
                else:
                    print('You guessed it wrong, and it is cold..')
                
    except:
        print(f'Please enter a valid number inside the range, range to guess: 1 - {difficulties[difficulty]}')


