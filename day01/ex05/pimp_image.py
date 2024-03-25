import numpy as np


"""
Pimp images with different filters
"""


def ft_invert(array: np.ndarray) -> list:
    """
    Invert color of an image
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array = array.tolist()
        final = []
        for row in range(0, len(array)):
            new_line = []
            for column in range(0, len(array[0])):
                if isinstance(array[row][column], list):
                    if isinstance(array[row][column][0], list):
                        raise Exception("Invalid image (4 dimensions found")
                    else:
                        new_line.append([255 - x for x in array[row][column]])
                else:
                    new_line.append(255 - array[row][column])
            final.append(new_line)
        return final
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)


def ft_invert_np(array: np.ndarray) -> np.ndarray:
    """
    Invert color of an image
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array = 255 - array
        return array
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)


def ft_red(array: np.ndarray) -> list:
    """
    Transform image in variations of red
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array = array.tolist()
        final = []
        for row in range(0, len(array)):
            new_line = []
            for column in range(0, len(array[0])):
                if isinstance(array[row][column], list):
                    if isinstance(array[row][column][0], list):
                        raise Exception("Invalid image (4 dimensions found")
                    else:
                        pixels = [0, 0, 0]
                        pixels[0] = array[row][column][0]
                        new_line.append(pixels)
                else:
                    new_line.append(array[row][column])
            final.append(new_line)
        return final
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)


def ft_red_np(array: np.ndarray) -> np.ndarray:
    """
    Transform image in variations of red
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array[..., 1] = 0
        array[..., 2] = 0
        return array
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)


def ft_green(array: np.ndarray) -> list:
    """
    Transform image in variations of green
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array = array.tolist()
        final = []
        for row in range(0, len(array)):
            new_line = []
            for column in range(0, len(array[0])):
                if isinstance(array[row][column], list):
                    if isinstance(array[row][column][0], list):
                        raise Exception("Invalid image (4 dimensions found")
                    else:
                        pixels = [0, 0, 0]
                        pixels[1] = array[row][column][1]
                        new_line.append(pixels)
                else:
                    new_line.append(array[row][column])
            final.append(new_line)
        return final
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)


def ft_green_np(array: np.ndarray) -> np.ndarray:
    """
    Transform image in variations of green
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array[..., 0] = 0
        array[..., 2] = 0
        return array
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)


def ft_blue(array: np.ndarray) -> list:
    """
    Transform image in variations of blue
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array = array.tolist()
        final = []
        for row in range(0, len(array)):
            new_line = []
            for column in range(0, len(array[0])):
                if isinstance(array[row][column], list):
                    if isinstance(array[row][column][0], list):
                        raise Exception("Invalid image (4 dimensions found")
                    else:
                        pixels = [0, 0, 0]
                        pixels[2] = array[row][column][2]
                        new_line.append(pixels)
                else:
                    new_line.append(array[row][column])
            final.append(new_line)
        return final
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)


def ft_blue_np(array: np.ndarray) -> np.ndarray:
    """
    Transform image in variations of blue
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array[..., 0] = 0
        array[..., 1] = 0
        return array
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)


def ft_grey(array: np.ndarray) -> list:
    """
    Transform image in variations of grey
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array = array.tolist()
        final = []
        for row in range(0, len(array)):
            new_line = []
            for column in range(0, len(array[0])):
                if isinstance(array[row][column], list):
                    if isinstance(array[row][column][0], list):
                        raise Exception("Invalid image (4 dimensions found")
                    else:
                        pixels = [0, 0, 0]
                        pixels[0] = array[row][column][0] / 3
                        pixels[1] = array[row][column][1] / 3
                        pixels[2] = array[row][column][2] / 3
                        pixel = np.sum(pixels)
                        new_line.append(pixel)
                else:
                    new_line.append(array[row][column])
            final.append(new_line)
        return final
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)


def ft_grey_np(array: np.ndarray) -> np.ndarray:
    """
    Transform image in variations of grey
    """
    try:
        assert type(array) is np.ndarray, "invalid array type (np.ndarray)"
        array[..., 0] *= 0.2989
        array[..., 1] *= 0.5870
        array[..., 2] *= 0.1140
        return array
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print("Error:", msg)
