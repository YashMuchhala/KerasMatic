# Movies similar to a SPECIFIC movie

import pandas

CORR_MATRIX = pandas.DataFrame()


def setup():
    CORR_MATRIX = pandas.read_csv(
        'main/recommender/models/movie_based_collaborative_filtering.csv')


def get_similar_movies(movie_name, rating):

    if movie_name in CORR_MATRIX.columns:
        similar_ratings = CORR_MATRIX[movie_name] * (rating - 2.5)
        similar_ratings = similar_ratings.sort_values(ascending=False)
        return similar_ratings
    else:
        return []


def predict(list_of_movies):
    predictions = []

    try:
        for movie, rating in list_of_movies:
            predictions.append(get_similar_movies(movie, rating))
        return predictions
    except:
        return [[]]
