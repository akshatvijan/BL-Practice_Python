# find genration
year=int(input("Enter the year in which you were born"))
print(f"Birth Year is {year}",
    f" is Baby Boomer {year>1946  and year<1964}",
    f" is Gen x {year>=1965 and year<=1980}",
    f" is Millennial {year>=1981 and year<=1997}",
    f" is Gen z {year>=1997  and year<2012}",
    f" is Gen alpha {year>=2013 and year<=2025}",sep='\n')