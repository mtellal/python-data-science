import cv2
from PYL import Image

def ft_load(path: str):
    img = cv2.imread(path)
    assert img is not None, "image could not be read"
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(img, img.format)

def main():
    ft_load("./landscape.jpg")

if __name__ == "__main__":
    main()
