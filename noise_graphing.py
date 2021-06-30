import perlin

def show_perlin_noise():
    noise=perlin.Perlin(15)
    lista = []

    time=[i for i in range(100000)]
    for i in time:
        lista.append(int(noise.valueAt(i) * 10))
    print(lista)
show_perlin_noise()