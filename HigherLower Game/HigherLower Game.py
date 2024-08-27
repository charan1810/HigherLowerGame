from art import logo,vs
from Gamedata import data
import random

def format_data(account):
    '''Takes the account data and returns the printable format.'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(user_guess, a_followers, b_followers):
    '''Take a user's guess and the follower counts and return if they got it right or not'''
    if a_followers > b_followers  :
        return guess == "a"
    else:
        return guess == "b"

game_should_continue=True
print(logo)
score=0
account_b=random.choice(data)
while game_should_continue:
    account_a=account_b
    account_b=random.choice(data)
    while True:
        if account_a==account_b:
            account_b=random.choice(data)
        else:
            break

    print(f"Compare A: {format_data(account_a)} .")
    print(vs)
    print(f"Against B: {format_data(account_b)} .")

    guess= input("Who has more followers? Type 'A' or 'B' : ").lower()

    print("\n"*20)
    print(logo)

    a_follower_count= account_a["follower_count"]
    b_follower_count= account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score+=1
        print(f"You.re right! Current score {score}")
    else:
        print(f"Sorry, You're wrong, you're final score is {score}")
        game_should_continue=False