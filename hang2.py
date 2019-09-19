#!/usr/bin/env python3
import sys
import random

if len(sys.argv) != 2:
    word_list = './test.txt'
else:
    word_list = sys.argv[1]

numguesses = 0
word_file = open(word_list)
choword = word_file.readlines()
word = random.choice(choword)
wordl = len(word)

print("Let's play a game of hangman your word is " + str(wordl) + " letter's long guess a letter!")
print("_" * wordl)
word_guess = input("-> ")

while numguesses < 8:
    
    if word_guess in word:
        print(word_guess)
        word_guess = input("--> ")

    else:
        print("_")
        numguesses += 1
        word_guess = input("--> ")
print("you lose")