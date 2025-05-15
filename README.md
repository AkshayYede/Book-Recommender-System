# 📚 Book Recommender System

A machine learning-based web application that recommends books to users based on their input. Built using Python, Pandas, Scikit-learn, and Streamlit. This project uses collaborative filtering and popularity-based techniques to generate recommendations.

---

## 🚀 Features

* 📖 Recommend books based on a user's favorite book
* 🌟 Display top 50 most popular books
* 🧠 Uses cosine similarity and vectorization for recommendations
* 💻 Clean, responsive UI using HTML and Bootstrap
* 🗃️ EDA performed on Books, Ratings, and Users datasets

---

## 📂 Dataset

The project uses the [Book-Crossing Dataset]([http://www2.informatik.uni-freiburg.de/~cziegler/BX/](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) which consists of three files:

* `books.csv` — Book metadata (Title, Author, Year, Publisher, Image URLs)
* `users.csv` — User demographic info (User ID, Location, Age)
* `ratings.csv` — Ratings assigned by users (User ID, ISBN, Book-Rating)

---

## 📊 EDA Highlights

* Analyzed book publication trends, top publishers, and top-rated books
* Cleaned user age and location data
* Separated implicit and explicit ratings
* Identified most active users and most rated books

---

## 🧠 Recommendation Logic

* **Popularity-Based**: Top 50 books based on number of ratings and average rating
* **Collaborative Filtering**: Cosine similarity between book vectors using CountVectorizer/Tfidf
