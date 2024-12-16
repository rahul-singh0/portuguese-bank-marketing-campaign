from sqlalchemy import create_engine
import pandas as pd

# Connection Details
database_url = 'postgresql://postgres@localhost:5432/bank_campaign_data'

# Create a connection engine to the SQL database
engine = create_engine(database_url)

# SQL query to fetch all data from the cleaned table
query = "SELECT * FROM bank_marketing_campaign"

# Load the cleaned data into a pandas DataFrame
df = pd.read_sql(query, engine)
print(df.head())

# Check for missing values in the dataset
missing_values = df.isnull().sum()
print(missing_values)

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# List of all categorical columns in the dataset
categorical_columns = ['job', 'education', 'marital', 'default', 'housing', 'loan', 
                       'contact', 'month', 'day_of_week', 'poutcome', 'y']

# Check for unique values in each categorical column
for column in categorical_columns:
    print(f"Unique values in {column}: {df[column].unique()}")

categorical_columns = ['job', 'education', 'marital', 'default', 'housing', 'loan', 
                       'contact', 'month', 'day_of_week', 'poutcome', 'y']

# Check for leading or trailing spaces in all categorical columns
rows_with_spaces = df[categorical_columns].apply(lambda x: x.str.strip() != x).any(axis=1)

# Display rows with leading or trailing spaces
print(df[rows_with_spaces])