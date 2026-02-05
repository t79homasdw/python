from modules import functions
import time
import FreeSimpleGUI as sg

sg.theme("Black")

label_clock = sg.Text('', key='clock')
label = sg.Text("Type in a to do")
input_box = sg.InputText(tooltip="Enter your to do", key="todo")
list_box = sg.Listbox(values=functions.get_todos(),
                     key='todos',
                     enable_events=True,
                     size=[45, 10])

add_button = sg.Button("Add", size=[10, 1])
edit_button = sg.Button("Edit", size=[10, 1])
remove_button = sg.Button("Remove", size=[10, 1])
exit_button = sg.Exit("Exit", size=[10, 1])

left_column = sg.Column([
    [label],
    [input_box],
    [list_box]
])
right_column = sg.Column([
    [add_button],
    [edit_button],
    [remove_button],
    [exit_button]
])

layout = [
    [label_clock],
    [left_column, right_column]
]

window = sg.Window('My To Do App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))

    # Reload current todos from file/function for each loop iteration
    todos = [(item.title()).strip("\n") for item in functions.get_todos()]
    todos_list = [(item.title()).strip() + "\n" for item in todos]

    match event:
        case "Add":
            try:
                new_todo = values['todo'].strip()
                if new_todo != "":
                    todos_list.append(new_todo.title() + "\n")
                    functions.write_todos(todos_list)

                    # Update the Listbox with the new list of todos
                    window['todos'].update(values=todos_list)
                    window['todo'].update("")
                else:
                    sg.popup("Invalid input. Please enter a valid to-do item.", font=('Helvetica', 20))
            except ValueError:
                sg.popup("Invalid input. Please enter a valid to-do item.", font=('Helvetica', 20))
        case "Edit":
            try:
                if values['todos']:
                    todo_to_edit = (((values['todos'][0]).title()).strip("\n"))
                    index = todos.index(todo_to_edit)
                    new_todo = (values['todo']).strip() + "\n"
                    todos_list[index] = new_todo.title()
                    functions.write_todos(todos_list)
                    window['todos'].update(values=todos_list)
                    window['todo'].update("")
                else:
                    sg.popup("Please select a todo item to edit.", font=('Helvetica', 20))
            except ValueError:
                sg.popup("Todo not found. Please check the input.", font=('Helvetica', 20))
        case "Remove":
            try:
                if values['todos']:
                    todo_to_remove = (((values['todos'][0]).title()).strip("\n"))
                    index = todos.index(todo_to_remove)
                    todos_list.pop(index)
                    functions.write_todos(todos_list)
                    window['todos'].update(values=todos_list)
                    window['todo'].update("")
                else:
                    sg.popup("Please select a todo item to remove.", font=('Helvetica', 20))
            except ValueError:
                sg.popup("Todo not found. Please check the input.", font=('Helvetica', 20))
        case "todos":
            window['todo'].update(((values['todos'][0]).title()).strip("\n"))
        case "Exit" | sg.WIN_CLOSED:
            exit()
            break
window.close()
