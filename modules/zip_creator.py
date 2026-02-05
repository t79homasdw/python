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

def decompress_file(source_file, destination_folder):
    try:
        if not pathlib.Path(destination_folder).exists():
            pathlib.Path(destination_folder).mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(source_file, "r") as zipf:
            zipf.extractall(destination_folder)

    except FileNotFoundError:
        sg.popup("File not found.")
    return