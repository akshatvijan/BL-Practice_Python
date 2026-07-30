def latitude_longitude(city,info):
    if city in info:
        print(f"{city}: longitutde: {info[city][0]} latitude: {info[city][1]}")
    else:
        print("City not found")

my_dict={
'mumbai': (19.076, 72.8777),
'bangalore': (12.9716, 77.5946),
'chennai': (13.0827, 80.2707),
'pune': (18.5204, 73.8567),
'hyderabad': (17.385, 78.4867)
}
while(True):
    city=input("Enter the city or type exit to exit")
    if(city=='exit'):
        break
    latitude_longitude(city,my_dict)