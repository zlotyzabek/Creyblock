import pickle

with open(f'level52.txt', 'rb') as filehandle:
    blocks = pickle.load(filehandle)

print(blocks)