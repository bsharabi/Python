try:
    text = input('Enter something: ')

    if len(text) < 3:
        raise Exception()  # Exception - is built-in in python
    print("Good input")

except Exception:
    print("Sorry - to short")

print("End of app")



"""

OUTPUT 1:
_________________________________________
Enter something: t
Sorry - to short
End of app


OUTPUT 2:
_________________________________________
Enter something: te
Sorry - to short
End of app

OUTPUT 3:
_________________________________________
Enter something: test
Good input
End of app

"""
