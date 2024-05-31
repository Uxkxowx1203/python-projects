import streamlit as st
import f
todos=f.get_todos()

def add_todo():
    todo=st.session_state["value"]+"\n"
    todos.append(todo)
    f.write_todos(todos)


st.title("My Todo app")
st.subheader("This is my todo list")
st.write("This app increases our productivity")

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()




text=st.text_input(label="", placeholder="Add a new todo"
                   ,key='value',on_change=add_todo)



