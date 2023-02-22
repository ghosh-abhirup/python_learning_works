from hangman_words import word_list

from hangman_art import stages, logo

import random

print(logo)

word = random.choice(word_list)  # random word choice
print(word)

# list of spaces
word_list = []
for _ in range(len(word)):
    word_list += "_"

print(word_list)

end_of_game = 7

while end_of_game>0:
    # guessing a letter
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for pos in range(len(word)):
            letter = word[pos]
            if letter == guess:
                word_list[pos] = guess
        print(' '.join(word_list))
    else:
        end_of_game-=1
        print(stages[end_of_game])

        if end_of_game==0:
            print("You lose")

    if "_" not in word_list:
        end_of_game = 0
        print("You win")
