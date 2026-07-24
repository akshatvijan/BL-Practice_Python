def compute_avg(number):
    total=sum(number)
    count=len(number)
    if count==0:
        return '0 length'
       
    else:
         return total/count
      
number=[]
print(f"original list is",number)
ans=compute_avg(number)
print(f"Avg is",ans)