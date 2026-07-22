#program 5 Proper Hard Coding Practice
#hard coding of variables(constants) should be avoided as we complile are code it chnages to byte code that is already constant
#how wver we can make the values constant that are constant through out their lifetime like pi (3.14)
#contants are genenrally written in uppercase
#we use input to take values from the user and the return type of input is always a string
#if we want to convert one datatype to another datatype then it is called type acsting it may be implicit or explicit
#implicit is generally when data types are given by python we are not chnaging it and in explixit we genrally chnage our data from one datatype to another

PI=3.14 #constant are gennerally written in uppercase

def area(r):
    return PI*r**2
radius=2
ans=area(radius)
print("Area of circle with radius",radius," is ",ans)


def calculate(a:int,b:int):
    return a+b

val1=int(input("Enter the number")) #type coversion
val2=int(input("Enter the number"))

ans=calculate(val1,val2)
print("Answer is ",ans)