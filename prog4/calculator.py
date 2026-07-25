class ZeroError(Exception):
    pass
try:
    def add(num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1-num2
    def mul(num1,num2):
        return num1*num2
    def div(num1,num2):
        if num2==0:
            raise ZeroError("Cant divide by 0")
        return round(num1/num2,2)
    
except ZeroError as err:
    print("the err is",ZeroError)