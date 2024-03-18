from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(img):
    x = slice(100, 500)
    new_tab = img[x]
    print(new_tab)
    final = []
    slice_obj = slice(450, 850)
    for i in range(0, len(new_tab)):
        final_row = new_tab[i, slice_obj]
        #final_row = list(map(lambda pixels: [int(pixels[0] * 0.2989), int(pixels[1] * 0.5870), int(pixels[2] * 0.1140)], final_row))
        final.append(final_row)
    final = np.array(final) 
    #print(f"New shape after slicing: ({len(final)}, {len(final[0]}, {len(final}) or ")
    #final = list(map(lambda pixels: [int((pixels[0] + pixels[1] + pixels[2]) / 3)], final))
    final = np.dot(final[..., :3], [0.2989, 0.5870, 0.1140])
    print(final)
    plt.imshow(final, cmap='gray')
    plt.axis('off')
    plt.show()


def main():
    img = ft_load("animal.jpeg")
    zoom(img)

if __name__ == "__main__":
    main()
