IMDb 2024 Data Scraping and Visualizations

Project Overview
This project focuses on extracting and analyzing movie data from IMDb for the year 2024. The process involves:

Data Extraction: Scraping movie information using Selenium.
Data Organization: Categorizing data by genre and saving it as individual CSV files.
Data Integration: Combining the CSV files into a SQL database.
Data Visualization: Providing interactive visualizations and filtering functionality using Streamlit.

Repository Structure:
Main_File.ipynb: Jupyter Notebook for data extraction, cleaning, and storage.
IMDB.py: Python script for data visualization using Streamlit.
IMDb Project.pptx: Presentation summarizing the project's objectives, methodologies, and findings.
genre_combined_df.csv: Combined dataset of all genres.
genre_df_cleaned.csv: Cleaned dataset ready for analysis.
IMDb_BrandBanner_1920x425.jpg: Brand banner image used in the Streamlit app.
Setup and Installation
Clone the Repository:
git clone https://github.com/Shanchai-bit/IMDB-2024-Data-Scraping-and-Visualizations.git
cd IMDB-2024-Data-Scraping-and-Visualizations
Install Dependencies: Ensure you have Python installed. Then, install the required packages:
pip install -r requirements.txt
Database Configuration: Set up a MySQL database named imdb_2024_genres. Update the database credentials in the scripts as needed.

Usage
Data Extraction and Cleaning: Run Main_File.ipynb to scrape data from IMDb, clean it, and store it in the database.
Data Visualization: Execute IMDB.py to launch the Streamlit application:
streamlit run IMDB.py
Navigate through the app to explore various visualizations and insights.

Features
Advanced Title Search: Filter movies based on genre, rating, duration, and votes.
Genre Analysis: Explore the distribution and average ratings of movies across different genres.
Duration Insights: Analyze the relationship between movie duration and other factors like ratings and votes.
Voting Trends: Examine how voting patterns vary with different movie attributes.
Rating Distribution: Visualize how ratings are distributed across genres and identify top-rated movies.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

License
This project is licensed under the MIT License.
