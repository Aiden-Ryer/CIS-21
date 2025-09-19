'''
number = 1
while number <= 10:
    print(number)
    number += 1

for number in range(1, 10+1):
    print(number)

number = 2
while number <= 10:
    print(number)
    number += 2
print( )
print( )
for number in range(1,11):
    if number % 2 == 0:
        print(number)
print()
print()
for number in range(2,11,2):
    print(number)
'''
'''
#1
high = int(input("Give me a maximum number: "))
for number in range(5, high, 2):
    print(number)
'''
'''
#2
total = 0
number = int(input("Enter a number, enter q when you are complete: "))
while number != 'q':
    total += number
    print(total)
    number = int(input("Enter a number, enter q when you are complete: "))
    '''
x = 123
for number in x:
    print(number)