import random
from art import logo
print(logo)
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def check_answer(user_guess, actual_answer, turns):
    if user_guess==actual_answer:
        print("you guessed correctly")
        return turns
    elif user_guess>actual_answer:
        print ("you guessed too high")
        return turns-1
    elif user_guess<actual_answer:
        print("you guessed too low")
        return turns-1
def set_difficulty():
    level=input("Choose a difficulty.Type 'easy' or 'hard' ").lower()
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1,100)
    turns=set_difficulty()
    guess=0
    print(answer)
    while guess != answer:
        print(f"You have {turns} attempts to guess the number: .")
        guess=int(input("Make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You ran out of guesses")
            print(f"The number I was thinking of was {answer}")
            return
game()


