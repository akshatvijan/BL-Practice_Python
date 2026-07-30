current_sign=input("Enter the email seperated  by ,")
new_sign=input("Enter the email seperated  by ,")
current_sign_list=current_sign.split(', ')
new_sign_list=new_sign.split(',')

s1=set(current_sign_list)
s2=set(new_sign_list)
s3=s1.intersection(s2)

if(len(s3)>0):
    for i in s3:
        print(f"{i} exist")
else:
    print("No email exist")