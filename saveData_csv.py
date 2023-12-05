import pandas as pd
from sqlalchemy import create_engine


# Database connection URL (using SQLite for example)
db_url = "sqlite:///your_database.db"

# CSV file path
csv_file_path = "/Users/sopiokvantaliani/PythonApplications/Project2/data.csv"

# Create a SQLAlchemy engine
engine = create_engine(db_url, echo=True)

# Read CSV into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Define the table structure (customize this based on your database schema)
table_name = "customers_data"
df.to_sql(table_name, engine, if_exists="append", index=False, chunksize=1000)
