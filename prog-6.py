
def get_friend_detail(friend_details):
    friend=input("enter choice friend1/friend2/friend3/friend4/friend5")
    choice=input("enter choice city/pincode/email/phone")
    for i in friend_details[friend]:
        if choice in i:
          print(i[choice])


def main():
    friend_details = {
    'friend1': [
        {"city": "New York", "pincode": 1234},
        {"email": "friend1@gmail.com", "phone": 9876543210}
    ],
    'friend2': [
        {"city": "London", "pincode": 5678},
        {"email": "friend2@gmail.com", "phone": 9876543211}
    ],
    'friend3': [
        {"city": "Toronto", "pincode": 9101},
        {"email": "friend3@gmail.com", "phone": 9876543212}
    ],
    'friend4': [
        {"city": "Sydney", "pincode": 1122},
        {"email": "friend4@gmail.com", "phone": 9876543213}
    ],
    'friend5': [
        {"city": "Delhi", "pincode": 3344},
        {"email": "friend5@gmail.com", "phone": 9876543214}
    ]}
     
    get_friend_detail(friend_details)
    


if __name__=='__main__':
    main()