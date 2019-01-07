def print_max(x, y):
    '''Prints the maximum of two numbers. The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)

# __doc__ - is a keyword in python that returns the string that is written in ''' ''' right under the function declaration
print(print_max.__doc__)

"""
OUTPUT:
____________________________________

5 is maximum
Prints the maximum of two numbers. The two values must be integers.
"""