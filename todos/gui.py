import f
import PySimpleGUI as ps
import time
import os
if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass
ps.theme("DarkTeal2")
clock=ps.Text('',key="clock")
label=ps.Text("Type in a TODO")
input_box=ps.InputText(tooltip="Enter a TODO", key="TODO")
add_button=ps.Button("Add")
list_box=ps.Listbox(values=f.get_todos(),
                    key="todos",
                    enable_events=True, size=[45,10])
edit_button=ps.Button("Edit")
complete_button=ps.Button("Complete")
exit_button=ps.Button("Exit")
window=ps.Window('My TODO App', 
                layout=[[clock],[label],
                        [input_box,add_button],
                        [list_box,edit_button, complete_button],
                        [exit_button]],
                font=('Helvetica',20))
while True:
    event,value =window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(value)
    match event:
        case "Add":
            todos=f.get_todos()
            new_todos=value['TODO']+"\n"
            todos.append(new_todos)
            f.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit=value['todos'][0]
                new_todos=value['TODO']
                todos=f.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todos
                f.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                ps.popup("Please select an item first")

        case "Complete":
            try:    
                todo_to_complete=value["todos"][0]
                todos=f.get_todos()
                todos.remove(todo_to_complete)
                f.write_todos(todos)
                window['todos'].update(values=todos)
                window['TODO'].update(value='')
            except IndexError:
                ps.popup("Please select an item first")
        case "Exit":
            break
        case "todos":
            window['TODO'].update(value['todos'][0])

        case ps.WIN_CLOSED:
            break
            _


window.close()