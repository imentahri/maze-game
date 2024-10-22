from collections import deque
import random
import turtle

class Graphe:
    def __init__(self, lignes, cols):
        self.lignes = lignes
        self.cols = cols
        self.graphe = {(0, 0): []}

    def ajt_noeud(self, i, j):
        if (i, j) not in self.graphe.keys():
            self.graphe[(i, j)] = []

    def ajt_arete(self, noeud1, noeud2, porte=False):
        if noeud2 in self.graphe.keys() and noeud1 in self.graphe.keys() and ((noeud2), True) not in self.graphe[noeud1] and ((noeud2), False) not in self.graphe[noeud1] and ((noeud1), True) not in self.graphe[noeud2] and ((noeud1), False) not in self.graphe[noeud2]:
            self.graphe[noeud1].append((noeud2, porte))
            self.graphe[noeud2].append((noeud1, porte))

    def list_noeuds(self):
        return self.graphe.keys()

    def list_aretes(self, noeud):
        if noeud not in self.graphe.keys():
            return self.graphe.values()

    def adjacence_noeud(self, noeud1, noeud2):
        voisins = self.graphe[noeud1]
        return (noeud2, True) in voisins or (noeud2, False) in voisins

    def afficher_graphe(self):
        print("Graphe:")
        for noeud, voisins in self.graphe.items():
            print(noeud, ": ", voisins)

    def successeurs(self, k):
        succ = []
        for voisin in self.graphe[k]:
            if voisin[1]:
                succ.append(voisin[0])
        return succ

    def ajt_aretes_voisins(self):
        for i in range(self.lignes):
            for j in range(self.cols):
                if i > 0:
                    self.ajt_arete((i, j), (i - 1, j), random.choice([True, False]))
                if i < self.lignes - 1:
                    self.ajt_arete((i, j), (i + 1, j), random.choice([True, False]))
                if j > 0:
                    self.ajt_arete((i, j), (i, j - 1), random.choice([True, False]))
                if j < self.cols - 1:
                    self.ajt_arete((i, j), (i, j + 1), random.choice([True, False]))

    def afficher_labyrinthe(self):
        turtle.speed(0)
        taille_case = 30
        chemin_trouve = [(0, 0)]
        for noeud in self.BFS((0, 0), (9, 9)):
            chemin_trouve.append(noeud)

        col = "#FFA500"

        for i in range(self.lignes):
            for j in range(self.cols):
                x = j * taille_case
                y = -i * taille_case
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                if (i, j) in chemin_trouve:
                    turtle.fillcolor(col)
                    turtle.begin_fill()
                if not a_mur_au_dessus(self.cols, i, j):
                    turtle.setheading(0)
                    turtle.forward(taille_case)
                else:
                    if ((i - 1, j), False) in self.graphe.get((i, j), []):
                        turtle.setheading(0)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(0)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()

                if not a_mur_a_droite(self.cols, i, j):
                    turtle.setheading(-90)
                    turtle.forward(taille_case)
                else:
                    if ((i, j + 1), False) in self.graphe.get((i, j), []):
                        turtle.setheading(-90)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(-90)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()

                if not a_mur_en_bas(self.cols, i, j):
                    turtle.setheading(180)
                    turtle.forward(taille_case)
                else:
                    if ((i + 1, j), False) in self.graphe.get((i, j), []):
                        turtle.setheading(180)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(180)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()

                if not a_mur_a_gauche(self.cols, i, j):
                    turtle.setheading(90)
                    turtle.forward(taille_case)
                else:
                    if ((i, j - 1), False) in self.graphe.get((i, j), []):
                        turtle.setheading(90)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(90)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()
                if (i, j) in chemin_trouve:
                    turtle.end_fill()

        turtle.hideturtle()
        turtle.done()

    def labyrinthe_aleatoire(self, depart, arrivee):
        for i in range(lignes):
            for j in range(cols):
                self.ajt_noeud(i, j)
        t = None
        while t == None:
            self.graphe = {(0, 0): []}
            for i in range(lignes):
                for j in range(cols):
                    self.ajt_noeud(i, j)
            self.ajt_aretes_voisins()
            t = self.BFS(depart, arrivee)

    def BFS(self, depart, arrivee): #trouver le chemin entre start et fin selon bfs(en largeur)
        file = deque()
        file.append(depart)
        visites = [depart]
        accessibles = {}
        while len(file) > 0:
            actuel = file.popleft()
            for voisin in self.successeurs(actuel):
                if voisin not in visites:
                    accessibles[voisin] = actuel
                    file.append(voisin)
                    visites.append(voisin)

        chemin_fwd = {}
        cellule = arrivee
        while cellule != (0, 0):
            try:
                chemin_fwd[accessibles[cellule]] = cellule
                cellule = accessibles[cellule]
            except:
                print('N\'existe pas!')
                return None
        return chemin_fwd


def a_mur_au_dessus(cols, ligne, col):
    if ligne == 0:
        return False
    else:
        return True


def a_mur_en_bas(cols, ligne, col):
    if ligne == cols - 1:
        return False
    else:
        return True


def a_mur_a_gauche(cols, ligne, col):
    if col == 0:
        return False
    else:
        return True


def a_mur_a_droite(cols, ligne, col):
    if col == cols - 1:
        return False
    else:
        return True


lignes = 10
cols = 10
labyrinthe = Graphe(lignes, cols)
labyrinthe.labyrinthe_aleatoire((0, 0), (9, 9))
labyrinthe.afficher_labyrinthe()
