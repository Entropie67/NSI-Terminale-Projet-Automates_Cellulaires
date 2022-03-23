
class Cellule:

    def __init__(self):
        self._actuel = False
        self._futur = False
        self._voisins = None

    def est_vivant(self):
        return self._actuel

    def naitre(self):
        self._futur = True

    def mourrir(self):
        self._futur = False

    def set_voisins(self, liste):
        self._voisins = liste

    def get_voisins(self):
        return self._voisins

    def basculer(self):
        self._actuel = self._futur

    def __str__(self):
        return "\033[92m" + "X" + "\033[94m" if self._actuel else "\033[93m" + "-" + "\033[94m"

    def calcule_etat_futur(self):
        nb_vivants = sum([1 if cel.est_vivant() else 0 for cel in self._voisins])
        if self._actuel and not (nb_vivants == 2 or nb_vivants == 3):
            self.mourrir()
        if not self._actuel and nb_vivants == 3:
            self.naitre()