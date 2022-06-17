# for loop- we can execute a set of statement, once for each item in a tuple ,list and set etc.
"""
x=[1,2,3,4,5]
for i in x:
    print(i)
"""
"""
for i in range(10):
     print(i)
"""
"""
for i in range(2,10,2):  # 2 is the differnce
    print(i)
"""
#using break statement
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
"""
#Using continue statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#Inside for using if and else statement
for x in range(6):
  if x == 5: break
  print(x)
else:
  print("Finally finished!")