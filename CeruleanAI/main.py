from datetime import datetime
now = datetime.now()
print(now)

print("""===================
Cerulean
Learning Without End
v0.01
===================""")

ceruleanversion = "v0.01"
while True:
    user_input = input("You:  ")

    if user_input == "/quit":
        print("Cerulean:  Goodbye!")
        break

    elif user_input == "/info":
        print("Cerulean:  Cerulean is an AI assistant designed for students. Future versions may include features like screen sharing, goal planning, and voice input.")

    elif user_input == "/version":
        print("Cerulean:  ", ceruleanversion)

    elif user_input == "/time":
        print("Cerulean:  ",now.strftime("%H:%M:%S"))

    elif user_input == "/commands":
        print("Cerulean:  /quit: Ends Conversation")
        print("           /version: Version info")
        print("           /info: Cerulean info")
        print("           /time: Current time")

    else:
        print("""Cerulean:  Unknown command
           Please use /commands for help""")
