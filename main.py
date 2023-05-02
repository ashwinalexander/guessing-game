#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo 
import random 

def hint_and_print(new_guess, answer):
  if new_guess < answer:
    print("Too Low \nGuess Again\n")
    return False
  elif new_guess == answer:
    print(f"You win! {answer} is the correct answer")
    return True
  elif new_guess > answer:
    print("Too High \nGuess Again\n")
    return False


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
the_answer = random.randint(1, 100)
# print(f"I guessed {the_answer}")
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
tries = 5 
if difficulty == 'easy':
  tries = 10
elif difficulty == 'hard':
  tries = 5
else: 
  print("Incorrect input.")
while tries > 0:
  print(f"You have {tries} attempts remaining to guess the number")
  new_guess = int(input("Make a guess: "))
  isGameOver = hint_and_print(new_guess, the_answer)
  if not isGameOver:
    tries -=1 
  else:
    tries = -1
if tries == 0:
   print(f"Game Over. You lose. The answer was {the_answer}")
  



