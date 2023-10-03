'''
Create a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The pogram should indicate if the guess value was too low or too high. If the user guesses correctly, the program should print a congratulatory message.
'''

import random

def main():
    print("Guess a number between 1 and 10")
    random_number = random.randint(1,10)
    while True:
        guess = int(input("Enter your guess: "))
        if guess == random_number:
            print("You guessed correctly!")
            break
        elif guess < random_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

if __name__ == "__main__":
    main()

