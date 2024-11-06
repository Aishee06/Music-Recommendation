import streamlit as st
import pickle
import pandas as pd
import requests

# Fetch Poster Function (Removed since we're replacing posters with emojis)
def fetch_poster(music_title):
    return "🎶"  # Returning a simple music emoji instead of a poster

# Recommendation Function
def recommend(musics):
    music_index = music[music['title'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_music = []
    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommended_music.append(music_title)
    return recommended_music

# Load Data
music_dict = pickle.load(open('E:\\Documents\\Code\\Music-Recommendation\\musicrec.pkl', 'rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open('E:\\Documents\\Code\\Music-Recommendation\\similarities.pkl', 'rb'))

# Streamlit Title and Header
st.set_page_config(page_title="🎶 Music Recommendation System 🎵", page_icon="🎧")
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #FF6347;
        text-align: center;
    }
    .button {
        background-color: #FF6347;
        color: white;
        border-radius: 10px;
        font-size: 18px;
        padding: 12px 24px;
        border: none;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        transition: background-color 0.3s ease;
    }
    .button:hover {
        background-color: #FF4500;
    }
    .recommender {
        text-align: center;
        margin-top: 30px;
    }
    .song-title {
        font-size: 16px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #888;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for music selection with emoji
st.sidebar.header("🎶 **Select your favorite music!**")
selected_music_name = st.sidebar.selectbox('🎧 Choose a music you like', music['title'].values)

# Recommendation Button with emoji
if st.sidebar.button('🔍 **Recommend Similar Music** 🔍', key='recommend_button'):
    names = recommend(selected_music_name)

    # Displaying the recommendation section with emojis and more color
    st.markdown("<h2 style='color:#FF6347;'>🎤 Discover the Tunes You’ll Love 🎶</h2>", unsafe_allow_html=True)
    st.write("✨ Discover your next favorite track with a personalized playlist just for you! ✨")

    # Display recommendations on different lines, each on a new line with emoji
    for name in names:
        st.markdown(f"🎶 **{name}** 🎧")
        st.write("---")