# block of code - that can throw error
try: 
    my_num=int(input("enter number: "))

#if the code in try threw a 'KeyboardInterrupt' error - this block is executed
except KeyboardInterrupt:  
    print("you pressed control + c : GOOD BYE")


#if the code in try threw a 'ValueError' error - this block is executed
except ValueError:
    print("you entered invalid value")

#if the code in try executed with no error - this block will be executed  
else:
    print("you entered:", my_num)

#this line will run alwayes (also if we passed in `except`)    
finally:
    print("End of app")



"""

OUTPUT 1:
_________________________________________
enter number: TEST
you entered invalid value
End of app


OUTPUT 2:
_________________________________________
enter number: 8
you entered: 8
End of app


OUTPUT 3:
_________________________________________
enter number: (WE PRESSED CONTROL + C)
you pressed control + c : GOOD BYE
End of app

"""
