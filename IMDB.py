import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shan",
    database="imdb_2024_genres",
    autocommit=True
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM test")
data = mycursor.fetchall()
mycursor.close()
mydb.close()

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Movie Name', 'Rating', 'Voting', 'Duration', 'Genre'])

Nav_session = st.sidebar.radio('IMDb Insights *2024*', ['Home', 'Genre Analysis', 'Duration Insights', 'Voting Trends', 'Rating distribution'])

if Nav_session == 'Home':
    st.image('D:/Guvi_Project/IMDB_ST/Image/IMDb_BrandBanner_1920x425.jpg',use_container_width = True)
    st.header('IMDB 2024 Data Scraping and Visualizations')
    st.write("""This project focuses on extracting and analyzing movie data from IMDb for the year 2024. The task involves scraping data such as movie names, genres, ratings, voting counts, and durations from IMDb's 2024 movie list using Selenium. The data will then be organized genre-wise, saved as individual CSV files, and combined into a single dataset stored in an SQL database. Finally, the project will provide interactive visualizations and filtering functionality using Streamlit to answer key questions and allow users to customize their exploration of the dataset.""")

    # Display the DataFrame
    st.write("Here, click the button to view the data that are scrapped from the IMDb website.")
    if st.button("cilck me 😊"):
        st.dataframe(df, hide_index=True,use_container_width = True)
        

elif Nav_session == 'Genre Analysis':
    st.write("Here, we are giving the insights of the data based on the genre.")
    st.write("1. Identify the unique genres in the dataset.")
    st.write("2. Visualize the distribution of movies across genres using a bar plot.") #find count
    st.write("3. Calculate the average rating and voting count for each genre.")         
    st.write("4. Display the top 5 genres based on average rating")         
    st.write("5. Display the top 5 genres based on highest voting count")         
    
    
elif Nav_session == 'Duration Insights':
    st.write("Here, we are giving the insights of the data based on the duration.")
    st.write("1. Analyze the average duration of movies across genres.")
    st.write("2. Analyze the relationship between movie duration and rating.")
    st.write("3. Identify the longest and shortest movies in the dataset.")
    st.write("4. Display the top 5 genres with the longest duration.")
    st.write("5. Display the top 5 genres with the shortest duration.")
    
    
elif Nav_session == 'Voting Trends':
    st.write("Here, we are giving the insights of the data based on the voting trends.")
    st.write("1. Analyze the relationship between movie duration and voting count.")
    st.write("2. Identify the movies with the highest voting counts.")
    st.write("3. Display the top 5 movies with the highest voting counts.") 
    st.write("4. Display the top 5 movies with the lowest voting counts.")
    st.write("5. Visualize the voting distribution using a histogram along with genres.")
    
    
elif Nav_session == 'Rating distribution':
    st.write("Here, we are giving the insights of the data based on the rating distribution.")
    st.write("1. Analyze the relationship between movie rating and voting count.")
    st.write("2. Identify the movies with the highest and lowest ratings.")
    st.write("3. Display the top 5 genres with the highest rating.")
    st.write("4. Display the top 5 genres with the lowest rating.")
    st.write("5. Visualize the voting distribution using a histogram along with ratings.")
    
    
else:
    st.write("Error! Please select a valid option from the sidebar.")