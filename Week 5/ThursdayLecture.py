#write a function that takes an int adds two, multiplies by 4, prints the result

def my_fnct(number):
    number += 2
    number *= 4
    return number

result1 = my_fnct(10)
result2 = my_fnct(result1)
 # print(result2)
 # print(my_fnct(my_fnct(10)))

def add_5 (number):
    number += 5
    return number

def times_2 (number):
    number *= 2
    return number

x = times_2(add_5(10))

# write ^2 function to calculate (3^2)^2

def power_2 (number):
   number = number ** 2
   return number

 # print(power_2(power_2(power_2(3))))
result = 5
for i in range(0,10):
    result = times_2(result)
    
 # print(result)
 
def product(num1, num2):
    result = num1 * num2
    return result
# x = product(3,4)
# print(x)

'''
print 'banana' =
lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']
print(lyst[1])

lyst that prints 4, false, and 4.5 =
print(lyst[2], lyst[3], lyst[4])

p in grapes =
print(lyst[5][3])

every element of the lyst one a time =
for element in lyst:
  print(element)

to add an element:
lyst.append('stuff')
print(lyst)
'''
