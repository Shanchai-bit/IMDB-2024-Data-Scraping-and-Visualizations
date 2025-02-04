import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sqlalchemy import create_engine



st.title('IMDB 2024 Data Scraping and Visualizations')
st.header('movie data')
st.subheader('Data Scraping')
st.write("All movie data was scraped from IMDB's website using the selenium library in Python. The data was then cleaned and saved as a CSV file.")

# Create a database connection
engine = create_engine("mysql+mysqldb://root:shan@localhost:3306/imdb_2024_genres")

# Using Pandas to read the SQL query directly
query = "SELECT * FROM imdb_2024_genres.test"
df = pd.read_sql(query, con=engine)

# Display DataFrame in Streamlit
st.write(df['Movie Name'])
