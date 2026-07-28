import re
def check_password(password):
    length=len(password)
    pattern=r'^[0-9+-@#$]'
    check_start= not re.match(pattern,password)
    check_digit=re.search(r'\d',password)
    check_special=False
    check_upper=False
    check_lower=False
    for ch in password:
        if ch in '@#$%^&*':
            check_special=True
        if ch.isupper():
            check_upper=True
        if ch.islower():
            
            check_lower=True
    
    if length>=8 and check_start and check_digit and check_special and check_upper and check_lower:
        print("Passowrd is valid")
    else :
        print("Password is invalid")

password=input("Enter the password")
check_password(password)