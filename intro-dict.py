# dictionary is a data structure that stores value in key value pair
fruit_dict={'Apple':'Red',"Banana":'yellow'}
# fruit_dict={'Apple':{'Red','Green'},"Banana":'yellow'} nested dictionary
print(fruit_dict)
print(type(fruit_dict))
print(len(fruit_dict))
# value can be repeated but keys can not be repeated and keys are case-senstive
print(fruit_dict['Banana'])
print(fruit_dict.get('Banana'))
print(fruit_dict.keys())
print(fruit_dict.values())
print(fruit_dict.items())
print("Banana" in fruit_dict)