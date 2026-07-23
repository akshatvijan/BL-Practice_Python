#oops banner
print("oops")

#program 2
#print f string is better beacuase it evalutes with {} expression and chnage it to string at the same place that is why is has high performance
username=input("Enter your name")
first_place=input("First place you want to visit")
second_place=input("Second place you want to visit")
third_place=input("Third place you want to visit")
year=int(input("Enter the year"))

print(f"{username} will visit {first_place}",second_place,third_place,sep=', ',end=' ') 
print(f"in year {year}")