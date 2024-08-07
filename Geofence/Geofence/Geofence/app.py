from flask import Flask, render_template, request

from shapely.geometry import Polygon, Point

app = Flask(__name__)


# Define your geofence
geofence_coordinates = [(13.014080, 80.235918), (13.014127, 80.236981), (13.013210, 80.236855), (13.013271, 80.235633)]
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

    return {'latitude': lat, 'longitude': lon, 'status': location_status}

if __name__ == '__main__':
    app.run(debug=True)
