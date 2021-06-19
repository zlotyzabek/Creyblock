import wget
import zipfile
import os
import sys
import shutil

#wget.download("https://github.com/zlotyzabek/Creyblock/archive/refs/heads/main.zip")

#with zipfile.ZipFile("Creyblock-main.zip", 'r') as zip_ref:
#    zip_ref.extractall("Creyblock-main")

#os.remove("Creyblock-main.zip")

shutil.move("Creyblock-main/Creyblock-main", sys.path[0])