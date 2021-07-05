#! E:\skrótyPulpit\PrograminngProject\Python\3D_Game\ven\Scripts\python.exe

import sys

import pygame
from pygame.locals import *

import game
import worldGenFlat

# Creyblock

class Main:

    def __init__(self):

        gamePathExe = sys.path[0].split("\\")[:-1]
        gamePathExe = ['\\'.join([str(i) for i in gamePathExe])][0]

        #self.gamePath = gamePathExe
        self.gamePath = sys.path[0]

        pygame.init()

        self.sizeScreen = 1920, 1080
        self.screenReal = pygame.display.set_mode((1920, 1080), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.screenReal.copy()
        pygame.display.set_caption("CreyBlock - Menu")
        self.screenReal = pygame.display.set_mode(self.sizeScreen, HWSURFACE | DOUBLEBUF | RESIZABLE)

        pic = pygame.surface.Surface((50, 50))
        pic.fill((255, 100, 200))

        # TEXTURES AND STRINGS PRINT
        self.mainWallpeper = pygame.image.load(f'{self.gamePath}/assest/textures/mainWallpeper.png').convert_alpha()
        self.mainButton = pygame.image.load(f'{self.gamePath}/assest/textures/mainButtonTexture.png').convert_alpha()
        self.mainFontB = pygame.font.Font(f'{self.gamePath}/assest/fonts/menu.ttf', 202)
        self.mainFont = pygame.font.Font(f'{self.gamePath}/assest/fonts/menu.ttf', 200)
        self.mainFontType = pygame.font.Font(f'{self.gamePath}/assest/fonts/menu.ttf', 100)

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
        # WALPAPER
        self.screen.blit(self.mainWallpeper, (0, 0))

        # CAPITION
        self.screen.blit(self.mainFontB.render("Creyblock", True, (10, 10, 10)), (370, 105))
        self.screen.blit(self.mainFont.render("Creyblock", True, (250, 250, 250)), (370, 110))

        # BUTTON SINGLEPLAYER
        self.screen.blit(self.mainButton, (560, 500))
        self.screen.blit(self.mainFontType.render("SinglePlayer", True, (250, 250, 250)), (605, 510))
        # BUTTON GENERATE_NEW_WORLD
        self.screen.blit(self.mainButton, (560, 650))
        self.screen.blit(self.mainFontType.render("New World", True, (250, 250, 250)), (655, 660))
        # BUTTON SETTINGS
        self.screen.blit(self.mainButton, (560, 800))
        self.screen.blit(self.mainFontType.render("Settings", True, (250, 250, 250)), (720, 810))

    def buttonClick(self):
        self.sizeScreen = 1920, 1080
        self.xPosMouse, self.yPosMouse = pygame.mouse.get_pos()[0] * (
                self.sizeScreen[0] / self.screenReal.get_rect().size[0]), pygame.mouse.get_pos()[
                                             1] * (self.sizeScreen[1] /
                                                   self.screenReal.get_rect().size[1])
        if pygame.mouse.get_pressed(3)[0]:
            self.buttonSinglePlayer()
            self.buttonNewWorld()

    def buttonSinglePlayer(self):
        hitBox = pygame.rect.Rect(560, 500, 800, 100)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            game.Game(self.gamePath)
            sys.exit()

    def buttonNewWorld(self):
        hitBox = pygame.rect.Rect(560, 650, 800, 100)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            worldGenFlat.New_world(self.gamePath)
            sys.exit()

    def buttonSettings(self):
        hitBox = pygame.rect.Rect(560, 800, 800, 100)
        collide = hitBox.collidepoint(self.xPosMouse, self.yPosMouse)
        if collide:
            pass

if __name__ == "__main__":
    Main()