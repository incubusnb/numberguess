import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')


for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    