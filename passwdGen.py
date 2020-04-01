import random

element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!"

passwd=""

longueur = int(input("Combien de caractères voulez-vous dans votre mot de passe> "))

for i in range(longueur):
    passwd = passwd + element[random.randint(0, len(element) - 1)]
print("Voici votre mot de passe: \n" + passwd)