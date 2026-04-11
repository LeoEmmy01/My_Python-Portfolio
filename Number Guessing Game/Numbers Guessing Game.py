#Version 1
import random

print("NUMBER GUESSING GAME")
print("=" * 30)
print("I'm thinking of a number between 1 and 20")

secret = random.randint(1, 20)
guess = 0

while guess != secret:
    guess = int(input("Your guess: "))
    
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
        
    else:
        
        print("Correct! You got the it!")
        
        
        
#Version 2

import random

print("NUMBER GUESS GAME")
print("=" *30)

secret = random.randint(1, 20)
attempts = 0
max_attempts = 5

print(f"I'm thinking of 1-20. You have {max_attempts} guesses!")

while attempts < max_attempts:
    guess = int(input("You guess: "))
    attempts += 1
    
    if guess < secret:
        print(f"Too low! ({max_attempts - attempts} left)")
    elif guess > secret:
        print(f"Too high! ({max_attempts - attempts} left)")
    else:
        print(f"Correct in {attempts} attempts")
        break
else:
    print(f"Game over! The number was {secret}")
    
#Version 3

import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("\nNEW GAME!")
    print("I'm thinking 1-100")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess {attempts +1}/{max_attempts}: "))
            attempts += 1
            
            diff = abs(guess - secret)
            
            if guess < secret:
                if diff <= 10:
                    print("Too low, but close!")
                else:
                    print("Too low!")
            elif guess > secret:
                if diff <= 10:
                    print("Too high, but close!")
                else:
                    print("Too high!")
            else:
                print(f"WINNER! Got it in {attempts} guess!")
                return True
        
        except ValueError:
            print("Please enter a number")
            
    print(f"Game over! The number was {secret}")
    return False

#main game loop
print("=" * 40)
print("NUMBER GUESSING GAME".center(40))
print("=" *40)

score = 0
games = 0

while True:
    play_game()
    games += 1
    
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        break
    print(f"\nThanks for playing! You played {games} games!")