import pandas as pd
import numpy as np                # for scientific computing
import matplotlib.pyplot as plt
from scipy.stats import linregress
#%%
#reading Dataset
imdb_data= pd.read_csv("/home/ubuntu/Desktop/Assignment/Movie-Review-Sentiment-Analysis/imdb_1000.csv")
#%%
#With best public review or with critics rating
sorted_imdb_data = imdb_data.sort_values(by='star_rating', ascending=False)

# Display the top-rated movies (e.g., top 10)
top_rated_movies = sorted_imdb_data.head(10)
print(top_rated_movies)
