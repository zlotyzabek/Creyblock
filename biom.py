import random
import os

class BiomGen:

    def __init__(self):
        self.structursToBiome = {}
        self.biomes = os.listdir(f"assest/structures")

        for i in range(len(self.biomes)):
            with open(f"assest/structures/{self.biomes[i]}/{self.biomes[i]}.txt", "r") as f:
                structuresTemp = []
                for line in f:
                    tempLineSplit = (line.split(","))
                    tempLineSplit[6] = tempLineSplit[6].split("\n")[0]
                    structuresTemp.append(tempLineSplit + [0])
            self.structursToBiome[self.biomes[i]] = structuresTemp

    def structurs(self, biom):
        structur = 1
        randomSpawn = random.randint(1, 100)
        for i in range(len(self.structursToBiome[self.biomes[biom -1]])):
            biomGen = self.structursToBiome[self.biomes[biom - 1]][i]
            if int(biomGen[0]) <= randomSpawn <= int(biomGen[1]):
                structur = biomGen[2]
        return structur

    def biomGen(self, sz, wys, swiat, biome):
        biomes = {1: self.dessert, 2: self.frozen, 3: self.grass, 4: self.mountains, 5: self.mushroom, 6: self.path, 7: self.podzol}
        try:
            return biomes[biome](swiat)[wys]
        except Exception:
            return [0, 0, 0, 0]


    def grass(self, swiat):
        worldGen = {}
        worldGen[3 + swiat] = ([16, 16, 16,0])
        worldGen[2 + swiat] = ([14, 14, 14, 0])
        worldGen[1 + swiat] = ([4, 4, 4, 0])
        worldGen[0 + swiat] = ([4, 4, 4, 0])
        for i in range(-1, -100 - swiat, -1):
            worldGen[i + swiat] = ([2, 2, 2, 0])
        worldGen[-98] = ([1, 1, 1, 0])
        return worldGen


    def frozen(self, swiat):
        worldGen = {}
        worldGen[3 + swiat] = ([18, 18, 18, 0])
        worldGen[2 + swiat] = ([14, 14, 14, 0])
        worldGen[1 + swiat] = ([12, 12, 12, 0])
        worldGen[0 + swiat] = ([12, 12, 12, 0])
        for i in range(-1, -100 - swiat, -1):
            worldGen[i + swiat] = ([2, 2, 2, 0])
        worldGen[-98] = ([1, 1, 1, 0])
        return worldGen


    def dessert(self, swiat):
        worldGen = {}
        worldGen[3 + swiat] = ([3, 3, 3, 0])
        worldGen[2 + swiat] = ([3, 3, 3, 0])
        worldGen[1 + swiat] = ([3, 3, 3, 0])
        worldGen[0 + swiat] = ([4, 4, 4, 0])
        for i in range(-1, -100 - swiat, -1):
            worldGen[i + swiat] = ([2, 2, 2, 0])
        worldGen[-98] = ([1, 1, 1, 0])
        return worldGen


    def podzol(self, swiat):
        worldGen = {}
        worldGen[3 + swiat] = ([24, 24, 24, 0])
        worldGen[2 + swiat] = ([14, 14, 14, 0])
        worldGen[1 + swiat] = ([13, 13, 13, 0])
        worldGen[0 + swiat] = ([13, 13, 13, 0])
        for i in range(-1, -100 - swiat, -1):
            worldGen[i + swiat] = ([2, 2, 2, 0])
        worldGen[-98] = ([1, 1, 1, 0])
        return worldGen


    def path(self, swiat):
        worldGen = {}
        worldGen[3 + swiat] = ([17, 17, 17, 0])
        worldGen[2 + swiat] = ([14, 14, 14, 0])
        worldGen[1 + swiat] = ([4, 4, 4, 0])
        worldGen[0 + swiat] = ([4, 4, 4, 0])
        for i in range(-1, -100 - swiat, -1):
            worldGen[i + swiat] = ([2, 2, 2, 0])
        worldGen[-98] = ([1, 1, 1, 0])
        return worldGen

    def mountains(self, swiat):
        swiat *= 2
        worldGen = {}
        worldGen[3 + swiat] = ([26, 26, 26, 0])
        worldGen[2 + swiat] = ([26, 26, 26, 0])
        worldGen[1 + swiat] = ([12, 12, 12, 0])
        worldGen[0 + swiat] = ([2, 2, 2, 0])
        for i in range(-1, -100 - swiat, -1):
            worldGen[i + swiat] = ([2, 2, 2, 0])
        worldGen[-97] = ([1, 1, 1, 0])
        return worldGen

    def mushroom(self, swiat):
        worldGen = {}
        worldGen[3 + swiat] = ([41, 41, 41,0])
        worldGen[2 + swiat] = ([15, 15, 15, 0])
        worldGen[1 + swiat] = ([14, 14, 14, 0])
        worldGen[0 + swiat] = ([4, 4, 4, 0])
        for i in range(-1, -100 - swiat, -1):
            worldGen[i + swiat] = ([2, 2, 2, 0])
        worldGen[-98] = ([1, 1, 1, 0])
        return worldGen