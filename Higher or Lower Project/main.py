from art import logo, vs
from game_data import data
import random

data_a = 0
data_b = 0
score = 0
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
game_data = data
def compare_a():
    data_a = random.choice(game_data)
    print(f"Compare A: {data_a['name']}, {data_a['description']}, {data_a['country']}")
compare_a()
print(vs)

def compare_b():
    data_b = random.choice(game_data)
    print(f"Against B: {data_b['name']}, {data_b['description']}, {data_b['country']}")
compare_b()

guess= input("Who has more followers? Type 'A' or 'B': ").lower()

a_follower_count = data_a['followers_count']
b_follower_count = data_b['followers_count']

is_correct = check_answer(guess, a_follower_count, b_follower_count)
if is_correct:
    score += 1
    print(f"you're right!current score {score}")
else:
    print(f"you are wrong!final score{score}")

