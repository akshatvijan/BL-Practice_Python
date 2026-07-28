import random
ANS=random.randint(1,100)
print(ANS)

def guess_number():
    cnt=10
    flag=True
    while(cnt!=0):
        
        num=int(input("Enter the number"))
        if( num>ANS):
            cnt=cnt-1
            print(f"too hight chances left {cnt}")

        elif(num<ANS):
            cnt=cnt-1
            print(f"too low chances left {cnt}")
        else:
            print("you win")
            flag=False
            break
    if flag:
        print("you lose")

guess_number()