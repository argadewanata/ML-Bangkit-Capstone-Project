# Important : v2 is using only 1 API call for the whole city, so it is faster.

# Import libraries
import requests
import json

# Define constants
API_KEY = "AIzaSyAnZNq3mo7LON6UyvVbvnqum-wzxtV31Nk"
QUERY = "kafe atau restoran di Yogyakarta"
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

# Save data to JSON file
with open("./response/respontest.json", "w") as file:
    json.dump(data, file)

print("DONE!")
