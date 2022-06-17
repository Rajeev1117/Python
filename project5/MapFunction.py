#SYNTAX: map(function, iterables)

def function(a):
    return a*a
x = map(function, (1,2,3,4))  #x is the map object
print(x)
print(set(x))

#the rounded values for each item present in the list. We will make use of round() as the function to map().
my_list = [2.6743,3.63526,4.2325,5.9687967,6.3265,7.6988,8.232,9.6907]
updated_list = map(round, my_list)
print(updated_list)
print(list(updated_list))


#using map function with tuples to change the letter in uppercase
def myMapFunc(n):
    return n.upper()

my_tuple = ('php','java','python','c++','c')

updated_list = map(myMapFunc, my_tuple)
print(updated_list)
print(list(updated_list))