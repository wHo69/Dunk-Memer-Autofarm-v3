# User Info

# Libraries
import os
import requests
import termcolor

import DunkMemer_v3
import settingsHandler

# Functions
def clear_screen():
    os.system("cls")
    print("\n" * 50)

def getUserData(token : str):
    r = requests.get("https://discord.com/api/v6/users/@me", headers={"Authorization": token})
    data = r.json()

    return data

def userInfoScreen():
    clear_screen()
    os.system(f"cls & mode 85,20 & title [Dank Memer Autofarm] - User Info")

    data = getUserData(settingsHandler.read_settings()["token"])

    print(f"""{DunkMemer_v3.dankTitle}

{termcolor.colored('USER INFO', 'green')}
================
Username: {data['username']}#{data['discriminator']}
User ID: {data['id']}
Bio: {'None' if data['bio'] == '' else data['bio']}
Email: {data['email']}
Phone: {data['phone']}

Press enter to go back
    """)

    input()
    DunkMemer_v3.main()
