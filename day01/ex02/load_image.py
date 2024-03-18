from PIL import Image
import numpy as np

"""
    Load an image from a path and display her informations
"""

def ft_load(path: str) -> None:
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
            img = img.convert("RGB")
            array = np.array(img)
            _str = "The shape of this image is:"
            if len(array) == 0:
                _str += " (0, 0, 0)"
            else:
                _str += f"({len(array)}, {len(array[0])}, {len(array[0, 0])})"
            print(_str)
            print(array)
    except FileNotFoundError as msg:
        print("Error: file not found:", msg)
    except PermissionError as msg:
        print("Error: permission error:", msg)
    except Exception as msg:
        print("Error: opening file failed:", msg)


def main():
    ft_load("./landscape.jpg")
    ft_load("dwf")
    ft_load([1, 3, 4])
    ft_load({"dw", 2})
    ft_load("./index.html")
    ft_load("./img")
    ft_load("./limg")
    ft_load("./image2.jpg")
    ft_load("./robot.png")
    ft_load("./robot.jpeg")


if __name__ == "__main__":
    main()
