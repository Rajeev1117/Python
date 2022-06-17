from array import *

arr = array('i', [])  # i means the array is integer

n = int(input("Enter the length of the array: "))

for i in range(n):  # this i is range like 0 1 2 3
    x = int(input("Enter the next Value: "))
    arr.append(x)

print(arr)

# Now Search value from array and print its index number

val = int(input("Enter the value for Search: "))
k = 0          # for print the index value
for e in arr:  # this e is value like 11 12 13 14
    if e == val:
        print(k)
        break
    k += 1
# We have a another method to print index value
# print(arr.index(val))    when we write this so it will also print the index value
else:
    print("not found in the array")
