import streamlit as st
import pandas
import requests
import snowflake.connector

st.title("My first page")
st.header("🥗 Breakfast Menu")
st.text("🐔 Omega 3 and Blueberry")
st.text("🥑 Bread Jam with Avocado")
st.text("🍞 Poha")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input("What is the choice of fruit?","kiwi")
st.write("User entered",fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
fruityvice_normalised = pandas.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalised)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
st.header("The fruit load list contains")
st.dataframe(my_data_row)

added_fruit = st.text_input("What fruit would you like to add?","jackfruit")
st.write("Thanks for chhosing ", added_fruit)



