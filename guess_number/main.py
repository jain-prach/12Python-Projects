import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("guess again, too low")
        elif guess > random_number:
            print("guess again, too high")
    print(f"You guessed the random number {random_number} correctly")
    
guess(15)