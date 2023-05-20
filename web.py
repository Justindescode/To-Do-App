import streamlit as st
import functions

todos = functions.get_todos()



def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("I hope you enjoy this app as much as I enjoyed developing it!:)")
st.write("This app is to increase your productivity. ")


for todo in todos:
    option = st.checkbox(todo)


st.text_input(label="", placeholder="Add a new todo....",
              on_change=add_todo, key='new_todo')

st.session_state