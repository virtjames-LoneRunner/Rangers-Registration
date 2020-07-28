import sys
import time
import register, login
import typewriter as tp
import os

#Messages
welcome = "Welcome to the Rangers\' Initiative\n"
instructions = "To register type \"Register\"\n\
To Login type \"Login\"\n"

#Variables
user_input = ''
access_to_menu = bool
user = ''

def main_prompt():
    os.system("clear")
    tp.typewriter(welcome)
    tp.typewriter(instructions)
    user_input = input("> ")
    if user_input == "Register":
        tp.typewriter("Registering...\n")
        access_to_menu = register.register()
        return access_to_menu, None
    elif user_input == "Login":
        tp.typewriter("Loggin in...\n")
        access_to_menu = login.login()
        return access_to_menu

#Main
access_to_menu, user = main_prompt()
if access_to_menu == True:
    tp.typewriter("\nACCESS GRANTED!\n")
    tp.typewriter(f"Welcome {user}!\n")
elif access_to_menu == False:
    tp.typewriter("\nClosing...\n")