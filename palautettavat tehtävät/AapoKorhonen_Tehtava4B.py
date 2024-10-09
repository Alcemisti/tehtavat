def generoi_yhdistelmat(merkit, pituus, yhdistelma=""):
    if len(yhdistelma) == pituus:
        print(yhdistelma)
        return
    for merkki in merkit:
        generoi_yhdistelmat(merkit, pituus, yhdistelma + merkki)
merkit = ['1', '7', '9', '0']
pituus = 6
generoi_yhdistelmat(merkit, pituus)
