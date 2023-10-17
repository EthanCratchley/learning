import pandas as pd
from sqlalchemy import create_engine

# Step 3: Load data into DataFrame
# Replace with the actual path to your CSV file
csv_file_path = r'/path/to/your/csvfile.csv'  
df = pd.read_csv(csv_file_path)  

# Step 4: Create SQLAlchemy Engine
# Replace these with your actual MySQL credentials
username = 'your_username'
password = 'your_password'
server = 'localhost'
database_name = 'your_database_name'
engine = create_engine(f'mysql+pymysql://{username}:{password}@{server}/{database_name}')

# Step 5: Write Data to MySQL
# Replace 'your_table_name' with the actual name of your table
table_name = 'your_table_name'
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Print a success message
print(f"Data from {csv_file_path} has been written to {table_name} table in {database_name} database.")
