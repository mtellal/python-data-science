from load_image import ft_load
import numpy as np
from PIL import Image, ImageDraw


"""
A program that should load the image "animal.jpeg", print some information
about it and display it after "zooming".

- The size in pixel on both X and Y axis
- The number of channel
- The pixel content of the image
- Display the scale on x and u axis on the image

"""


def createFinalImage(img: Image) -> Image:
    """
    Take an image, animal.jpeg in this case,
    and create a new image with graduate scale pixels informations

    Arguments:
        img (Image): image to scale and graduate
    Returns:
        f_img: final image with border graduation/scale
    """
    border_w = 50
    graduation_interval = 50
    black = (0, 0, 0)
    white = (255, 255, 255)

    width = img.width + 2 * border_w
    height = img.height + 2 * border_w

    f_img = Image.new("RGB", (width, height), white)
    f_img.paste(img, (border_w, border_w))

    draw = ImageDraw.Draw(f_img)

    for x in range(border_w, width, graduation_interval):
        draw.text((x - 5, border_w - 25), str(x - border_w), fill=black)
        draw.line(((x, border_w), (x, border_w - 10)), black)

    for y in range(border_w, height, graduation_interval):
        draw.text((border_w - 30, y - 5), str(y - border_w), fill=black)
        draw.line(((border_w, y), (border_w - 10, y)), black)
    return f_img


def printImageInformations(img: Image):
    """
    Print the shape and the contant of an image
    Arguments:
        img (Image): image to use
    """
    size = img.size
    array = np.array(img)
    array = [[[x] for x in row] for row in array]
    array = np.asarray(array)
    shape = np.shape(array)
    print("The shape of image is:", str(shape), "or", str(size))
    print(array)
    return array


def transpose(img: Image) -> np.ndarray:
    """
    Transpose an image (90deg rotation)
    Arguments:
        img (Image): image to transpose
    Returns:
        final (np.ndarray): transposed array
    """
    final = []
    array = np.asarray(img)
    column = len(array)
    row = len(array[0])
    for c in range(column, 0, -1):
        final.append([ row[c - 1] for row in array])
    final = np.array(final)
    return final


def main():
    array = ft_load("animal.jpeg", _print=False)
    img = Image.fromarray(array)
    img = img.crop((450, 100, 850, 500))
    img = img.convert("L")
    printImageInformations(img)
    array = transpose(img)
    img = Image.fromarray(array)
    print("New shape after Transpose:", img.size)
    print(np.asarray(img))
    final_img = createFinalImage(img)
    final_img.show()


if __name__ == "__main__":
    main()