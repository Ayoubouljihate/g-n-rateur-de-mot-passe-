import random
# demander à l'utilisateur de saisir la longueur du mot passe avec 'input'
nombres_de_caractères=int(input('donner nombre de caractères du mdp'))
# la liste des lettres, majuscules et nombre pour le mot de passe
liste_majuscules_lettres_nombre='abcdefghijklmnopqrstuvwxyza0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# regrouper les caractères selectionnés en un seul bloc
motdepasse="".join(random.sample(liste_majuscules_lettres_nombre,nombres_de_caractères))
print(motdepasse)


# demander à l'utilisateur de saisir le nombre de caractères du login avec  'input'
nombres_de_caractère=int(input('donner nombre de caractères du login'))
# la liste des lettres, majuscules et nombre pour le mot de passe
liste_majuscules_lettres_nombres='abcdefghijklmnopqrstuvwxyza0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# regrouper les caractères selectionnés en un seul bloc
login="".join(random.sample(liste_majuscules_lettres_nombres,nombres_de_caractère))
print(login)







#objectif(fini): regrouper les  caractéres selectionnés aléatoirement en un seul mot et générer un login pour plus tard.