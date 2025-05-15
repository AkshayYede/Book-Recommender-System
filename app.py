import streamlit as st
import pickle
import numpy as np

# Load data
popular_df = pickle.load(open('popularity.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_score.pkl','rb'))

st.set_page_config(page_title="Book Recommender System", layout="wide")

# Title centered and bold
st.markdown(
    """
    <h1 style='text-align: center; font-weight: bold; margin-bottom: 1rem;'>
        Book Recommender System
    </h1>
    """, unsafe_allow_html=True
)

# Persistent session state to hold selected page
if 'page' not in st.session_state:
    st.session_state['page'] = 'top50'

def select_page(page):
    st.session_state['page'] = page

# Two clickable options stacked vertically
if st.button("Top 50 Books"):
    select_page('top50')

if st.button("Recommend Books"):
    select_page('recommend')

def show_top_books():
    st.subheader("Top 50 Books")
    cols = st.columns(4)
    for idx in range(len(popular_df)):
        col = cols[idx % 4]
        with col:
            st.image(popular_df.iloc[idx]['Image-URL-M'], use_container_width=True)
            st.markdown(f"**{popular_df.iloc[idx]['Book-Title']}**")
            st.markdown(f"*Author: {popular_df.iloc[idx]['Book-Author']}*")
            st.markdown(f"Votes: {popular_df.iloc[idx]['num_ratings']}")
            st.markdown(f"Rating: {popular_df.iloc[idx]['avg_ratings']}")

def recommend_books(book_name):
    if book_name not in pt.index:
        st.warning("Book not found in our database. Please try another.")
        return
    
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    st.subheader(f"Books similar to '{book_name}':")
    cols = st.columns(5)
    for idx, i in enumerate(similar_items):
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        book = temp_df.iloc[0]
        col = cols[idx % 5]
        with col:
            st.image(book['Image-URL-M'], use_container_width=True)
            st.markdown(f"**{book['Book-Title']}**")
            st.markdown(f"*Author: {book['Book-Author']}*")

# Show content based on selected page
if st.session_state['page'] == 'top50':
    show_top_books()
else:
    st.subheader("Recommend Books")
    user_input = st.text_input("Enter a book name:")
    if st.button("Recommend"):
        recommend_books(user_input)