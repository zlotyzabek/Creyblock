import sys
import pickle

with open(f'{sys.path[0]}/assest/saves/save/playerSave.data', 'rb') as filehandle:
    blockFileRead = pickle.load(filehandle)
print(blockFileRead)