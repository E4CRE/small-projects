
#!/usr/bin/env python

##### Libraries #####

import random as rd
import string
import secrets

##### Variables #####

symbols = string.punctuation
numbers = string.digits
letters = string.ascii_letters
characters = symbols + numbers + letters



##### Functions ######

def psdgen(l:int):
    """Generate a secured password, l = length >11"""

    if l < 12:
        return "The password length must be at least 12 characters."

    psd = [secrets.choice(characters) for i in range(l)]
    rd.shuffle(psd)
    print("your password :",''.join(psd))
    return ''.join(psd)

def menu():
    print("""
┏┓┏┓┏┓┳┓┏┓╻╹   ┏┳┓    ┓ 
┣ ┃┃┃ ┣┫┣ ┃ ┏   ┃ ┏┓┏┓┃┏
┗┛┗╋┗┛┛┗┗┛• ┛   ┻ ┗┛┗┛┗┛
                        
""")
    selection = input("""
1 : Generate a password.
2 : Password analyzer.
3 : Check if an email adress is in a data breach.
4: Exit.
"""
)
    if selection == "1":
        l = int(input("Password length ?(>11) :"))

        #Verification
        if l>11:
            psdgen(l)
            menu()
        else:
            print("The password length must be at least 12 characters.")
            menu()

    elif selection =="4":
        exit()

def analyze(psd:str):
    pass


##### Code #####

menu()
