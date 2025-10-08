'''
days_of_the_week =  ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

#workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#a tuple is an immuatable list, (data, data, data) not [data, data, data]
workdays = list(days_of_the_week[0:5])
workdays.append('Saturday')

print(workdays)

#print(days_of_the_week[2])
#days_of_the_week[2] = 'Wacky Wednesday'     #Causes an Error because it's immutable because the lyst uses parenthesis
# #print(days_of_the_week)    



#print(lyst)
#lyst.append('Saturday')
#lyst.append('Sunday')
#print(lyst)

print(lyst)
lyst[2] = 'Wacky Wednesday'
print(lyst)

word = 'apfle'
print(word)
word[2] = 'p' # does not work, cannot change internal of a string (immutable)
print(word)     # only works with lysts (mutable)

x = 'apple'
y = x
print(x)
print(y)
x += 's'
print(x)
print(y)

x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
y = x
print(x)
print(y)

x[4] = 'Funday'
print(x)
print(y)
'''
my_word = 'Peter Piper picked a peck of pickled peppers'
result = ['Peter', 'Piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']
words = ""
def string_to_list(word):
    words = []
    found_word = ""
    for letter in word:
        if letter == " ":
            words.append(found_word)
            found_word = ""
        else:
            found_word += letter
    words.append(found_word)
    return words
print(string_to_list(my_word))