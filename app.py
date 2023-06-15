import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl", "rb"))
similar = pickle.load(open("similarity.pkl", "rb"))
movie_title = movies["title"].values


st.header("MOVIE RECOMMENDATION")
movie_selected = st.selectbox("Select Movie", movie_title)

def recommend(movie_name):
    index = movies[movies["title"] == movie_name].index[0]
    distance = sorted(list(enumerate(similar[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

if st.button("Show"):
    movie_names = recommend(movie_selected)

    st.write("Recommended Movies:")
    for movie_name in movie_names:
        st.text(movie_name)
