from django.shortcuts import render
import pandas

from recommender import movies_based_on_item_item_collaborative_filtering
from recommender import movies_from_movie_based_on_movie, arya
from .apps import WebConfig as config


def index(request):

    movie = request.GET.get(
        'search', "Jumanji (1995)")
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
