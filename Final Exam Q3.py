# This Python program is designed to help users memorize a set of random words, and then test their recall ability by asking them to input the words they remember.
# It shows basic usage of lists, user input handling, and random word selection. The coder's intention is to create a simple word recall game. 
# This is question 3/3 of the final exam.

import random

allwords = ['apple', 'banana', 'cherry', 'dog', 'elephant', 'fox', 'giraffe', 'house', 'igloo', 'jacket']
mem_words = []
memorize = int(input('How many words do you want to memorize?: '))
for element in range(1,memorize+1):
    rand_words = random.choice(allwords)
    mem_words.append(rand_words)
print('Memorize these words:',mem_words)
enter = input('(Press Enter to continue...)')
for spaces in range(1,11):
    print()
num = 0
words_rem = input('What words do you remember?: ')
words_rem_split = words_rem.split()
for element in mem_words:
    if element in words_rem_split:
        num += 1
print('You remembered',num,'words correctly.')
