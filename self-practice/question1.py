def make_str(firstname,middlename,lastname):
    ans=firstname+' '+middlename+' '+lastname if(middlename) else firstname+" "+lastname
    val=ans.title()
    return val
firstname=input("Enter the first Name")
middlename=input("Enter the middle name")
lastname=input("Enter the last name")
print(f"{make_str(firstname,middlename,lastname)}")
