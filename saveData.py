import csv
import os


# Replace this with the actual path where your 'data.csv' file is located
path = '/Users/sopiokvantaliani/PythonApplications/Project2'
path2 = '/Users/sopiokvantaliani/PythonApplications/Project2'

file_path = os.path.join(path, "data.csv")
with open(file_path, "r", encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        full_name = row['full_name']
        first_name = row['first_name']
        last_name = row['last_name']
        title = row['title']
        organization_name = row['organization_name']
        email = row['email']
        linkedin = row['linkedin']
        twitter = row['twitter']

        # Print or process the extracted values as needed
        print(f"Full Name: {full_name}, First Name: {first_name}, Last Name: {last_name}, Title: {
              title}, Organization: {organization_name}, Email: {email}, LinkedIn: {linkedin}, Twitter: {twitter}")
