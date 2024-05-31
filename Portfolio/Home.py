import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2= st.columns(2)

with col1:
    st.image("/home/test/Desktop/python/Portfolio/images/photo.png")
with col2:
    st.title("Amritash Sharma")
    content="""My name is Amritash. """
    st.info(content)
col3,empty_col, col4=st.columns([1.5,0.5,1.5])
df =pd.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.info(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
        

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.info(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

