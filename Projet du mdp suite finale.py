import random
# demander à l'utilisateur de saisir la longueur du mot passe avec 'input'

nombres_de_caractères=int(input('donner nombre de caractères du mdp '))
# la liste des lettres, majuscules et nombre pour le mot de passe

liste_majuscules_lettres_nombre='abcdefghijklmnopqrstuvwxyza0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# regrouper les caractères selectionnés en un seul bloc en utlisant la méthode join

motdepasse="".join(random.sample(liste_majuscules_lettres_nombre,nombres_de_caractères))

print(motdepasse)









