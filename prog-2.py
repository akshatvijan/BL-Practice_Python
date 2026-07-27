#slicing in string
str="akshat"
print(str[::])
print(str[0:3])
print(str[-4::2])

def create_str(str):
    first_char=str[0]
    last_char=str[-1]
    middle_index=len(str)//2
    middle_char=str[middle_index]
    print("Concatenating first char middle char last char",first_char+middle_char+last_char)
try:
    str=input("Enter the string")
    create_str(str)
except ValueError as err:
    print("the error os",err)


