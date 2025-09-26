def count_letters():

    word = input("Enter a word: ")
    count = 0
    for letter in (word):
        count += 1
    print(count)

    print("----------")

    for index in range(0, len(word) + 1):
        print(index, word[index])

#code for how many vowels are in a word
#aeiou
# word = input("Enter a word: "). lower()

def count_vowels(word):

    count = 0
    for char in word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "y":
            count += 1
    
    return count

def count_vowels_return(word):
    word1 = 'hello world'
    word2 = 'apples and bananas'
    word3 = 'happy times'

    count_vowels1 = count_vowels(word1)
    count_vowels2 = count_vowels(word2)
    count_vowels3 = count_vowels(word3)

    total_vowel_count = count_vowels1 + count_vowels2 + count_vowels3


