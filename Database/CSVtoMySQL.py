import csv
import os

CSV_FILEPATH = "Database/CSV/Places.csv"
SQL_FILEPATH = "Database/PlacesInsertData.sql"

def generate_insert_statement(row):
    insert_statement = "INSERT INTO Places VALUES ("
    insert_statement += "'{}', '{}', '{}', '{}', {}, {}, {}, {}, '{}', {}, {}, {}, {}, {}, {}, '{}', '{}', '{}', '{}', '{}');".format(
        row['Place_ID'], row['Name'], row['FormattedPhone'], row['FormattedAddress'], row['Latitude'], 
        row['Longitude'], row['OverallRating'],row['PriceLevel'], row['Website'], row['UserRatingTotal'], 
        row['ServesBeer'], row['ServesWine'], row['ServesVegetarianFood'], row['WheelchairAccessibleEntrance'], row['Halal'], 
        row['StreetAddress'], row['District'], row['City'], row['Regency'],row['Province'],row['PostalNumber']  
    )
    return insert_statement

with open(CSV_FILEPATH, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    total_rows = sum(1 for row in reader)
    csvfile.seek(0)  # Reset the file pointer
    next(reader)  # Skip the header row
    with open(SQL_FILEPATH, 'w', encoding='utf-8') as sqlfile:
        for i, row in enumerate(reader, 1):
            insert_statement = generate_insert_statement(row)
            sqlfile.write(insert_statement)
            if i != total_rows:
                sqlfile.write("\n")  # Add a new line after each insert statement, except for the last one
            print("Progress: {}/{}".format(i, total_rows))

print("DONE!")  








