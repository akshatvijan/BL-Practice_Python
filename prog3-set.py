school_friend=['a','b','c','d']
collage_frind=['c','d','e','f']
s1=set(school_friend)
s2=set(collage_frind)
print("all friend with | operator",list(s1|s2))
print("Commen friends with intersection",list(s1.union(s2)))