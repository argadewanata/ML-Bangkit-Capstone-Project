# note : This script is used to get data from google places API using nearby search

import requests
import json
import os

API_KEY = "YOUR_API_KEY"

# Yogyakarta Boundary
# 8º 30'–7º 20' Lintang Selatan, dan 109º 40'–111º 0' Bujur Timur
LATITUDE_START = -8.3
LATITUDE_END = -7.2
LONGITUDE_START = 109.4
LONGITUDE_END = 111.0

# Define constants and parameters
RADIUS = 50000
TYPE = "restaurant|bar|cafe"
LANGUAGE = "id"
REGION = "id"
NEARBY_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
PLACE_URL = "https://maps.googleapis.com/maps/api/place/details/json"
RESPONSE_FILE_PATH = "./GetData/response/WholeYogyakartav2.json"

# Define categories
basic_category = ["address_components", "adr_address", "business_status", "formatted_address",
                  "geometry", "icon", "icon_mask_base_uri", "icon_background_color",
                  "name", "photo", "place_id", "plus_code", "type", "url", "utc_offset", "vicinity",
                  "wheelchair_accessible_entrance"]

contact_category = ["formatted_phone_number", "international_phone_number",
                    "opening_hours", "secondary_opening_hours", "website"]

atmosphere_category = ["curbside_pickup", "delivery", "dine_in", "editorial_summary",
                       "price_level", "rating", "reservable", "reviews", "serves_beer",
                       "serves_breakfast", "serves_brunch", "serves_dinner", "serves_lunch",
                       "serves_vegetarian_food", "serves_wine", "takeout", "user_ratings_total"]

show2android_fields = ["name", "rating", "opening_hours", "price_level",
                       "user_ratings_total", "reviews", "types", "website",
                       "formatted_phone_number", "formatted_address", "geometry",
                       "serves_wine", "serves_beer", "wheelchair_accessible_entrance"]

all_possible_fields = basic_category + contact_category + atmosphere_category


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
                    # "fields": ','.join(all_possible_fields),
                    "fields": ','.join(show2android_fields),
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
