import wget
import shutil
import winshel

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
    shutil.move(f"{os.getenv('APPDATA')}\\CreyBlock\\files\\laucher.py", f"{os.getenv('APPDATA')}\\CreyBlock\\laucher")

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

def reInstall():
    unInstall()
    firstLaunch()

def unInstall():
    print("Deleting game files")
    shutil.rmtree(f"{os.getenv('APPDATA')}\\CreyBlock", onerror=on_rm_error)

while True:
    print("==================================")
    print("Welcome to the CreyBlock laucher")
    print("==================================\n")
    print("Choose an option:")
    print("1. start - Starting game")
    print("2. install - Downloads and installs the game files for the first time on your computer")
    print("3. update - Updating the game, not removing save")
    print("4. reinstall - Delate and installs the latest version of the game.")
    print("5. uninstall - Deletes all game files from the computer :(")

    options = {1: lunchGame, 2: firstLaunch, 3: updating, 4: reInstall, 5: unInstall, "start": lunchGame, "install": firstLaunch, "update": updating, "reinstall": reInstall, "uninstall": unInstall}

    try:
        option = input("->").lower()
    except Exception:
        option = int(input("->"))

    options[option]()
