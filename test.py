import pickle

with open('assest/saves/save/worldSave.data', 'rb') as filehandle:
    blockFileRead = pickle.load(filehandle)
list = ['196512,-2568,0', '196512,-2472,0', '196512,-2376,0', '196512,-2280,0', '196512,-2184,0', '196512,-2088,0', '196512,-1992,0', '196512,-1896,0', '196512,-1800,0', '196512,-1704,0', '196512,-1608,0', '196512,-1512,0', '196512,-1416,0', '196512,-1320,0', '196512,-1224,0', '196512,-1128,0', '196512,-1032,0', '196512,-936,0', '196512,-840,0', '196512,-744,0', '196512,-648,0', '196512,-552,0', '196512,-456,0', '196512,-360,0', '196512,-264,0', '196512,-168,0', '196512,-72,0', '196512,24,0', '196512,120,0', '196512,216,0', '196512,312,0', '196512,408,3', '196512,504,2', '196512,600,2', '196512,696,2', '196512,792,1', '196512,888,1', '196512,984,1', '196512,1080,1', '196512,1176,1', '196512,1272,1', '196512,1272,1', '196512,1368,1', '196512,1464,1', '196512,1560,1', '196512,1656,1', '196512,1752,1', '196512,1848,1', '196512,1944,1', '196512,2040,1', '196512,2136,1', '196512,2232,1', '196512,2328,1', '196512,2424,1', '196512,2520,1', '196512,2616,1', '196512,2712,1', '196512,2808,1', '196512,2904,1', '196512,3000,1', '196512,3096,1', '196512,3192,1', '196512,3288,1', '196512,3384,1', '196512,3480,1', '196512,3576,1', '196512,3672,1', '196512,3768,1', '196512,3864,1', '196512,3960,1', '196512,4056,1', '196512,4152,1', '196512,4248,1', '196512,4344,1', '196512,4440,1', '196512,4536,1', '196512,4632,1', '196512,4728,1', '196512,4824,1', '196512,4920,1', '196512,5016,1', '196512,5112,1', '196512,5208,1', '196512,5304,1', '196512,5400,1', '196512,5496,1', '196512,5592,1', '196512,5688,1', '196512,5784,1', '196512,5880,1', '196512,5976,1', '196512,6072,1', '196512,6168,1', '196512,6264,1', '196512,6360,1', '196512,6456,1', '196512,6552,1', '196512,6648,1']
print(len(list))

#print(blockFileRead)