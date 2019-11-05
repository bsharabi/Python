def get_number():
    # block of code - that can throw error
    try: 
        my_num=int(input("enter number: "))

    #if the code in try threw a 'KeyboardInterrupt' error - this block is executed
    except KeyboardInterrupt:  
        return("you pressed control + c : GOOD BYE")


    #if the code in try threw a 'ValueError' error - this block is executed
    except ValueError:
        return("you entered invalid value")

    #if the code in try executed with no error - this block will be executed  
    else:
        return("you entered: "+ str(my_num))

    #this line will always run (althogh we have `return` in `try` and in `except`)    
    finally:    
        print("End of app")

res=get_number()
print("I got from get_number:",res)

"""

OUTPUT 1:
_________________________________________
enter number: TEST
End of app
I got from get_number: you entered invalid value



OUTPUT 2:
_________________________________________
enter number: 8
End of app
I got from get_number: you entered: 8


OUTPUT 3:
_________________________________________
enter number: (WE PRESSED CONTROL + C)
End of app
I got from get_number: you pressed control + c : GOOD BYE

"""
