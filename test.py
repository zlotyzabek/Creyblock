"""import os, winshell
from win32com.client import Dispatch
desktop = winshell.desktop()

path = os.path.join(desktop, "myNeatWebsite.url")
target = "http://www.google.com/"
shortcut = open(path, 'w')
shortcut.write('[InternetShortcut]\n')
shortcut.write('URL=%s' % target)
shortcut.close()"""


#path = os.path.join(desktop, "Media Player Classic.lnk")
#target = r"P:\Media\Media Player Classic\mplayerc.exe"
#wDir = r"P:\Media\Media Player Classic"
#icon = r"P:\Media\Media Player Classic\mplayerc.exe"
#shell = Dispatch('WScript.Shell')
#shortcut = shell.CreateShortCut(path)
#shortcut.Targetpath = target
#shortcut.WorkingDirectory = wDir
#shortcut.IconLocation = icon
#shortcut.save()


desktop = winshell.desktop()
path = os.path.join(desktop, 'CreyBlock.lnk')
target = r"C:\Users\lenovo\Documents\sample2.txt"
icon = r"C:\Users\lenovo\Documents\sample2.txt"
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()