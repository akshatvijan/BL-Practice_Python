#tuple is similiar to that of list in python like it also have indexing, contain nested object contain data of different data type 
#list are muatable where as tuple are immuatable
#tuple are generally used when you want to store a large hetrogenous data in a sinple variable and you using it for analysing purpose
my_tuple=()
print(my_tuple)
my_tuple_int=(1,2,3)
print(my_tuple_int)
my_tuple_mixed=(1,2,3,"hello",8.5)
print(my_tuple_mixed)
my_tuple_nested=(1,2,3,("hello",8.5))
print(my_tuple_nested)
my_tuple_lst=(1,2,3,["hello",8.5])
print(my_tuple_lst)


tuple1=("Hello")
print(type(tuple1))
tuple2=("Hello",)
print(type(tuple2))