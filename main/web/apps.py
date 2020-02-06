from django.apps import AppConfig
import pandas


class WebConfig(AppConfig):
    name = 'web'
    RELATIONAL_DATA = pandas.read_csv(
        'main/recommender/models/relational.csv', index_col=0)
