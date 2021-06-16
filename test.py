import pickle

with open('assest/saves/save/playerSave.data', 'rb') as filehandle:
    print(pickle.load(filehandle))