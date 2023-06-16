# Note: This script is used to get JSON data from Google Places API using Nearby Search method

import requests
import json
import os

# Define constants
API_KEY = "YOUR_API_KEY"
LATITUDE = -7.7829
LONGITUDE = 110.3671  # Tugu Yogyakarta
RADIUS = 50000  # 50 km
TYPE = "restaurant"
LANGUAGE = "id"
REGION = "id"
NEARBY_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# Define parameters
params = {
    "location": f'{LATITUDE},{LONGITUDE}',
    "radius": RADIUS,
    "key": API_KEY,
    "type": TYPE,
    "language": LANGUAGE,
    "region": REGION,
}

# GET data from Google Places API
response = requests.get(NEARBY_URL, params=params)

# Convert data to JSON
data = response.json()

# Create the response directory if it doesn't exist
directory = "./GetData/response/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the response as a JSON file
file_path = os.path.join(directory, "test.json")
with open(file_path, "w") as file:
    json.dump(data, file)

print("DONE!")
