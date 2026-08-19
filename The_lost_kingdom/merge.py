def merge(arr,s,e):
    mid=(s+e)//2
    len1=mid-s+1
    len2=e-mid
    first=[0]*len1
    second=[0]*len2
    k=s
    for i in range(len1):
        first[i]=arr[k]
        k+=1
    k=mid+1
    for i in range(len2):
        second[i]=arr[k]
        k+=1

    # merging 2 array
    i=0
    j=0
    k=s
    while(i<len1 and j<len2):
        if first[i]<second[j]:
            arr[k]=first[i]
            i+=1
            k+=1
        else:
            arr[k]=second[j]
            k+=1
            j+=1

    while(i<len1):
        arr[k]=first[i]
        k+=1
        i+=1
    while(j<len2):
        arr[k]=second[j]
        k+=1
        j+=1

def merge_sort(arr,s,e):
    if s>=e:
        return
    mid=(s+e)//2
    merge_sort(arr,s,mid)
    merge_sort(arr,mid+1,e)
    merge(arr,s,e)