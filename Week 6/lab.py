#1
'''
1. An isogram is a word that has no duplicate letters. Write a function that takes a string word and
returns either True or False depending on whether or not it’s an isogram.
Examples:
 is isogram(” algorism”) → True
 is isogram(” password”) → False
 is isogram(” consecutive”) → False
'''
#Code
'''
def is_isogram(word):
    word = word.lower()
    return len(word) == len(set(word))
'''
#2
'''
In each input list, every number repeats at least once, except for one. Write a function that takes an
array numbers and returns the single unique number.
Examples:
 find unique([1, 2, 2, 3, 3, 4, 4]) → 1,
 find unique([7, 8, 8, 9, 9, 10, 10]) → 7,
 find unique([5, 6, 6, 7, 7, 8, 8, 5, 9]) → 9
'''
#code
'''
def find_unique(numbers):
    number_dict = {}
    for number in numbers:
        if number not in number_dict:
            number_dict[number] = 1
        else:
            number_dict[number] += 1

        if number_dict[number] == 1:
            return number_dict[number]
print(find_unique([1, 2, 2, 3, 3, 4, 4]))
'''
#3
'''
In each input list, every number repeats at least once, except for two. Write a function that takes an
array numbers and returns the two unique numbers.
Examples:
 return unique([1, 9, 8, 8, 7, 6, 1, 6]) → [9, 7],
 return unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) → [2, 1],
 return unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) → [5, 6
'''
#code
def find_unique(numbers):
    number_dict = {}
    lyst = []
    for number in numbers:
        if number not in number_dict:
            number_dict[number] = 1
        else:
            number_dict[number] += 1
        if number_dict[number] == 1:
            lyst.append(number)
    return lyst
print(find_unique([1, 9, 8, 8, 7, 6, 1, 6]))








#6 Find number of repeated letters
'''
def repeat_letters(word):
    letter_dict = {}
    for letter in word:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict
user_word = input("Enter a word with repeating letters: ")
print(repeat_letters(user_word))
'''
