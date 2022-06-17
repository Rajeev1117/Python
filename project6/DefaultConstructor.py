#When we do not declare a constructor

class DefaultConstructor:
    num = 101

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
obj = DefaultConstructor()

# calling the instance method using the object obj
obj.read_number()

#we do not have a constructor but still we are able to create an object for the class.
# This is because there is a default constructor