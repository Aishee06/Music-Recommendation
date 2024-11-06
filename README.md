# Music Recommendation System 🎶🎧

This is a personalized **Music Recommendation System** built using Streamlit, Pandas, and Python. The web app suggests similar music based on the song you like. The system leverages a pre-trained similarity model to recommend tracks that match your taste and helps you discover new music based on your current preferences.

## Features ✨

- **Personalized Recommendations:** Based on your favorite track, the app suggests a list of similar songs.
- **Streamlined User Interface:** Easy-to-navigate interface powered by Streamlit, perfect for discovering your next favorite song!

## Technologies Used 🛠️

- **Streamlit:** To create an interactive and responsive web app.
- **Pandas:** For data manipulation and handling the music dataset.
- **Pickle:** For loading pre-trained models and datasets.
- **Requests:** For API integration to fetch music recommendations.

## How to Run the Project 🚀

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- Streamlit
- Pandas
- Requests
- Pickle

### Steps to Run:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Aishee06/Music-Recommendation.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run run.py
   ```

4. Open your browser and go to `http://localhost:8501` to access the Music Recommendation app.

## How It Works ⚙️

1. **Music Selection:** Users can select a song they like from the sidebar.
2. **Recommendation Engine:** When the user clicks the "Recommend Similar Music" button, the system fetches the most similar tracks based on a pre-trained similarity model.
3. **Display Results:** The app displays a list of recommended songs on the main page.
---
Get ready to groove with personalized music picks just for you! 🎶🎧💫

