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

VERSION = "v0.03"

print("""===================
Cerulean
Learning Without End
v0.03
===================""")

def quit_command():
    print("Exiting Cerulean...")
    exit()

def info_command():
    print("Cerulean:  Cerulean is an AI assistant designed for students and startups. The main focus it to help your dream come true. It is a work in progress and will be updated regularly.")

def version_command():
    print("Cerulean:  ",VERSION)

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

def save_memory():
    with open("memory.json", "w") as f:
        json.dump(memory, f)

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

commands = {
    "/quit": quit_command,
    "/info": info_command,
    "/version": version_command,
    "/time": time_command,
    "/date": date_command,
    "/help": help_command,
    "/setname": setname_command,
    "/name": name_command

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
