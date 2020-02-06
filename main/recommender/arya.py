import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys


def predict(movie_title='Jumanji (1995)', filter_type='collaborative'):
    movies = pd.read_csv(
        'main/recommender/input/ml-latest-small/ml-latest-small/movies.csv')
    #genome_scores = pd.read_csv('ml-20m/genome-scores.csv')
    tags = pd.read_csv(
        'main/recommender/input/ml-latest-small/ml-latest-small/tags.csv')
    #genome_tags = pd.read_csv('ml-20m/genome-tags.csv')
    # Use ratings data to downsample tags data to only movies with ratings
    ratings = pd.read_csv(
        'main/recommender/input/ml-latest-small/ml-latest-small/ratings.csv')

    movies.tail()
    movies['genres'] = movies['genres'].str.replace('|', ' ')

    ratings_f = ratings.groupby('userId').filter(lambda x: len(x) >= 55)

    # list the movie titles that survive the filtering
    movie_list_rating = ratings_f.movieId.unique().tolist()

    movies = movies[movies.movieId.isin(movie_list_rating)]

    Mapping_file = dict(zip(movies.title.tolist(), movies.movieId.tolist()))
    tags.drop(['timestamp'], 1, inplace=True)
    ratings_f.drop(['timestamp'], 1, inplace=True)
    mixed = pd.merge(movies, tags, on='movieId', how='left')
    mixed.fillna("", inplace=True)
    mixed = pd.DataFrame(mixed.groupby('movieId')['tag'].apply(
        lambda x: "%s" % ' '.join(x)))
    Final = pd.merge(movies, mixed, on='movieId', how='left')
    Final['metadata'] = Final[['tag', 'genres']].apply(
        lambda x: ' '.join(x), axis=1)

    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(Final['metadata'])
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), index=Final.index.tolist())

    from sklearn.decomposition import TruncatedSVD
    svd = TruncatedSVD(n_components=200)
    latent_matrix = svd.fit_transform(tfidf_df)
    # plot var expalined to see what latent dimensions to use
    explained = svd.explained_variance_ratio_.cumsum()

    n = 200
    latent_matrix_1_df = pd.DataFrame(
        latent_matrix[:, 0:n], index=Final.title.tolist())

    ratings_f1 = pd.merge(movies[['movieId']],
                          ratings_f, on="movieId", how="right")

    ratings_f2 = ratings_f1.pivot(
        index='movieId', columns='userId', values='rating').fillna(0)

    from sklearn.decomposition import TruncatedSVD
    svd = TruncatedSVD(n_components=200)
    latent_matrix_2 = svd.fit_transform(ratings_f2)
    latent_matrix_2_df = pd.DataFrame(
        latent_matrix_2,
        index=Final.title.tolist())

    explained = svd.explained_variance_ratio_.cumsum()

    from sklearn.metrics.pairwise import cosine_similarity
    # take the latent vectors for a selected movie from both content
    # and collaborative matrixes
    a_1 = np.array(latent_matrix_1_df.loc[movie_title]).reshape(1, -1)
    a_2 = np.array(latent_matrix_2_df.loc[movie_title]).reshape(1, -1)

    # calculate the similartity of this movie with the others in the list
    score_1 = cosine_similarity(latent_matrix_1_df, a_1).reshape(-1)
    score_2 = cosine_similarity(latent_matrix_2_df, a_2).reshape(-1)

    # an average measure of both content and collaborative
    hybrid = ((score_1 + score_2)/2.0)

    # form a data frame of similar movies
    dictDf = {'content': score_1, 'collaborative': score_2, 'hybrid': hybrid}
    similar = pd.DataFrame(dictDf, index=latent_matrix_1_df.index)

    # sort it on the basis of either: content, collaborative or hybrid,
    # here : content
    similar.sort_values(filter_type, ascending=False, inplace=True)

    return similar[1:].head(10)
