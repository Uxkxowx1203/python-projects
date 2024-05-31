import streamlit as st
import plotly.express as px
from backend import get_days
st.title("Weather forecast for the next few days")
place=st.text_input("Place :")
days=st.slider("Forecast days", min_value=1,max_value=5, help="Number of forecasted days")
option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
    filtered_data=get_days(place,days,option)
    if option=="Temperature":
        temperature=[dict["main"]["temp"] for dict in filtered_data]
        dates=[dict["dt_txt"] for dict in filtered_data]
        figure=px.line(x=dates,y=temperature,labels={"X": "Days", "Y": "Temperatures (C)"})
        st.plotly_chart(figure)
    if option=="Sky":
        images={"Clear":"/home/test/Desktop/python/Weatherforecast/images/clear.png",
                "Clouds":"/home/test/Desktop/python/Weatherforecast/images/cloud.png",
                "Rain":"/home/test/Desktop/python/Weatherforecast/images/rain.png",
                "Snow":"/home/test/Desktop/python/Weatherforecast/images/snow.png" }
        
        sky_conditions=[dict["weather"][0]["main"] for dict in filtered_data]  
        img_path=[images[condition] for condition in sky_conditions]
        st.image(img_path,width=115)
