import streamlit as st
from modules import functions

st.title("Welcome to My Todo App")
st.subheader("Add your tasks here:")
st.write("This is app is to help you manage your tasks.")
todos_list = functions.get_todos()

def add_todo():
    """Adds a new to-do item to the list and updates the text file."""
    todo = st.session_state["new_todo"]
    for i, item in enumerate(todos_list):
        todos_list[i] = item.title() + "\n"
    todos_list.append(todo.title() + "\n")
    functions.write_todos(todos_list)

for todo in todos_list:
    st.checkbox(todo)

todo_input = st.text_input(label="Enter a new task:",
                           placeholder="Add a new task...",
                           on_change=add_todo,
                           key="new_todo")


add_task_button = st.button(label="Add Task")

st.session_state

