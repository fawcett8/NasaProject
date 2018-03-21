import requests
search_date = "2018-03-18"
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key=Ey6IJ2zvbnEYKNfiKskFVkxFLmRmGrEaAhRNpLAM"
payload = {"earth_date" : search_date, "camera" : "FHAZ"}
response = requests.get(endpoint, params=payload)
data = response.json()

any_photos = data["photos"]
if any_photos:
	result = any_photos[0]["img_src"]
else:
	result = "No photos for {0}".format(search_date)
print result