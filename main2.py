# circumfrnece and areaa
PI=22/7
radius_inch=float(input("Enter the radius in inch"))
radius_cm=radius_inch*2.54

circumfrence=2*PI*radius_cm
area=PI*(radius_cm**2) #first solve parenthesis then multiply with 2 PEMDAS is followed
print(f"the circumfrence is {circumfrence:.2f}cm and area is {area:.2f}sqcm")