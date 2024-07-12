"""
Trouver l'erreur dans la fonction
Dans cet exercice, la fonction multiplicateur_mot retourne une erreur.

Trouvez cette erreur et modifiez la fonction pour qu'elle ne retourne plus d'erreur.

Il y a plusieurs façons de fixer cette erreur.

Votre script doit afficher 5 fois le mot Bonjour à la suite (parce que dans la vie,
il est important de faire des scripts bien élevés...) : BonjourBonjourBonjourBonjourBonjour

"""


def multiplicateur_mot(mult, mot):
    return mot * mult


mot_multiplie = multiplicateur_mot(5, "Bonjour")
print(mot_multiplie)



# Correction
def multiplicateur_mot_c(mot, mult=5):
    return mot * mult


mot_multiplie_c = multiplicateur_mot_c(mot="Bonjour")
print(mot_multiplie_c)


"""
EXPLICATIONS

L'ordre des paramètres par défaut dans une fonction a son importance !

En effet, si vous définissez une valeur par défaut pour un paramètre qui se trouve en première position, 
vous avez l'obligation de définir une valeur par défaut pour tous les paramètres qui suivent.

La façon rapide de régler l'erreur qui se trouvait dans ce script était donc soit de définir une 
valeur par défaut pour les deux paramètres de la fonction, soit d'inverser l'ordre des paramètres, 
ce que nous avons fait dans la solution proposée ci-dessus.

POINTS IMPORTANTS À RETENIR

L'ordre des paramètres dans une fonction a son importance : vous ne pouvez pas mettre un paramètre 
sans valeur par défaut après un paramètre qui en a une.
"""