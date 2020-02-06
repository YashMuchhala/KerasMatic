import pandas

from .apps import RecommenderConfig as config


def predict(movie_id):
    predictions = config.TOP_30_SIMILARITY_MODEL.loc[movie_id].values

    return predictions
