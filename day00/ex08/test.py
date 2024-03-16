from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


"""
    Tests of ft_tqdm and tqdm
"""

print("100 elements")
for elem in ft_tqdm(range(100)):
    sleep(0.005)
print()
for elem in tqdm(range(100)):
    sleep(0.005)
print("0 elements")
for elem in ft_tqdm(range(0)):
    sleep(0.005)
print()
for elem in tqdm(range(0)):
    sleep(0.005)
print("1 element")
for elem in ft_tqdm(range(1)):
    sleep(0.005)
print()
for elem in tqdm(range(1)):
    sleep(0.005)
print("10 elements")
for elem in ft_tqdm(range(10)):
    sleep(0.005)
print()
for elem in tqdm(range(10)):
    sleep(0.005)
print("8 elements range(2, 10)")
for elem in ft_tqdm(range(2, 10)):
    sleep(0.005)
print()
for elem in tqdm(range(2, 10)):
    sleep(0.005)
print("500 elements")
for elem in ft_tqdm(range(500)):
    sleep(0.005)
print()
for elem in tqdm(range(500)):
    sleep(0.005)
