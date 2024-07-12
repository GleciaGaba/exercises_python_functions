"""
Trouver l'erreur dans la fonction
Dans cet exercice, le script ne retourne pas d'erreur mais n'affiche pas le résultat escompté.

La fonction addition devrait nous permettre d'additionner deux nombres ensemble.

Cependant, quand on print la variable resultat, Python nous retourne None, au lieu du résultat de l'addition (ici 15).

Modifiez la fonction pour que le print de resultat affiche le résultat de l'addition.

"""


def addition(a, b):
    return a + b


resultat = addition(5, 10)
print(resultat)


"""
Explications

Une fonction peut, dans certains cas, ne pas retourner de résultat (par exemple, 
une fonction qui exécute plusieurs print à la suite, pour afficher un message de bienvenue 
par exemple, n'a pas besoin de retourner de valeur spécifique).

Cependant, ici, la fonction sert à calculer la somme de deux valeurs. Il faut donc 
retourner d'une façon où d'une autre le résultat de cette addition.

Pour retourner une valeur dans une fonction, on utilise le mot clé return, comme ici :

return c
Cela nous permet de récupérer la valeur de l'addition lors de l'appel de la 
fonction dans une variable :

resultat = addition(5, 10)
Points importants à retenir

Pour retourner une valeur à l'intérieur d'une fonction, on utilise le mot clé return.

"""