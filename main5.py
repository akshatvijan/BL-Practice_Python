#finally block always run
try:
    print("Inside try")
    num=20
    print(num)
except:
    print("Error")
finally:
    print("Finally block executed \n \n")


try:
    num=20
    print(20/0)
except ZeroDivisionError as err:
    print("the error is",err)
finally:
    print("Finally block exucuted")




try:
    file=open("data.txt","r")
    print(file.read())
except FileNotFoundError as err:
    print("the error is",err)
finally:
    print("Closing the program")

