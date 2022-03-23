from models.grille import Grille

def main():
    g = Grille(10, 10)
    g.remplir_alea(50)
    print(g)
    continuer = True
    while continuer:
        # print("\u001B[H\u001B[J")
        g.jeu()
        g.actualise()
        print(g)

if __name__ == "__main__":
    main()