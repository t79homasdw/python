import json
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)
total_questions = len(data)

for index, question in enumerate(data):
    clear_screen()
    print(f"{index+1}. {question['question_txt']} \n" )
    for i, alternative in enumerate(question["alternatives"]):
        print(f"{i+1}. {alternative}")
    answer = int(input("Press choose an answer: "))
    question["user_choice"] = answer
    print("\n")

clear_screen()
score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        print(f"Correct!\n")
        print(f"Your answer is for:\n{question['question_txt']}: {question['alternatives'][question['user_choice'] - 1]}")
        print(f"The correct answer is: {question['correct_answer']} - {question['alternatives'][index]}")
        score = score + 1

    else:
        print("Incorrect!\n")
        print(f"Your answer is for:\n{question['question_txt']}: {question['alternatives'][question['user_choice'] - 1]}")
        print(f"The correct answer is: {question['correct_answer']} - {question['alternatives'][index]}")

print(f"\nYour score is {score} / {total_questions}")
