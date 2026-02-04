import datetime
import FreeSimpleGUI as sg
import os
import zipfile
import io

def compress_file(source_files, zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            for file in source_files:
                zipf.write(file.strip("\n"), os.path.basename(file.strip("\n")))
    except FileNotFoundError:
        sg.popup("File not found.")
    return

# Labels
af_label = sg.Text("Select a file to compress")
des_label = sg.Text("Enter destination folder")

# Inputs Boxes
af_input = sg.InputText(tooltip="Select a file", key="file")
des_input = sg.InputText(tooltip="Enter destination folder", key="folder")

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
        filenames = (values['file'].strip("\n")).split(";")
        destination_folder = values['folder'].strip("\n")
        zip1 = os.path.basename(filenames[0])
        zip_filename = destination_folder + "/" + zip1[:-4] + ".zip"
        compress_file(filenames, zip_filename)

window.close()