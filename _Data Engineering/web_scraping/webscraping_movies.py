import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3


# Initialization of known entities

# URL of the website
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0 # Counter for the number of movies

# Loading the webpage for Webscraping

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

