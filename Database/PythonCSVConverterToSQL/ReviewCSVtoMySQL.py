import csv
import os

REVIEW_CSV_FILEPATH = "Database/CSV/Review2SQL.csv"
REVIEW_SQL_FILEPATH = "Database/SQL/ReviewInsertData.sql"


def generate_insert_statement(row):
    columns = [
        "Place_ID", "Name", "Star", "ReviewText"
    ]
    insert_statement = "INSERT INTO Reviews ("
    values = []

    for column in columns:
        if row[column] is not None and row[column] != "":
            insert_statement += column + ", "
            if isinstance(row[column], str):
                # Escape single quotes by doubling them
                value = row[column].replace("'", "''")
                values.append("'" + value + "'")
            else:
                values.append(str(row[column]))

    insert_statement = insert_statement.rstrip(
        ", ") + ") VALUES (" + ", ".join(values) + ");"
    return insert_statement


with open(REVIEW_CSV_FILEPATH, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    total_rows = sum(1 for row in reader)
    csvfile.seek(0)  # Reset the file pointer
    next(reader)  # Skip the header row
    with open(REVIEW_SQL_FILEPATH, 'w', encoding='utf-8') as sqlfile:
        for i, row in enumerate(reader, 1):
            insert_statement = generate_insert_statement(row)
            sqlfile.write(insert_statement)
            if i != total_rows:
                # Add a new line after each insert statement, except for the last one
                sqlfile.write("\n")
            print("Progress: {}/{}".format(i, total_rows))

print("DONE!")
