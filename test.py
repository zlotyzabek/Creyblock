from opensimplex import OpenSimplex
tmp = OpenSimplex()
for i in range(100):
    b = ""
    for szer in range(int(tmp.noise2d(x=i / 8, y=1) * 12) + 7):
        b += "="
    print(b)