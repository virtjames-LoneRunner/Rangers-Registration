import typewriter as tp
import os
import time
from getpass import getpass
import procedures

#Messages
message = "*" * 10 + "Welcome to the Rangers Initiative" + "*" * 10 + '\n'
message1 = "*" * 8 + "Please enter the required information" + "*" * 8 + '\n'
message2 = "If you wish to quit, enter \"quit\"." + '\n'
registering = 'Registering.....................................\nDone!'
goodbye = "Goodbye!"
passprompt = "Enter a password"
passprompt2 = "Enter password again"
retype = "Try again"

#Variables
filename = 'Member-List.txt'
string_data = ''
not_equal_to_quit = bool

 
#User input Variables
input_data = {}

#Dictionary
prompts = { "Ranger Name": "","First Name": "", "Last Name": "", "Middle Name": "", "Age": 0, "Address": ""}

#Creating Objects
action = procedures.Procedures()

#Making sure this code doesn't run immediately when imported
def main():
    pass
if __name__ == "__main__":
    main()


#Functions
def collect_data():
    user_input = ''
    for prompt in prompts:
        tp.typewriter(prompt)
        user_input = input(": ")
        if user_input != "quit":
            if user_input.isdigit():
                user_input = int(user_input)
                prompts[prompt] = user_input
            elif user_input.isdigit() is False:
                prompts[prompt] = user_input
        elif user_input == 'quit':
            tp.typewriter("Closing...")
            return False
            break
    return prompts

def check_if_user_exists():
    user = prompts["First Name"]
    with open(filename) as cred_file:
        lines = cred_file.readlines()
    for line in lines:
        if user in line:
            print("User already exists!")
            break
            return True
        else:
            return False


def write_to_file():
    input_data = str(prompts)
    first_name = prompts["First Name"]
    with open(filename, 'a') as file_objects:
        file_objects.write(first_name + '\'s Data: \n' + input_data + "\n" + "\n")

def passwd():
    while True:
        tp.typewriter(passprompt)
        passwd = getpass(": ")
        tp.typewriter(passprompt2)
        passwd2 = getpass(": ")
        if passwd == passwd2:
            return passwd
        else:
            pass

#Start
def register():
    input_data = ''
    os.system('clear')
    action.welcome_message(message)
    action.welcome_message(message1)
    action.welcome_message(message2)

    while True:
        response = ''
        not_equal_to_quit = collect_data()
        if not_equal_to_quit == False:
            break
        #input_data = str(collect_data())
        #if check_if_user_exists() is False:
        prompts["Password"] = passwd()
        write_to_file()
        tp.typewriter("You have now been added to the system " + prompts["Ranger Name"] + "!")
        print('\n')
        tp.typewriter("Would you like to enter another Ranger? Yes/No \n")
        response = input("> ")
        response = response.lower()
        if response == 'yes':
            prompts.pop("Password")
            pass
        elif response == 'no':
            return False
            break
        #else:
        #    break
