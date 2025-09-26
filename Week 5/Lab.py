import math
#Functions
#1
#user_base = float(input("Enter the base of the pyramid: "))
#user_height = float(input("Enter the height of the pyramid: "))
def pyramid_volume(base, height):
    volume = ((base ** 2) * (height)) / 3
    print(volume)
 # pyramid_volume(user_base, user_height)

#2
#user_base = float(input("Enter the base of the cone: "))
#user_height = float(input("Enter the height: "))
def cone_volume(base, height):
    volume = math.pi * (((base ** 2) * (height)) / 3)
    print(volume)
#pyramid_volume(user_base, user_height)

#11
def convert_knuts(knuts):
    output = ""
    #29 knuts per sickle
    #17 sickles per galleon
    knuts
#Strings
#2
#input_temp = input("What is the temperature of the person? ")
def is_fever(input_temp):
    #How to extract F or C
    #How to extract the temp
    #If > 98.6 F = fever
    #If > 37 C = fever
    degree = input_temp[-1]
    temp = input_temp[:-1]
    if degree == "F" and temp > "98.6":
        print("This person has a fever!")
    elif degree == "C" and temp > "37":
        print("This person has a fever!")
    else:
        print("This person does not have a fever.")

#is_fever(input_temp)

#4
'''
def hamming_distance(word1,word2):
    counter = 0
    if len(word1) != len(word2):
        print("words should be the same length.")
    
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            counter += 1
        return counter
word1 = input("Enter a word: ")
word2 = input("Enter another word: ")
print(f"the hamming distance is {hamming_distance(word1, word2)}")
'''
#8
def last_letters(sentence):
    encode = ""
    for i in range(0, len(sentence)):
        if sentence[i] == ' ':
            encode = encode + sentence[i - 1]
    encode += sentence[-1]
    return encode
sentence = input("Enter a sentence: ")
print(last_letters(sentence))