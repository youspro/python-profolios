
print("Welcome to my computer number guessing game.\nYo)

number = input("Type down a number: ")
guesses = 0
lives = 5
if number.isdigit():
    number = int(number)
else:
    print("Please type down a number next time.")
    quit()

random_number = random.randint(0, number)


while lives != 0:
    guesses += 1
    lives -= 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print(f"Good job you got it.\nYou had {lives} lives left and you made {guesses} guesses")
            break
        elif user_guess > random_number:
            print(f"That is higher than the number.\nYou have {lives} lives left")
        else:
            print(f"That is lower than the number.\nYou have {lives} lives left")
    else:
        print("Please type down a number next time.")
        break
