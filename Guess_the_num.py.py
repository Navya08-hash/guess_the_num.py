#Guess the number game
import random
import logo_for_game
def game():
    print(logo_for_game.logo)
    print("Welcome to the Number Guessing Game!")
def set_difficulty(level):
    if level == "easy":
        return 10
    else:
        return 5

def check_answer(guess, answer, attempts):
    if guess < answer:
        print("Your guess is too low.")
        return attempts - 1
    elif guess > answer:
        print("Your guess is too high.")
        return attempts - 1
    else:
        print(f"You Won! The answer was {answer}.")
        return attempts
game()
print("Let me think of a number between 1 and 100")
number = random.randint(1, 100)
level = input("Choose a difficulty level....Type 'easy' or 'hard': ")
attempts = set_difficulty(level)
guess_number = 0

while attempts > 0 and guess_number != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess_number = int(input("Guess the number: "))
    attempts = check_answer(guess_number, number, attempts)
    if guess_number == number:
        break
    if attempts == 0:
        print(f"You've run out of attempts. The answer was {number}.")
    else:
        print("Guess again.")
print("Thanks for playing!")

# End of the game