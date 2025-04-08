import random

lowest_num = 1
highest_num = 100
is_running = True
guesses = 0

answer = random.randint(lowest_num, highest_num)

print("Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")
    guesses += 1
    if guess.isdigit():
        guess = int(guess)
        if guess < lowest_num or guess > highest_num:
            print("Guess is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Your guess is too low! Try again!")
        elif guess > answer:
            print("Your guess is too high! Try again!")
        else:
            print("CORRECT!")
            print(f"The number of guesses is {guesses}!")
            is_running = False
    else:
        print("Invalid input")
        print(f"Select a number between {lowest_num} and {highest_num}")
