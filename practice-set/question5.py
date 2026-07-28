import time
def stop_watch(second):
    if(second==0):
        print("time finish")
        return
    h=second//3600
    m=((second//3600)) % 60
    s=second%60
    print(f"{h:02}:{m:02}:{s:02}")
    time.sleep(1)
    second=second-1
    stop_watch(second)
second=int(input("Enter the number of second"))
stop_watch(second)