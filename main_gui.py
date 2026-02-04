from modules import functions
import time
import FreeSimpleGUI as sg

label = sg.Text("Type in a to do")
input_box = sg.InputText(tooltip="Enter your to do", key="todo")
list_box = sg.Listbox(values=functions.get_todos(),
                     key='todos',
                     enable_events=True,
                     size=[45, 10])

add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")
exit_button = sg.Exit("Exit")


layout = [
    [label],
    [input_box, add_button],
    [list_box, edit_button, remove_button, exit_button]
]

window = sg.Window('My To Do App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read()

    # Reload current todos from file/function for each loop iteration
    todos = [(item.title()).strip("\n") for item in functions.get_todos()]
    todos_list = [(item.title()).strip() + "\n" for item in todos]

    match event:
        case "Add":
            new_todo = values['todo'].strip()
            if new_todo:
                todos_list.append(new_todo.title() + "\n")
                functions.write_todos(todos_list)

                # Update the Listbox with the new list of todos
                window['todos'].update(values=todos_list)
        case "Edit":
            try:
                if values['todos']:
                    todo_to_edit = (((values['todos'][0]).title()).strip("\n"))
                    index = todos.index(todo_to_edit)
                    new_todo = (values['todo']).strip() + "\n"
                    todos_list[index] = new_todo.title()
                    functions.write_todos(todos_list)
                    window['todos'].update(values=todos_list)
                else:
                    sg.popup("Please select a todo item to edit.")
            except ValueError:
                sg.popup("Todo not found. Please check the input.")
        case "Remove":
            try:
                if values['todos']:
                    todo_to_remove = (((values['todos'][0]).title()).strip("\n"))
                    index = todos.index(todo_to_remove)
                    todos_list.pop(index)
                    functions.write_todos(todos_list)
                    window['todos'].update(values=todos_list)
                else:
                    sg.popup("Please select a todo item to remove.")
            except ValueError:
                sg.popup("Todo not found. Please check the input.")
        case "todos":
            window['todo'].update(((values['todos'][0]).title()).strip("\n"))
        case "Exit" | sg.WIN_CLOSED:
            break
print("Goodbye!")
window.close()
