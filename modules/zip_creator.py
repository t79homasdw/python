import zipfile
import FreeSimpleGUI as sg
import os
import pathlib

def compress_file(source_files, zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            for file in source_files:
                zipf.write(file.strip("\n"), os.path.basename(file.strip("\n")))
    except FileNotFoundError:
        sg.popup("File not found.")
    return

