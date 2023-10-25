import streamlit as st
import pandas

st.title("My first page")
st.header("🥗 Breakfast Menu")
st.text("🐔 Omega 3 and Blueberry")
st.text("🥑 Bread Jam with Avocado")
st.text("🍞 Poha")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)


