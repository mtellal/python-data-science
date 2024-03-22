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
        with Image.open(path) as img:
            assert img is not None, "image could not be read"
            err_format = "bad format file, JPEG or JPG ony"
            assert ["JPEG", "JPG"].count(img.format) > 0, err_format
            array = np.array(img)
            print("The shape of this image is: ", end='')
            if len(array) == 0:
                print("(0, 0, 0)")
            else:
                print(array.shape)
            print(array)
            return array.tolist()
    except AssertionError as msg:
        print("AssertionError:", msg)
    except FileNotFoundError as msg:
        print("FileNotFoundError:", msg)
    except UnidentifiedImageError as msg:
        print("UnidentifiedImageError:", msg)
    except PermissionError as msg:
        print("PermissionError:", msg)
    return []


def main():
    ft_load(10)
    ft_load([1, 2])
    ft_load("not_found")
    print("not_found.jpeg")
    ft_load("not_found.jpeg")
    print("animal_permission")
    ft_load("animal_permission")
    print("animal_not_jpeg")
    ft_load("animal_not_jpeg")
    print("animal_corrupted")
    ft_load("animal_corrupted")
    #ft_load("animal.jpeg")

    pass


if __name__ == "__main__":
    main()
