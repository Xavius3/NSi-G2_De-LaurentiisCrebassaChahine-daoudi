from p5 import *
a = 125
def setup():
    size(400, 400)  # Taille du canevas
    no_stroke()     # Pas de contours

def draw():

    global a
    background(220)

    # Corps du fantôme
    fill(0, 150, 255)          # Couleur bleu du fantôme
    ellipse((200, 250), 120, 120)  # Tête
    rect((140, 250), 120, 80)      # Bas du corps

    # Dentelures en bas du corps
    fill(220)  # Couleur de fond pour créer les vagues
    for i in range(6):
        ellipse((a + i * 30, 330), 30, 30)  # Cercles en bas
    a = a + 1
    if a == 155:
        a =125

    # Yeux du fantôme
    fill(255)  # Blanc pour les yeux
    ellipse((180, 230), 25, 35)  # Oeil gauche
    ellipse((220, 230), 25, 35)  # Oeil droit

    # Pupilles
    fill(0)  # Noir pour les pupilles
    ellipse((180, 240), 10, 10)  # Pupille gauche
    ellipse((220, 240), 10, 10)  # Pupille droite

run()