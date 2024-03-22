from load_image import ft_load
from pimp_image import ft_invert, ft_invert_np, ft_red, ft_red_np, ft_green, ft_green_np, ft_blue, ft_blue_np, ft_grey, ft_grey_np
from PIL import Image
import numpy as np

def createImage(array, title = None):
    array = np.array(array, np.uint8)
    print(array.shape)
    print("array => ", array)
    img = Image.fromarray(array)
    img.show(title)


# ORIGINAL

_array = ft_load("landscape.jpg")
createImage(_array)


# INVERT
array = ft_invert(_array)
createImage(array, "invert")

#array = ft_invert_np(_array)
#createImage(array, "invert_np")


# RED

array = ft_red(_array)
createImage(array, "red")

#array = ft_red_np(_array)
#createImage(array, "red_np")



# GREEN

array = ft_green(_array)
createImage(array)

#array = ft_green_np(_array)
#createImage(array)


# BLUE

array = ft_blue(_array)
createImage(array)

#array = ft_blue_np(_array)
#createImage(array)



# GREY

array = ft_grey(_array)
createImage(array)

#array = ft_grey_np(_array)
#createImage(array)

