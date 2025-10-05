# README  

## Assignment Overview  
This assignment involves analyzing the CORD-19 research dataset and building a simple Streamlit application to present the findings. The focus is on fundamental data analysis, visualization, and creating an interactive web application.  

## Learning Objectives  
By completing this assignment, you will:  
- Practice loading and exploring a real-world dataset.  
- Learn basic data cleaning techniques.  
- Create meaningful visualizations.  
- Build a simple interactive web application.  
- Present data insights effectively.  

## Dataset Information  
The dataset used is `metadata.csv` from the CORD-19 dataset, which contains information about COVID-19 research papers, including:  
- Paper titles and abstracts.  
- Publication dates.  
- Authors and journals.  
- Source information.  

You can download the dataset from Kaggle: [CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).  

## Required Tools  
- Python 3.7+  
- Libraries: `pandas`, `matplotlib`, `seaborn`, `streamlit`  
- Jupyter Notebook (optional for exploration)  

Install the required packages:  
```bash  
pip install pandas matplotlib seaborn streamlit  
```  

## Steps to Run the Assignment  

### 1. Data Loading and Exploration  
- Download the `metadata.csv` file from the CORD-19 dataset.  
- Load the data into a pandas DataFrame.  
- Explore the dataset by checking dimensions, data types, missing values, and basic statistics.  

### 2. Data Cleaning and Preparation  
- Handle missing data by removing or filling missing values.  
- Convert date columns to datetime format and extract the year for analysis.  
- Create additional columns if needed (e.g., abstract word count).  

### 3. Data Analysis and Visualization  
- Analyze the data to count papers by publication year, identify top journals, and find frequent words in titles.  
- Create visualizations such as:  
    - Publications over time.  
    - Bar chart of top publishing journals.  
    - Word cloud of paper titles.  
    - Distribution of paper counts by source.  

### 4. Streamlit Application  
- Build a Streamlit app with the following structure:  
    - Title and description.  
    - Interactive widgets (e.g., sliders, dropdowns).  
    - Display visualizations and a sample of the data.  

Example code snippet for the app:  
```python  
import streamlit as st  
import pandas as pd  
import matplotlib.pyplot as plt  

st.title("CORD-19 Data Explorer")  
st.write("Simple exploration of COVID-19 research papers")  

# Add interactive elements  
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))  
# Add visualizations based on selection  
```  

### 5. Documentation and Reflection  
- Add comments to your code for clarity.  
- Write a brief report summarizing your findings.  
- Reflect on challenges faced and lessons learned.  

## Submission  
- Upload your work to a GitHub repository named `Frameworks_Assignment`.  
- Submit the GitHub repository URL for evaluation.  

## Evaluation Criteria  
- **Complete Implementation (40%)**: All tasks completed.  
- **Code Quality (30%)**: Readable, well-commented code.  
- **Visualizations (20%)**: Clear and appropriate charts.  
- **Streamlit App (10%)**: Functional and interactive application.  

## Tips for Success  
- Start with a subset of the data if the full file is too large.  
- Focus on the basics and debug incrementally.  
- Use documentation and seek help when needed.  

By completing this assignment, you will gain hands-on experience with the data science workflow and build a functional Streamlit application.  