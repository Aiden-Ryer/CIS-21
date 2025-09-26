import math
'''
#1
larger = int(input("pick a large number: "))
smaller = int(input("pick a smaller number: "))
counter = 0
while larger/2 > smaller:
    counter += 1
    larger /= 2
print(counter)
'''
'''
#2
user_word = input("Enter a word: ")
for i in range(1, len(user_word), 2):
    print(user_word[i],end="")

#3
for i in range(38, 1051, 2):
    print(i)
#4
letter = ""
word = ""
while letter != "done":
    word += letter
    letter = input("Enter a letter: ")
print(word)
#5
sum = 0
for i in range(51, 518, 2):
    sum += i
print(sum)

#6
number = 0
sum = 0
while number >= 0:
    sum += number
    number = int(input("Enter a number: "))
print(sum)

#7
n = 25
while n!=1:
    if n%2==0:
        int(print(n))
        n=n/2
        -
    else:
        int(print(n))
        n=3*n+1
'''