import PIL
from PIL import Image
import numpy as np

"""
    Load an image from a path and display informations
"""

def printImageInformations(img: Image):
    array = np.array(img)
    _str = "The shape of this image is:"
    if len(array) == 0:
        _str += " (0, 0, 0)"
    print("The shape of image is:", array.shape)
    print(array)
    return array


def ft_load(path: str) -> list:
    """
        Load an image from a path and display image informations

        Arguments:
            path (str): the path to the file
        Returns:
            nothing: only print in stdin        
    """
    try:
        assert type(path) is str, "path not a str"
        with Image.open(path) as img:
            assert img is not None, "image could not be read"
            err_format = "bad format file, JPEG or JPG ony"
            assert ["JPEG", "JPG"].count(img.format) > 0, err_format
            array = printImageInformations(img)
            return array
    except FileNotFoundError as msg:
        print("Error: file not found:", msg)
    #except PIL.UnidentifiedImageError as msg:
        #print("Error:", msg)
    except PermissionError as msg:
        print("Error: permission error:", msg)

def main():
    ft_load("./landscape.jpg")
    #ft_load("dwf")
    #ft_load([1, 3, 4])
    #ft_load({"dw", 2})
    #ft_load("./index.html")
    #ft_load("./img")
    #ft_load("./limg")
    #ft_load("./image2.jpg")
    #ft_load("./robot.png")
    #ft_load("./robot.jpeg")
    pass

if __name__ == "__main__":
    main()
