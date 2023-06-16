# Important : v2 is using only 1 API call for the whole city, so it is faster.

# Import libraries
import requests
import json
import os

# Define constants
API_KEY = "YOUR_API_KEY"
QUERY = "kafe di Yogyakarta"
RADIUS = 50000  # 50 km
LANGUAGE = "id"
REGION = "id"
CITY_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# Define parameters
params = {
    "query": QUERY,
    "radius": RADIUS,
    "key": API_KEY,
    "language": LANGUAGE,
    "region": REGION,
    "reviews_no_translations": True,
}

# GET data from Google Places API
response = requests.get(CITY_URL, params=params)

# Convert data to JSON
data = response.json()

# Create the response directory if it doesn't exist
directory = "./GetData/response/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the response as a JSON file
file_path = os.path.join(directory, "1City_v2_all_fields.json")
with open(file_path, "w") as file:
    json.dump(data, file)

print("DONE!")
