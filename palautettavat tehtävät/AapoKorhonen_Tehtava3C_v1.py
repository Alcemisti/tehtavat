from random import randrange
random_numero = randrange(1,41)
import random

yritys=[]
voittavat_numerot = [40, 38, 12, 23]
arvotut_numerot = []
yritysten_määrä = int
yritysten_määrä == 0

#aliohjelma että generoidaan numerot listaan
def arvo_lottonumerot():
    arvotut_numerot = []
    while len(arvotut_numerot) < 4:
        numero = random.randint(1, 40)  # Lotto numerot välillä 1-40
        if numero not in arvotut_numerot:
            arvotut_numerot.append(numero)
    return arvotut_numerot


while True:
    if yritys==voittavat_numerot:
        print("")
        break
    else:
        yritysten_määrä + 1
