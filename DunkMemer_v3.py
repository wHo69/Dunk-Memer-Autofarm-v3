# Dank Memer Autofarm Script, 3rd rewrite
# Made by wHo69 on GitHub

"""
Functions to be added:
1. Auto beg
2. Auto dig
3. Auto fish
4. Auto hunt
5. Auto deposit
6. Save token and settings
7. Selling items
"""

# Libraries
import requests
import os
import termcolor
import traceback

import settingsHandler
import optionsHandler
import userInfo
import autofarm

# Variables
positive = "[" + termcolor.colored("+", "green") + "] "
negative = "[" + termcolor.colored("-", "red") + "] "
inputCaret = termcolor.colored("> ", "green")

dankTitle = termcolor.colored("""=======================================================================================
  _____              _      __  __                                          _
 |  __ \            | |    |  \/  |                              /\        | |
 | |  | | __ _ _ __ | | __ | \  / | ___ _ __ ___   ___ _ __     /  \  _   _| |_ ___
 | |  | |/ _` | '_ \| |/ / | |\/| |/ _ \ '_ ` _ \ / _ \ '__|   / /\ \| | | | __/ _ \ 
 | |__| | (_| | | | |   <  | |  | |  __/ | | | | |  __/ |     / ____ \ |_| | || (_) |
 |_____/ \__,_|_| |_|_|\_\ |_|  |_|\___|_| |_| |_|\___|_|    /_/    \_\__,_|\__\___/
======================================================================================""", "cyan") + """
Version 1.0
Made by wHo69 on GitHub
"""

# Functions
def clear_screen():
    os.system("cls")
    print("\n" * 50)

def validate(token : str):
    r = requests.get("https://discord.com/api/v6/users/@me", headers={"Authorization": token})
    return r.status_code == 200

def getUsername(token : str):
    r = requests.get("https://discord.com/api/v6/users/@me", headers={"Authorization": token}).json()
    return r["username"]

def getUserDiscriminator(token : str):
    r = requests.get("https://discord.com/api/v6/users/@me", headers={"Authorization": token}).json()
    return r["discriminator"]

# Initialisation
def initialise():
    clear_screen()
    os.system("cls & mode 85,20 & title [Dank Memer Autofarm] - Setup")

    print(dankTitle)

    print("\n" + positive + "Reading from settings file...")

    # Load up settings and fix missing keys
    settings = settingsHandler.read_settings()

    # Fix up missing settings
    if "token" not in settings.keys():
        settingsHandler.saveToken()

    if "guildId" not in settings.keys():
        settingsHandler.saveGuildId()

    if "channelId" not in settings.keys():
        settingsHandler.saveChannelId()

    print(positive + "Saved Settings!")

# Main
def main():
    clear_screen()
    os.system(f"cls & mode 85,20 & title [Dank Memer Autofarm] - Connected to: {getUsername(settingsHandler.read_settings()['token'])}#{getUserDiscriminator(settingsHandler.read_settings()['token'])}")

    print(dankTitle)

    print(f"""Connected to: \x1b[1;33;40m{getUsername(settingsHandler.read_settings()['token'])}#{getUserDiscriminator(settingsHandler.read_settings()['token'])}\x1b[0m
╔═════════════════════════════╦════════════════════════════════════════════════════╗
║ [1] Start Autofarm          ║                                                    ║
║ [2] Change Settings         ║             Report any bugs found :>               ║
║ [3] Change Autofarm Options ║        Try to include some screenshots along :D    ║
║ [4] User Info               ║                                                    ║
╚═════════════════════════════╩════════════════════════════════════════════════════╝""") # characters taken from: https://en.wikipedia.org/wiki/Box-drawing_character

    choice = input(inputCaret + "Option: ")
    choiceHandler(choice)

def choiceHandler(choice):
    options = ["1", "2", "3", "4"]

    while choice not in options:
        print(negative + "Invalid choice!")
        choice = input(inputCaret + "Option: ")

    if choice == "1":
        autofarm.autofarmMenu()
    if choice == "2":
        settingsHandler.settingsMenu()
    if choice == "3":
        optionsHandler.optionsMenu()
    if choice == "4":
        userInfo.userInfoScreen()

if __name__ == "__main__":
    try:
        initialise()
        main()
    except Exception as e:
        clear_screen()
        os.system(f"cls & mode 85,20 & title ERROR!")
        print("""\x1b[1;31;40m=======================================================================================
  _____              _      __  __                                          _
 |  __ \            | |    |  \/  |                              /\        | |
 | |  | | __ _ _ __ | | __ | \  / | ___ _ __ ___   ___ _ __     /  \  _   _| |_ ___
 | |  | |/ _` | '_ \| |/ / | |\/| |/ _ \ '_ ` _ \ / _ \ '__|   / /\ \| | | | __/ _ \ 
 | |__| | (_| | | | |   <  | |  | |  __/ | | | | |  __/ |     / ____ \ |_| | || (_) |
 |_____/ \__,_|_| |_|_|\_\ |_|  |_|\___|_| |_| |_|\___|_|    /_/    \_\__,_|\__\___/
======================================================================================\x1b[0m""")
        print("[" + termcolor.colored("ERROR", "red") + "] An error occured!")
        print("Please screenshot the text below and report this bug:\n")
        print("".join(traceback.TracebackException.from_exception(e).format()))
        input("\nPress enter to quit.")
