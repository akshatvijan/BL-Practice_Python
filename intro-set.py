s1={1,2,3,3,2,1,4}
# print(s1)
# print(type(s1))
# s1.add(4)
# print(s1)
# s1.update([1,"helo",3],{7,8,9})
# print(s1)
# s1.remove(10)
print(s1)
s1={1,2,3}
s2={2,3,4}
s3={3,4,5}
s4=s1.intersection(s2,s3)

print(s4)
s4=s1.difference(s2) #elemets of s1 that are not in s2
s4=s2.difference(s1) #elemets of s2 that are not in s1
s4=s2.symmetric_difference(s1) #opposite of intersection
s4=s1.union(s2)
print(s4)
my_set=frozenset([1,2,3,4])
# my_set.add(5)
print(type(my_set))