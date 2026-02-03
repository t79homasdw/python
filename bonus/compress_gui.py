import datetime
import FreeSimpleGUI as sg
import os
import zipfile
import io

def test_compress_file():
    source_file = "test.txt"
    destination_folder = "test_folder"
    compress_file()
    assert os.path.exists(os.path.join(destination_folder, os.path.basename(source_file) + ".zip"))

def compress_file():
    source_file = af_input.get()
    destination_folder = des_input.get()

    if len(source_file) == 0 or len(destination_folder) == 0:
        sg.popup("Please select a file and destination folder.")
        return
    elif len(source_file) == 1:
        sg.popup("Please select a file.")
        try:
            with zipfile.ZipFile(os.path.join(destination_folder, os.path.basename(source_file) + ".zip"), "w") as zipf:
                zipf.write(source_file, os.path.basename(source_file))
        except FileNotFoundError:
            sg.popup("File not found.")
        return
    elif len(source_file) > 1:
        try:
            for file in source_file:
                with zipfile.ZipFile(os.path.join(destination_folder, os.path.basename(source_file[0]) + ".zip"), "w") as zipf:
                    zipf.write(file, os.path.basename(file))
        except FileNotFoundError:
            sg.popup("File not found.")
        return


# Labels
af_label = sg.Text("Select a file to compress")
des_label = sg.Text("Enter destination folder")

# Inputs Boxes
af_input = sg.InputText(tooltip="Select a file")
des_input = sg.InputText(tooltip="Enter destination folder")

# Buttons
af_button = sg.FilesBrowse("Add File",tooltip="Select a file")
des_button = sg.FolderBrowse("Add Destination",tooltip="Enter destination folder")
cp_button = sg.Button("Compress")
exit_button = sg.Exit("Exit")

layout = [[af_label, af_input, af_button],
          [des_label, des_input, des_button],
          [cp_button, exit_button]]

window = sg.Window('File Zipper', layout=layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Compress":
        compress_file()
window.close()