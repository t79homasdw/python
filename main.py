#Modules
# from functions import get_todos, write_todos
from modules import functions
import time

#Variables
todos_local = []
todos_list = []
todos = functions.get_todos()

#Time
print("The time is below:")
print("Today is", time.strftime("%A, %B %d, %Y %H:%M:%S"))

while True:
    user_action = input("Type add, show, edit, remove, exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = input("Enter your to do: ")
        todos.append(todo)

    elif user_action.startswith("show"):
        print([element.capitalize() for element in todos])
        for index, item in enumerate(todos):
            print(f"{index + 1} {'-'} {item.title()}")

    elif user_action.startswith("edit"):
        try:
            for index, item in enumerate(todos):
                print(f"{index + 1} {'-'} {item.title()}")
            number = int(input("Please choose your item number to edit: ")) - 1
            todos[number] = input("Enter new to do: ")
        except IndexError:
            print("Invalid item number. Please choose a valid number.")
            continue

    elif user_action.startswith("remove"):
        try:
            for index, item in enumerate(todos):
                print(f"{index + 1} {'-'} {item.title()}")
            number = int(input("Please choose your item number to remove: ")) - 1
            todos.pop(number)
            print([element.title() for element in todos])
        except IndexError:
            print("Invalid item number. Please choose a valid number.")
            continue

    elif user_action.startswith("exit"):
        for item in todos:
            todos_list.append(item.title() + "\n")
        print("Saving todos...")
        functions.write_todos(todos_list)
        print("Goodbye!")
        exit()

    else:
        print("Invalid command")
