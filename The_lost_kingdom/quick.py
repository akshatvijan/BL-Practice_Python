def partition(arr,s,e):
    pivot=arr[s]
    cnt=0
    for i in range(s+1,e+1):
        if arr[i]<pivot:
            cnt+=1
    pivotindex=cnt+s
    arr[pivotindex],arr[s]=arr[s],arr[pivotindex]

    i=s
    j=e
    while(i<pivotindex and j>pivotindex):
        while arr[i]<pivot:
            i+=1
        while arr[j]>pivot:
            j=j-1
        if i<pivotindex and j>pivotindex:
            arr[i],arr[j]=arr[j],arr[i]
    return pivotindex
def quick_sort(arr,s,e):
    if s>=e:
        return 

    p=partition(arr,s,e)
    quick_sort(arr,s,p-1)
    quick_sort(arr,p+1,e)