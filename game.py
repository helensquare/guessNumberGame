#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

print(art.logo)

# Computer randomly chooses an int from 1 to 100 for the user to guess
secretNumber = random.randint(1, 100)
print("I'm thinking about a number from 1 to 100.")

# User is asked to choose a level
EASY = 10
HARD = 5
levelChoice = input("Do you want the easy or the hard level? Type 'easy' or 'hard'\n")

# Number of lives to guess the secretNumber is set based on users previous input
if levelChoice == "easy":
  lives = EASY
elif levelChoice == "hard":
  lives = HARD
else:
  print("You typed something invalid.")


def giveHint(guess, secretNumber):
  if guess < secretNumber:
    print("You didn't guess. Your number was too low.")
  else: 
    print("You didn't guess. Your number was too high.")

# We check the guess against the secretNumber
def checkNumber(lives, secretNumber):
  continueGame = True
  while continueGame:
    # User is asked to guess secretNumber
    guess = int(input("Guess a number:\n"))
    # I need to check secretNumber AND track how many lives the user has left
    if guess != secretNumber:
      lives -= 1
      #Check if player run out of lives. If so, game over.
      if lives == 0:
        print(f"You run out of lives. The Secret Number was {secretNumber}")
        continueGame = False
      else:
        giveHint(guess, secretNumber)
        print(f"You have {lives} lives left.")
          
    else:
      print(f"You win! The Secret Number was {secretNumber}")
      print(art.youWin)
      continueGame = False


  
checkNumber(lives, secretNumber)

