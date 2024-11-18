from p5 import *

def setup():
    size(400, 400)  # Définir la taille du canevas

def draw():
    background(0)  # Couleur de fond (noir)

    for i in range(int(random_uniform(15, 40))):  # Nombre d'étoiles aléatoire
        fill(255, 255, 255)  # Couleur blanche pour les étoiles
        ellipse(random_uniform(0, 400), random_uniform(0, 400), 5, 5)  # Position aléatoire des étoiles

run()
