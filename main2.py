# car loan payment
def car_loan(p:float,time:float,rate:float):
    t=12*time
    r=rate/(12*100)
    total_amount=(p*r)/(1-((1+r)**-t))
    print(f"Total amount to be paid in month is  ",round(total_amount,2))
principle=float(input("Enter the principle value"))
rate=float(input("Enter the rate"))
time=float(input("Enter the time"))
car_loan(principle,rate,time)