# retunring multiple values
def compute_values(number_list):
    """ 
    description: the function is used to find minimum and maximum value
    parameter: number_list
    retrun: min_value,max_value

    """
    min_value=min(number_list)
    max_value=max(number_list)
    return min_value,max_value
size=int(input("Enter the size of list"))
number_list=[]

for i in range(size):
    num=int(input("Enter the number for list: "))
    number_list.append(num)
min,max=compute_values(number_list)
print(f"The minimum value is {min}")
print(f"The maximum value is {max}")