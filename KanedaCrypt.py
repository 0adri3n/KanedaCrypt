##################################################################################################################
#____  __.                        .___        _________                                                          #
#|    |/ _|____    ____   ____   __| _/____    \_   ___ \_______ ___.__._______/  |_                             #
#|      < \__  \  /    \_/ __ \ / __ |\__  \   /    \  \/\_  __ <   |  |\____ \   __\                            #
#|    |  \ / __ \|   |  \  ___// /_/ | / __ \_ \     \____|  | \/\___  ||  |_> >  |                              #
#|____|__ (____  /___|  /\___  >____ |(____  /  \______  /|__|   / ____||   __/|__|                              #
#        \/    \/     \/     \/     \/     \/          \/        \/     |__|                                     #
#                                                                                                                #
#                                                                                made by akira   01/04/2020      #
#                                                                               https://github.com/akira-trinity #
##################################################################################################################




import random
from cryptography.fernet import Fernet
import os
import time
import base64





element_symb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!"

element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

passwd=""

terminal_lauched = True

def clear():
    if os.name == 'nt':
        os.system("cls")
        os.system("color 2") 
    else:
        os.system("clear")

def color():
    if os.name == 'nt':
        os.system("color 2") 






kaneda = ("\
____  __.                        .___        _________                              \n\
|    |/ _|____    ____   ____   __| _/____    \_   ___ \_______ ___.__._______/  |_ \n\
|      < \__  \  /    \_/ __ \ / __ |\__  \   /    \  \/\_  __ <   |  |\____ \   __\ \n\
|    |  \ / __ \|   |  \  ___// /_/ | / __ \_ \     \____|  | \/\___  ||  |_> >  |  \n\
|____|__ (____  /___|  /\___  >____ |(____  /  \______  /|__|   / ____||   __/|__|  \n\
        \/    \/     \/     \/     \/     \/          \/        \/     |__|         \n\
                                                                                                           \n\
                                                                                made by akira   01/04/2020 \n\
                                                                                https://github.com/akira-trinity \n\
")


clear()

print(kaneda)

while terminal_lauched:
    color()
    choice = int(input("\
[1] Generate a password \n\
[2] Generate your personal key \n\
[3] Encrypt \n\
[4] Decrypt \n\
[5] Exit \n\
[6] Clear \n\
\n\
Kaneda Crypt> "))




    if choice == 1:
        longueur = int(input("\nHow many caracters you want in your password?> "))
        symb = input("\nDo you want symbols in your password?[Y/N]> ")
        if symb == "Y":
            for i in range(longueur):
                passwd = passwd + element_symb[random.randint(0, len(element_symb) - 1)]
            print("\nYour password: \n \n" + passwd + "\n\n")
        elif symb == "N":
            for i in range(longueur):
                passwd = passwd + element[random.randint(0, len(element) - 1)]
            print("\nYour password: \n \n" + passwd + "\n\n")



    elif choice == 2:
        key = Fernet.generate_key()
        print("\nThis is your personal key. /!\ Don't forget it /!\ \n\n", key ,"\n\nDon't copy the b and the ' ' !\n\n")


    elif choice == 3:

        txt = (input("\nWhat do you want to encrypt> "))
        txt_en = bytes(txt, 'utf-8')
        key = input("\nPlease insert your encryption key: \n")
        cipher_suite = Fernet(key)
        txt_encode = cipher_suite.encrypt(txt_en)

        print("\nThis your text encrypted: \n", txt_encode  ,"\n\nDon't copy the b and the ' ' !\n\n")

    elif choice == 4:

        txt2 = input("\nWhat do you want to decrypt?> ")
        txt_de = bytes(txt2, 'utf-8')
        key2 = input("\nPlease insert your encryption key: \n")
        cipher_suite2 = Fernet(key2)
        txt_decode = cipher_suite2.decrypt(txt_de)

        print("\nThis your text decrypted: \n", txt_decode  ,"\n\nDon't read the b and the ' ' !\n\n")


    elif choice == 5:
        print("\n                                            | Goodbye. |                                                          akira")
        time.sleep(0.2)
        terminal_lauched = False

    elif choice == 6:
        clear()
        print("\
____  __.                        .___        _________                              \n\
|    |/ _|____    ____   ____   __| _/____    \_   ___ \_______ ___.__._______/  |_ \n\
|      < \__  \  /    \_/ __ \ / __ |\__  \   /    \  \/\_  __ <   |  |\____ \   __\ \n\
|    |  \ / __ \|   |  \  ___// /_/ | / __ \_ \     \____|  | \/\___  ||  |_> >  |  \n\
|____|__ (____  /___|  /\___  >____ |(____  /  \______  /|__|   / ____||   __/|__|  \n\
        \/    \/     \/     \/     \/     \/          \/        \/     |__|         \n\
                                                                                                           \n\
                                                                                made by akira   01/04/2020 \n\
                                                                                https://github.com/akira-trinity \n\
")


    else:
        print("\nThis command doesn't exist. Please try another command.\n\n")