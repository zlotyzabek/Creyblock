import threading
import ast

import pygame
from pygame.locals import *
from pygame.math import Vector2
import pyautogui


class Game:

    def __init__(self):

        # CONFIG
        self.saveTimeWorld = 3   # Time in minutes how many times the world should record. Set to 0 to disable.

        pygame.init()

        self.programRun = 1

        self.block = []

        self.clock = pygame.time.Clock()
        self.delta = 0.00

        self.saveToTime = 0
        self.saveImageDisplay = 0

        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()

        self.blockFileRead = []

        self.selectBlock = 2

        # LOADING WORLD
        with open("assest/saves/save.mov", "r") as f:
            for line in f:
                x = line.split('\n')[:-1][0]
                self.blockFileRead.append(ast.literal_eval(str(x)))

        # SCREEN
        self.sizeScreen = pyautogui.size()[0], pyautogui.size()[1]
        self.screenReal = pygame.display.set_mode(self.sizeScreen, HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.screenReal.copy()
        pygame.display.set_caption("CreyBlock - GAME")

        # CORDYNATS
        self.PosCam = Vector2(int(self.blockFileRead[0][0]) * -1, int(self.blockFileRead[0][1]))

        # COLIZION
        self.blockCollizionDetect = [0, 0, 0, 0, 0, 0, 0, 0]

        # TEXTURES
        with open("assest/textures/texturesLoad.txt", "r") as f:
            readTEMPtextures = str(f.read()).split('\n')[:-1]
        self.typeBlockTexture = {}
        for i, list in enumerate(readTEMPtextures):
            self.typeBlockTexture[i + 1] = pygame.transform.scale(pygame.image.load(list).convert_alpha(), (96, 96))

        self.head = pygame.image.load('assest/textures/player/head.png').convert_alpha()
        self.head = pygame.transform.scale(self.head, (64, 64))

        self.legs = pygame.image.load('assest/textures/player/legs.png').convert_alpha()
        self.legs = pygame.transform.scale(self.legs, (20, 32))

        self.skyColor = 60, 210, 220
        self.errorTextures = 255, 0, 255
        self.chest = 150, 100, 50
        self.body = 150, 100, 50

        self.always()

    def always(self):
        while self.programRun == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.savingWorld()
                    self.programRun = 0

                elif event.type == VIDEORESIZE:
                    self.screenReal = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.blockCollizionDetect[7] > 0 and self.blockCollizionDetect[6] < 1:
                        threading.Thread(target=self.controlsJump()).start()

            self.delta += self.clock.tick()/1000.0
            while self.delta > 1 / 360.0:
                self.ticking()
                self.delta -= 1 / 360.0

            self.screen.fill(self.skyColor)
            self.drawing()
            self.screenReal.blit(pygame.transform.scale(self.screen, self.screenReal.get_rect().size), (0, 0))
            pygame.display.update()

    def ticking(self):
        self.controls()
        if self.saveToTime >= self.saveTimeWorld * 7200:
            threading.Thread(target=self.savingWorld).start()

        self.saveToTime += 1

    def savingWorld(self):
        if self.saveTimeWorld != 0:
            self.saveImageDisplay = 1
            self.saveToTime = 0
            swiatFileToWrite = self.blockFileRead

            with open("assest/saves/save.mov", "w") as f:
                f.write(f"{int(self.PosCam.x * -1)},{int(self.PosCam.y) - 48}\n")
                f.write("0,0\n")
                f.write("0,0\n")

                for szerokosc in range(3, len(swiatFileToWrite)):
                    f.write(f"{swiatFileToWrite[szerokosc]}\n")

            self.saveImageDisplay = 0

    def drawing(self):
        self.blockCollizionDetect = [0, 0, 0, 0, 0, 0, 0, 0]
        for szer in range(int((-1 * self.PosCam.x + 200) / 96), int((-1 * self.PosCam.x + 2320) / 96)):
            for wys in range(96):
                if -100 < int(self.blockFileRead[szer][wys].split(",")[0]) + self.PosCam.x < 2020 and -100 < int(
                        self.blockFileRead[szer][wys].split(",")[1]) + self.PosCam.y < 1180:

                    block = (pygame.Rect(int(self.blockFileRead[szer][wys].split(",")[0]) + self.PosCam.x,
                                         int(self.blockFileRead[szer][wys].split(",")[1]) + self.PosCam.y, 96, 96))

                    self.blockRemovingAndSetter((szer, wys), block)

                    if self.blockFileRead[szer][wys].split(",")[2] != "0":
                        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()[0] * (
                                self.sizeScreen[0] / self.screenReal.get_rect().size[0]), pygame.mouse.get_pos()[
                                                             1] * (self.sizeScreen[1] /
                                                                 self.screenReal.get_rect().size[1])
                        try:
                            self.screen.blit(self.typeBlockTexture[int(self.blockFileRead[szer][wys].split(",")[2])], (
                                int(self.blockFileRead[szer][wys].split(",")[0]) + self.PosCam.x,
                                int(self.blockFileRead[szer][wys].split(",")[1]) + self.PosCam.y))
                            if block.colliderect(pygame.Rect(936, 491, 48, 1)) == 1:
                                self.blockCollizionDetect[2] += 1
                            if block.colliderect(pygame.Rect(927, 500, 1, 48)) == 1:
                                self.blockCollizionDetect[0] += 1
                            if block.colliderect(pygame.Rect(992, 500, 1, 48)) == 1:
                                self.blockCollizionDetect[1] += 1
                            if block.colliderect(pygame.Rect(936, 556, 48, 1)) == 1:
                                self.blockCollizionDetect[3] += 1

                            if block.colliderect(pygame.Rect(936, 481, 48, 1)) == 1:
                                self.blockCollizionDetect[6] += 1
                            if block.colliderect(pygame.Rect(925, 500, 1, 48)) == 1:
                                self.blockCollizionDetect[4] += 1
                            if block.colliderect(pygame.Rect(994, 500, 1, 48)) == 1:
                                self.blockCollizionDetect[5] += 1
                            if block.colliderect(pygame.Rect(936, 558, 48, 1)) == 1:
                                self.blockCollizionDetect[7] += 1
                        except Exception:
                            pass

                    self.drawGui()
                    self.drawBody()


    def drawBody(self):
        self.screen.blit(self.head, (928, 492))
        #self.screen.blit(self.legs, (930, 556))
        #self.screen.blit(self.legs, (970, 556))

    def drawGui(self):
        if self.saveImageDisplay == 1:
            savingGui = (pygame.Rect(98, 98, 48, 48))
            pygame.draw.rect(self.screen, self.chest, savingGui)

    def blockRemovingAndSetter(self, blockColor, block):
        collide = block.collidepoint(self.xPosMouse, self.yPosMouse)
        if pygame.mouse.get_pressed(3)[0] and self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[2] != "0" and collide:
            temp = [self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[0], self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[1]]
            self.blockFileRead[blockColor[0]][blockColor[1]] = f"{temp[0]},{temp[1]},0"

        elif pygame.mouse.get_pressed(3)[2] and self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[2] == "0" and collide:
            temp = [self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[0], self.blockFileRead[blockColor[0]][blockColor[1]].split(",")[1]]
            self.blockFileRead[blockColor[0]][blockColor[1]] = f"{temp[0]},{temp[1]},{self.selectBlock}"

    def controls(self):
        keys = pygame.key.get_pressed()

# RIGH AND LEFT

        if keys[97] and self.blockCollizionDetect[4] < 1:
            self.PosCam += Vector2(1, 0)
            if keys[pygame.K_LSHIFT]:
                self.PosCam += Vector2(1, 0)

        elif self.blockCollizionDetect[0] > 0:
            self.PosCam += Vector2(-0.1, 0)

        if keys[100] and self.blockCollizionDetect[5] < 1:
            self.PosCam += Vector2(-1, 0)
            if keys[pygame.K_LSHIFT]:
                self.PosCam += Vector2(-1, 0)

        elif self.blockCollizionDetect[1] > 0:
            self.PosCam += Vector2(0.1, 0)

# JUMP AND GRAVITY
        if self.blockCollizionDetect[7] < 1:
            self.PosCam += Vector2(0, -2)

        elif self.blockCollizionDetect[3] > 0:
            self.PosCam += Vector2(0, 0.1)

# UP
        if self.blockCollizionDetect[2] > 0:
            self.PosCam += Vector2(0, -2.1)

# EQ
        for i in range(49, 58):
            if keys[i]:
                self.selectBlock = i - 48
                break


    def controlsJump(self):
        for i in range(220):
            self.PosCam += Vector2(0, 1)