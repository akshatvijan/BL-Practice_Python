def create_default():
    friend_detail={
        'Name':'John Doe',
        'City of stay':'Mumbai',
        'pincode':43008
    }
    print(friend_detail)
    friend_detail.setdefault('country','india')
    print(friend_detail)

    friend_detail.setdefault('Friend-Type','')
    print("after adding friend-type",friend_detail)
    list=['school','neighbour','office']
    for i,value in enumerate(list):
        print(f"{i+1} {value}")
    choice=int(input("Enter the number"))
    friend_detail['Friend-Type']=list[choice-1]
    print(friend_detail)
create_default()