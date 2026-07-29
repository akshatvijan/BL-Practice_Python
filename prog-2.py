import sys
import timeit
my_list=[1,2,3,4,5,6,7,8,9,10]
my_tuple=(1,2,3,4,5,6,7,8,9,10)
print(f"{sys.getsizeof(my_list)} bytes")
print(f"{sys.getsizeof(my_tuple)} bytes")

print(f"Time for creating a list {timeit.timeit(stmt=lambda:my_list,number=1000000)}")
print(f"Time for creating a tuple {timeit.timeit(stmt=lambda:my_tuple,number=1000000)}")