'iterator- it is an object that contains a countable number of values'

'Return an iterator from a tuple, and print each value'
# mytuple = ("Rajeev", "Aakash", "Sunil")
# myit = iter(mytuple)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))

'Strings are also iterable objects, containing a sequence of characters'
# mystr = "Rajeev"
# myit = iter(mystr)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration


values = TopTen()

print(next(values))

# print(values.__next__())
# print(values.__next__())

for i in values:
    print(i)


