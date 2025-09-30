🎬 Movie Recommendation System A content-based movie recommendation system that suggests movies based on their similarity. Built with Python, Pandas, and Scikit-learn.

✨ Features Content-Based Filtering: Recommends movies by analyzing plot keywords, genres, cast, and crew.

Interactive UI: A simple web interface built with Streamlit to easily find movie recommendations.

TMDb Dataset: Utilizes the rich "TMDb 5000 Movie Dataset".

🚀 How It Works The recommendation logic is based on content-based filtering.

Data Preprocessing: Movie metadata (genres, keywords, cast, crew) is combined into a single text-based "tags" feature.

Vectorization: The "tags" for all movies are converted into numerical vectors using the TF-IDF (Term Frequency-Inverse Document Frequency) technique.

Similarity Calculation: The cosine similarity is computed between the vectors of all movies to determine how similar they are to each other.

Recommendation: When you select a movie, the system finds the movies with the highest cosine similarity scores and recommends them.

🛠️ Setup & Run Follow these steps to get the project running on your local machine.

Prerequisites:

Python 3.8 or higher

pip

Clone the Repository
Bash

git clone https://github.com/prabhujot-deshwal/Movie-Recommendation-System.git cd Movie-Recommendation-System 2. Install Dependencies

Bash

pip install -r requirements.txt 3. Run the Application

Bash

streamlit run app.py Now, open your web browser and navigate to http://localhost:8501.

📂 Project Files app.py: The main script to run the Streamlit web application.

Movie_Recommend_System.ipynb: Jupyter Notebook detailing the data cleaning, model building, and analysis process.

movies.pkl: A serialized file containing the pre-processed movie data and similarity matrix for the app.

requirements.txt: A list of required Python packages.

tmdb_5000_*.csv: The raw dataset files.
