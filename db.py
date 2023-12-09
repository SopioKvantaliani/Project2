
import csv
import psycopg2
from psycopg2 import sql
from psycopg2 import connect, sql


# Establish connection to DB
con = connect(
    host="localhost",
    database="ClientDataBase",
    user="postgres",
    password="Giorgi2008!",
    port=5432  # it's optional
)

cursor = con.cursor()

# Create the table if it doesn't exist
create_table_query = sql.SQL("""
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
""")
cursor.execute(create_table_query)

# Insert data from CSV into the table
with open('/Users/sopiokvantaliani/PythonApplications/Project2/data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        insert_query = sql.SQL("""
            INSERT INTO clientDb (full_name, first_name, last_name, title, organization_name, email, linkedin, twitter)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """)
        cursor.execute(insert_query, (
            row['full_name'],
            row['first_name'],
            row['last_name'],
            row['title'],
            row['organization_name'],
            row['email'],
            row['linkedin'],
            row['twitter']
        ))

# Commit changes to the database
con.commit()

try:
    cursor.execute(insert_query, (
        # ... values here
    ))
    con.commit()
except Exception as e:
    print(f"Error: {e}")


# Execute a query to fetch and print data
cursor.execute("SELECT full_name, email FROM clientDb")
rows = cursor.fetchall()
for r in rows:
    print(f"Full Name: {r[0]} Email: {r[1]}")

# Close the cursor and connection
cursor.close()
con.close()
