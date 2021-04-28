import os
os.system("cls")
os.system("pip install colorama")
os.system("cls")
from colorama import * 
banner = """
                      ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
                      ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
                      ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
                      ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
                      ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
                      ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                 
                                           Installing requirements

"""
def Auther():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing other requirements")
        os.system("pip install pywin32")
        try:
            os.system("pip install datetime")
            os.system('pip install sys')
            os.system("pip install math")
            os.system("pip install os")
            os.system("pip install terminatables")
            os.system("pip install json")
            os.system('pip install re')
            os.system("pip install time")
        except:
            pass
        input("")
        

    except:
        pass
    input("")
def pyinstaller():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing PyInstaller")
        os.system("pip install pyinstaller")
    except:
        print(Fore.RED + " ! "+Fore.RESET+"An error has occurred...")

def discord():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing discord")
        os.system('pip install discord')

    except:
        print(Fore.RED + " ! "+Fore.RESET+"An error has occurred...")
        pass

def pyfiglet():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing Pyfiglet")
        os.system('pip install pyfiglet')

    except:
        print(Fore.RED + " ! "+Fore.RESET+"An error has occurred...")
        pass

def art():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing ART")
        os.system('pip install art')

    except:
        print(Fore.RED + " ! "+Fore.RESET+"An error has occurred...")
        pass


def json():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing json")
        os.system('pip install json')

    except:
        print(Fore.RED + " ! "+Fore.RESET+"An error has occurred...")
        pass


def bs4():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing BS4")
        os.system('pip install bs4')
    except:
        print(Fore.RED + " ! "+Fore.RESET+"An error has occurred...")

def requests():    
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing requests")
        os.system("pip install requests")
    except:
        print(Fore.RED + " ! "+Fore.RESET+"An error has occurred...")

def installer():
    try:
        print(Fore.BLUE + banner + Fore.RESET)
        os.system("python -m pip install --upgrade pip")
        requests()
        art()
        bs4()
        pyinstaller()
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Succesfully installed press enter pls")
        try:
            choice = input("\n["+Fore.GREEN+"INFO"+Fore.RESET+"] Installe other requirements ?(o/n) > ")
            if choice == "o" or "O":
                try:
                    os.system('cls')
                    print(Fore.YELLOW + banner + Fore.RESET)
                    Auther()
                    print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Succesfully installed other requirements")
                    detail = input("["+Fore.RED+"INFO"+Fore.RESET+"] Do you want to view the logs? (o/n) >")
                    if detail == "O" or "o":
                        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] The requirements to install sound: sys, os datetime, math, terminal tables, json, re, time, art, colorama, pafiglet, bs4, requests, discord, pyinstaller")
                    else:
                        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Ok you can close all the requirements to install!")
                        input("")

                except:
                    pass
                input("")
            else:
                try:
                    print(Fore.GREEN + 'Ok you can close !'+Fore.RESET)
                except:
                    pass
                input("")
        except:
            pass
        input("")
    except:
        print(Fore.RED + " ! "+Fore.RESET+"An error has occurred...")

installer()

