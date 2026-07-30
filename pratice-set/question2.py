def check_fruit():
    fruit=input("enter the fruit")
    if fruit in in_stock:
        print(f"{fruit} is in stock")
    else:
        print(f"{fruit} is not in stock")
def list_all_itms():
    for i in in_stock:
        print(i)
def update_stock():
    fruit=input("enter the fruit")
    ds=input("Enter in to add and remove to remove from stock")
    if ds=="in":
        in_stock.add(fruit)
        out_of_stock.remove(fruit)
    elif ds=="out":
        in_stock.remove(fruit)
        out_of_stock.add(fruit)

        
try:
    in_stock = {'apple','watermelon','strawberry' }
    out_of_stock = {'banana', 'orange', 'guava'}

    while(True):
        print(f"{'-'*3} fruit inventory {'-'*3}")
        print("1. Check if a fruit is in stock")
        print("2. List all items in the store")
        print("3. Update stock (add/remove item)")
        print("4. Exit")
        choice=input("Enter the choice")
        choice=int(choice)
        if(choice==1):
            check_fruit()
        elif choice==2:
            list_all_itms()
        elif choice==3:
            update_stock()
        elif choice==4:
            break
        else:
            if(type(choice)==int):
                print("ENter a number between 1 and 4")
            
finally:
    print("Code finished")
