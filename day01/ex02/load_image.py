from PIL import Image, UnidentifiedImageError
import numpy as np


"""
    Load an image from a path and display informations
"""


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
        assert len(path) > 0, "path empty"
        with Image.open(path) as img:
            assert img is not None, "image could not be read"
            err_format = "bad format file, JPEG or JPG only: "
            assert ["JPEG", "JPG"].count(img.format) > 0, err_format + img.format
            array = np.array(img)
            print("The shape of this image is: ", end='')
            if len(array) == 0:
                print("(0, 0, 0)")
            else:
                print(array.shape)
            print(array)
            return array
    except AssertionError as msg:
        print("AssertionError:", msg)
    except FileNotFoundError as msg:
        print("FileNotFoundError:", msg)
    except UnidentifiedImageError as msg:
        print("UnidentifiedImageError:", msg)
    except PermissionError as msg:
        print("PermissionError:", msg)
    return []
