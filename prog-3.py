def merge_dict():
    friend_detail={'name':'John doe','city of stay':'Mumbai','pincode':12345}
    contact_detail={'Email':'John.doe@example.com'}

    # update method
    friend_copy=friend_detail.copy()
    friend_copy.update(contact_detail)
    print(friend_copy)
    print_details(friend_copy)

    #unpacking (**)
    merged_dict={**friend_detail,**contact_detail}
    print(merged_dict)
    print_details(merged_dict)

    # | operator
    operator_dict=friend_detail | contact_detail
    print(operator_dict)
    print_details(operator_dict)
    
    
    # |= operator 
    copy_friend=friend_detail.copy()
    copy_friend |= contact_detail
    print(copy_friend)
    print_details(copy_friend)


def print_details(dict):
    print("keys are",dict.keys())
    print("keys are",dict.values())
    print("keys are",dict.items())

merge_dict()