import random
import sys
import pygame
from pygame.locals import *
import main
import pickle
import os
import perlin
from math import *


class new_World():
    def __init__(self):
        pygame.init()

        self.sizeScreen = 1920, 1080
        self.screenReal = pygame.display.set_mode((1920, 1080), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.screenReal.copy()
        pygame.display.set_caption("CreyBlock - WorldCreator")
        self.screenReal = pygame.display.set_mode(self.sizeScreen, HWSURFACE | DOUBLEBUF | RESIZABLE)

        self.generateWorldSize = 2
        self.generateWorldType = "def"

        pic = pygame.surface.Surface((50, 50))
        pic.fill((255, 100, 200))

        self.mainWallpeper = pygame.image.load(f'{sys.path[0]}/assest/textures/worldGenWapllpeper.png').convert_alpha()
        self.mainButton = pygame.image.load(f'{sys.path[0]}/assest/textures/mainButtonTexture.png').convert_alpha()

        self.mainFont = pygame.font.Font((f"{sys.path[0]}/assest/fonts/menu.ttf"), 150)
        self.mainFontB = pygame.font.Font((f"{sys.path[0]}/assest/fonts/menu.ttf"), 90)

        self.always()

    def always(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == VIDEORESIZE:
                    self.screenReal = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

            self.drawing()

            self.screenReal.blit(pygame.transform.scale(self.screen, self.screenReal.get_rect().size), (0, 0))
            pygame.display.update()

            self.buttonClick()

    def drawing(self):
        self.screen.blit(self.mainWallpeper, (0, 0))
        self.screen.blit(self.mainFont.render("World Generator", True, (200, 200, 200)), (250, 50))

        # SMALL SIZE BUTTON
        self.screen.blit(pygame.transform.scale(self.mainButton, (400, 120)), (260, 300))
        self.screen.blit(self.mainFontB.render("Small", True, (220, 220, 220)), (325, 320))

        # MEDIUM SIZE BUTTON
        self.screen.blit(pygame.transform.scale(self.mainButton, (400, 120)), (760, 300))
        self.screen.blit(self.mainFontB.render("Medium", True, (220, 220, 220)), (780, 320))

        # LARGE SIZE BUTTON
        self.screen.blit(pygame.transform.scale(self.mainButton, (400, 120)), (1260, 300))
        self.screen.blit(self.mainFontB.render("Large", True, (220, 220, 220)), (1325, 320))

        # GENERATE WORLD BUTTON
        self.screen.blit(pygame.transform.scale(self.mainButton, (1400, 240)), (260, 750))
        self.screen.blit(self.mainFont.render("GENERATE WORLD", True, (220, 220, 220)), (300, 800))



    def buttonClick(self):
        self.sizeScreen = 1920, 1080
        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()[0] * (
                self.sizeScreen[0] / self.screenReal.get_rect().size[0]), pygame.mouse.get_pos()[
                                             1] * (self.sizeScreen[1] /
                                                   self.screenReal.get_rect().size[1])
        if pygame.mouse.get_pressed(3)[0]:
            self.buttonSize()
            self.buttonGenerateWorld()

    def buttonSize(self):
        hitBox = pygame.rect.Rect(260, 300, 400, 120)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            self.generateWorldSize = 32769

        hitBox = pygame.rect.Rect(760, 300, 400, 120)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            self.generateWorldSize = 65537

        hitBox = pygame.rect.Rect(1260, 300, 400, 120)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            self.generateWorldSize = 131073

    def biomGenList(self, dlugosc):
        biomList = []
        while len(biomList) <= dlugosc:
            biom = random.randint(1, 5)
            for i in range(random.randint(250, 500)):
                biomList.append(biom)

        return biomList


    def buttonGenerateWorld(self):
        hitBox = pygame.rect.Rect(260, 750, 1400, 240)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            def GenerateTerainGrassland(szerokosc):
                noise = perlin.Perlin(15)
                t = []

                time = [i for i in range(szerokosc)]
                for i in time:
                    t.append(int(noise.valueAt(i) * 5))

                return t

            trybGeneratora = self.generateWorldType
            dlugosc = self.generateWorldSize

            if trybGeneratora == "def":
                self.structursToBiome = {}
                biomes = ["grass", "frozen", "dessert", "podzol", "path"]

                for i in range(len(biomes)):
                    with open(f"{sys.path[0]}/assest/structures/structurGenWorld/{biomes[i]}.txt", "r") as f:
                        structures = []
                        for line in f:
                            tempLineSplit = (line.split(","))
                            tempLineSplit[2] = tempLineSplit[2].split("\n")[0]
                            structures.append([int(tempLineSplit[0]), int(tempLineSplit[1]), tempLineSplit[2]])
                    self.structursToBiome[biomes[i]] = structures

                swiat = GenerateTerainGrassland(dlugosc)

                biome = self.biomGenList(dlugosc)

                swiatFileToWrite = []

                def structurs(sz, swiat, biom):
                    randomSpawn = random.randint(1,100)
                    spawn = 0
                    for i in range(len(self.structursToBiome[biom])):
                        biomGen = self.structursToBiome[biom][i]
                        if biomGen[0] <= randomSpawn <= biomGen[1]:
                            swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},{biomGen[2]}")
                            spawn = 1

                    if spawn == 0:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},{0}")

                def oreAndTreeDiscrybution(swiat):
                    swiatFileToWrite[sz].append(f"0,{biome[sz]},{swiat},{sz}")

                for sz in range(dlugosc):
                    swiatFileToWrite.append([])
                    oreAndTreeDiscrybution(swiat[sz])

                playerInfo = [dlugosc * 48, 600, dlugosc]
            # SPAWN WORLD SETTER
                try:
                    os.makedirs("assest/saves/save")
                except Exception:
                    pass

                with open(f'{sys.path[0]}/assest/saves/save/worldSave.data', 'wb') as filehandle:
                    pickle.dump(swiatFileToWrite, filehandle)

                with open(f'{sys.path[0]}/assest/saves/save/playerSave.data', 'wb') as filehandle:
                    pickle.dump(playerInfo, filehandle)

                main.Main()