import requests
import json
import os

# Define constants
API_KEY = "YOUR_API_KEY"
QUERY = "Kafe di Tugu Yogyakarta"
RADIUS = 50000  # 50 km
LANGUAGE = "id"
REGION = "id"
CITY_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
PLACE_URL = "https://maps.googleapis.com/maps/api/place/details/json"

# Define categories and fields
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

# Define parameters
params = {
    "query": QUERY,
    "radius": RADIUS,
    "key": API_KEY,
    "language": LANGUAGE,
    "region": REGION,
}

# GET data from Google Places API
response = requests.get(CITY_URL, params=params)

# Convert data to JSON
data = response.json()

# Get place IDs
place_ids = [result["place_id"] for result in data.get("results", [])]

# Get place details and append to the existing data
existing_data = []
file_path = "./GetData/response/1City_v1_all_fields.json"

# Check if the file exists
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        existing_data = json.load(file)

# Get the existing place IDs
existing_place_ids = [place_data.get("place_id") for place_data in existing_data]

# Filter out place IDs that already exist in the data
new_place_ids = [place_id for place_id in place_ids if place_id not in existing_place_ids]

# Get place details for new place IDs
new_places_data = []
for place_id in new_place_ids:
    place_params = {
        "place_id": place_id,
        "fields": ','.join(all_possible_fields),
        "key": API_KEY,
        "language": LANGUAGE,
        "region": REGION,
        "reviews_no_translations": True,
    }
    place_response = requests.get(PLACE_URL, params=place_params)
    place_data = place_response.json()
    new_places_data.append(place_data)

# Append new data to the existing data
all_places_data = existing_data + new_places_data

# Save the response as a JSON file
with open(file_path, "w") as file:
    json.dump(all_places_data, file)

print("DONE!")
