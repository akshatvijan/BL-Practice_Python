from collections import defaultdict
def dfs():
    graph=defaultdict(list)
    road=int(input("Enter the number of roads"))
    for i in range(road):
        u=input("Enter")
        v=input("enter")
        graph[u].append(v)
        graph[v].append(u)

    start=input("Enter the start")
    stack=[]
    stack.append(start)
    visited=set()
    while stack:
        curr=stack.pop()
        
        if curr not in visited:
            visited.add(curr)
            print(curr,"->",end='')

        for nei in graph[curr]:
            if nei not in visited:
                stack.append(nei)
    return visited