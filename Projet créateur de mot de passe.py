import random
# demander à l'utilisateur de saisir la longueur du mot passe avec 'input'
nombres_de_caractères=int(input('donner le nombre de caractères du mot de passe'))
# la liste des lettres, majuscules et nombre pour le mot de passe
liste_majuscules_lettres_nombre='abcdefghijklmnopqrstuvwxyza0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#cette fonction permet de selectionner des caractéres au hasard dans l'ensemble 'liste_majuscules_lettres_nombre'
print(random.sample(liste_majuscules_lettres_nombre,nombres_de_caractères))



nombres_de_caractère=int(input('donner le nombre de caractères du login'))
liste_majuscules_lettres_nombres='abcdefghijklmnopqrstuvwxyza0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(random.sample(liste_majuscules_lettres_nombres,nombres_de_caractère))







#objectif(plus tard): regrouper les  caractéres selectionnés aléatoirement en un seul mot et générer un login pour plus tard.