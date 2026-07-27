import re
def is_valid_email(email):
    pattern=r'^[a-zA-z0-9.%_+-]+\@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$'
    if(re.match(pattern,email)):
        return True
    else:
        return False

email=input("Enter the email")
if is_valid_email(email):
    print(f"{email} is a valid email")
else:
    print(f"{email} is not valid")
