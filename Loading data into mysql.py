#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[11]:


import pandas as pd
from sqlalchemy import create_engine

# Database connection details
username = 'your_username'
password = 'your_password'
host = 'your_host'
port = 3306
database = 'your_database_name'

# Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Load dataset into Pandas DataFrame
file_path = 'Path to your data'
df = pd.read_csv(file_path)

# Upload dataset to MySQL
table_name = 'your_table_name'
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Verify the upload
with engine.connect() as connection:
    result = connection.execute(f"SELECT * FROM {table_name} LIMIT 5;")
    for row in result:
        print(row)




# In[ ]:




