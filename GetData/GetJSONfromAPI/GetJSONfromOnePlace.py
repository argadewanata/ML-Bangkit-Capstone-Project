# Note: This script is used to get JSON data from Google Places API for one place

# Import libraries
import requests
import json
import os

# Define constants
REGION = "id"
LANGUAGE = "id"
API_KEY = "AIzaSyAnZNq3mo7LON6UyvVbvnqum-wzxtV31Nk"
PLACE_ID = "ChIJvb0GwNhYei4R1QHPGGdxI_A"  # Filosopi Kopi Jogja
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
    "place_id": PLACE_ID,
    "fields": ','.join(all_possible_fields),
    # "fields": ','.join(show2android_fields),
    "key": API_KEY,
    "language": LANGUAGE,
    "region": REGION,
    # "opennow": True,
    "reviews_no_translations": True,
}

# GET data from Google Places API
response = requests.get(PLACE_URL, params=params)

# Convert data to JSON
data = response.json()

# Create the response directory if it doesn't exist
directory = "./GetData/response/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the response as a JSON file
file_path = os.path.join(directory, "1Place_all_fields.json")
with open(file_path, "w") as file:
    json.dump(data, file)

print("DONE")
