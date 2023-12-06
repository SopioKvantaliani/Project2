import csv
import os

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

# Check if the email already exists
with open(file_path, "r", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['email'] == new_data['email']:
            print("Error: Email address already exists in the system.")
            break
    else:
        # Write the new data to the CSV file
        with open(file_path, "a", newline='', encoding='utf-8') as file:
            fieldnames = ['full_name', 'first_name', 'last_name', 'title',
                          'organization_name', 'email', 'linkedin', 'twitter']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the new data
            writer.writerow(new_data)

        print("Data saved successfully.")
