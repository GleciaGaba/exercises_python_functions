# test()


def test():
    print("Bonjour")


#  NameError: name 'test' is not defined
"""
Python va lire le script ligne par ligne et comme la
fonction a été définie après l'appel de la fonction, cela va retourner une erreur NameError.
"""


def test1():
    affiche_bonjour()


def affiche_bonjour():
    print("Bonjour")


test1()
