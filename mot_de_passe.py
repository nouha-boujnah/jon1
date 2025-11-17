import re

while True:
    p = input("Entrez un mot de passe : ")

    if len(p) < 8:
        print

    if not re.search("[a-z]", p):
        print
    if not re.search("[A-Z]", p):
        print

    if not re.search("[0-9]", p):
        print

    if not re.search("[!@#$%^&*]", p):
        print

    print(" Mot de passe valide !")
    break
