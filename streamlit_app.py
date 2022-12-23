import streamlit
streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Bluebery Oatmeal')
streamlit.text('🥗 Kale,Spinach and Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

