#1
'''
def is_isogram(word):
    word = word.lower()
    return len(set(word)) == len(word)
user_word = input("Enter a word: ")
print(is_isogram(user_word))
'''
#2
'''
def find_unique(numbers):
    for i in range(len(numbers)):
        is_unique = True
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                is_unique = False
                break
        if is_unique:
            return numbers[i]
user_numbers = input("Enter a list of repeating numbers with 1 unique number: ")
print(find_unique(user_numbers))
'''
#3
'''
def find_two_unique_numbers(numbers):
    unique_numbers = []

    # We want to find two numbers that appear only once
    for _ in range(2):
        for i in range(len(numbers)):
            num = numbers[i]
            # Assume this number is unique
            is_unique = True
            # Compare with every other number
            for j in range(len(numbers)):
                if i != j and numbers[j] == num:
                    # Found a duplicate, so it's not unique
                    is_unique = False
                    break
            # If still unique after checking all others
            if is_unique:
                unique_numbers.append(num)
                # Remove all copies of this number
                new_list = []
                for n in numbers:
                    if n != num:
                        new_list.append(n)
                numbers = new_list
                break  # Move on to find the next unique number
    return unique_numbers
user_numbers = input("Enter a list of repeating numbers with 2 unique numbers: ")
print(find_two_unique_numbers(user_numbers))
'''
#4
'''
def get_names(names):
    names_list = []
    for key in names:
        names_list.append(names[key])
    return names_list
print(get_names({"01234" : "Steve", "2345" : "Aiden", "13234": "Krish"}))
'''
#5
'''
def find_oldest(people):
    oldest_name = ""
    oldest_age = -1
    for name in people:
        age = people[name]
        if age > oldest_age:
            oldest_age = age
            oldest_name = name
    return oldest_name
people = {"Aiden" : 18, "Krish" : 20, "Calvin" : 19}
print(find_oldest(people))
'''
#6
'''
def letter_count(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts
print(letter_count("retardinator"))
'''
#7
'''
def min_grade(exams):
    class_name = ''
    class_grade = 101
    for classes in exams:
        grade = exams[classes]
        if grade < class_grade:
             class_grade = grade
             class_name = classes
    return class_name
exams = {"Chem" : 99, "Math" : 89, "Bio" : 92}
print(min_grade(exams))
'''
#9
'''
def total_cost(reciept):
    cost = 0
    for item in reciept:
        cost += reciept[item]
    return cost
reciept = {"apple" : 4, "banana" : 2, "orange" : 7}
print(total_cost(reciept))
'''
'''
def item_cost(items):
    for item in items:
        print(item, items[item])
items= {"apple" : 4, "banana" : 2, "orange" : 7}
item_cost(items)
'''
#18
'''
def majority_element(numbers):
    counts = {}
    for num in numbers:
        num = str(num)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    for num in counts:
    

numbers = [2, 2, 2, 3, 1, 1]
print(majority_element(numbers))
'''




    