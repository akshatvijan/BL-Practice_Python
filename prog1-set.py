school_friend=['a','b','c','d']
collage_frind=['c','d','e','f']

def common_friend(school,collage):
    common=[]
    for friend in school:
        if friend in collage:
            common.append(friend)
    print(common)

print("Collage friends: ",school_friend)
print("Collage friends: ",collage_frind)
common_friend(school_friend,collage_frind)
print("Commen friends with intersection")
s1=set(school_friend)
s2=set(collage_frind)
s3=list(s1.intersection(s2))
print(s3)
print("Common friend with & operator",list(s1&s2))