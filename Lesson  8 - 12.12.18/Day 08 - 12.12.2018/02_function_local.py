x = 50


def func(x):
    ''' In this function the "x" is not the global "x" - it is a local "x" '''
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)


"""
OUTPUT:
____________________________________

x is 50
Changed local x to 2
x is still 50
"""