import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Bluebery Oatmeal')
streamlit.text('🥗 Kale,Spinach and Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)
# Create repeatable code as function

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else :
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()

# Display fruit list from API call in a table
# do not run anything past here while we troubleshoot
streamlit.header("The fruit load list contains:")
#snowflake related functions
def get_fruit_load_list():
        with my_cnx.cursor() as my_cur:
             my_cur.execute("SELECT * FROM fruit_load_list")
             return my_cur.fetchall()

#add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

# allow end user to add a fruit to the list

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('" + fruit_choice + "')")
        return "Thanks fro adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)
#streamlit.write('The user entered ', fruit_choice2)
#streamlit.write('Thanks for adding ', fruit_choice2)

#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

