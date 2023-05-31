import csv
import os

DIR_PATH = "./Database/CSV/"
CSV_FILENAME = "Places.csv"
CSV_PATH = os.path.join(DIR_PATH, CSV_FILENAME)

print(CSV_PATH)


def generate_insert_statement(row):
    insert_statement = "INSERT INTO Places VALUES ("
    insert_statement += "'{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, '{}', {}, {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
        row['Places_ID'], row['Name'], row['FormattedAddress'], row['FormattedPhone'], row['Latitude'], row['Longitude'], row['rating'], row['ServesBeer'], row['ServesWine'], row['UserRatingTotal'], row[
            'Website'], row['PriceLevel'], row['WheelchairAccessibleEntrance'], row['StreetAddress'], row['District'], row['City'], row['Regency'], row['Province'], row['PostalNumber'], row['PhotoLink']
    )
    return insert_statement


with open(CSV_PATH, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        insert_statement = generate_insert_statement(row)
        print(insert_statement)
