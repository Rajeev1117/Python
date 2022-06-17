from functools import reduce

# SYNTAX: reduce(function, iterables)

#calculate the sum of two numbers
nums = [1, 2, 3, 4]
ans = reduce(lambda x, y: x + y, nums)
print(ans)

#calculate the multiplication of two numbers
def product(x,y):
    return x*y

ans = reduce(product, [2, 5, 3, 7])
print(ans)


#calculate the sum of the elements of the list
def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)
