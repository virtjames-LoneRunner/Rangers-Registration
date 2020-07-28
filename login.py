import typewriter as tp
import os
import time
from getpass import getpass
import procedures

filename = 'Member-List.txt'

#Messages
user_prompt = "Enter your Ranger Name"
pass_prompt = "Enter your Password"
prompt = "Enter your Credentials\n"

#User Input
user = ''
passwd = ''
user_input = ''

#Dictionaries
credentials = {"Ranger Name":'', "Password": ''}

#Authentication
authenticated_member = ''
auth_member_dictionary = {}
grant_access = bool

#Functions
def get_credentials():
    tp.typewriter(user_prompt)
    user = input(": ")
    tp.typewriter(pass_prompt)
    passwd = getpass(": ")
    return user, passwd

def open_file(user):
    with open(filename) as cred_file:
        lines = cred_file.readlines()
    for line in lines:
        if user in line:
            authenticated_member = line
            return authenticated_member
    

def authenticate_user(passwd, auth_member_dictionary):
#    auth_member_dictionary = eval(authenticated_member)
    if passwd == auth_member_dictionary["Password"]:
        return True
    else:
        return False

def login():
    os.system("clear")
#    print(f'Grant Access? {grant_access}')

    tp.typewriter(prompt)
    user, passwd = get_credentials()

    authenticated_member = open_file(user)
#    print(authenticated_member)

    if authenticated_member:
        auth_member_dictionary = eval(authenticated_member)
#        print(type(auth_member_dictionary))
#        print(auth_member_dictionary["Password"])

        grant_access = authenticate_user(passwd, auth_member_dictionary)
        
#        print(grant_access)
        if grant_access == True:
            return True, user
    elif authenticated_member == None:
#        print("Access denied")
        return False, user