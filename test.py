import wget
import shutil

import zipfile
import os
import stat

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def lunchGame():
    os.system(f"{os.getenv('APPDATA')}\\CreyBlock\\files\\ven\\Scripts\\python.exe {os.getenv('APPDATA')}\\CreyBlock\\files\\main.py")

def firstLaunch():
    print("Folder initialization")
    os.mkdir(f"{os.getenv('APPDATA')}\\CreyBlock")
    os.mkdir(f"{os.getenv('APPDATA')}\\CreyBlock\\saves")
    os.mkdir(f"{os.getenv('APPDATA')}\\CreyBlock\\temp")
    os.mkdir(f"{os.getenv('APPDATA')}\\CreyBlock\\laucher")
    print("Downloading main file")
    wget.download("https://github.com/zlotyzabek/Creyblock/archive/refs/heads/main.zip", f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\Creyblock-main.zip")
    print("Extracting main file")
    with zipfile.ZipFile(f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\Creyblock-main.zip", 'r') as zip_ref:
        zip_ref.extractall(f"{os.getenv('APPDATA')}\\CreyBlock\\temp")
    print("Deleting unnecessary files")
    os.remove(f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\Creyblock-main.zip")
    os.rename(f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\Creyblock-main", f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\files")
    shutil.move(f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\files", f"{os.getenv('APPDATA')}\\CreyBlock")

def updating():
    print("Deleting game files")
    shutil.rmtree(f"{os.getenv('APPDATA')}\\CreyBlock\\files", onerror=on_rm_error)
    print("Downloading main file")
    wget.download("https://github.com/zlotyzabek/Creyblock/archive/refs/heads/main.zip",
                  f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\Creyblock-main.zip")
    print("Extracting main file")
    with zipfile.ZipFile(f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\Creyblock-main.zip", 'r') as zip_ref:
        zip_ref.extractall(f"{os.getenv('APPDATA')}\\CreyBlock\\temp")
    print("Deleting unnecessary files")
    os.remove(f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\Creyblock-main.zip")
    os.rename(f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\Creyblock-main",
              f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\files")
    shutil.move(f"{os.getenv('APPDATA')}\\CreyBlock\\temp\\files", f"{os.getenv('APPDATA')}\\CreyBlock")

#updating()
lunchGame()
#firstLaunch()


