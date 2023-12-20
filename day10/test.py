from PIL import Image, ImageDraw


def lire_labyrinthe(fichier):
    # Ouvrir le fichier et lire son contenu
    with open(fichier, 'r') as file:
        lines = file.readlines()

    # Créer une liste pour stocker les lignes du labyrinthe
    labyrinthe = [list(line.strip()) for line in lines]

    return labyrinthe


def dessiner_labyrinthe(labyrinthe, taille_case=20):
    # Déterminer la taille de l'image en fonction du labyrinthe
    largeur = len(labyrinthe[0]) * taille_case
    hauteur = len(labyrinthe) * taille_case

    # Créer une image blanche
    image = Image.new("RGB", (largeur, hauteur), "white")
    draw = ImageDraw.Draw(image)

    # Parcourir le labyrinthe et dessiner chaque élément
    # Le but c'est de voir un labyrinthe :
    # - Le . représente du vide
    # - Le - représente une barre horizontale
    # - Le | représente une barre verticale
    # - Le F représente un coin nord-ouest
    # - Le 7 un coin nord-est
    # - Le L un coin sud-ouest
    # - Le J un coin sud-est
    for i in range(len(labyrinthe)):
        for j in range(len(labyrinthe[i])):
            x1, y1 = j * taille_case, i * taille_case # x1, y1 = coin haut gauche
            x2, y2 = x1 + taille_case, y1 + taille_case # x2, y2 = coin bas droit

            if labyrinthe[i][j] == '.':
                draw.rectangle([x1, y1, x2, y2], fill="white")
            elif labyrinthe[i][j] == '-':
                draw.line([(x1, (y1 + y2) // 2), (x2, (y1 + y2) // 2)], fill="black", width=2)
            elif labyrinthe[i][j] == '|':
                draw.line([((x1 + x2) // 2, y1), ((x1 + x2) // 2, y2)], fill="black", width=2)
            elif labyrinthe[i][j] == 'F':
                draw.line([((x1 + x2) // 2, (y1 + y2) // 2), ((x1 + x2) // 2, y2)], fill="black", width=2)
                draw.line([(x2, (y1 + y2) // 2), ((x1 + x2) // 2, (y1 + y2) // 2)], fill="black", width=2)
            elif labyrinthe[i][j] == '7':
                draw.line([((x1 + x2) // 2, (y1 + y2) // 2), ((x1 + x2) // 2, y2)], fill="black", width=2)
                draw.line([(x1, (y1 + y2) // 2), ((x1 + x2) // 2, (y1 + y2) // 2)], fill="black", width=2)
            elif labyrinthe[i][j] == 'L':
                draw.line([((x1 + x2) // 2, (y1 + y2) // 2), ((x1 + x2) // 2, y1)], fill="black", width=2)
                draw.line([(x2, (y1 + y2) // 2), ((x1 + x2) // 2, (y1 + y2) // 2)], fill="black", width=2)
            elif labyrinthe[i][j] == 'J':
                draw.line([((x1 + x2) // 2, (y1 + y2) // 2), ((x1 + x2) // 2, y1)], fill="black", width=2)
                draw.line([(x1, (y1 + y2) // 2), ((x1 + x2) // 2, (y1 + y2) // 2)], fill="black", width=2)

    # Enregistrer l'image
    image.save("labyrinthe.png")

if __name__ == '__main__':
    # Utilisation
    fichier_labyrinthe = "UselessRemove.txt"
    labyrinthe = lire_labyrinthe(fichier_labyrinthe)
    dessiner_labyrinthe(labyrinthe)
