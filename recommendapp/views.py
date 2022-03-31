# loading libraries
import json
from django.shortcuts import render
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.contrib.auth.decorators import login_required

# Reading csv file
movie_data = pd.read_csv('F:/PROJECT MOVIE/movie-recommendation-app/recommendapp/movie_datasets.csv')


def Make_Recommend():
    selected_features = ['genre', 'crew']
    print(selected_features)

    combined_features = movie_data['genre'] + ' ' + ['crew']
    # print(combined_features)

    # TfidfVectorizer Term frequency inverse document frequency is a text vectorizer that transforms the text into a
    # usable vector.

    vectorizer = TfidfVectorizer()
    feature_vector = vectorizer.fit_transform(combined_features)
    print("This is feature vector")
    # print(feature_vector)

    print("Now getting similarity")
    similarity = cosine_similarity(feature_vector)
    # print(similarity)
    return similarity


def input_form(request):
    # print("value")
    # using json fle to display data in home screen
    with open('F:/PROJECT MOVIE/movie-recommendation-app/recommendapp/datasets.json') as file_object:
        movie_datas = json.load(file_object)[0:24]
        context = {
            'data': movie_datas
        }
        return render(request, 'form.html', context)


@login_required(login_url='login')
def read_input(request):
    similarity = Make_Recommend()
    x = request.POST['val']
    title_list = movie_data['title'].to_list()
    # print(title_list)

    # difflib ->helps us find the similarity between two sequences and
    # get_close_matches->if you give a list of string  it will give the top result that are similar to the given string.

    find_close_match = difflib.get_close_matches(x, title_list)
    if len(find_close_match) != 0:
        close_match = find_close_match[0]
        index_of_movie = movie_data[movie_data.title == close_match].index.values[0]
        response = "Started"
        if index_of_movie == 0:
            response = ""
        else:
            print("Finding similarity of the best match movies")
            similarity_score = list(enumerate(similarity[index_of_movie]))
            print(similarity_score)

            print("Sorting the movie based on similarity score")
            sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
            display = sorted_similar_movies[1:8]
            print(sorted_similar_movies)
            # print("Movie suggested for you are:\n")
            i = 1
            required_movie_array = []
            for movie in display:
                # loc[] is used to retrieve the data  in terms of row and column and iloc[] is used to retrieve the data
                # in terms of row and column but here it  is Index based data selecting method.
                # iloc[ rows, column]
                # eg:iloc[0:4,0:7] note:last index value is not considered we will get the value from 0 to 3 in rows.

                required_movie_array.append(movie_data.iloc[movie[0:1]])
            # response = "".join(str(re) for re in required_movie_array)
            # response = " ".join([str(x) for x in required_movie_array])
            # response = "".join(map(str, required_movie_array))
            response = required_movie_array
            return render(request, "home.html", {"data": response})
    else:
        response = x
    return render(request, "notfound.html", {"data": response})


def print_hi(request):
    # movie_data = pd.read_csv('F:/movieapp/recommendapp/recommendapp/movie_datasets.csv')
    # movie_data = pd.read_json('F:/movieapp/recommendapp/recommendapp/movie_datasets.json')
    with open('F:/PROJECT MOVIE/movie-recommendation-app/recommendapp/datasets.json') as file_object:
        movie_datas = json.load(file_object)
        print(movie_datas)
        context = {
            'data': movie_datas
        }
        return render(request, 'form.html', context)
