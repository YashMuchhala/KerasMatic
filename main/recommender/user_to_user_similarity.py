import pandas

TOP_30_SIMILARITY_MODEL = pandas.DataFrame()


def setup():
    TOP_30_SIMILARITY_MODEL = pandas.read_csv(
        'main/recommender/models/user_to_user_similarity_matrix.csv', index_col=0)


def predict(movie_title):
    predictions = TOP_30_SIMILARITY_MODEL['userId'].values
    return predictions
