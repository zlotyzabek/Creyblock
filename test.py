import noise

help(noise)


perlin = []

for y in range(5):
    for x in range(5):
        perlin.append(int(noise.snoise2(x, y, octaves=1, persistence=1, lacunarity=2, base=0) * 10))
    perlin.append("\n")

print(perlin)