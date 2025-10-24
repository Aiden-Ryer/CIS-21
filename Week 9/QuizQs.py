#1
'''
from random import randint

def heads_or_tails(guess):
    value = randint(0, 1)
    if guess == "heads" :
        guess = 1
    elif guess == "tails":
        guess = 0
    if value == guess:
        print("Correct!")
    else:
        print("Incorrect")
user_guess = input("heads or tails: ")
heads_or_tails(user_guess)  
'''
#15
def is_odd(numbers):
    odds = []
    for nums in numbers:
        if nums % 2 != 0:
            odds.append(nums)
    return odds

def is_neg(numbers):
    negs = []
    for nums in numbers:
        if nums < 0:
            negs.append(nums)
    return negs

def report_odd_negatives(numbers):
    odds = is_odd(numbers)
    negs = is_neg(odds)
    return negs
numbers = [-1, 2, -3, -4, 5, 17]
print(report_odd_negatives(numbers))
