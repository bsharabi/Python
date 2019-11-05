def print_max(x, y):
    '''Prints the maximum of two numbers. The two values must be integers.'''
    # convert to integers, if possible
    try:
        x = int(x)
        y = int(y)
        if x > y:
            return(x, 'is maximum')
        else:
            return(y, 'is maximum')
    except:
      print("Something went wrong")
    else:
      print("Nothing went wrong")
    finally :
      return 0
      print("Function End")



# __doc__ - is a keyword in python that returns the string that is written in ''' ''' right under the function declaration
print(print_max.__doc__)
res=print_max(5,"s")
print(res)
"""
OUTPUT:
____________________________________
5 is maximum
Prints the maximum of two numbers. The two values must be integers.
"""