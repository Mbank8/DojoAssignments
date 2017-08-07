
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


def draw_stars(x):
    total = 0
    for value in x:
        if isinstance(value, int):
            print value * "*"
        elif isinstance(value, str):
            print value[0] * len(value)
            

print draw_stars(x)