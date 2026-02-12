import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['input_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    del st.session_state[tod]



st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app si to increase my productivity")


for index, tod in enumerate(todos):
    checkbox = st.checkbox(tod, key=tod)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[tod]
        st.rerun()

st.text_input(label="",
              placeholder="Add new todo:",
              on_change=add_todo,
              key='input_todo'
              )

