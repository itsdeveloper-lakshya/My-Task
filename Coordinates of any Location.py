pip install geopy

//First Method for finding coordinates of any location
from geopy.geocoders import ArcGIS
nom=ArcGIS()
location=input("Enter name of location : ")
nom.geocode(location)


//Second Method For finding Coordinates of any locatoion
from geopy.geocoders import ArcGIS

nom = ArcGIS()

try:
    location = input("Enter name of location: ")
    result = nom.geocode(location)
    
    if result is not None:
        print("Coordinates of", location, "are:", result.latitude, ",", result.longitude)
    else:
        print("Location not found.")
except Exception as e:
    print("An error occurred:", e)

    
