import csv
import os
import psycopg2

path = '/Users/sopiokvantaliani/PythonApplications/Project2'
file_path = os.path.join(path, "data.csv")

# Check if the file exists, create it if not
if not os.path.isfile(file_path):
    with open(file_path, "w", newline='', encoding='utf-8') as file:
        fieldnames = ['full_name', 'first_name', 'last_name', 'title',
                      'organization_name', 'email', 'linkedin', 'twitter']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

# Get input from the user
new_data = {}
print("Enter the following details:")
for field in ['full_name', 'first_name', 'last_name', 'title', 'organization_name', 'email', 'linkedin', 'twitter']:
    new_data[field] = input(f"{field.capitalize()}: ")

# Establish a connection to the PostgreSQL database
con = psycopg2.connect(
    host="localhost",
    database="ClientDataBase",
    user="postgres",
    password="Giorgi2008!",
    port=5432
)

cursor = con.cursor()

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
