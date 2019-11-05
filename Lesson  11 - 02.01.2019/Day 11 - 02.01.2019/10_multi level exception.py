class UnderAgeExeption(Exception):
    '''A user-defined exception class.'''
    def __init__(self):
        Exception.__init__(self)


class OverAgeExeption(Exception):
    '''A user-defined exception class.'''
    def __init__(self):
        Exception.__init__(self)

try:
    age = int(input('Enter age: '))
    if age < 0:
        raise UnderAgeExeption()
    if age > 120:
        raise OverAgeExeption()
        
except Exception:  # catches all the exceptions that are from "Exception" class or sub-class
    print("non valid age")

else:
    print('valid age')


print("End of app")


"""

OUTPUT 1:
_________________________________________
Enter age: 130
non valid age
End of app


OUTPUT 2:
_________________________________________
Enter age: -5
non valid age
End of app


OUTPUT 3:
_________________________________________
Enter age: 5
valid age
End of app

"""