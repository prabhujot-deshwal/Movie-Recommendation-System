import streamlit as st
import pickle
import requests
import time

# Load similarity.pkl from Hugging Face
url = "https://huggingface.co/Prabhujot-Deshwal/movie-model-files/resolve/main/similarity.pkl"
response = requests.get(url)
similarity = pickle.loads(response.content)

# Load movies locally
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

@st.cache_data(ttl=86400)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=04af6d28d255b80cebb2f78ab18aa67b&language=en-US"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                poster_path = data.get('poster_path')
                if poster_path:
                    return "https://image.tmdb.org/t/p/w500/" + poster_path
                else:
                    return "https://via.placeholder.com/500x750.png?text=No+Poster"
            else:
                print("API Error:", response.status_code)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed:", e)
            time.sleep(1)

    return "https://via.placeholder.com/500x750.png?text=Error"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []

    for i in movies_list_sorted:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Enter your Favourite Movie',
    movies_list
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
