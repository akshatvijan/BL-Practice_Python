from bubble import bubble_sort
from selection import selection_sort
from merge import merge_sort
from quick import quick_sort
from dfs import dfs
from dfs_recurssion import dfs_recurssion
from monster import choose_monster
from collections import deque
from collections import defaultdict

def sorting():
    my_list=[450,720,310,890,560]
    choice=int(input("Enter the choice"))
    if choice==1:
        bubble_sort(my_list)
        print(my_list)
    elif choice==2:
        selection_sort(my_list)
        print(my_list)

    elif choice==3:
        merge_sort(my_list,0,len(my_list)-1)
        print(my_list)
    elif choice==4:
        quick_sort(my_list,0,len(my_list)-1)
        print(my_list)
    else:
        print("Invalid choice")
    return my_list[-1]


def searching():
    arr = [105, 118, 129, 145, 167, 189, 205, 221, 250]
    s=0
    e=len(arr)-1
    print(arr)
    target=int(input("Enter the value"))
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            s=mid+1
        else:
            e=mid-1
    return -1

def bfs():
    vertex=int(input("Add number of roads"))
    graph=defaultdict(list)
    for i in range (vertex):
        u=input("enter")
        v=input("enter")
        graph[u].append(v)
        graph[v].append(u)

    start=input("Enter the start position")
    destination=input("Enter the destination")

    q=deque()
    q.append(start)
    visited=set()
    visited.add(start)
    distance=defaultdict()
    distance[start]=0
    parent=defaultdict()

    while q:
        curr=q.popleft()
        if curr==destination:
            
            break
        for nei in graph[curr]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
                distance[nei]=distance[curr]+1
                parent[nei]=curr

    path=[]
    curr=destination
    while curr!=start:
        path.append(curr)
        curr=parent[curr]
    path.append(start)
    path.reverse()
    return path,distance[destination]






if __name__=="__main__":
    leaderboard=0
    treasure=0
    explore=0
    score=0
    leaderboard=sorting()
    idx=searching()
    if idx!=-1:
        print("Treasure found!")
        print("index",idx)
        treasure=100
        
    else:
     print("treasure not found")


    path_list,path=bfs()
    print(path)
    for i in path_list:
        print(i,"->",end='')
    

    visited=dfs()
    if len(visited)>0:
        explore=100
    
    # dfs_iterative()
    #dfs_recurssion()

    score=choose_monster()
    final_score=leaderboard+explore+score+treasure
    

    print("Final Score:", final_score)

    if final_score <= 299:
        rank = "Novice Explorer"
    elif final_score <= 599:
        rank = "Skilled Adventurer"
    elif final_score <= 999:
        rank = "Master Strategist"
    else:
        rank = "Algorithm Legend"

    print("Rank:", rank)

    


