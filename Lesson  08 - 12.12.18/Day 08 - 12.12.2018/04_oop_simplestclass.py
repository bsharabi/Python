#Declare a class
class Person:
    pass  # An empty block



#Create an instance of the class
p1 = Person()
print(p1)


#Create an instance of the class
p2 = Person()
print(p2)

p3=p2
print(p3)

"""
OUTPUT:
____________________________________

<__main__.Person object at 0x000002B4E4D5B630>
<__main__.Person object at 0x000002B4E4D5B6D8>
<__main__.Person object at 0x00000218EF49B6D8>
"""