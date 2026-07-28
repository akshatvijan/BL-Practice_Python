def merge_dict():
    friend_detail={'name':'John doe','city of stay':'Mumbai','pincode':12345}
    contact_detail={'Email':'John.doe@example.com'}
    merged_dict=friend_detail | contact_detail
    print(merged_dict)
    
    del merged_dict['pincode']
    print(merged_dict)
    merged_dict.pop('name')
    print(merged_dict)
merge_dict()