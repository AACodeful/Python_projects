import random

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2,", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)   #or put range of random number in range( , )
# number = random.random()   #for Floats
# option = random.choice(options) #to randomly pick from tuple
# random.shuffle(cards) # randomly shuffles deck
# print(number)
# print(options)
# print(cards)

# Number guessing game

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between {low} - {high}: "))
    guesses += 1
    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        if guess == number:
            print(f"Congrats!!! {guess} was the correct answer!!!")
            break
print(f"This round took you {guesses} guesses!")
