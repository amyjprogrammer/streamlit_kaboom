#importing Libraries

import streamlit as st 
import pandas as pd

st.title('Harry Potter Statistics')

st.markdown('''
This app performs simple webscraping of Harry Potter character stats.
* **Python libraries: **base64, pandas, streamlit
* **Data Source: **[Harry-Potter-reference.com](https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset)            
''')

#Web scraping for Character info
@st.cache   
def load_data():
    url = "https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset"
    html = pd.read_html(url, header=0)

#Sidebar- Pick gender
st.sidebar.header('User Input Features')
pick_gender = ['Male', 'Female']
selected_gender= st.sidebar.selectbox('Gender', pick_gender, pick_gender)

