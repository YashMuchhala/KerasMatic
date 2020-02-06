import pandas
from .apps import RecommenderConfig as config


# def setup():
#     config.COLLAB_FILTER = pandas.read_csv(
#         'main/recommender/models/ratings_merged.csv', index_col=0)


def get_similar_movies(movie_name, rating):

    if movie_name in config.CORR_MATRIX.columns:
        similar_ratings = config.CORR_MATRIX[movie_name] * (
            rating - 2.5)
        similar_ratings = similar_ratings.sort_values(ascending=False)
        return similar_ratings
    else:
        return pandas.Series()


def movies_from_movie_based_on_user(list_of_movies):
    predictions = []
    # try:
    for movie, rating in list_of_movies:
        predictions.append(get_similar_movies(movie, rating))
    return predictions
    # except:
    #     return [[]]


def predict(user_id):
    try:
        df_user = config.COLLAB_FILTER[config.COLLAB_FILTER["userId"] == user_id]
        df_user1 = df_user[["title", "rating"]]
        df_list = df_user1.values.tolist()
        df_user2 = []

        for x in df_list:
            df_user2.append(tuple(x))
        return movies_from_movie_based_on_user(df_user2)
    except:
        return [[]]
