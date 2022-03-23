from random import random
from time import sleep
from models.cellule import Cellule



class Grille:

    def __init__(self, largeur, hauteur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.matrix = [[Cellule() for _ in range(largeur)] for _ in range(hauteur)]

    def dans_grille(self, i, j):
        if 0 <= j < self.largeur and 0 <= i < self.hauteur:
            return True
        else:
            return False

    def setXY(self, i, j, cel):
        self.matrix[i][j] = cel

    def getXY(self, i, j):
        return self.matrix[i][j]

    def get_largeur(self):
        return self.largeur

    def get_hauteur(self):
        return self.hauteur

    # Ici les cellules dans les coins n'ont que 3 voisins.
    @staticmethod
    def est_voisin(i, j, x, y):
        if max(abs(x - i), abs(y - j)) > 1:
            return True

    def get_voisins(self, i, j):
        v = []
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if (x, y) != (i, j) and self.dans_grille(x, y):
                    v.append(self.getXY(x, y))
        return v

    def affecte_voisins(self):
        for i in range(self.hauteur):
            for j in range(self.largeur):
                self.matrix[i][j].set_voisins(self.get_voisins(i, j))

    def __str__(self):
        l = ""
        for i in range(self.hauteur):
            for j in range(self.largeur):
                l += str(self.matrix[i][j])
            l += "\n"
        return l

    def remplir_alea(self, taux):
        nb_cell = self.hauteur * self.largeur
        nb_viv = taux * nb_cell / 100
        # Parcours en hauteur de la matrice
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if random() <= taux / 100:
                    self.matrix[i][j].naitre()
                    self.matrix[i][j].basculer()

    def jeu(self):
        self.affecte_voisins()
        for i in range(self.hauteur):
            for j in range(self.largeur):
                self.matrix[i][j].calcule_etat_futur()

    def actualise(self):
        sleep(1)
        print("\u001B[H\u001B[J")
        for i in range(self.hauteur):
            for j in range(self.largeur):
                self.matrix[i][j].basculer()



