#Nested try except block
try:
    print("outer try")
    try:
        num=10
        print(10/0)
    except ZeroDivisionError as err:
        print(err)
except:
    print("outer except block")


# second program
try:
    print("outer try")
    try:
        num=int("abc")
    except ZeroDivisionError as err:
        print(err)
except:
    print("outer except block")

#third program

try:
    print("outer try block")
    try:
        num=int(input("Enter a number"))
        print(num/0)
    except ValueError as err:
        print("The error is",err)
    except ZeroDivisionError as err:
        print("the error is ",err)
except:
    print("outer blo0ck except")
finally:
    print("Code is completed")
