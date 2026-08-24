# A simple hangman game which can be played directly in terminal.
# The words are randomly pulled from an url source in word_generator.py
# The word source url does also contain weird words like 'aaa'. 
# At the moment I count it as higher difficulty lol
# The hangman drawings a stored in the file visuals.py

from word_generator import hangman_word, random_word
from visuals import hangman_pics

# Starting intro
print('Let\'s play hangman!\n\nWe\'re looking for a random word with a random amount of letters.\n')

start_game = input('\nDo you want to start? (y or n) ')

game_won = False

# if statement to check if the player wants to start the game or not
# By input 'y' the programm sets up different variables for the game functionality 
if start_game == 'y':
    word_unsolved = True
    hangman_counter = 0
    print(f'\n{hangman_pics[0]}')
    blank_word = []
    for i in hangman_word:
        blank_word.append('_')
    print('\n' + ' '.join(blank_word))
elif start_game == 'n':
    print('Okay, maybe next time.')
    word_unsolved = False
else:
    print('Wrong input, please restart game.')
    word_unsolved = False

# To find multiple occurences of the same letter. Source for the function: https://datagy.io/python-list-find-all-index/
def find_indices(list_to_check, item_to_find):
    return [idx for idx, value in enumerate(list_to_check) if value == item_to_find]

# Primary gameplay loop. The player can input letters to solve the unknown word until:
# a) the word is successfully solved = win
# b) the hangman drawing is complete, which happens after six wrong inputs are put in = loose
while word_unsolved and hangman_counter < 6:
    input_letter = input('\nEnter letter: ')
    try:
        input_letter = input_letter.upper()
    except ValueError:
        pass
    letter_indices = find_indices(hangman_word, input_letter)
    if input_letter in hangman_word:
        for i in letter_indices:
            blank_word[i] = input_letter
    else:
        hangman_counter = hangman_counter + 1
        print(f'\n{hangman_pics[hangman_counter]}')
        print('\nWrong letter! Try again.')
    print('\n' + ' '.join(blank_word))
    for i in blank_word:
        if '_' not in blank_word:
            word_unsolved = False
            game_won = True
        else:
            None

# Final check to resolve the game result and give a message wether the player has won or lost
# In both cases the random word is also printed in the terminal
if game_won == True:
    print(f'\nCorrect! The word was: {random_word}')
elif game_won == False and start_game != 'y':
    None
else:
    print(f'\nSorry, that wasn\'t correct. The word was: {random_word}')