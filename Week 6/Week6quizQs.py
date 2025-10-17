# 1
# Write a function that loops through a word and returns a list 
# with every other letter of the word starting with the first letter
# The function will take a single argument (word)
# Ex. skip_letter("counterattack") -> ["c","u","t","r","t","a","c"]
# Ex. skip_letter("banana sunday") -> ["b","n","n","s","n","a"]

# Code
'''
user_word = input("Enter a word: ")
def skip_letter(word):
    result = []
    for i in range(0, len(word), 2):
        result.append(word[i])
    return result

print(skip_letter(user_word))

#2
# Same thing but second letter

user_word = input("Enter a word: ")
def skip_letter(word):
    result = []
    for i in range(1, len(word), 2):
        result.append(word[i])
    return result

print(skip_letter(user_word))
'''
#3
#Write a function that loops through and returns a list with every even number between two integers
#(inclusive). The arguments to the function will be smaller num and larger num.
#Examples:
# output even(37, 1050) → [38, 40, 42, . . . 1048, 1050],
# output even(1, 2000) → [2, 4, 6, . . . 1998, 2000],
# output even(50, 199) → [50, 52, 54, . . . 196, 198]
'''
starting_num = int(input("Give me a number: "))
ending_num = int(input("Give me a larger second number: "))

def even_num(num1, num2):
    even = []
    for i in range(starting_num, ending_num + 1):
        if i % 2 == 0:
            even.append(i)
    return even
print(even_num(starting_num, ending_num))
'''
#4
# Same as 3 but odd numbers
'''
starting_num = int(input("Enter a number: "))
ending_num = int(input("Enter a larger second number: "))

def odd_num(num1, num2):
    odd = []
    for i in range(starting_num, ending_num + 1):
        if i % 2 == 1:
            odd.append(i)
    return odd
print(odd_num(starting_num, ending_num))
'''
#5
'''
user_num = int(input("Give me a positive number: "))
def hailstone_seq(user_num):
    seq = [user_num]
    while user_num != 1:
        if user_num % 2 == 0:
            user_num = user_num // 2
        else:
            user_num = (user_num * 3) + 1
        seq.append(user_num)
    return seq
print(hailstone_seq(user_num))
'''
#6 Find Factors in a list
def find_factors(nums):
    
