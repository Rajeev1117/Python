#This function like map(), can take user-defined functions and lambda functions as parameters.

def func(x):
    if x>=3:
        return x
y = filter(func, (1,2,3,4))     #filter (function, iterables)
print(y)
print(list(y))


"""
#Lambda within filter() functions
#The condition to be checked is defined by the lambda function that is provided as an argument.
y = filter(lambda x: (x>=3), (1,2,3,4,5,6,7,8))
print(list(y))
"""



#for getting vowels
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'p', 's', 'u']

# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)