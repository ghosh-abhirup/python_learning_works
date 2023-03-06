import random


def compareNum(num1, num2):
    if num1 > num2:
        print("Too high.")
        print("Guess again.")
        return False
    elif num1 < num2:
        print("Too low.")
        print("Guess again.")
        return False
    else:
        print(f"You got it. The number was {num1}.")
        return True


print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempt = 10
else:
    attempt = 5

while attempt > 0:
    print(f"You have {attempt} attempt remaining to guess the number")
    guess = int(input("Make a guess. "))
    res = compareNum(guess, number)
    if res:
        attempt = 0
    else:
        attempt -= 1
