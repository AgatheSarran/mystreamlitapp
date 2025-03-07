import requests
import streamlit as st
import numpy as np

st.set_page_config(page_title="Hello", page_icon=":sunny:")

st.markdown("# This page is awesome! 🌅")

if st.button("Click :)"):
    st.image("raw_data/le_wagon.png")


st.write(st.secrets["a_new_section"]['new_spell'])

query = st.text_input("Search a GIF")
url = "https://api.giphy.com/v1/gifs/search"
params={"api_key": st.secrets.api_key, "q": query, "limit": 10}
response = requests.get(url= url, params=params).json()

while not query:
    st.stop()

gif_url = response['data'][np.random.randint(0,10)]['embed_url']
st.write(
    f'<iframe src="{gif_url}" width="480" height="240">',
    unsafe_allow_html=True
)
