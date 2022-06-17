
a=5   #101
b=6   #110

# using of 3rd variable
# temp=a
# a=b
# b=temp

#without using of third variable
# in this method we still wasting 1bit so we didn't use this method
#a=a+b   #11  but it takes 4 bit so we still wasting 1 bit
#b=a-b   #5
#a=a-b   #6

#another method by using xor
#a=a^b
#b=a^b
#a=a^b

#simple way is swaps the two top most stack items
a,b=b,a

print(a)
print(b)