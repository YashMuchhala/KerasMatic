from django.shortcuts import render
import pandas

from recommender import movies_based_on_item_item_collaborative_filtering
from recommender import movies_from_movie_based_on_movie, arya
from .apps import WebConfig as config


def index(request):

    movie = request.GET.get(
        'search', "Casper (1995)")
    filter_type = request.GET.get('type', 'collaborative')
    print(movie)
    movie_id = config.RELATIONAL_DATA[config.RELATIONAL_DATA['title']
                                      == movie]['movieId']
    if len(movie_id.tolist()) == 0:
        movie_id = 100
    else:
        movie_id = movie_id.tolist()[0]
    USER_ID = 4
    # movie_recommendations_1 = movies_based_on_item_item_collaborative_filtering.predict(
    #     USER_ID)

    # movie_recommendations_2_preds = movies_from_movie_based_on_movie.predict(
    #     movie_id)
    movie_recommendations_2_preds = arya.predict(movie, filter_type)
    x = movie_recommendations_2_preds.index
    movie_recommendations_2_preds = []
    for i in x:
        movie_recommendations_2_preds.append(i)

    mr2_data = []
    for mr2 in movie_recommendations_2_preds:

        x = config.RELATIONAL_DATA[config.RELATIONAL_DATA['title'] == mr2]

        if len(x['title'].values.tolist()) == 0 or len(x['img_url'].values.tolist()) == 0:
            continue
        mr2_data.append({
            "title": x['title'].values.tolist()[0],
            "url": x['img_url'].values.tolist()[0]
        })

    context = {
        "movie_recommendations_1": mr2_data,
        "user_id": USER_ID,
    }
    return render(request, 'web/index.html', context=context)


def splash(request):
    context = {
        "starter_movies": [
            {
                "title": "Treasure Island (1950)",
                "url": "https://m.media-amazon.com/images/M/MV5BMWMzZDM5ZTEtNDY2Yi00NjhjLTkwZjgtYjQ2MjVlMGZhYmQ2XkEyXkFqcGdeQXVyNjUwMzI2NzU@._V1_UY268_CR1,0,182,268_AL__QL50.jpg",
            },
            {
                "title": "Godfather, The (1972)",
                "url": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL__QL50.jpg",
            },
            {
                "title": "Reservoir Dogs (1992)",
                "url": "https://m.media-amazon.com/images/M/MV5BZmExNmEwYWItYmQzOS00YjA5LTk2MjktZjEyZDE1Y2QxNjA1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
            },
            {
                "title": "Pulp Fiction (1994)",
                "url": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR1,0,182,268_AL__QL50.jpg",
            },
            {
                "title": "Star Wars: Episode IV - A New Hope (1977)",
                "url": "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
            },
            {
                "title": "Silence of the Lambs, The (1991)",
                "url": "https://m.media-amazon.com/images/M/MV5BNjNhZTk0ZmEtNjJhMi00YzFlLWE1MmEtYzM1M2ZmMGMwMTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
            },
            {
                "title": "Reservoir Dogs (1992)",
                "url": "https://m.media-amazon.com/images/M/MV5BZmExNmEwYWItYmQzOS00YjA5LTk2MjktZjEyZDE1Y2QxNjA1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
            },
            {
                "title": "Pulp Fiction (1994)",
                "url": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR1,0,182,268_AL__QL50.jpg",
            },
        ]
    }
    return render(request, 'web/splash.html', context=context)
