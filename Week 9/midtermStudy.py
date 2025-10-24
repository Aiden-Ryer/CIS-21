#1 print the second letter of every word
#Ex. "banana sunday" = a, a, a, s, n, a
'''
def skip_letter(word):
    letters = []
    for i in range(1, len(word), 2):
        letters.append(word[i])
    return letters
print(skip_letter("banana sunday"))
'''

#2 count cards
'''
def count(cards):
    count = 0
    high_cards = ["10", "j", "q", "k", "a"]
    low_cards = [2, 3, 4, 5, 6]
    for card in cards:
        if card in low_cards:
            count += 1
        elif card in high_cards:
            count -= 1
        else:
            count = count
    return count
cards = ["a", 2, 4, "j", "q"] #-1
print(count(cards))
'''
#3 last letters in words
'''
def last_letter(words):
    letters = ""
    index = 0
    for i in words:
        if i == " ":
            letters += words[index - 1]
            index += 1
        else:
            index += 1
    letters += words[index - 1]
    return letters
print(last_letter("wingardium leviosa makes objects float"))
'''


#1 again
'''
def skip_letter(word):
    letters = []
    for letter in range(1, len(word), 2):
        letters.append(word[letter])
    return letters
print(skip_letter("retardinator")) #e, a, d, n, t, r
'''
#2 again
'''
def count_cards(cards):
    count = 0
    low_cards = [2, 3, 4, 5, 6]
    high_cards = [10, "j", "q", "k", "a"]
    for card in cards:
        if card in low_cards:
            count += 1
        elif card in high_cards:
            count -= 1
        else:
            count = count
    return count
cards = [2, 4, "j", "k", 4, 4, 9, 8]
print(count_cards(cards))
'''

#3 again
'''
def last_letters(words):
    letters = ""
    index = 0
    for letter in words:
        if letter == ' ':
            letters += (words[index - 1])
            index += 1
        else:
            index += 1
    letters += (words[index -1])
    return letters
words = ("Calvin has a super duper tiny penis")
print(last_letters(words))
'''