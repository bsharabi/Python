text = input('Enter something: ')

if len(text) < 3:
    raise Exception()  # Exception - is built-in in python

print("End of app")



"""

OUTPUT 1:
_________________________________________
Enter something: t
Exception



OUTPUT 2:
_________________________________________
Enter something: te
Exception


OUTPUT 3:
_________________________________________
Enter something: test
End of app

"""
