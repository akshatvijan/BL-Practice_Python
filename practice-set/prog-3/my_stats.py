import random
import custom
import numpy as np
n=int(input("Enter the number"))
list=[]
for i in range(n):
    list.append(random.uniform(0.0,100.0))
print(custom.mean(list))
print(custom.std(list))
print(custom.variance(list))
print("Numpy")
print(np.mean(list))
print(np.std(list))
print(np.var(list))

