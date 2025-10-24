#1
from random import randint
'''
value = randint(0,1)
def heads_or_tails (guess):
    if guess == value:
        return "Correct!"
    else:
        return "Incorrect!"
user_guess = int(input("Guess heads or tails, heads = 1, tails = 0: "))
print(heads_or_tails(user_guess))
'''

#2
'''
def odd_even(guess):
    value = randint(0,9)
    value %= 2
    value_guess = ""
    if value != 0:
        value_guess = "odd"
    else:
        value_guess = "even"
    if guess == value_guess:
        return "Correct!"
    else:
        return "Incorrect!"
user_guess = input("odd or even: ")
print(odd_even(user_guess))
'''
#3
def count_duplicates(num1, num2, num3):
    duplicates = 0
    if num1 == num2:
        duplicates = 2
    if num1 == num3:
        duplicates = 2
    if num2 == num3:
        duplicates = 2
    if num1 == num2 == num3:
        duplicates = 3
    if duplicates == 0:
        return "Each number is unique"
    else:
        return "there are "f'{duplicates}'" of the same number"
user_num1 = int(input("Enter a number: "))
user_num2 = int(input("Enter a number: "))
user_num3 = int(input("Enter a number: "))
print(count_duplicates(user_num1, user_num2, user_num3))
