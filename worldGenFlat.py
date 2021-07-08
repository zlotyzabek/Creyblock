import random
import sys
import pygame
from pygame.locals import *
import main
import pickle
import os
import perlin


class New_world:
    def __init__(self, gamePath):
        pygame.init()

        self.gamePath = gamePath

        self.sizeScreen = 1920, 1080
        self.screenReal = pygame.display.set_mode((1920, 1080), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.screenReal.copy()
        pygame.display.set_caption("CreyBlock - WorldCreator")
        self.screenReal = pygame.display.set_mode(self.sizeScreen, HWSURFACE | DOUBLEBUF | RESIZABLE)

        self.generateWorldSize = 2
        self.generateWorldType = "def"

        pic = pygame.surface.Surface((50, 50))
        pic.fill((255, 100, 200))

        self.mainWallpeper = pygame.image.load(f'{self.gamePath}/assest/textures/worldGenWapllpeper.png').convert_alpha()
        self.mainButton = pygame.image.load(f'{self.gamePath}/assest/textures/mainButtonTexture.png').convert_alpha()

        self.mainFont = pygame.font.Font((f"{self.gamePath}/assest/fonts/menu.ttf"), 150)
        self.mainFontB = pygame.font.Font((f"{self.gamePath}/assest/fonts/menu.ttf"), 90)

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
            biom = random.randint(1, len(os.listdir(f"{self.gamePath}/assest/structures")))
            for i in range(random.randint(200, 400)):
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
                swiat = GenerateTerainGrassland(dlugosc)

                biome = self.biomGenList(dlugosc)

                swiatFileToWrite = []

                def oreAndTreeDiscrybution(swiat):
                    swiatFileToWrite.append([])
                    swiatFileToWrite[sz].append([0,5,swiat,0])

                for sz in range(dlugosc):
                    oreAndTreeDiscrybution(swiat[sz])

                playerInfo = [dlugosc * 48, 600, dlugosc]
            # SPAWN WORLD SETTER
                try:
                    os.makedirs("assest/saves/save")
                except Exception:
                    pass

                with open(f'{self.gamePath}/assest/saves/save/worldSave.data', 'wb') as filehandle:
                    pickle.dump(swiatFileToWrite, filehandle)

                with open(f'{self.gamePath}/assest/saves/save/playerSave.data', 'wb') as filehandle:
                    pickle.dump(playerInfo, filehandle)

                main.Main()