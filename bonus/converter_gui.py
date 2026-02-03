import time
import FreeSimpleGUI as sg
import os
import zipfile

# Labels
ft_label = sg.Text("Enter feet:")
in_label = sg.Text("Enter inches:")

# Inputs Boxes
ft_input = sg.InputText(tooltip="feet")
in_input = sg.InputText(tooltip="inches")

# Buttons
conv_button = sg.Button("Convert",tooltip="Convert Feet and Inches to Meters")
exit_button = sg.Exit("Exit")


layout = [[ft_label, ft_input],
          [in_label, in_input],
          [conv_button, exit_button]]


window = sg.Window('Converter', layout=layout)
event, values = window.read()
window.close()

