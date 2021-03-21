import random
playing = True

while True:
    secretNumber = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.')


    for guessesTaken in range(1, 7):
        print('Take a guess.')
        guess = int(input())

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break
        
    if guess == secretNumber:
        print('Good Job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))

    print('Would you like to play again? y/N')
    if input() == 'y':
        continue
    else:
        break
print('Thanks for playing! Good Bye!')
