# high-low.py: a simple guess the number game
import random

name = input("what is your name: ")

secret = random.randint(1, 500)  # 100
count = 0
while True:
    count += 1
    s = input(f"{name}, Guess #{count} Enter your guess (1-100): ")
    if s == "quit":
        break
    guess = int(s)
    if guess == secret:
        print(f"{name}, Correct! That's the right number.")
        break
    elif guess < secret:
        print(f"{name}, Your guess is too low.")
    elif guess > secret:
        print(f"{name}, Your guess is too high.")
    if abs(secret - guess) <= 10:
        print(f"{name}, You are getting close.")

print(f"{name}, game over")
