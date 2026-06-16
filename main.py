import json
from datetime import datetime

try:
    with open("memory.json", "r") as f:
        memory = json.load(f)
except FileNotFoundError:
    memory = {}


def save_memory():
    with open("memory.json", "w") as f:
        json.dump(memory, f)

VERSION = "v0.04"

print(f"""===================
Cerulean
Learning Without End
{VERSION}
==================""")

def quit_command():
    print("Exiting Cerulean...")
    exit()

def info_command():
    print(
        "Cerulean:  Cerulean is an AI assistant designed for students and startups. The main focus it to help your dream come true. It is a work in progress and will be updated regularly.")

def version_command():
    print("Cerulean:  ", VERSION)

def time_command():
    current = datetime.now()
    print("Cerulean:  Current time: ", current.strftime("%H:%M:%S"))

def date_command():
    current = datetime.now()
    print("Cerulean:  Current date: ", current.strftime("%Y-%m-%d"))

def help_command():
    print("Cerulean:  Available commands:")
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

def setname_command():
    name = input("Enter your name: ")
    memory["name"] = name
    save_memory()
    print("Cerulean:  Name saved.")

def name_command():
    name = memory.get("name")
    if name:
        print(f"Cerulean:  Your name is {name}.")
    else:
        print("Cerulean:  You haven't set your name yet. Use /setname to set it.")

def setsubjects_command():
    subjects = input("Enter your subjects: ")
    memory["subjects"] = subjects
    save_memory()
    print("Cerulean:  Subjects saved.")

def subjects_command():
    subjects = memory.get("subjects")
    if subjects:
        print(f"Cerulean:  Your subjects are {subjects}.")
    else:
        print("Cerulean:  You haven't set your subjects yet. Use /setsubjects to set them.")

def setgoal_command():
    goal = input("Enter your goal: ")
    memory["goal"] = goal
    save_memory()
    print("Cerulean:  Goal saved.")

def goal_command():
    goal = memory.get("goal")
    if goal:
        print(f"Cerulean:  Your goal is to {goal}.")
    else:
        print("Cerulean:  You haven't set your goal. Use /setgoal to set it.")

def profile_command():
    name = memory.get("name","Not set")
    goal = memory.get("goal","Not set")
    subjects = memory.get("subjects","Not set")

    print("===== Cerulean Profile =======================================================")
    print("Name:", name)
    print("Goal:", goal)
    print("Subjects:", subjects)
    print("==============================================================================")

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
    "/profile": profile_command

}

name = memory.get("name")
if name:
    print(f"Cerulean:  Welcome back, {name}! Type /help for a list of commands.")
else:
    print("Cerulean:  Welcome back! Type /help for a list of commands.")

while True:
    user_input = input("You:  ")

    if user_input.startswith("/"):
        command = commands.get(user_input)

        if command:
            command()
        else:
            print("Cerulean:  Unknown command. Type /help for a command list.")
    else:
        print("Cerulean:  I'm not smart enough to chat yet!")
