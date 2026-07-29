my_list=[x**2 for x in range(10)]
print("List of squares is",my_list)
my_tuple=tuple(my_list)
print(f"Tuple of squares is: ",my_tuple)
print("using indexing")
print("3rd element is",my_tuple[2])
print("5rd element is",my_tuple[4])
print("7rd element is",my_tuple[6])

print("First three elemets of tuple are: ",my_tuple[0:3:])
