from django.apps import AppConfig

import pandas


class RecommenderConfig(AppConfig):
    name = 'recommender'
    COLLAB_FILTER = pandas.read_csv(
        'main/recommender/models/ratings_merged.csv', index_col=0)
    CORR_MATRIX = pandas.read_csv(
        'main/recommender/models/movie_based_collaborative_filtering.csv', index_col=0)
    TOP_30_SIMILARITY_MODEL = pandas.read_csv(
        'main/recommender/models/movie_to_movie_similarity_matrix.csv', index_col=0)

    def ready(self):
        # from . import movies_based_on_item_item_collaborative_filtering
        # from . import movies_from_movie_based_on_movie
        # from . import movies_from_movie_based_on_poster
        # from . import movies_from_movie_based_on_user
        # from . import user_to_user_similarity
        # movies_based_on_item_item_collaborative_filtering.setup()
        # movies_from_movie_based_on_movie.setup()
        # movies_from_movie_based_on_poster.setup()
        # movies_from_movie_based_on_user.setup()
        # user_to_user_similarity.setup()
        pass
