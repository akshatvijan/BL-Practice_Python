# greet function
# def greet_function():
#     print("hello")
# greet_function()

# def greet_friend(name:string):
#     print(f"hello {name}")
# greet_friend("Alice")
# greet_friend("Bob")


# def user_input(name:string):
#     print(f"hello {name} ")
# name=input("Enter your name")
# user_input(name)

#to check name contains alphabet

def check_alpha(name:string):
    if name.isalpha():
        print(f"hello {name}")
    else:
        print(f"Enter only alphabets")
name=input("Enter your name")

check_alpha(name)#dry priciple is do not repeat yourselft means you can make your code modular using funtion block to re use it again and again