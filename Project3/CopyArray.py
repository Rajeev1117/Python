from numpy import *
arr1 = array([2,6,8,1,3])
""" if we didn't use .view() method the address of both the array will same
so create two differnt array we can use .view() method
this is a shallow copy it means if we change the value of arr1 after assigning arr2 so the changes will
shows also in arr2  """

""" if we use .copy() method it means it was a deep copy so it means if we change the 
value of arr1 after assigning arr2 so the changes will occur only in arr1 not in arr2 """

arr2 = arr1.view()
arr1[2]=7

print(arr1)
print(arr2)

# for print the address
print(id(arr1))
print(id(arr2))
