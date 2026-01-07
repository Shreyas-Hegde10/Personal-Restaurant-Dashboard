import sqlite3 
import pandas as pd

# Loading dataframe
df = pd.read_csv('restaurants.csv')

# Data cleanup(replacing 'N/A' values with None)
df = df.replace('N/A', None) 
df['restaurant_id'] = df.index + 1  # Adding a unique restaurant ID

# Creating SQLite database and connection 
conn = sqlite3.connect('restaurants.db') 

# Load dataframe into SQLite database 
df.to_sql('restaurants', conn, if_exists='replace', index=False)

# Verifying data insertion
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM restaurants")
count = cursor.fetchone()[0]
print(f"✅ Successfully inserted {count} records into the 'restaurants' table in 'restaurants.db'")

# Closing the connection
conn.close()



