# app.py - Streamlit Application
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re

st.title("CORD-19 Data Explorer")
st.write("A simple interactive exploration of COVID-19 research papers from the metadata dataset.")

# Load data (assume metadata.csv is in the same directory)
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', nrows=20000)  # Sample for app speed
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract'] = df['abstract'].fillna('')
    return df

df = load_data()

# Sidebar for filters
st.sidebar.header("Filters")
min_year = st.sidebar.slider("Min Year", 2019, 2022, 2019)
max_year = st.sidebar.slider("Max Year", 2019, 2022, 2022)
filtered_df = df[(df['year'] >= min_year) & (df['year'] <= max_year)]

# Display sample data
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'authors', 'journal', 'year']].head(10))

# Interactive visualizations
st.subheader("Visualizations")

# Publications by year
year_counts = filtered_df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values)
ax1.set_title('Publications by Year')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Papers')
st.pyplot(fig1)

# Top journals
if not filtered_df.empty:
    top_journals = filtered_df['journal'].value_counts().head(5)
    fig2, ax2 = plt.subplots()
    top_journals.plot(kind='bar', ax=ax2)
    ax2.set_title('Top 5 Journals')
    ax2.set_xlabel('Journal')
    ax2.set_ylabel('Number of Papers')
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

    # Word cloud based on titles in range
    def get_words(text):
        words = re.findall(r'\b\w+\b', str(text).lower())
        return [w for w in words if len(w) > 3]

    all_title_words = []
    for title in filtered_df['title']:
        all_title_words.extend(get_words(title))

    word_freq = Counter(all_title_words)
    if word_freq:
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
        fig3, ax3 = plt.subplots()
        ax3.imshow(wordcloud, interpolation='bilinear')
        ax3.set_title('Word Cloud of Titles')
        ax3.axis('off')
        st.pyplot(fig3)

st.write("Explore the trends in COVID-19 research publications interactively!")