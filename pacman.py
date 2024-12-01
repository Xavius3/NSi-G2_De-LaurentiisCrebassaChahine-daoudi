from p5 import *
a = 0
b = 0
positionXPA = 200
positionYPA = 200

def setup():
    size(400, 400)  # Taille du canevas
    noStroke()      # Contour

def draw():
    global a, b, positionXPA, positionYPA

    background(220)
    # Corps de Pac-Man
    fill(255, 255, 0)                # Couleur de Pac-Man
    circle(positionXPA, positionYPA, 75)  # Forme de Pac-Man avec un diamètre de 75

    # Yeux
    fill(0)
    circle(positionXPA, positionYPA - 20, 7)  # Yeux ajustés à la taille de Pac-Man

    # Bouche ouvre/ferme
    fill(220)                        # Couleur bouche
    triangle(positionXPA, positionYPA, positionXPA + 75, positionYPA - 35 + a, positionXPA + 75, positionYPA + 35 + b)
    a = a + 1
    b = b - 1

    if a == 71:
        a = 0
        b = 0

run()
