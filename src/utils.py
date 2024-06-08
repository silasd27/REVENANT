import time
from colorama import Fore
import pickle
import os

def cstring(string: str, color: str) -> str:
    match color:
        case "red":
            return f"{Fore.RED}{string}{Fore.RESET}"
        case "green":
            return f"{Fore.GREEN}{string}{Fore.RESET}"
        case "blue":
            return f"{Fore.BLUE}{string}{Fore.RESET}"
        case "cyan":
            return f"{Fore.CYAN}{string}{Fore.RESET}"
        case "magenta":
            return f"{Fore.MAGENTA}{string}{Fore.RESET}"
        case "yellow":
            return f"{Fore.YELLOW}{string}{Fore.RESET}"
        case _:
            return string

def tprint(string: str, wait: float) -> None:
    time.sleep(wait)
    print(string)

def typewriter(string: str, wait: float=0) -> None:
    time.sleep(wait)
    for char in string:
        print(char, end="", flush=True)

def dialogue(name: str, string: str, color: str) -> str:
    return f"{cstring(name, color)}: {string}"

def save(data: dict):
    with open("savedata.pkl", 'wb') as file:
        pickle.dump(data, file)

def read() -> dict:
    with open("savedata.pkl", 'rb') as file:
        return pickle.load(file)

def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def user_clear(typewriter_mode = False) -> None:
    if typewriter_mode:
        typewriter(cstring("CONTINUE", "red").join(" >"))
    else:
        print(cstring("CONTINUE", "red").join(" >"))