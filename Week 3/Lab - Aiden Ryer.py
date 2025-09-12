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
'''
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
