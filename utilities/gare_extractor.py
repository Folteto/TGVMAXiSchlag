def import_gares_from_csv(csv):
    gares = []
    with open(csv, 'r') as f:
        for line in f:
            gare = line.split(';')[6]
            if gare not in gares:
                gares.append(gare)
            gare2 = line.split(';')[7]
            if gare2 not in gares:
                gares.append(gare2)
    return gares


def write_gares_to_file(gares, file):
    with open(file, 'w') as f:
        for gare in gares:
            f.write(gare + '\n')


gares = import_gares_from_csv('..\data\tgvmax.csv')
write_gares_to_file(gares, '..\data\gares.txt')
