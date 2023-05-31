# V3 is using nearby search so we provided a point lattitude and longitude and then we move that point.

import requests
import json
import os

# Define constants
API_KEY = "your-api-key"
LATITUDE = -7.7829
LONGITUDE = 110.3671  # Tugu Yogyakarta
RADIUS = 50000  # 50 km
TYPE = "restaurant|bar|cafe"
LANGUAGE = "id"
REGION = "id"
NEARBY_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
PLACE_URL = "https://maps.googleapis.com/maps/api/place/details/json"

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

# Get place IDs
place_ids = [result["place_id"] for result in data.get("results", [])]

# Get place details
all_places_data = []
for place_id in place_ids:
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
    all_places_data.append(place_data)

# Create the response directory if it doesn't exist
directory = "./GetData/response/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the response as a JSON file
file_path = os.path.join(directory, "1City_v3_selected_fields.json")
with open(file_path, "w") as file:
    json.dump(data, file)

print("DONE!")
