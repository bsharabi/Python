class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something: ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
        
except ShortInputException as my_ex:
    print(my_ex.length, my_ex.atleast)

else:
    print('No exception was raised.')


print("End of app")

"""


OUTPUT 1:
_________________________________________
Enter something: t
1 , 3
End of app


OUTPUT 2:
_________________________________________
Enter something: te
2 , 3
End of app


OUTPUT 3:
_________________________________________
Enter something: test
No exception was raised.
End of app


"""
