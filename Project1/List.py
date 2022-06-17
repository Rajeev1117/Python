# index value of a is like 0,1,2,3,4
a = [25, 12, 36, 95, 14]
# both are print the same value
print(a[-1])
print(a[4])

# in list we perform some operations by using certain method
# append= add element at the ends & takes only one argument at a time

a.append(45)
print(a)

#Insert= insert element with specifying the index value
a.insert(2,77)  #2 is the index no.
print(a)

#pop= which index value we will remove & if we not passed any value inside pop so it will remove the last value
a.pop(1)
print(a)

#remove= remove the values
a.remove(14)
print(a)

#delete= delete the value with specifying the index value
del a[2:]    #delete value from index 2 to end
print(a)

#extend= use for extend the values
a.extend([29,12,14])
print(a)
