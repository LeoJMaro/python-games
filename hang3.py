#!/usr/bin/env python3
import sys
import random

if len(sys.argv) != 2:
    word_list = './test.txt'
else:
    word_list = sys.argv[1]

number_guesses = 0
word_file = open(word_list)
choword = word_file.readlines()
word = random.choice(choword)
wordl = len(word)
guesses = []
print("Let's play a game of hangman your word is " + str(wordl) + " letter's long guess a letter!")


while number_guesses < 6:
    word_guess = input("--> ")
    guesses.append(word_guess)
    if word_guess in word:
        print("leter is in the word")
    else:
        print("Wrong guess again")
        number_guesses += 1

    for i in word:
        if i in guesses:   
            print(i, end = "")
        else:
            print('_', end = "")
    if guesses == word:
        print("you win")
        break
        
if number_guesses == 6:
    print(' you lose')