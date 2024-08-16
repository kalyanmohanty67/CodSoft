#Task : Python program Rock-Paper-Scissor Game.

import random

def play(r , p , s):
    print(f"Let's play {r}, {p} ,{s}")
    tie = 0
    r_count = 0
    p_count = 0
    s_count = 0
    choices = (r , p , s)

    user_choice =input(f"Enter a choice {r} ,{p} ,{s}: ").capitalize()
    if user_choice not in choices:
        print("Invalid choice")
        return play(r , p , s)
    
    computer_choice = random.choice(choices)
    print(f"\n You: {user_choice}, Computer: {computer_choice}.\n")

    if user_choice == computer_choice:
        print(" It's a tie!")

    elif (
        (user_choice == r and computer_choice == p) or
        (user_choice == p and computer_choice == s) or
        (user_choice == s and computer_choice == r)
    ):
        print("You Win!!")
    else:
        print("Computer Win!!")


r ="Rock"
p = "Paper"
s = "Scissors"
play(r , p , s)
        