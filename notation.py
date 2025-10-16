# notation.py
# TODO : Version buggée — à corriger après exécution des tests unitaires
# TODO : Mettre des commentaires pour identifier les bugs trouvés et comment vous les avez corrigés.

def valider_notes(notes: list[float]) -> bool:
    """
    Vérifie que la liste de notes contient exactement 9 entiers entre -3 et +3.
    :param notes: liste de notes
    :returns: vrai si la liste et valide, sinon faux.
    """
    if len(notes) < 9 or len(notes) > 9: # ajout de plus petit que 9 puisque ca doit etre exactement 9
        return False

    for n in notes:
        if n > 3 or n < -3: # ajout de -3 puisque ca doit etre entre -3 et 3
            return False

    return True


def calculer_points(vbase: float, notes: list[float]) -> float:
    """
    Calcule la note finale d’un mouvement.
    :param vbase: valeur de base de la note
    :param notes: liste de notes
    :returns: valeur de la note finale
    """
    try:
        statut =  valider_notes(notes)
        if statut == False:
            return "Erreur" # si la liste est plus petite ou grande que 9, renvoie une erreur

        note_max = max(notes)
        note_min = min(notes)

        #for i in range(len(notes)):
            #if notes[i] == note_max or note_min:
                #notes.remove(notes[i])
        notes.remove(note_max)
        notes.remove(note_min) # remplacé la boucle par une action, pusique la boucle enlevait le max et min plusieurs fois.


        moyenne = sum(notes) / 7 # 9 remplacé par 7, pusique qu'il y a seulement 7 valeurs
        total = round(vbase + moyenne, 2) # arrondi
        return total

    except ValueError:
        print("Erreur")
        return 0



