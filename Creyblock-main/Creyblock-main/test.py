import sys
import time
from PIL import Image
from PIL import ImageEnhance
import pygame

pygame.init()

sizeScreen = 1920, 1080
screenReal = pygame.display.set_mode((1920, 1080), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

start = time.time()

with open(f"{sys.path[0]}/assest/textures/texturesBlockLoad.txt", "r") as f:
    readTEMPtextures = str(f.read()).split('\n')[:-1]
typeBlockTextureBlock = {}
typeBlockTextureInventory = {}
for i, list in enumerate(readTEMPtextures):
    if list.split(",")[1] == "c":
        typeBlockTextureBlock[i + 1] = [
            pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha().convert(), (96, 96)),
            list.split(",")[2]]
        typeBlockTextureInventory[i + 1] = pygame.transform.scale(
            pygame.image.load(list.split(",")[0]).convert_alpha().convert(), (64, 64))
    if list.split(",")[1] == "a":
        typeBlockTextureBlock[i + 1] = [
            pygame.transform.scale(pygame.image.load(list.split(",")[0]).convert_alpha(), (96, 96)), list.split(",")[2]]
        typeBlockTextureInventory[i + 1] = pygame.transform.scale(
            pygame.image.load(list.split(",")[0]).convert_alpha(), (64, 64))

print(time.time() - start)