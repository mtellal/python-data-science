from load_image import ft_load, printImageInformations
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def createFinalImage(img: Image):
    border_width = 50
    graduation_interval = 50
    black=(0, 0, 0)
    white=(255, 255, 255)

    width = img.width + 2 * border_width
    height = img.height + 2 * border_width

    f_img = Image.new("RGB", (width, height), white)

    f_img.paste(img, (border_width, border_width))

    draw = ImageDraw.Draw(f_img)
    font = ImageFont.load_default()

    for x in range(border_width, width, graduation_interval):
        draw.text((x - 5, border_width - 25), str(x - border_width), fill=black)
        draw.line(((x, border_width), (x, border_width - 10)), black)

    for y in range(border_width, height, graduation_interval):
        draw.text((border_width - 30, y - 5), str(y - border_width), fill=black)
        draw.line(((border_width, y), (border_width - 10, y)), black)
    return f_img


def main():
    array = ft_load("animal.jpeg")
    img = Image.fromarray(array)
    img = img.crop((450, 100, 850, 500))
    print("New shape after slicing:", img.size)
    img = img.convert("L")
    array = np.array(img)

    final_img = createFinalImage(img)
    final_img.show()


if __name__ == "__main__":
    main()
