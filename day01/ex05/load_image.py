from PIL import Image, UnidentifiedImageError
import numpy as np


"""
    Load an image from a path and display informations
"""


def ft_load(path: str, _print: bool = False) -> np.ndarray:
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
            valid_format = ["JPEG", "JPG"]
            _format = img.format
            assert valid_format.count(_format) > 0, err_format + _format
            array = np.array(img)
            if _print is True:
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
    except Exception as msg:
        print("Exception:", msg)
    return []
