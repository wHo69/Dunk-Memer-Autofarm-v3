# Autofarm part

# Libraries
import requests
import os

import termcolor

import DunkMemer_v3
import optionsHandler
import settingsHandler

# Variables
begTimer = 55
digTimer = 50
fishTimer = 45
searchTimer = 35
huntTimer = 40
depTimer = 120

# Functions
def clear_screen():
    os.system("cls")
    print("\n" * 50)

def listenForQuit():
    input()
    #TODO: Quit from autofarm

def send(msg : str):
    data = settingsHandler.read_settings()
    channel_id = data['channelId']
    headers = {"Authorization": data['token']}

    r = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': msg})
    return r.status_code

def farm():
    global begTimer, digTimer, fishTimer, searchTimer, huntTimer, depTimer

    option = optionsHandler.read_options()

    while True:
        begTimer -= 1
        digTimer -= 1
        fishTimer -= 1
        searchTimer -= 1
        huntTimer -= 1
        depTimer -= 1

        if begTimer == 0 and option['beg']:
            send("pls beg")
            begTimer = 55

        if digTimer == 0 and option['dig']:
            send("pls dig")
            digTimer = 50

        if fishTimer == 0 and option['fish']:
            send("pls fish")
            fishTimer = 45

        if searchTimer == 0 and option['search']:
            # TODO: add searching
            searchTimer = 35

        if huntTimer == 0 and option['hunt']:
            send("pls hunt")
            huntTimer = 40

        if depTimer == 0 and option['deposit']:
            send("pls dep all")
            depTimer = 120

def autofarmMenu():
    clear_screen()
    os.system(f"cls & mode 85,20 & title [Dank Memer Autofarm] - Connected to: {DunkMemer_v3.getUsername(settingsHandler.read_settings()['token'])}#{DunkMemer_v3.getUserDiscriminator(settingsHandler.read_settings()['token'])}")

    print(DunkMemer_v3.dankTitle)
    print(f"Connected to: \x1b[1;33;40m{DunkMemer_v3.getUsername(settingsHandler.read_settings()['token'])}#{DunkMemer_v3.getUserDiscriminator(settingsHandler.read_settings()['token'])}\x1b[0m")

    print(f"========== {termcolor.colored('Autofarm', 'yellow')} ==========")
    farm()