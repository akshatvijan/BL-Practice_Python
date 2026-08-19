from collections import defaultdict
def depth_first_search(graph,start,visited):
    print(start)
    visited.add(start)
    for nei in graph[start]:
        if nei not in visited:
            depth_first_search(graph,nei,visited)

def dfs_recurssion():
    graph=defaultdict(list)
    road=int(input("Enter the number of roads"))
    for i in range(road):
        u=input("Enter")
        v=input("enter")
        graph[u].append(v)
        graph[v].append(u)

    start=input("Enter the start")
    visited=set()
    depth_first_search(graph,start,visited)