import random
import sys
import pickle
import os
from opensimplex import OpenSimplex
tmp = OpenSimplex(seed = random.randint(1,1000000))


class New_world:
    def __init__(self):
        self.sizeScreen = 1920, 1080

        self.generateWorldSize = 65536
        self.generateWorldType = "def"


    def biomGenList(self, dlugosc):
        biomList = []
        i = 1
        while len(biomList) <= dlugosc:
            i += 1
            biom = ((int(tmp.noise2d(x=i, y=3) * 12)) % len(os.listdir(f"assest/structures")) + 1)
            if biom < 0:
                biom *= -1
            szerBiom = int(tmp.noise2d(x=i / 8, y=3) * 200)
            if szerBiom < 0:
                szerBiom *= -1
            for szer in range(szerBiom + 30):
                biomList.append(biom)

        return biomList

    def generateWorld(self):
        trybGeneratora = self.generateWorldType
        dlugosc = self.generateWorldSize

        if trybGeneratora == "def":
            biome = self.biomGenList(dlugosc)

            swiatFileToWrite = {}

            def oreAndTreeDiscrybution():
                swiatFileToWrite[sz] = [0,biome[sz],int(tmp.noise2d(x=sz / 8, y=1) * 6),0]

            for sz in range(dlugosc):
                oreAndTreeDiscrybution()

            playerInfo = [int(dlugosc / 2), int(tmp.noise2d(x=int(dlugosc / 2) / 8, y=1) * 6) + 2, 0, dlugosc, []]

        # SPAWN WORLD SETTER
            try:
                os.makedirs("assest/saves/save")
            except Exception:
                pass

            with open(f'assest/saves/save/worldSave.data', 'wb') as filehandle:
                pickle.dump(swiatFileToWrite, filehandle)

            with open(f'assest/saves/save/playerSave.data', 'wb') as filehandle:
                pickle.dump(playerInfo, filehandle)

gen = New_world()
gen.generateWorld()