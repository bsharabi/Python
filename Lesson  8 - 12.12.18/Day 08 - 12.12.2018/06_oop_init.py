class Person:

    # __init__ - is a keyword to the class constructor
    def __init__(self, name):
        #here we add a new property to the class
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p1 = Person('Bob')
p1.say_hi()


p2 = Person('Tom')
p2.say_hi()

Person('Alice').say_hi()


"""
OUTPUT:
____________________________________

Hello, my name is Bob
Hello, my name is Tom
Hello, my name is Alice
"""