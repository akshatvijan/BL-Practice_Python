def mean(number):
    mean=sum(number)/len(number)
    return mean
def variance(number):
    avg=mean(number)
    total=0
    for i in number:
        total+=(i-avg)**2
    return total/len(number)
def std(number):
    v=variance(number)
    std=v**0.5
    return std