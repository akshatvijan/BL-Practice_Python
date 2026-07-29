def swap(a,b):
    # c=a
    # a=b
    # b=c
    a=a+b
    b=a-b
    a=a-b
    return a,b
a=int(input("Enter the number a"))
b=int(input("Enter the number b"))
print(a,b)
a,b=swap(a,b)
print(a,b)


#pythonic way
a=int(input("Enter the number a"))
b=int(input("Enter the number b"))
print(a,b)
a,b=b,a
print(a,b)