import random

def biomGenList(dlugosc):
    biomList = [0]
    while len(biomList) <= dlugosc:
        biom = random.randint(1, 3)
        for i in range(random.randint(250, 1000)):
            biomList.append(biom)

    print(biomList)
    return biomList

biomGenList(1024)

