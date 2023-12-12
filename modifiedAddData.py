import csv
import os
import psycopg2
from psycopg2 import sql

path = '/Users/sopiokvantaliani/PythonApplications/Project2'
file_path = os.path.join(path, "data.csv")

# Establish a connection to the PostgreSQL database
con = psycopg2.connect(
    host="localhost",
    database="ClientDataBase",
    user="postgres",
    password="Giorgi2008!",
    port=5432
)

cursor = con.cursor()

# Create the 'clientDb' table if it doesn't exist
create_table_query = """
    CREATE TABLE IF NOT EXISTS clientDb (
        full_name TEXT,
        first_name TEXT,
        last_name TEXT,
        title TEXT,
        organization_name TEXT,
        email TEXT,
        linkedin TEXT,
        twitter TEXT
    )
"""
cursor.execute(create_table_query)

# Commit the changes to ensure the table creation is applied
con.commit()


# Define fieldnames variable
fieldnames = ['full_name', 'first_name', 'last_name', 'title',
              'organization_name', 'email', 'linkedin', 'twitter']

# Check if the file exists, create it if not
if not os.path.isfile(file_path):
    with open(file_path, "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

# Get input from the user
new_data = {}
print("Enter the following details:")
for field in ['full_name', 'first_name', 'last_name', 'title', 'organization_name', 'email', 'linkedin', 'twitter']:
    new_data[field] = input(f"{field.capitalize()}: ")

with open(file_path, "r", newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    if any(row['email'] == new_data['email'] for row in csv_reader):
        print("Error: Email address already exists in the CSV file.")
    else:
        # Reset the file position to the beginning before writing
        csv_file.seek(0)
        # Insert the new data into the CSV file
        with open(file_path, "a", newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if csv_file.tell() == 0:
                # Write header only if the file is empty
                csv_writer.writeheader()
            csv_writer.writerow(new_data)

# Check if the email already exists in the 'clientDb' table
cursor.execute("SELECT email FROM clientDb WHERE email = %s",
               (new_data['email'],))
if cursor.fetchone():
    print("Error: Email address already exists in the system.")
else:
    # Insert the new data into the 'clientDb' table
    insert_query = """
        INSERT INTO clientDb (full_name, first_name, last_name, title, organization_name, email, linkedin, twitter)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    data_values = (
        new_data['full_name'],
        new_data['first_name'],
        new_data['last_name'],
        new_data['title'],
        new_data['organization_name'],
        new_data['email'],
        new_data['linkedin'],
        new_data['twitter']
    )

    cursor.execute(insert_query, data_values)
    print("Data saved successfully.")

# Commit the changes and close the connection
con.commit()
cursor.close()
con.close()
