# Created by Aiden Ryer
'''
#3
light_color = input("Enter the color; red, green, or yellow: ")
if light_color == "green":
    print("GO!")
elif light_color == "red":
    print("stop!")
elif light_color == "yellow":
    print("yield")
else:
    print("error")

#4
age = int(input("Enter your age: "))
athleticism = input("Is your athleticism above average or below average? ")
if age >= 20 and age < 40:
    if athleticism == "above average":
        print("Resting heartrate is 47-72.")
    else:
        print("Resting heartrate is 73-93.")
if age >= 40 and age < 60:
    if athleticism == "above average":
        print("Resting heartrate is 46-71.")
    else:
        print("Resting heratrate is 72-94")
else:
    if athleticism == "above average":
        print("Resting heartrate is 45-70.")
    else:
        print("Resting heartrate is 71-94.")
'''
'''
#5
int1 = int(input("Enter first number: "))
int2 = int(input("Enter second number: "))
int3 = int(input("Enter third number: "))
nums = [int1, int2, int3]
if int1 <= int2 <= int3:
    print(int1, int2, int3)
elif int1 >= int2 >= int3:
    print(int3, int2, int1)
elif int1 <= int3 <= int2:
    print(int1, int3, int2)
elif int3 <= int1 <= int2:
    print(int3, int1, int2)
elif int2 <= int1 < int3:
    print(int2, int1, int3)
elif int2 <= int3 <= int1:
    print(int2, int3, int1)
'''