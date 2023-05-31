import requests
import json
import os

API_KEY = "your-api-key"

# Yogyakarta Boundary
# 8º 30'–7º 20' Lintang Selatan, dan 109º 40'–111º 0' Bujur Timur
LATITUDE_START = -7.3
LATITUDE_END = -8.5
LONGITUDE_START = 109.4
LONGITUDE_END = 111.0

# Define constants and parameters
RADIUS = 50000
TYPE = "restaurant|bar|cafe"
LANGUAGE = "id"
REGION = "id"
NEARBY_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
PLACE_URL = "https://maps.googleapis.com/maps/api/place/details/json"
SHOW2ANDROID_FIELDS = ["name", "rating", "opening_hours", "price_level", "user_ratings_total", "reviews", "types",
                       "website", "formatted_phone_number", "formatted_address", "geometry", "serves_wine",
                       "serves_beer", "wheelchair_accessible_entrance"]
RESPONSE_FILE_PATH = "./GetData/response/WholeYogyakarta.json"

# Check if the response file exists
if os.path.exists(RESPONSE_FILE_PATH):
    # Read the existing file content
    with open(RESPONSE_FILE_PATH, "r") as file:
        existing_data = json.load(file)
else:
    existing_data = {"results": []}

# Total number of iterations
total_iterations = abs(int((LATITUDE_END - LATITUDE_START) / 0.4) *
                       int((LONGITUDE_END - LONGITUDE_START) / 0.4))
current_iteration = 0

# Iterate over latitude and longitude range
for latitude in range(int(LATITUDE_START * 10), int(LATITUDE_END * 10), -5):
    for longitude in range(int(LONGITUDE_START * 10), int(LONGITUDE_END * 10), 5):
        # Calculate current latitude and longitude
        current_latitude = latitude / 10.0
        current_longitude = longitude / 10.0

        print(f"Processing: {current_latitude},{current_longitude}")

        # Define parameters
        params = {
            "location": f'{current_latitude},{current_longitude}',
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

        # Get place IDs
        place_ids = [result["place_id"] for result in data.get("results", [])]

        # Get place details
        new_place_data = []
        for index, place_id in enumerate(place_ids):
            if place_id not in existing_data["results"]:
                print(
                    f"Processing: {current_latitude},{current_longitude} - Place ID: {place_id} ({index+1}/{len(place_ids)})")
                place_params = {
                    "place_id": place_id,
                    "fields": ','.join(SHOW2ANDROID_FIELDS),
                    "key": API_KEY,
                    "language": LANGUAGE,
                    "region": REGION,
                    "reviews_no_translations": True,
                }
                place_response = requests.get(PLACE_URL, params=place_params)
                place_data = place_response.json()
                new_place_data.append(place_data)

        # Append the new data to the existing results
        existing_data["results"].extend(data.get("results", []))

        # Append the new place details to the existing places data
        existing_data["results"].extend(new_place_data)

        current_iteration += 1
        print(f"Progress: {current_iteration}/{total_iterations}")

# Save the updated response as a JSON file
with open(RESPONSE_FILE_PATH, "w") as file:
    json.dump(existing_data, file)

print("DONE!")
