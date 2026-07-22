#program 4 Proper function usage practice

#primitive data types are -> int,float,bool,str
#derived data type are ->list,dict,set,tuple
# but in case of python every thing is a object either it is primitive or deriverd that belongs to a certain class
#operator overloading means that same operator is performing different behaviour like if we write 10+30 we get 40 and if we write 'hello'+'akshat'
#result will be 'helloakshat' so the + operator is behaving diffrent with diffrent datatypes so it is operator overloading

#use of global variable is a bad practice we should avoid

def calculation(x:int,y:int): # here we define the datatype which is a good practice and default data type is any
    return x+y

a=10
b=20
print("type of a is",type(a),"\n type of b is",type(b)) #type is basically used to see the data type of a variable
c=calculation(a,b)
print("value of c is",c)


