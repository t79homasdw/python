dir_name = "output"
file_name = "todos.txt"

if __name__ != "__main__":
    file_path = f"{dir_name}/{file_name}"
else:
    file_path = f"../{dir_name}/{file_name}"

print(file_path)
print(__name__)

def get_todos(filepath_l = file_path):
    """Reads a text file and returns the list of to-do items."""
    with open(filepath_l, "r") as file:
        todos_local = file.readlines()
    return [item.strip('\n') for item in todos_local]

def write_todos(todos_arg, filepath_l = file_path):
    """Writes a list of to-do items into a text file."""
    with open(filepath_l, "w") as file:
        file.writelines([item for item in todos_arg])

if __name__ == "__main__":
    for index, item in enumerate(get_todos()):
        print(f"{index + 1} {'-'} {item.title()}")
else:
    print("Functions module imported successfully.")