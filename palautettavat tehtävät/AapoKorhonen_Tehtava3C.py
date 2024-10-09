import random

# Oikeat tämän viikon lottonumerot (voit päivittää nämä manuaalisesti)
oikeat_numerot = [5, 12, 16, 20]

# Funktio, joka arpoo lottonumerot
def arvo_lottonumerot():
    arvotut_numerot = []
    while len(arvotut_numerot) < 4:
        numero = random.randint(1, 40)  # Lotto numerot välillä 1-40
        if numero not in arvotut_numerot:
            arvotut_numerot.append(numero)
    return arvotut_numerot

# Laskuri yrityksille
yritykset = 0

# Toistetaan silmukkaa, kunnes arvotut numerot osuvat oikeisiin numeroihin
while True:
    yritykset += 1
    arvotut = arvo_lottonumerot()
    
    # Tarkista, onko arvotut numerot samat kuin oikeat numerot
    if sorted(arvotut) == sorted(oikeat_numerot):
        break

# Tulostetaan tulos
print(f"oot nyt miljonäri, näin monta yritystä meni {yritykset}")
