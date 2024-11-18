from p5 import *

# Variables globales
a = 0
b = 0
pacman_x = 50
pacman_y = 200
boules = [[150, 200], [250, 200], [350, 200]]  # Positions des boules
current_target = 0  # Indice de la boule ciblée

def setup():
    size(400, 400)
    no_stroke()

def draw():
    global a, b, pacman_x, pacman_y, current_target

    background(220)

    # Animation de Pac-Man
    fill(255, 255, 0)
    circle(pacman_x, pacman_y, 50)  # Corps
    fill(0)
    circle(pacman_x, pacman_y - 12.5, 5)  # Oeil
    fill(220)
    triangle(
        pacman_x, pacman_y,
        pacman_x + 25, pacman_y - 17.5 + a,
        pacman_x + 25, pacman_y + 17.5 + b
    )
    a += 1
    b -= 1
    if a == 70:
        a = 0
        b = 0

    # Déplacement automatique vers la boule cible
    if current_target < len(boules):
        target_x, target_y = boules[current_target]
        if pacman_x < target_x:
            pacman_x += 2  # Déplacement vers la droite
        elif pacman_x > target_x:
            pacman_x -= 2  # Déplacement vers la gauche

        if pacman_y < target_y:
            pacman_y += 2  # Déplacement vers le bas
        elif pacman_y > target_y:
            pacman_y -= 2  # Déplacement vers le haut

        # Si Pac-Man atteint la boule
        if distance((pacman_x, pacman_y), (target_x, target_y)) < 25 + 10:
            current_target += 1  # Passer à la prochaine boule

    # Dessiner les boules restantes
    for i in range(current_target, len(boules)):
        boule_x, boule_y = boules[i]
        fill(255, 0, 0)
        circle(boule_x, boule_y, 20)

run()
