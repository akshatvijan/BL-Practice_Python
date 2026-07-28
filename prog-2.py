def print_details():
    details={input("enter the key value"):input("Enter the name"),'City of Stay':input("Enter the city"),'PinCOde':input("Enter the pincode")}
    print(type(details))
    for key in details:
        print(f"{key}:{details[key]}")
    print("Printing using items()")
    for key,value in details.items():
        print(f"{key}:{value}")

print_details()