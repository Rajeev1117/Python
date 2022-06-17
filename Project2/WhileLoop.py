# While, Break and Continue Statement
# While loop- we can execute a set of statements as long as a condition is true.

"""
i = 1

while i <= 5:
    print(i)
    i += 1
"""

#using while loop inside the while loop

i=1
while i<=5:
    print("Rajeev",end="")
    j=1
    while j<=4:
        print(" Kumar",end="")
        j+=1
    i+=1
    print()

# break Statement- we can stop the loop the loop even if while condition is true
"""
i=1
while i<=5:
    print(i)
    if i==3:
        break
    i+=1
"""
# Continue Statement- we can stop the current iteration and continue with the next
"""
i=0
while i<=5:
    i+=1
    if i==3:
        continue
    print(i)
"""