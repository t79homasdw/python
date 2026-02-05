import time
import FreeSimpleGUI as sg
from modules import zip_creator
import pathlib
import os
import zipfile
import io

sg.theme("Black")

# Labels
sc_label = sg.Text("Select a file to decompress:")
dest_label = sg.Text("Enter destination folder:")

success_label = sg.Text(key="success", text_color="green", visible=False)
fail_label = sg.Text(key="fail", text_color="red", visible=False)

# Inputs Boxes
sc_input = sg.InputText(tooltip="Select a file", key="file")
dest_input = sg.InputText(tooltip="Enter destination folder", key="folder")

# Buttons
sc_button = sg.FileBrowse("Add Zip File",tooltip="Select a file",file_types=(("Zip Files", "*.zip"),("All Files", "*.*")), target="file")
dest_button = sg.FolderBrowse("Add Destination",tooltip="Enter destination folder where to decompress the file", target="folder")

dec_button = sg.Button("Extract", key="Decompress")
exit_button = sg.Exit("Exit")

col1 = sg.Column([[sc_label], [dest_label]])
col2 = sg.Column([[sc_input], [dest_input]])
col3 = sg.Column([[sc_button], [dest_button]])
col4 = sg.Column([[dec_button, exit_button,success_label, fail_label]])

layout = [
    [col1, col2, col3],
    [col4]
]

window = sg.Window('Extract Archive',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Decompress":
        filename = (values['file'].strip("\n"))
        destination_folder = (values['folder'].strip("\n"))
        zip_creator.decompress_file(filename, destination_folder)

        window["success"].update("The file has been decompressed successfully.", visible=True)
        sg.popup("File decompressed successfully.")
        window["file"].update("")
        window["folder"].update("")
window.close()