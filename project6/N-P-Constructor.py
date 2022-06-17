#When we declare a constructor
class NPConstructor:
    num = 101

    # non-parameterized constructor
    def __init__(self):
        self.num = 999

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
obj = NPConstructor()

# calling the instance method using the object obj
obj.read_number()

#In this case, python does not create a constructor in our program.

