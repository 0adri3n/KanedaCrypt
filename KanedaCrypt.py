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

passwd2 = ""

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
[4] Encrypt a .txt file\n\
[5] Decrypt \n\
[6] Exit \n\
[7] Clear \n\
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
                passwd2 = passwd2 + element[random.randint(0, len(element) - 1)]
            print("\nYour password: \n \n" + passwd2 + "\n\n")



    elif choice == 2:
        key = Fernet.generate_key()
        key_bytes = bytes(key)
        print("\nThis is your personal key. /!\ Don't forget it /!\ \n\n", key_bytes ,"\n\nDon't copy the b and the ' ' !\n\n")


    elif choice == 3:

        txt = (input("\nWhat do you want to encrypt> "))
        txt_en = bytes(txt, 'utf-8')
        key = input("\nPlease insert your encryption key: \n")
        cipher_suite = Fernet(key)
        txt_encode = cipher_suite.encrypt(txt_en)


        print("\nThis your text encrypted: \n", txt_encode  ,"\n\nDon't copy the b and the ' ' !\n\n")


    elif choice == 4:

        path = input("\nPlease put the path to the folder of the .txt file: \n")
        os.chdir(path) 
        file = input("\nPlease put the name of the file: \n")
        file_1 = (file + ".txt")
        fichier = open(file_1, "r")
        contenu = fichier.read()
        fichier.close()
        contenu_enc = bytes(contenu, 'utf-8')
        key2 = input("\nPlease insert your encryption key: \n")
        cipher_suite2 = Fernet(key2)
        file_enc = cipher_suite2.encrypt(contenu_enc)
        name_newFile = input("\nPlease insert the name of the new .txt file encrypted: \n")
        name_newFile_1 = (name_newFile + ".txt")
        new_File = open(name_newFile_1, "x")
        file_enc2 = str(file_enc)
        finale_file = new_File.write(file_enc2)
        new_File.close()
        print("\nYour file is now ready!\n")


    elif choice == 5:

        txt2 = input("\nWhat do you want to decrypt?> ")
        txt_de = bytes(txt2, 'utf-8')
        key2 = input("\nPlease insert your encryption key: \n")
        cipher_suite2 = Fernet(key2)
        txt_decode = cipher_suite2.decrypt(txt_de)

        print("\nThis your text decrypted: \n", txt_decode  ,"\n\nDon't read the b and the ' ' !\n\n")





    elif choice == 6:
        print("\n                                            | Goodbye. |                                                          akira")
        time.sleep(0.2)
        terminal_lauched = False

    elif choice == 7:
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