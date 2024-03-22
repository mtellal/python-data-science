from array import array
import numpy as np


"""
Pimp images with different filters



"""


def ft_invert(array) -> list:
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


def ft_invert_np(array) -> np.ndarray:
    np_array = np.array(array)
    np_array = 255 - np_array
    return np_array


def ft_red(array) -> list:
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


def ft_red_np(array) -> np.ndarray:
    final = []
    np_array = np.array(array)
    np_array[..., 1] = 0
    np_array[..., 2] = 0
    return np_array


def ft_green(array) -> list:
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


def ft_green_np(array) -> np.ndarray:
    final = []
    np_array = np.array(array)
    np_array[..., 0] = 0
    np_array[..., 2] = 0
    return np_array



def ft_blue(array) -> list:
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


def ft_blue_np(array) -> np.ndarray:
    final = []
    np_array = np.array(array)
    np_array[..., 0] = 0
    np_array[..., 1] = 0
    return np_array


def ft_grey(array) -> list:
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
                    pixel = pixels[0] + pixels[1] + pixels[2]
                    new_line.append(pixel)
            else:
               new_line.append(array[row][column])
        final.append(new_line)
    return final


def ft_grey_np(array) -> np.ndarray:
    final = []
    np_array = np.array(array)
    np_array[..., 0] *= 0.2989
    np_array[..., 1] *= 0.5870
    np_array[..., 2] *= 0.1140
    return np_array

