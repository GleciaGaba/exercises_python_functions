"""
Les fonctions locals() et globals() en Python sont très utiles pour comprendre et manipuler les espaces de
noms (namespaces). Voici une explication de chacune :
"""

# globals()

"""
Description: La fonction globals() renvoie un dictionnaire représentant l'espace de noms global actuel.

Utilisation: Cet espace de noms global contient toutes les variables globales
et les fonctions définies au niveau global.

"""

x = 10


def my_function():
    y = 5
    print(globals())


my_function()

"""
output:
{'__name__': '__main__', '__doc__': '\nLes fonctions locals() et globals() en Python sont très 
utiles pour comprendre et manipuler les espaces de\nnoms (namespaces). 
Voici une explication de chacune :\n', '__package__': None, '__loader__': <_frozen_importlib_external.
SourceFileLoader object at 0x000002867A5C4850>, '__spec__': None, '__annotations__': {}, '__builtins__':
<module 'builtins' (built-in)>, '__file__': 'C:\\Users\\Bazinga\\Documents\\python_2024\\formation_python_fonctions
\\fonctions_locals_globals.py', '__cached__': None, 'x': 10, 'my_function': <function my_function at 0x000002867A62B2E0>}
"""

#  locals()

"""
Description: La fonction locals() renvoie un dictionnaire représentant l'espace de noms local actuel.

Utilisation: Cet espace de noms local contient les variables locales et les paramètres locaux disponibles
dans la portée courante. Si locals() est appelée au niveau global, elle fonctionne de la même manière que globals()

"""
x1 = 10


def my_function1():
    y1 = 5
    print(locals())


my_function1()

# {'y1': 5}


"""
Différences Clés
Portée:

globals() renvoie l'espace de noms global, quel que soit l'endroit où il est appelé.
locals() renvoie l'espace de noms local de l'endroit où il est appelé (dans une fonction ou au niveau global).
Modification:

Modifier le dictionnaire renvoyé par globals() affecte directement l'espace de noms global.
Modifier le dictionnaire renvoyé par locals() ne modifie pas nécessairement les variables
locales, surtout dans une fonction.


"""