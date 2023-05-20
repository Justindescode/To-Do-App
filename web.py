import streamlit as st
import functions


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("I hope you enjoy this app as much as I enjoyed developing it!:)")
st.write("This app is to increase your productivity. ")


for todo in todos:
    option = st.checkbox(todo)


st.text_input(label="", placeholder="Add a new todo...")