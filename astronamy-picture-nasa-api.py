import requests
import streamlit as st

# NASA URL
url = 'https://api.nasa.gov/planetary/apod?api_key=dgLSbydaXgTp0JxeosW9BXtbBVkKKHThNajupAH3'
response = requests.get(url)
request_data = response.json()
title  = request_data['title']
image_text = request_data['explanation']
image_url = request_data['url']

# st.set_page_config(layout='wide')
st.title(title)

# col = st.columns(1)
# with col:
st.image(image_url)
st.write(image_text)


