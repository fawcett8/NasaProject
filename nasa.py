
from  flask import Flask, render_template, request

app = Flask("Nasa")

def get_img(search_date):
	import requests
	endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key=Ey6IJ2zvbnEYKNfiKskFVkxFLmRmGrEaAhRNpLAM"
	payload = {"earth_date" : search_date, "camera" : "FHAZ"}
	response = requests.get(endpoint, params=payload)
	data = response.json()

	any_photos = data["photos"]

	if any_photos:
		return any_photos[0]["img_src"]
	else:
		return None


@app.route("/")
def nasa():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
	date = request.form['date']
	img_src = get_img(date)
	if img_src:
		return render_template('curiosity.html', img_src=img_src)







app.run(debug=True)
