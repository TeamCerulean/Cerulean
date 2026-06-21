#Known Issues
#001 - Pycharm accepts keyboard input while TTS is speaking, will be solved when GUI is added

import random
import json
from datetime import datetime
import win32com.client
import msvcrt

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def save_memory():
    with open("memory.json", "w") as f:
        json.dump(memory, f)

VERSION = "v0.06"

def speak(text):
        print(f"Cerulean: {text}")
        speaker.Speak(str(text))

try:
    with open("memory.json", "r") as f:
        memory = json.load(f)
except FileNotFoundError:
    memory = {}

print(f"""====================
Cerulean
Learning Without End
{VERSION}
====================""")

def quit_command():
    print("Exiting Cerulean...")
    exit()

def info_command():
    speak("Cerulean:  Cerulean is an AI assistant designed for students and startups. The main focus of Cerulean is to help your dreams that seem impossible come true. It is a work in progress and will be updated regularly.")

def version_command():
    speak(VERSION)

def time_command():
    current = datetime.now()
    speak( current.strftime("%H:%M:%S"))

def date_command():
    current = datetime.now()
    speak(current.strftime("%Y-%m-%d"))

def help_command():
    speak("Available commands:")
    print("           /quit - Exit the program")
    print("           /info - Get information about Cerulean")
    print("           /version - Get the current version of Cerulean")
    print("           /time - Get the current time")
    print("           /date - Get the current date")
    print("           /help - Show this help message")
    print("           /setname - Set your name")
    print("           /name - Get your saved name")
    print("           /setsubjects - Set your subjects")
    print("           /subjects - Get your saved subjects")
    print("           /setgoal - Set your goal")
    print("           /goal - Get your saved goal")
    print("           /profile - See your Cerulean profile")
    print("           /tasks - Get your saved tasks")
    print("           /finishtask - Finish your tasks")
    print("           /settask - Set your tasks")
    print("           /sing - Makes Cerulean sing a song")

def setname_command():
    name = input("Enter your name: ")
    memory["name"] = name
    save_memory()
    speak("Name saved.")

def name_command():
    name = memory.get("name")
    if name:
        speak(f"Your name is {name}.")
    else:
        speak("You haven't set your name yet. Use /setname to set it.")

def setsubjects_command():
    subjects = input("Enter your subjects: ")
    memory["subjects"] = subjects.split(", ")
    save_memory()
    speak("Subjects saved.")

def subjects_command():
    subjects = memory.get("subjects")
    if subjects:
        speak(f"Your subjects are {subjects}.")
    else:
        speak("You haven't set your subjects yet. Use /setsubjects to set them.")

def setgoal_command():
    goal = input("Enter your goal: ")
    memory["goal"] = goal
    save_memory()
    speak("Goal saved.")

def goal_command():
    goal = memory.get("goal")
    if goal:
        speak(f"Your goal is to {goal}.")
    else:
        speak("You haven't set your goal. Use /setgoal to set it.")

def settask_command():
    task = input("Enter your task: ")

    if "tasks" not in memory:
        memory["tasks"] = []

    memory["tasks"].append(task)

    save_memory()
    speak("Task saved.")

def tasks_command():
    tasks = memory.get("tasks")

    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        speak("You haven't set any tasks yet. Use /settask to set one.")

def finishtask_command():
    tasks = memory.get("tasks")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    speak("What task did you finish?")

    choice = int(input("Enter task number: "))

    completed = tasks.pop(choice - 1)

    save_memory()

    speak(f"Completed task: {completed}.")

def deletetask_command():
    tasks = memory.get("tasks")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    speak("What task did you want to delete?")

    choice = int(input("Enter task number: "))

    deleted = tasks.pop(choice - 1)

    save_memory()

    speak(f"Removed task: {deleted}.")

def sing_command():
    speak("Twinkle, twinkle, little star,")
    speak("How I wonder what you are!")
    speak("Up above the world so high,")
    speak("Like a diamond in the sky!")
    speak("Twinkle, twinkle, little star,")
    speak("How I wonder what you are!")

def profile_command():
    name = memory.get("name", "Not set")
    goal = memory.get("goal", "Not set")
    subjects = memory.get("subjects", "Not set")

    print("===== Cerulean Profile ====================================")

    print(f"Name: {name}")
    print(f"Subjects: {subjects}")
    print(f"Goal: {goal}")

    speaker.Speak(
        f"Name: {name}. "
        f"Subjects: {subjects}."
        f"Goal: {goal}. "
    )

    print("===========================================================")

name = memory.get("name",)
goal = memory.get("goal",)
subjects = memory.get("subjects",)

commands = {
    "/quit": quit_command,
    "/info": info_command,
    "/version": version_command,
    "/time": time_command,
    "/date": date_command,
    "/help": help_command,
    "/setname": setname_command,
    "/name": name_command,
    "/setsubjects": setsubjects_command,
    "/subjects": subjects_command,
    "/setgoal": setgoal_command,
    "/goal": goal_command,
    "/profile": profile_command,
    "/settask": settask_command,
    "/tasks": tasks_command,
    "/finishtask": finishtask_command,
    "/deletetask": deletetask_command,
    "/sing": sing_command,

}

if name:
     greetings = [
       f"Welcome back, {name}! Ready to learn?",
       f"Hello again, {name}! What are we practicing today?",
       f"Ready to learn, {name}?",
        f"Welcome back to Cerulean, {name}!",
       f"Let's make some progress today, {name}!",
       f"How about we practice {random.choice(subjects)}, {name}?"
     ]

else:
    greetings = [
       f"Welcome back! Ready to learn?",
       f"Hello again! What are we practicing today?",
       f"Ready to learn?",
       f"Welcome back to Cerulean!",
       f"Let's make some progress today!"
        ]


speak(random.choice(greetings))

while True:

    while msvcrt.kbhit():
        msvcrt.getch()

    user_input = input("You:  ")

    if user_input.startswith("/"):
        command = commands.get(user_input)

        if command:
            command()
        else:
            speak("Unknown command. Type /help for a command list.")
        continue

    text = user_input.lower()

    if text in ["hello", "hi"]:
        speak("Hello from Cerulean!")

    elif text in ["what should i study"]:
        speak(f"I think you should study {random.choice(subjects)} today!")

    elif text in ["goodbye", "bye"]:
        speak("Goodbye! Use /quit to exit the program.")

    else:
        speak("I'm not smart enough to chat properly yet!")
