import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

movies_df = pd.read_csv('/Users/mason/Desktop/Python_Practice/movies.csv')
links_df = pd.read_csv('/Users/mason/Desktop/Python_Practice/links.csv')
tags_df = pd.read_csv('/Users/mason/Desktop/Python_Practice/tags.csv')
ratings_df = pd.read_csv('/Users/mason/Desktop/Python_Practice/ratings.csv')


#Using regular expressions to find a year stored between parentheses
#We specify the parantheses so we don't conflict with movies that have years in their titles
movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))',expand=False)
#Removing the parentheses
movies_df['year'] = movies_df.year.str.extract('(\d\d\d\d)',expand=False)
#Removing the years from the 'title' column
movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '')
#Applying the strip function to get rid of any ending whitespace characters that may have appeared
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
display(movies_df.head())

# splitting the values in genre into a list of genres
movies_df['genres'] = movies_df.genres.str.split('|')
display(movies_df['genres'].head())

#now genres are stored as a list inside the dataframe; using one hot encoding technique to convert the list of genres to a vector
#where each column corresponds to one possible value of the feature.

moviesWithGenres_df = movies_df.copy()

for index, row in movies_df.iterrows():
    for genre in row['genres']:
        moviesWithGenres_df.at[index, genre] = 1
moviesWithGenres_df = moviesWithGenres_df.fillna(0)
display(moviesWithGenres_df.head())

#now looking at ratings file
display(ratings_df.head())

#dropping timestamp column from dataframe because it is not needed
ratings_df = ratings_df.drop('timestamp', 1)


#starting our recommender system by creating variable userinput with movies that have been watched by the user
user_input = [
    {'title': 'Breakfast Club, The', 'rating':5},
    {'title': 'Toy Story', 'rating':3.5},
    {'title': 'Jumanji', 'rating':2},
    {'title': 'Pulp Fiction', 'rating':5},
    {'title': 'Akira', 'rating':4.5}
    
     ]
inputMovies = pd.DataFrame(user_input)

#next we will extract the movie ID number from the movies dataframe and add them into our input movies dataframe

#filtering out movies by title
inputId = movies_df[movies_df['title'].isin(inputMovies['title'].tolist())]
inputMovies = pd.merge(inputId, inputMovies)
#dropping genres and years from dataframe
inputMovies = inputMovies.drop('genres', 1).drop('year', 1)
display(inputMovies.head())

#getting the subset of movies that the input has watched from the dataframe containing genres defined with binary values
userMovies = moviesWithGenres_df[moviesWithGenres_df['movieId'].isin(inputMovies['moviedId'].tolist())]

#cleaning the data by resetting the index and dropping movieId, title, genres, and year columns
userMovies = userMovies.reset_index(drop=True)
userGenreTable = userMovies.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)
display(userGenreTable)

#now to start learning the user's preferences; to do this we will turn each genre into weights using the dot product
userProfile = userGenreTable.transpose().dot(inputMovies['rating'])

#now that we have the user profile with weights corresponding to each movie genre, we can recommend movies from the
#original movie list dataframe

#creating genre table and removing unecessary information
genreTable = moviesWithGenres_df.set_index(moviesWithGenres_df['movieId'])
genreTable = genreTable.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)

#now we will multiply the genres by the weights and then take the weighted average
recommendationTable_df = ((genreTable * userProfile).sum(axis=1)) / (userProfile.sum())

recommendationTable_df = recommendationTable_df.sort_values(ascending=False)

#now that we have a table with weights corresponding to each movie Id, we create a final table with movie names
display(movies_df.loc[movies_df['movieId'].isin(recommendationTable_df.head(20).keys())])






