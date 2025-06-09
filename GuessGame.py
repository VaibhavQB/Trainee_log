# Project: Guess the Number Game

# Importing random module to generate random numbers
import random 

# Function to start and play the Game
def guess_the_number():
    num = random.randint(100, 150) # Random number between 100 and 150

    while True:
        try:
            guess = int(input("Guess The number (between 100 and 150): ")) # User input for guessing the number
            if guess < 100 or guess > 150:
                print("Your Guess is out of the Guessing range" ) # User guesssed out of range
            elif guess < num :
                print("You guessed too low, Go higher!")  # User Guessed too Low
            elif guess > num:
                print("You guessed too high, Go lower!")  # User Guessed too High
            else:
                print("Congratulations! You guessed the number correctly!") # User Guessed Correctly
                break

        except:
            pass

if __name__ == "__main__":
    guess_the_number()