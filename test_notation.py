# test_notation.py
# Tests unitaires pour le module notation.py

import pytest

import notation
from notation import *

# -----------------------------
# TODO : Tests unitaires pour valider_notes()
# -----------------------------
def test_valider_notes():
    # Arrange
    notes = [3, 2, 1, 2, 3, 3, 2, 2, 3]

    resultat_attendu = True
    # Act
    resultat_fonc = notation.valider_notes(notes)

    # Assert
    assert resultat_attendu == resultat_fonc




# -----------------------------
# TODO : Tests unitaires pour calculer_points()
# -----------------------------
def test_calculer_points():
    # Arrange
    vbase = (1)
    notes = [-1,-2,-1,-3,-2,-1,-3,-2,-3]
    resultat_attendu = -1

    # Act
    resultat_fonc2 = notation.calculer_points(vbase, notes)
    # Assert
    assert resultat_attendu == resultat_fonc2
