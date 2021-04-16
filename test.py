import random

t = [0]
r = 0

def ifRandomRSet(n, r1, r2):
    if t[-1] == n:
        return random.randrange(r1, r2)
    else:
        return None


def GenerateTerainGrassland(szerokosc=2048):
    for i in range(szerokosc):

        r = ifRandomRSet(0, 0, 2)
        if r != None:
            t.append(r)

        r = ifRandomRSet(1, 0, 3)
        if r != None:
            t.append(r)

        r = ifRandomRSet(2, 1, 4)
        if r != None:
            t.append(r)

        r = ifRandomRSet(3, 2, 5)
        if r != None:
            t.append(r)

        r = ifRandomRSet(4, 3, 6)
        if r != None:
            t.append(r)


        r = ifRandomRSet(5, 4, 5)
        if r != None:
            t.append(r)

    return t

print("Wpisz na ile kratek ma być świat(Szerokosćcc)")
dlugosc = int(input("->"))

swiat = GenerateTerainGrassland(dlugosc)

swiatFileToWrite = []

for sz in range(dlugosc):
    swiatFileToWrite.append([])
    if swiat[sz] == 0:
        for i in range(0, 36 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{792 - i},0\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{840},3\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{888},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{936},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{984},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1032},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1080},1\n")
        for i in range(0, 52 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1")
    elif swiat[sz] == 1:
        for i in range(0, 35 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{744 - i},0\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{792},3\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{840},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{888},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{936},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{984},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1032},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1080},1\n")
        for i in range(0, 52 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")
    elif swiat[sz] == 2:
        for i in range(0, 34 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{696 - i},0\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{744},3\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{792},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{840},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{888},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{936},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{984},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1032},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1080},1\n")
        for i in range(0, 52 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")
    elif swiat[sz] == 3:
        for i in range(0, 33 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{648 - i},0\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{696},3\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{744},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{792},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{840},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{888},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{936},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{984},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1032},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1080},1\n")
        for i in range(0, 52 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")
    elif swiat[sz] == 4 :
        for i in range(0, 32 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{600 - i},0\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{648},3\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{696},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{744},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{792},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{840},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{888},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{936},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{984},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1032},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1080},1\n")
        for i in range(0, 52 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")
    elif swiat[sz] == 5 :
        for i in range(0, 28 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{600 - i},0\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{456},4\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{504},4\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{552},4\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{600},4\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{648},3\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{696},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{744},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{792},2\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{840},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{888},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{936},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{984},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1032},1\n")
        swiatFileToWrite[sz].append(f"{sz * 48},{1080},1\n")
        for i in range(0, 52 * 48, 48):
            swiatFileToWrite[sz].append(f"{sz * 48},{1080 + i},1\n")

saveTemp = []

for szerokosc in range(dlugosc):
    for wysokosc in range(100):
        try:
            saveTemp.append(swiatFileToWrite[szerokosc][wysokosc])
        except Exception:
            pass

f = open("save.mov", "w")

f.writelines(saveTemp)