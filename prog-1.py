def print_details(details):
    print(type(details))
    for key in details:
        print(f"{key}:{details[key]}")
    for key,value in details.items():
        print(f"{key}:{value}")
friend_detail={'Name':'John','City of Stay':'Mumbai','PinCOde':40048}
print_details(friend_detail)