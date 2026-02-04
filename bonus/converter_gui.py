import time
import FreeSimpleGUI as sg
import os
import zipfile

# Labels
ft_label = sg.Text("Enter feet:")
in_label = sg.Text("Enter inches:")
meters_label = sg.Text(key="meters", text_color="green", visible=False)

# Inputs Boxes
ft_input = sg.InputText(tooltip="feet", key="ft", default_text="0")
in_input = sg.InputText(tooltip="inches", key="in", default_text="0")

# Buttons
conv_button = sg.Button("Convert", tooltip="Convert Feet and Inches to Meters")
exit_button = sg.Exit("Exit")


layout = [[ft_label, ft_input],
          [in_label, in_input],
          [conv_button, meters_label, exit_button]]

window = sg.Window('Feet and Inches Converter', layout=layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Convert":
        ft = float(values["ft"])
        in_ = float(values["in"])
        meters = ft * 0.3048 + in_ * 0.0254
        window["meters"].update(f"{meters:.3f} m", visible=True)
        sg.popup(f"{ft} feet and {in_} inches is equal to {meters:.3f} meters.")
        window["ft"].update("")
        window["in"].update("")
        window["meters"].update(visible=False)
window.close()


