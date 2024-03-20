from load_image import ft_load, printImageInformations
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def main():
    array = ft_load("animal.jpeg")
    img = Image.fromarray(array)
    img = img.crop((450, 100, 850, 500))
    print("New shape after slicing:", img.size)
    img = img.convert("L")
    array = np.array(img)

    border_width = 50
    border_color = (255, 255, 255)  # Couleur blanche pour la bordure
    graduation_interval = 50

    # Définir la taille de l'image avec la bordure
    new_width = img.width + 2 * border_width
    new_height = img.height + 2 * border_width

    # Créer une nouvelle image avec une bordure blanche
    border_image = Image.new("RGB", (new_width, new_height), border_color)

    # Copier l'image d'origine dans la nouvelle image avec la bordure
    border_image.paste(img, (border_width, border_width))

    # Dessiner la graduation sur la bordure
    draw = ImageDraw.Draw(border_image)
    font = ImageFont.load_default()

    # Graduation sur l'axe des x
    for x in range(border_width, new_width, graduation_interval):
        draw.text((x - 5, border_width - 25), str(x - border_width), font=font, fill=(0, 0, 0))
        draw.text((x - 1, border_width - 12), str("|"), font=font, fill=(0, 0, 0))

    # Graduation sur l'axe des y
    for y in range(border_width, new_height, graduation_interval):
        draw.text((border_width - 40, y), str(y - border_width), font=font, fill=(0, 0, 0))

    # Afficher l'image avec la bordure graduée
    border_image.show()


if __name__ == "__main__":
    main()
