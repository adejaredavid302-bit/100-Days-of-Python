import random
from game_data import data
from art import *
def format_data(account):
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]
    return f"{account_name},{account_description} from {account_country}"
def check_answer(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess=='a'
    elif b_followers > a_followers:
        return user_guess=='b'
    else:
        return False
score=0
game_again=True

account_B=random.choice(data)
while game_again:
    print(logo)
    account_A=account_B
    account_B=random.choice(data)
    if account_A==account_B:
        acc_B=random.choice(data)

    print(f"Compare A:{format_data(account_A)}")
    print(vs)
    print(f"Against B:{format_data(account_B)} ")

    guess=input("who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count=account_A["follower_count"]
    b_follower_count=account_B["follower_count"]

    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    if is_correct:
        score+=1
        print("\n"*20)
        print(f"You are right! current score: {score}")
    else:
        game_again=False
        print(f"You are wrong. Final score: {score}")