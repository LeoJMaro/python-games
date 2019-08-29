#!/usr/bin/env python3
import random
ranu = random.randrange(1, 100)

guess = int(input("Please guess the number between 1 and 100 -> "))
while guess != ranu:
    if guess > ranu: 
        guess = int(input("Too high, guess again -> "))
    elif guess < ranu:
        guess = int(input("Too low, guess again -> "))
if guess == (ranu):
    print("That's the number!")