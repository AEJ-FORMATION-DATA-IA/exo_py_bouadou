# Initialisation des variables

a = 15
b = 4
c = a + b
d = a * b
e = (a**b)  # Se traduit par a exposant b
f = (a/b)
g = (a//b)  # Faire une division entière
h = (a % b)

# On affiche le résultat des opérations

print(f'Le resultat de {a} + {b} = {c}')
print(f'Le resultat de {a} x {b} = {d}')
print(f'Le resultat de {a} exposant {b} = {e}')
print(f'Le resultat de {a} / {b} = {f}')
print(f'Le resultat de la division entiere entre {a} et {b} est {g}')
print(f'Le reste de {a} / {b} est {h}')

# Création et initialisation du tuple
tuple_1 = (a, b, c)

# Ajout d'une valeur au tuple
tuple_1 += (d,)

# Modification de la valeur A par 16
"""
De nature il n'est pas possible de modifer une donnée dans un tuple.
Une alternative serait de convertir ce tuple en une liste,
modifer la valeur, puis convertir la liste en tuple

Je vais donc définir une fonction modifier_valeur_tuple(t, index, valeur)
qui va retourner un tuple
* t est un tuple
* Index est la position de la donnée à modifier
* Valeur est la nouvelle valeur de la donnée
"""


def modifier_valeur_tuple(t, index, valeur) -> tuple:
    liste = list(t)  # Conversion du tuple en liste
    liste[index] = valeur  # Modification de la valeur
    t = tuple(liste)  # Conversion de la liste en tuple

    return t


# On modifie la valeur du tuple
tuple_1 = modifier_valeur_tuple(tuple_1, 0, 16)

# Supression du tuple
del tuple_1

# Création du dictionnaire
dico = {'a': a, 'b': b, 'a+b': c, 'axb': d, 'a**b': e, 'a/b': f, 'a//b': g}

# Ajout de la variable h au dictionnaire
dico['modulo'] = h

# Suppression de c dans dico
del dico['a+b']

# Affichage des clés du dicionnaire
print('\nCles du dictionnaire')
[print(key) for key in dico]

# Affichage des valeurs du dictionnaire
print('\nValeurs du dictionnaire')
[print(dico[key]) for key in dico]

# Affichage des clés et des valeurs dans dico
print('\n[Cles] => Valeurs du dictionnaire')
[print(f'[{key}] => { dico[key]}') for key in dico]

# Création de la liste

premiere_liste = ['A', 'B', 'C', 'D']

# Cette liste contient la valeur des variable a, b, c, d initialisée plus haut
deuxieme_liste = [a, b, c, d]

# On ajoute les deux première liste au troisième
troisieme_liste = [premiere_liste, deuxieme_liste]

# On ajoute "E" et "F" à la première liste
premiere_liste.append('E')
premiere_liste.append('F')

# on supprime B de la li2ste
premiere_liste.remove('B')

# On remplace A par G
premiere_liste.pop(0)
premiere_liste.insert(0, 'G')

# ALGORITHME

# On initialise les variables valeur_1 et valeur_2 à 0
valeur_1 = 0
valeur_2 = 0

# On recupère la valeur saisie par l'utilisateur
valeur_1 = input('\nVeuillez entrer un premier nombre entier\n')

try:
    valeur_1 = int(valeur_1)
except:
    print('\nVous avez fais une erreur')
else:
    valeur_2 = input('\nVeuillez entrer un deuxieme nombre entier\n')
    valeur_2 = int(valeur_2)

    # On vérifie si le type de la valeur_2 est de type int et on affiche un message
    if (type(valeur_2) != int):
        print('\nVous avez fais une erreur')

        # On vérifie si valeur_1 est supérieur à valeur_2 et on affiche un message
    elif (valeur_1 > valeur_2):
        print(f'\n{valeur_1} est superieur a {valeur_2}')

        # On vérifie si valeur_1 est inférieur à valeur_2 et on affiche un message
    elif (valeur_1 < valeur_2):
        print(f'\n{valeur_2} est superieur a {valeur_1}')

        # Sinon probablement valeur_1 est égale à valeur_2 et on affiche un message
    else:
        print('\n' + str(valeur_1) + ' est egale a ' + str(valeur_2))
