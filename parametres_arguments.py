def affiche(message):  # paramètre
    print(message)


affiche("bonjour")  # argument


# le message "bonjour" sera envoyer au paramètre
# output bonjour

def affiche1(message="Message par défaut"):  # on peut definir valeur par défaut pour le paramètres
    print(message)


# le message par défaut est utilisé seulement si on n'envoyé pas d'argument à la fonction
affiche1()
# sinon, c'est l'argument envoyé qui sera pris en compte
affiche1("bonjour")


# on peut définir un ou plusieurs paramètres dans une fonction

# ces paramètres deviennent des variables qu'on peut utiliser à l'intérieur de la focntion

# on peut définir des valeurs par défaut pour les paramètres

# on peut spécifier explicitement à quel paramètre on envoi une valeur lors de l'appel de la fonction


def addition(a, b):
    return a + b


addition(b=10, a=5)  # ici on inverse la position des paramètres 
