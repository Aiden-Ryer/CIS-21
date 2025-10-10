#1
'''
def is_isogram(word):
    word = word.lower()
    return len(set(word)) == len(word)
user_word = input("Enter a word: ")
print(is_isogram(user_word))
'''
#2
def find_unique(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        if count == 1:
            return num
user_num = int(input("Enter a list of numbers: "))
print(find_unique(user_num))