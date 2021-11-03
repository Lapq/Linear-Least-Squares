def achataLista2d(l:list):
    lflat = list()
    for i in l:
        for j in i:
            lflat.append(j)
    return lflat
