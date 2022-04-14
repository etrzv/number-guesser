import random

n = input('Please type a number: ')
guesses = 0
random_number = random.randrange(1, 11)


if n.isdigit():
    user_guess = int(n)
    if user_guess <= 0:
        print('Please type a number larger than 0!')
else:
    print('Please type a number!')

while True:
    guesses += 1
    user_guess = int(n)
    if user_guess == random_number:
        print(f'Congratulations! You got it in {guesses} guesses!')
        break
    elif user_guess > random_number:
        print('You were above the number!')
    else:
        print('You were below the number!')
    n = input('Please type a number: ')
