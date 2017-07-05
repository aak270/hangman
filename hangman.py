"""
    This is an hangman game program for the final project
"""
import random
import string
import sys

print('Welcome to a guess word game, hangman!!!')
print('This is an animal hangman, which means you will guess an animal name.')
print('Hope you enjoy^^')
print()

#Put words in the txt to a list
animals = open('animals_list.txt','r')
for words in animals:
    words_list = words.split(',')
animals.close()

#Game code
while True:
    #Main body
    hp = 6
    word = random.choice(words_list)
    guessed_word = '*'*len(word)
    letter_in = ''
    while hp > 0:
        print('HP:',hp)
        print(guessed_word)
        letter = input('Enter a letter: ')
        while letter not in string.ascii_letters and letter is not ' ' or len(letter)>1:
            print('I don\'t understand, please enter a letter!')
            letter = input('Enter a letter: ')
        letter_in += letter
        print('\nLetters already used:',letter_in.upper())
        if letter.upper() in word:
            guessed_word = list(guessed_word)
            for i in range(len(word)):
                if word[i] == letter.upper():
                    guessed_word[i] = letter.upper()
            guessed_word = ''.join(guessed_word)
        else:
            hp -= 1
        if guessed_word == word:
            break
    #Lose clause
    else:
        print()
        print('YOU LOSE!!!')
        print("The word is '{}'".format(word))
    #Win clause
    if guessed_word == word:
        print()
        print('HP:',hp)
        print(guessed_word)
        print('Congratulations you WIN!!!')
    #Restart clause
    print()
    print('Do you want to play again?')
    while True:
        answer = input('Enter(Yes/No): ')
        if answer.upper() == 'YES':
            print()
            break
        elif answer.upper() == 'NO':
            sys.exit()
        else:
            print('I don\'t understand, please answer yes or no!')
