from load_image import ft_load

print(ft_load("landscape.jpg"))

###  MORE TESTS ###

# all images in /images folder

c='\033[0;1;97m'
nc='\033[0m'


def test_ft_load(path: str):
    print(f"path = '{path}'")
    ft_load(str(path))
    print()

print(c, "\nMORE TESTS\n", nc)


print(c, "\ninvalid args\n", nc)


test_ft_load(15)
test_ft_load([1, 2])
test_ft_load("")
test_ft_load(["images"])
test_ft_load("wdfoudwfoudwvoufddvwofuvwuofwvouvfuwdvd")
test_ft_load("images/image.png")


print(c, "\nvalid args but bad images\n", nc)

test_ft_load("./images/animal_pdf")
test_ft_load("./images/robot.jpeg")
test_ft_load("./images/robot.png")
test_ft_load("./images/img.png")
test_ft_load("./images/img2.webp")
test_ft_load("./images/index.html")



print(c, "\nvalid images\n", nc)

test_ft_load("./images/image.jpg")
test_ft_load("./images/animal.jpg")
test_ft_load("./images/animal.jpeg")
test_ft_load("./images/animal_corrupted")

# animal_corrupted  animal_not_jpeg  landscape.jpg  robot.jpeg
# animal.jpeg       image.jpg        limg           robot.png


