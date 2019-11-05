x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)

"""
OUTPUT:
____________________________________

x is 50
Changed global x to 2
Value of x is 2
"""