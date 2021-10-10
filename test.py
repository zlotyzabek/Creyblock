from opensimplex import OpenSimplex
tmp = OpenSimplex()
b = []
for i in range(10000):
    biom = ((int(tmp.noise2d(x=i, y=3) * 12)) % 6)
    if biom < 0:
        biom *= -1
    szerBiom = int(tmp.noise2d(x=i / 8, y=3) * 200)
    if szerBiom < 0:
        szerBiom *= -1

    for szer in range(szerBiom + 30):
        b.append(biom)

print(b)

