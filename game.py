import threading

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
            readTEMP = str(f.read()).split('\n')[:-1]

        for i in range(3, len(readTEMP)):
            self.blockFileRead.extend(map(int, readTEMP[i].split(",")))

        # SCREEN
        self.sizeScreen = pyautogui.size()[0], pyautogui.size()[1]
        self.screenReal = pygame.display.set_mode(self.sizeScreen, HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.screenReal.copy()
        pygame.display.set_caption("CreyBlock - GAME")

        # PHYSIC
        self.acceleration = Vector2(0, 0)
        self.speed = Vector2(0, 0)
        self.blokada = 0

        # CORDYNATS
        self.PosCam = Vector2(int(readTEMP[0].split(",")[0]) * -1, int(readTEMP[0].split(",")[1]))

        # COLIZION
        self.blockCollizionDetect = [0, 0, 0, 0, 0, 0, 0, 0]

        # TEXTURES
        self.dirt = pygame.image.load('assest/textures/dirt.png').convert_alpha()
        self.log = pygame.image.load('assest/textures/log.png').convert_alpha()
        self.grass = pygame.image.load('assest/textures/grass.png').convert_alpha()
        self.stone = pygame.image.load('assest/textures/stone.png').convert_alpha()
        self.leaves = pygame.image.load('assest/textures/leaves_oak.png').convert_alpha()
        self.planks = pygame.image.load('assest/textures/planks.png').convert_alpha()
        self.diamond = pygame.image.load('assest/textures/diamond_ore.png').convert_alpha()
        self.iron = pygame.image.load('assest/textures/iron_ore.png').convert_alpha()
        self.coal = pygame.image.load('assest/textures/coal_ore.png').convert_alpha()
        self.typeBlockTexture = {1: self.stone, 2: self.dirt, 3: self.grass, 4: self.log, 5: self.leaves, 6: self.planks, 7: self.coal, 8: self.iron, 9: self.diamond}
        for i in range(1, len(self.typeBlockTexture) + 1):
            self.typeBlockTexture[i] = pygame.transform.scale(self.typeBlockTexture[i], (96, 96))

        self.head = pygame.image.load('assest/textures/player/head.png').convert_alpha()
        self.head = pygame.transform.scale(self.head, (64, 64))

        self.legs = pygame.image.load('assest/textures/player/legs.png').convert_alpha()
        self.legs = pygame.transform.scale(self.legs, (20, 32))

        self.skyColor = 60, 210, 220
        self.errorTextures = 255, 0, 255
        self.chest = 150, 100, 50
        self.body = 150, 100, 50

        del readTEMP

        self.always()

    def always(self):
        while self.programRun == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.savingWorld()
                    self.programRun = 0

                elif event.type == VIDEORESIZE:
                    self.screenReal = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

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

        self.speed *= 0.9
        self.speed += self.acceleration
        self.PosCam += self.speed
        self.acceleration *= 0

        self.saveToTime += 1

    def savingWorld(self):
        if self.saveTimeWorld != 0:
            self.saveImageDisplay = 1
            self.saveToTime = 0
            swiatFileToWrite = []

            for i in range(0, len(self.blockFileRead), 3):
                swiatFileToWrite.append(f"{self.blockFileRead[i]},{self.blockFileRead[i + 1]},{self.blockFileRead[i + 2]}\n")

            with open("assest/saves/save.mov", "w") as f:
                f.write(f"{int(self.PosCam.x * -1)},{int(self.PosCam.y)}\n")
                f.write("0,0\n")
                f.write("0,0\n")
                f.writelines(swiatFileToWrite)

            self.saveImageDisplay = 0

    def drawing(self):
        try:
            self.blockCollizionDetect = [0, 0, 0, 0, 0, 0, 0, 0]
            for i in range((int((-1 * self.PosCam.x - 200))), (int((-1 * self.PosCam.x + 2120)))):
                if -100 < int(self.blockFileRead[i * 3]) + self.PosCam.x < 2020 and -100 < int(
                        self.blockFileRead[i * 3 + 1]) + self.PosCam.y < 1180:
                    block = (pygame.Rect(int(self.blockFileRead[3 * i]) + self.PosCam.x,
                                         int(self.blockFileRead[(3 * i) + 1]) + self.PosCam.y, 96, 96))
                    self.blockRemovingAndSetter(i, block)
                    if self.blockFileRead[3 * i + 2] != 0:
                        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()[0] * (
                                self.sizeScreen[0] / self.screenReal.get_rect().size[0]), pygame.mouse.get_pos()[1] * (
                                                                 self.sizeScreen[1] / self.screenReal.get_rect().size[1])

                        try:
                            self.screen.blit(self.typeBlockTexture[self.blockFileRead[3 * i + 2]], (
                                int(self.blockFileRead[3 * i]) + self.PosCam.x,
                                int(self.blockFileRead[(3 * i) + 1]) + self.PosCam.y))
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
        except Exception:
            pass

    def drawBody(self):
        self.screen.blit(self.head, (928, 492))
        self.screen.blit(self.legs, (930, 556))
        self.screen.blit(self.legs, (970, 556))

    def drawGui(self):
        if self.saveImageDisplay == 1:
            savingGui = (pygame.Rect(98, 98, 48, 48))
            pygame.draw.rect(self.screen, self.chest, savingGui)

    def blockRemovingAndSetter(self, blockIdNumber, block):
        collide = block.collidepoint(self.xPosMouse, self.yPosMouse)
        if pygame.mouse.get_pressed(3)[0] and self.blockFileRead[3 * blockIdNumber + 2] != 0 and collide:
                self.blockFileRead[blockIdNumber * 3 + 2] = 0

        elif pygame.mouse.get_pressed(3)[2] and self.blockFileRead[3 * blockIdNumber + 2] == 0 and collide:
                self.blockFileRead[blockIdNumber * 3 + 2] = self.selectBlock

    def controls(self):
        keys = pygame.key.get_pressed()

# RIGH AND LEFT

        if keys[97] and self.blockCollizionDetect[4] < 1:
            self.acceleration += Vector2(0.1, 0)
            if keys[pygame.K_LSHIFT]:
                self.acceleration += Vector2(0.1, 0)

        elif self.blockCollizionDetect[0] > 0:
            self.speed += Vector2(-0.1, 0)

        if keys[100] and self.blockCollizionDetect[5] < 1:
            self.acceleration += Vector2(-0.1, 0)
            if keys[pygame.K_LSHIFT]:
                self.acceleration += Vector2(-0.1, 0)

        elif self.blockCollizionDetect[1] > 0:
            self.speed += Vector2(0.1, 0)

# JUMP AND GRAVITY
        if self.blockCollizionDetect[7] < 1:
            self.speed += Vector2(0, -0.1)

        elif self.blockCollizionDetect[3] > 0:
            self.speed += Vector2(0, 0.05)

        if keys[119] and  self.blockCollizionDetect[7] > 0 and self.blockCollizionDetect[6] < 1:
            threading.Thread(target=self.controlsJump()).start()

# UP
        if self.blockCollizionDetect[6] > 0:
            self.speed += Vector2(0, -0.5)

# EQ
        for i in range(49, 58):
            if keys[i]:
                self.selectBlock = i - 48
                break


    def controlsJump(self):
        for i in range(4000):
            self.acceleration += Vector2(0, 0.001)