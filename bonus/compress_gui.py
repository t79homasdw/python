import datetime
import FreeSimpleGUI as sg
from modules import zip_creator
import pathlib
import os
import zipfile
import io

# Labels
af_label = sg.Text("Select a file to compress")
des_label = sg.Text("Enter destination folder")
success_label = sg.Text(key="success", text_color="green", visible=False)
fail_label = sg.Text(key="fail", text_color="red", visible=False)

# Inputs Boxes
af_input = sg.InputText(tooltip="Select a file", key="files")
des_input = sg.InputText(tooltip="Enter destination folder", key="folder")

# Buttons
af_button = sg.FilesBrowse("Add File",tooltip="Select a file")
des_button = sg.FolderBrowse("Add Destination",tooltip="Enter destination folder")
cp_button = sg.Button("Compress")
exit_button = sg.Exit("Exit")

layout = [[af_label, af_input, af_button],
          [des_label, des_input, des_button],
          [cp_button, exit_button, success_label, fail_label]]

window = sg.Window('File Zipper', layout=layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Compress":
        filenames = (values['files'].strip("\n")).split(";")
        extension = filenames[0].split(".")
        extension = len(extension[-1]) + 1
        destination_folder = values['folder'].strip("\n")
        zip1 = os.path.basename(filenames[0])
        zip_filename = destination_folder + "/" + zip1[:-extension] + ".zip"
        zip_creator.compress_file(filenames, zip_filename)

        window["success"].update("The file has been compressed successfully.", visible=True)
        sg.popup("File compressed successfully.")
        window["files"].update("")
        window["folder"].update("")
window.close()