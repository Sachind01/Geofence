from flask import Flask, render_template, request
from shapely.geometry import Polygon, Point

app = Flask(__name__)

# Define your geofence
geofence_coordinates = [(80.239299, 12.992705), (80.248408, 12.992772), (80.249236, 12.984367), (80.238747, 12.984367)]
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
