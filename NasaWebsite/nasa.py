import streamlit as st
import requests

api_key="4695F4AYgc5PjYh0rIkyAibfjHPxbHuoVb1rJ0Zp"
url="https://api.nasa.gov/planetary/apod?api_key=4695F4AYgc5PjYh0rIkyAibfjHPxbHuoVb1rJ0Zp"

request=requests.get(url)

data=request.json()



image=data["url"]
explanation=data["explanation"]
title=data["title"]

image_filepath = "img.png"
response2 = requests.get(image)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)