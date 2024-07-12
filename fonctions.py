"""
Une fonction permet de regrouper une suite d'instruction qui seront exécutées lors de l'appel de cette dernière.

Une fonction peut exécuter un comportement différent à chaque fois grâce à l'utilisation de paramètres
qui peuvent varier lors de l'appel de la fonction (grâce à l'envoi d'arguments).

"""
import os.path


#  Créer une fonction

def foo():
    print("La fonction s'exécute")


#  Il suffit ensuite d'utiliser le nom de la fonction suivie de parenthéses pour exécuter le code qu'elle contient:

def foo1():
    print("La fonction s'exécute")


foo1()


#  Les paramètres

# Une fonction peut posséder un ou plusieurs paramètres:

def somme(a, b):  # paramètres
    print(a + b)


somme(10, 5)  # arguments

#  Quand on appelle la fonction, on peut envoyer des objets à ces paramètres. Ces objets sont appelés arguments.

"""
Retourner une valeur
On peut retourner une valeur dans une fonction grâce au mot clé return.

Ce mot clé a pour effet de mettre fin à l'exécution de la fonction. 
Dans le code suivant, le print ne sera ainsi jamais exécuté. On parle de code inaccessible :

"""


def somme(a, b):
    return a + b
    print(a + b)


print(somme(10, 5))


#  La valeur retournée par une fonction peut être récupérée dans une variable lors de l'appel de la fonction

def somme(a, b):
    return a + b


resultat = somme(10, 5)
print(resultat)

# L'instruction retourne nous fait sortir de la foction

"""
Oui, l'instruction return dans une fonction en Python a pour effet de faire sortir
la fonction immédiatement et de renvoyer une valeur (ou None si aucune valeur n'est
spécifiée) à l'endroit où la fonction a été appelée. Dès que l'instruction return est 
exécutée, le contrôle du programme quitte la fonction et retourne à l'appelant.

"""


def retourne_moi_cinq():
    return 5
    print("Cette ligne ne sera jamais exécutée")


print(retourne_moi_cinq())


#  Cette fonction a pour objectif de vérifier si un fichier existe ou non.

def verifier_fichier():
    if os.path.exists("fichier.txt"):
        return True
    else:
        return False


# On peut écrire cette fonction différemment car return nous fait sortir de la fonction.

def verifier_fichier():
    if os.path.exists("fichier.txt"):
        return True

    return False

# C'est possible de simplifier encore le code, car une fonction retourne un boolean
def verifier_fichier():
    return os.path.exists("fichier.txt")

# Pour retourner une valeur on utilise l'instruction return

# L'instruction return arrête l'exécution de la fonction

# Par défaut, une fonction retourne l'objet None

