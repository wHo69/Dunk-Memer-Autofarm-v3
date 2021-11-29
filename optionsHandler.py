# Options handler
# Changes user options

# Libraries
import os
import json
import termcolor

import DunkMemer_v3

# Variables
filepath = "resources\\options.json"

positive = "[" + termcolor.colored("+", "green") + "] "
negative = "[" + termcolor.colored("-", "red") + "] "
inputCaret = termcolor.colored(">", "green")

options = [
    "beg",
    "dig",
    "fish",
    "hunt",
    "search",
    "deposit",
    "sell"
]

# Functions
def clear_screen():
    os.system("cls")
    print("\n" * 50)

def color(key : str, text : str):
    data = read_options()

    if data[key] == True:
        return termcolor.colored(text, "green")
    else:
        return termcolor.colored(text, "red")

def init():
    try:
        open(filepath, "r")
    except FileNotFoundError:
        with open(filepath, "x") as f:
            data = {}
            json.dump(data, f, indent=4)

def read_options():
    init()
    with open(filepath, "r")as f:
        data = json.load(f)
        f.close()
    return data

def write_options(key : str, value : any):
    data = read_options()
    data[key] = value

    with open(filepath, "w")as f:
        json.dump(data, f, indent=4)

def fixMissing():
    data = read_options()

    for i in options:
        if i not in data.keys():
            write_options(i, True)

def optionsMenu():
    while True:
        init()
        fixMissing()
        clear_screen()

        os.system(f"cls & mode 85,20 & title [Dank Memer Autofarm] - Options")
        print(DunkMemer_v3.dankTitle)

        print(termcolor.colored("Options:", "green"))
        print("1. " + color("beg", "Begging"))
        print("2. " + color("dig", "Digging"))
        print("3. " + color("fish", "Fishing"))
        print("4. " + color("hunt", "Hunting"))
        print("5. " + color("search", "Searching"))
        print("6. " + color("deposit", "Depositing"))
        print("7. " + color("sell", "Selling"))
        print(f"e. {termcolor.colored('Enable ALL', 'green')}")
        print(f"d. {termcolor.colored('Disable ALL', 'red')}")
        print("b. Back.")

        print("\nSelect the option to enable/disable it.")
        choice = input(inputCaret + "Option: ")

        handleChoice(choice)

def handleChoice(choice):
    choice_options = ["1", "2", "3", "4", "5", "6", "7", "e", "d", "b"]
    data = read_options()

    while choice.lower() not in choice_options:
        print(negative + "Invalid choice!")
        choice = input(inputCaret + "Option: ")

    if choice == "1":
        write_options("beg", not data["beg"])
    if choice == "2":
        write_options("dig", not data["dig"])
    if choice == "3":
        write_options("fish", not data["fish"])
    if choice == "4":
        write_options("hunt", not data["hunt"])
    if choice == "5":
        write_options("search", not data["search"])
    if choice == "6":
        write_options("deposit", not data["deposit"])
    if choice == "7":
        write_options("sell", not data["sell"])
    if choice == "e":
        for i in options:
            write_options(i, True)
    if choice == "d":
        for i in options:
            write_options(i, False)
    if choice == "b":
        DunkMemer_v3.main()