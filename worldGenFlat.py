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

        r = ifRandomRSet(4, 3, 4)
        if r != None:
            t.append(r)

    return t

def treeSpawning(szerokosc):
    treeSpawningList = [0]
    for i in range(szerokosc):
        treeSpawningList.append(random.randint(1,9))
        if treeSpawningList[i] == 1:
            treeSpawningList.append(0)

    return treeSpawningList

print("Generator Świata")
print("Wybierz tryb generowania świata flat/def")
trybGeneratora = input("--> ")
if trybGeneratora == "flat":
    print("Wpisz na ile kratek ma być świat(Szerokosć)")
    dlugosc = int(input("->"))

    def swiat0(sz):
        for i in range(35 * 96, -96, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{696 - i},0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 69 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    swiatFileToWrite = []

    for sz in range(dlugosc):
        swiatFileToWrite.append([])
        swiat0(sz)

    saveTemp = []

    for szerokosc in range(dlugosc):
        for wysokosc in range(96):
            saveTemp.append(swiatFileToWrite[szerokosc][wysokosc])

    f = open("assest/saves/save.mov", "w")

    f.writelines(saveTemp)

elif trybGeneratora == "def":
    print("Wpisz na ile kratek ma być świat(Szerokosćcc)")
    dlugosc = int(input("->"))

    swiat = GenerateTerainGrassland(dlugosc)

    swiatFileToWrite = []

    treeSpawningList = treeSpawning(dlugosc)

    def swiat0(sz):
        for i in range(34 * 96, -96, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{696 - i},0\n")
        if treeSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},696,4\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},696,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 69 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    def swiat1(sz):
        for i in range(33 * 96, -96, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{600 - i},0\n")
        if treeSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},600,4\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},600,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},696,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 57 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    def swiat2(sz):
        for i in range(32 * 96, -96, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{504 - i},0\n")
        if treeSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},504,4\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},504,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},600,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},696,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 57 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    def swiat3(sz):
        for i in range(31 * 96, -96, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{408 - i},0\n")
        if treeSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},408,4\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},408,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},504,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},600,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},696,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 57 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    def swiat4(sz):
        for i in range(30 * 96, -96, -96):
            swiatFileToWrite[sz].append(f"{sz * 96},{312 - i},0\n")
        if treeSpawningList[sz] == 1:
            swiatFileToWrite[sz].append(f"{sz * 96},312,4\n")
        else:
            swiatFileToWrite[sz].append(f"{sz * 96},312,0\n")
        swiatFileToWrite[sz].append(f"{sz * 96},408,3\n")
        swiatFileToWrite[sz].append(f"{sz * 96},504,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},600,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},696,2\n")
        swiatFileToWrite[sz].append(f"{sz * 96},792,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},888,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},984,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1080,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1176,1\n")
        swiatFileToWrite[sz].append(f"{sz * 96},1272,1\n")
        for i in range(0, 57 * 96, 96):
            swiatFileToWrite[sz].append(f"{sz * 96},{1272 + i},1\n")

    swiatGenSetting = {0: swiat0, 1: swiat1, 2: swiat2, 3: swiat3, 4: swiat4}

    for sz in range(dlugosc):
        swiatFileToWrite.append([])
        swiatGenSetting[swiat[sz]](sz)

    saveTemp = []

    """for szerokosc in range(dlugosc):
        for wysokosc in range(96):
            if swiatFileToWrite[szerokosc][wysokosc].split(",")[2].split("\n")[0] == "4":
                treeSize = random.randint(1, 5)
                diamondDiscrybution = random.randint(1, 10)
                ironDiscrybution = random.randint(1, 4)
                coalDiscrybution = random.randint(1, 3)
                try:
                    if diamondDiscrybution == 1:
                        wysDiamentow = []
                        wysDiamentow.append(random.randint(40, 50))
                        wysDiamentow.append(random.randint(50, 100))
                        swiatFileToWrite[szerokosc - wysDiamentow[1]][wysokosc + wysDiamentow[0]] = str(swiatFileToWrite[szerokosc - wysDiamentow[1]][wysokosc + wysDiamentow[0]])[
                                                                ::-1].replace("1,", "9,", 1)[::-1]

                    elif diamondDiscrybution == 2:
                        wysDiamentow = []
                        wysDiamentow.append(random.randint(40, 50))
                        wysDiamentow.append(random.randint(10, 300))
                        swiatFileToWrite[szerokosc - wysDiamentow[1]][wysokosc + wysDiamentow[0]] = str(swiatFileToWrite[szerokosc - wysDiamentow[1]][wysokosc + wysDiamentow[0]])[
                                                                ::-1].replace("1,", "9,", 1)[::-1]
                        swiatFileToWrite[szerokosc - wysDiamentow[1]+1][wysokosc + wysDiamentow[0]] = str(
                            swiatFileToWrite[szerokosc - wysDiamentow[1]+1][wysokosc + wysDiamentow[0]])[
                                                                ::-1].replace("1,","9,",1)[::-1]

                except Exception:
                    pass

                try:
                    if ironDiscrybution == 1:
                        wysIron = []
                        wysIron.append(random.randint(30, 50))
                        wysIron.append(random.randint(50, 100))
                        swiatFileToWrite[szerokosc - wysIron[1]][wysokosc + wysIron[0]] = str(swiatFileToWrite[szerokosc - wysIron[1]][wysokosc + wysIron[0]])[
                                                                ::-1].replace("1,", "8,", 1)[::-1]

                    elif ironDiscrybution == 2:
                        wysIron = []
                        wysIron.append(random.randint(30, 50))
                        wysIron.append(random.randint(50, 100))
                        swiatFileToWrite[szerokosc - wysIron[1]][wysokosc + wysIron[0]] = str(swiatFileToWrite[szerokosc - wysIron[1]][wysokosc + wysIron[0]])[
                                                                ::-1].replace("1,", "8,", 1)[::-1]
                        swiatFileToWrite[szerokosc - wysIron[1]+1][wysokosc + wysIron[0]] = str(
                            swiatFileToWrite[szerokosc - wysIron[1]+1][wysokosc + wysIron[0]])[
                                                                ::-1].replace("1,","8,",1)[::-1]

                except Exception:
                    pass

                try:
                    if coalDiscrybution == 1:
                        wysCoal = []
                        wysCoal.append(random.randint(10, 50))
                        wysCoal.append(random.randint(50, 1000))
                        swiatFileToWrite[szerokosc - wysCoal[1]][wysokosc + wysCoal[0]] = str(swiatFileToWrite[szerokosc - wysCoal[1]][wysokosc + wysCoal[0]])[
                                                                ::-1].replace("1,", "7,", 1)[::-1]

                    elif coalDiscrybution == 2:
                        wysCoal = []
                        wysCoal.append(random.randint(21, 50))
                        wysCoal.append(random.randint(50, 1000))
                        swiatFileToWrite[szerokosc - wysCoal[1]][wysokosc + wysCoal[0]] = str(swiatFileToWrite[szerokosc - wysCoal[1]][wysokosc + wysCoal[0]])[
                                                                ::-1].replace("1,", "7,", 1)[::-1]
                        swiatFileToWrite[szerokosc - wysCoal[1]+1][wysokosc + wysCoal[0]] = str(
                            swiatFileToWrite[szerokosc - wysCoal[1]+1][wysokosc + wysCoal[0]])[
                                                                ::-1].replace("1,","7,",1)[::-1]

                except Exception:
                    pass
                try:
                    if treeSize == 1:
                        swiatFileToWrite[szerokosc][wysokosc - 1] = str(swiatFileToWrite[szerokosc][wysokosc - 1])[
                                                                    ::-1].replace("0,", "4,", 1)[::-1]
                        swiatFileToWrite[szerokosc][wysokosc - 2] = str(swiatFileToWrite[szerokosc][wysokosc - 2])[
                                                                    ::-1].replace("0,", "4,", 1)[::-1]
                        swiatFileToWrite[szerokosc - 1][wysokosc - 2] = str(swiatFileToWrite[szerokosc - 1][wysokosc - 2])[
                                                                        ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc + 1][wysokosc - 2] = str(swiatFileToWrite[szerokosc + 1][wysokosc - 2])[
                                                                        ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc - 1][wysokosc - 1] = str(swiatFileToWrite[szerokosc - 1][wysokosc - 1])[
                                                                        ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc + 1][wysokosc - 1] = str(swiatFileToWrite[szerokosc + 1][wysokosc - 1])[
                                                                        ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc][wysokosc - 3] = str(swiatFileToWrite[szerokosc][wysokosc - 3])[
                                                                    ::-1].replace("0,", "5,", 1)[::-1]
                        break

                    if treeSize == 2:
                        swiatFileToWrite[szerokosc][wysokosc - 1] = str(swiatFileToWrite[szerokosc][wysokosc - 1])[
                                                                    ::-1].replace("0,", "4,", 1)[::-1]
                        swiatFileToWrite[szerokosc][wysokosc - 2] = str(swiatFileToWrite[szerokosc][wysokosc - 2])[
                                                                    ::-1].replace("0,", "4,", 1)[::-1]
                        swiatFileToWrite[szerokosc][wysokosc - 3] = str(swiatFileToWrite[szerokosc][wysokosc - 3])[
                                                                    ::-1].replace("0,", "4,", 1)[::-1]
                        swiatFileToWrite[szerokosc - 1][wysokosc - 3] = str(swiatFileToWrite[szerokosc - 1][wysokosc - 3])[
                                                                    ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc + 1][wysokosc - 3] = str(swiatFileToWrite[szerokosc + 1][wysokosc - 3])[
                                                                    ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc - 1][wysokosc - 2] = str(swiatFileToWrite[szerokosc - 1][wysokosc - 2])[
                                                                    ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc + 1][wysokosc - 2] = str(swiatFileToWrite[szerokosc + 1][wysokosc - 2])[
                                                                    ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc - 1][wysokosc - 1] = str(swiatFileToWrite[szerokosc - 1][wysokosc - 1])[
                                                                    ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc + 1][wysokosc - 1] = str(swiatFileToWrite[szerokosc + 1][wysokosc - 1])[
                                                                    ::-1].replace("0,", "5,", 1)[::-1]
                        swiatFileToWrite[szerokosc][wysokosc - 4] = str(swiatFileToWrite[szerokosc][wysokosc - 4])[
                                                                    ::-1].replace("0,", "5,", 1)[::-1]
                        break

                    if treeSize == 3:
                        swiatFileToWrite[szerokosc][wysokosc - 1] = str(swiatFileToWrite[szerokosc][wysokosc - 1])[
                                                                    ::-1].replace("0,", "5,", 1)[::-1]
                        break

                    if treeSize == 4:
                        swiatFileToWrite[szerokosc][wysokosc] = str(swiatFileToWrite[szerokosc][wysokosc])[
                                                                    ::-1].replace("4,", "5,", 1)[::-1]
                        break

                except Exception:
                    pass"""

    for szerokosc in range(dlugosc):
        for wysokosc in range(96):
            saveTemp.append(swiatFileToWrite[szerokosc][wysokosc])

    f = open("assest/saves/save.mov", "w")

    f.writelines(saveTemp)