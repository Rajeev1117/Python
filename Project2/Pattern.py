# first pattern
####
####
####
####

"""
for i in range(4):      #if i=0  print four # same i=1 print four #
    for j in range(4):
        print("# ", end="")

    print()
"""

# second pattern
#
##
###
####
"""
for i in range(4):   #if the value of i=0 it will print one # same i=1 print two #
    for j in range(i+1):
        print("# ", end="")

    print()
"""

#Third Pattern
####
###
##
#

for i in range(4):
    for j in range(4-i):
        print("# ", end="")

    print()