# to use join
def create_str():
    places=[]
    for i in range(1,6):
        state=input(f"Enter the place to visit {i}")
        places.append(state)
    
    str=', '.join(places)
    print("Places separated by comma space and uppercase: ",str.upper())
create_str()