# Settings Handler
# Reads and writes to settings file
# Returns setting values

# Libraries
import os
import json
import requests

import DunkMemer_v3

# Variables
positive = DunkMemer_v3.positive
negative = DunkMemer_v3.negative
inputCaret = DunkMemer_v3.inputCaret

# Functions
def clear_screen():
    os.system("cls")
    print("\n" * 50)

def createResFolder():
    try:
        os.mkdir("resources")
    except FileExistsError:
        pass

def read_settings():
    createResFolder()
    filepath = "resources/settings.json"

    try:
        with open(filepath, "r")as f:
            data = json.load(f)
            f.close()
    except FileNotFoundError:
        with open(filepath, "a")as f:
            f.write("{}")
            f.close()
        data = {}

    return data

def write_settings(key : any, value : any):
    createResFolder()
    filepath = "resources/settings.json"

    data = read_settings()
    data[key] = value

    with open(filepath, "w")as f:
        json.dump(data, f, indent=4)

def validate(token : str):
    r = requests.get("https://discord.com/api/v6/users/@me", headers={"Authorization": token})
    return r.status_code == 200

def saveToken():
    while True:
        token = input(inputCaret + " Token: ")
        print(positive + "Validating token...")
        if token != "" and validate(token) : break
        print(negative + "Invalid token!")
    write_settings("token", token)

def saveGuildId():
    while True:
        guildId = input(inputCaret + " Guild Id: ")
        if guildId != "" : break
    write_settings("guildId", guildId)

def saveChannelId():
    while True:
        channelId = input(inputCaret + " Channel Id: ")
        if channelId != "" : break
    write_settings("channelId", channelId)

def handleChoice(choice : str):
    choiceList = ["1", "2", "3", "b"]
    data = read_settings()

    while choice.lower() not in choiceList:
        choice = input(negative + "Invalid input!\n" + inputCaret + "Choice: ")

    if choice == "1":
        print(f"Current Token: {data['token']}")
        saveToken()
    if choice == "2":
        print(f"Current Guild ID: {data['guildId']}")
        saveGuildId()
    if choice == "3":
        print(f"Current Channel ID: {data['channelId']}")
        saveChannelId()
    if choice.lower() == "b":
        DunkMemer_v3.main()

def settingsMenu():
    while True:
        clear_screen()

        os.system(f"cls & mode 85,20 & title [Dank Memer Autofarm] - Settings")

        print(DunkMemer_v3.dankTitle)

        print("""
╔═════════════════════════════════════════════════════╗
║ [1] Change User Token                               ║
║ [2] Change Guild ID                                 ║
║ [3] Change Channel ID                               ║
║ [b] Back                                            ║
╚═════════════════════════════════════════════════════╝""")

        choice = input(inputCaret + "Choice: ")
        handleChoice(choice)