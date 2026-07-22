#Handling exception Practice
#error handling is basically used handle the runtime errors if we don't handle the error then our program will stop and handling error is a good practice
#error handling is done with try except block python generaaly created a well defined object as exception that are catch in except block

def calculate(x:int,y:int):
    return x+y

try:
    val1=int(input("Enter the value"))
    val2=int(input("Enter the value"))
    ans=calculate(val1,val2)
    print("The answer is ",ans)

# except: #this is a bad practice as we are not catching the error
#     print("Try entering with correct value")
except ValueError as err:
    print("the error is",err,"try again")
except:
    print("try with proper value")

