import re
def check(string):
    matches=re.findall(r'\d',string)
    print(matches) if (matches) else print("No digit found")

string=input("Enter a string")
check(string)