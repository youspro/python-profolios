import random
print("Welcome to my rock paper scissors game.")

options = ["rock", "paper", "scissors"]

user_wins = 0
computer_wins = 0

while True:
    user_pick = input("Type down rock/paper/scissors or q to quit: ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer chose {computer_pick}.")

    if user_pick == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_pick += 1
    elif user_pick == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost, computer won.")
        computer_wins += 1
print(f"You won {user_wins} times and the computer won {computer_wins} times.")
print("Bye see you next time.")