import pickle
import sys

with open(f'{sys.path[0]}/assest/saves/save/worldSave.data', 'rb') as filehandle:
    blockFileRead = pickle.load(filehandle)

print(blockFileRead[4096])