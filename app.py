from flask import Flask, render_template, request
from shapely.geometry import Polygon, Point

app = Flask(__name__)

# Define your geofence
geofence_coordinates = [(80.236175,13.009022), (80.237943,13.008820), (80.237774,13.007708), (80.236014,13.008572)]
geofence = Polygon(geofence_coordinates)

# Flask route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Flask route to receive location data from the JavaScript code
@app.route('/location', methods=['POST'])
def receive_location():
    lat = float(request.json['latitude'])
    lon = float(request.json['longitude'])
    current_location = Point(lon, lat)

    # Check if the current location is inside the geofence
    if geofence.contains(current_location):
        location_status = "Inside geofence"
    else:
        location_status = "Outside geofence"

    # Format the response with each item on a new line in a box
    response = f"Latitude: {lat}\nLongitude: {lon}\nStatus: {location_status}"

    return response

if __name__ == '__main__':
    app.run(debug=True)
