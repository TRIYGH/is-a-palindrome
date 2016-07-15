#W1D4 Hangman   235,886

import time
import random

word_list = []
alive = True

with open('/usr/share/dict/words','r') as f:
    for line in f:
        word_list.append(line)


easy_words = []
normal_words = []
hard_words = []
game_list = []

for each in word_list:
    if len(each) > 4 and len(each) < 8:
        easy_words.append(each)
for each in word_list:
    if len(each) > 6 and len(each) < 10:
        normal_words.append(each)
for each in word_list:
    if len(each) > 8:
        hard_words.append(each)


def word_difficulty():
    entry = input("Select difficulty level: (E)asy, (N)ormal, (H)ard:  ").lower()
    if entry == 'e':
        return easy_words
    elif entry == 'n':
        return normal_words
    elif entry == 'h':
        return hard_words


def get_myst_word(game_list):
    x = len(game_list)
    y = random.randint(1,x)
    return game_list[y]


def display_board(guesses_left):
    print("\n"*50)
    print(myst_word)
    print("\t",end='')
    for each in letters_to_display:
        print(each,end='')
    print("\n")

    print("\t",end='')
    for each in mwl:
        print("_ ",end='')
    print("\t\t*** You have {} guesses left. ***".format(guesses_left))
    print("\n\n")
    return


def get_guess():
    while True:
        entry = input("\n Guess a letter: ").lower()
        if entry not in all_guesses:
            all_guesses.append(entry)
            return entry
        print("You already guessed that letter  -  try again\n")


def check_guess(g):
    position_of_corr = []
    for index, each in enumerate(mwl):
        if each == g:
            position_of_corr.append(index)
    return position_of_corr


def change_display_letters(guess):
    for each in position_of_corr:
        pos = each * 2
        letters_to_display.insert(pos,guess)
        letters_to_display.pop(pos+1)


def did_you_win():
    for each in letters_to_display:
        if each == "#":
            win = False
            return win
    win = True
    return win


def end(winner):
    if winner:
        print("\n"*50)
        print("*"*60)
        print("\t\t       YOU WON !!!!!")
        print("*"*60)
        print("\n\n\n\n\n")
    else:
        print("\n"*50)
        print("-"*40)
        print("\t   Sorry, you lost")
        print("-"*40)
        print("\n\n")


#========================================================================

print("\n"*50)
print("#"*40)
print("\t   WELCOME TO HANGMAN")
print("#"*40)
print("\n\n")

game_list = word_difficulty()

myst_word = get_myst_word(game_list)
myst_word = myst_word.lower()
print(myst_word)
mwl = list(myst_word)
mwl.pop()
letters_to_display = []
for each in mwl:
    letters_to_display.append('#')
    letters_to_display.append(' ')
all_guesses = []
position_of_corr = []
guesses_left = 8
extra_guess = False

while alive:

    display_board(guesses_left)

    guess = get_guess()

    position_of_corr = check_guess(guess)

    change_display_letters(guess)

    winner = did_you_win()
    if winner:
        break

    if position_of_corr == []:
        guesses_left -= 1

    if guesses_left <= 0:
        alive = False

end(winner)
