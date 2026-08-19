def selection_sort(arr):
    for i in range(len(arr)-1):
        minpos=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minpos]:
                minpos=j
        arr[minpos],arr[i]=arr[i],arr[minpos]