import random
import sys
import pygame
from pygame.locals import *
import main
import pickle
import os


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
            self.generateWorldSize = 8193

        hitBox = pygame.rect.Rect(760, 300, 400, 120)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            self.generateWorldSize = 32768

        hitBox = pygame.rect.Rect(1260, 300, 400, 120)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            self.generateWorldSize = 65537

    def biomGenList(self, dlugosc):
        biomList = []
        while len(biomList) <= dlugosc:
            biom = random.randint(1, 3)
            for i in range(random.randint(250, 500)):
                biomList.append(biom)

        return biomList


    def buttonGenerateWorld(self):
        hitBox = pygame.rect.Rect(260, 750, 1400, 240)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            t = [0]
            def ifRandomRSet(n, r1, r2):
                if t[-1] == n:
                    return random.randrange(r1, r2)
                else:
                    return None

            def GenerateTerainGrassland(szerokosc):
                r = 0
                for i in range(szerokosc):

                    r = ifRandomRSet(0, 0, 2)
                    if r is not None:
                        t.append(r)

                    r = ifRandomRSet(1, 0, 3)
                    if r is not None:
                        t.append(r)

                    r = ifRandomRSet(2, 1, 4)
                    if r is not None:
                        t.append(r)

                    r = ifRandomRSet(3, 2, 5)
                    if r is not None:
                        t.append(r)

                    r = ifRandomRSet(4, 3, 6)
                    if r is not None:
                        t.append(r)

                    r = ifRandomRSet(5, 4, 7)
                    if r is not None:
                        t.append(r)

                    r = ifRandomRSet(6, 5, 8)
                    if r is not None:
                        t.append(r)

                    r = ifRandomRSet(7, 6, 9)
                    if r is not None:
                        t.append(r)

                    r = ifRandomRSet(8, 7, 8)
                    if r is not None:
                        t.append(r)

                return t

            def worldStructureSpawning(szerokosc):
                worldStructureSpawningList = []
                for i in range(szerokosc):
                    ifTreeSpawn = random.randint(1,2)
                    ifOreSpawn = random.randint(1,3)
                    randomSpawn = random.randint(1,150)
                    try:
                        if 0 <= randomSpawn <= 69  and worldStructureSpawningList[i-1] == 0 and ifTreeSpawn == 1:
                            worldStructureSpawningList.append(1)
                        elif 70 <= randomSpawn <= 80 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(2)
                        elif 81 <= randomSpawn <= 89 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(3)
                        elif 90 <= randomSpawn <= 95 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(4)
                        elif 96 <= randomSpawn <= 98 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(5)
                        elif 99 <= randomSpawn <= 101 and ifOreSpawn == 1:
                            worldStructureSpawningList.append(6)
                        elif 102 <= randomSpawn <= 121:
                            worldStructureSpawningList.append(7)
                        elif 121 <= randomSpawn <= 131:
                            worldStructureSpawningList.append(8)
                        else:
                            worldStructureSpawningList.append(0)
                    except Exception:
                        worldStructureSpawningList.append(0)

                return worldStructureSpawningList

            trybGeneratora = self.generateWorldType
            dlugosc = self.generateWorldSize

            if trybGeneratora == "def":

                swiat = GenerateTerainGrassland(dlugosc)

                biome = self.biomGenList(dlugosc)

                swiatFileToWrite = []

                worldStructureSpawningList = worldStructureSpawning(dlugosc)

                def grassBiom(sz, swiat):
                    swiatFileToWrite[sz].append(f"{sz * 96},{792 - (swiat * 96)},16")
                    swiatFileToWrite[sz].append(f"{sz * 96},{888 - (swiat * 96)},14")
                    swiatFileToWrite[sz].append(f"{sz * 96},{984 - (swiat * 96)},4")
                    swiatFileToWrite[sz].append(f"{sz * 96},{1080 - (swiat * 96)},4")
                    swiatFileToWrite[sz].append(f"{sz * 96},{1080 - (swiat * 96)},4")
                    for i in range((55 + swiat)):
                        swiatFileToWrite[sz].append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")

                def frozenBiom(sz, swiat):
                    swiatFileToWrite[sz].append(f"{sz * 96},{792 - (swiat * 96)},18")
                    swiatFileToWrite[sz].append(f"{sz * 96},{888 - (swiat * 96)},14")
                    swiatFileToWrite[sz].append(f"{sz * 96},{984 - (swiat * 96)},12")
                    swiatFileToWrite[sz].append(f"{sz * 96},{1080 - (swiat * 96)},12")
                    swiatFileToWrite[sz].append(f"{sz * 96},{1080 - (swiat * 96)},12")
                    for i in range((55 + swiat)):
                        swiatFileToWrite[sz].append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")

                def dessertBiome(sz, swiat):
                    swiatFileToWrite[sz].append(f"{sz * 96},{792 - (swiat * 96)},3")
                    swiatFileToWrite[sz].append(f"{sz * 96},{888 - (swiat * 96)},3")
                    swiatFileToWrite[sz].append(f"{sz * 96},{984 - (swiat * 96)},3")
                    swiatFileToWrite[sz].append(f"{sz * 96},{1080 - (swiat * 96)},4")
                    for i in range((56 + swiat)):
                        swiatFileToWrite[sz].append(f"{sz * 96},{(1176 + i * 96) - swiat * 96},2")

                def oreAndTreeDiscrybution(swiat):
                    for i in range((34 - swiat) * 96, 0, -96):
                        swiatFileToWrite[sz].append(f"{sz * 96},{(696 - i) - (swiat * 96)},0")

                    if worldStructureSpawningList[sz] == 1:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},tree")
                    elif worldStructureSpawningList[sz] == 2:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},coal")
                    elif worldStructureSpawningList[sz] == 3:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},iron")
                    elif worldStructureSpawningList[sz] == 4:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},gold")
                    elif worldStructureSpawningList[sz] == 5:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},diament")
                    elif worldStructureSpawningList[sz] == 6:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},emerald")
                    elif worldStructureSpawningList[sz] == 7:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},grass")
                    elif worldStructureSpawningList[sz] == 8:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},sgc")
                    else:
                        swiatFileToWrite[sz].append(f"{sz * 96},{696 - (swiat * 96)},0")

                    biomes = {1: grassBiom, 2: frozenBiom, 3: dessertBiome}

                    biomes[biome[sz]](sz, swiat)

                    swiatFileToWrite[sz].append(f"{sz * 96},{6552},bedrock")


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