from modules import functions
import time
import FreeSimpleGUI as sg

label = sg.Text("Type in a to do")
input_box = sg.InputText(tooltip="Enter your to do")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")
exit_button = sg.Button("Exit")


layout = [[label], [input_box, add_button, edit_button, remove_button, exit_button]]

window = sg.Window('My To Do App', layout=layout)
event, values = window.read()
window.close()
