print("Tervetuloa pelaaman kiuaskivi peliä")
print("Tervetuloa seikkailu peliin!")
print("Tehtävänäsi on mennä tokmanniin ja ostaa kiuaskiviä")
print("matkallasi saatat kohdata haasteita")
print("Peliä pelataan vastaamalla numeroilla, 1 tarkottaa ensimmäinen vastaus ja 2 toinen ja niin edelleen.")
print("-----------------------")


jee = int(input("Menetkö Tokmanniin(1) vai biltemaan(2) ostamaan kiuaskiviä?: "))


if jee == 1:
    print("menit tokamnniin jee")
    jee = int(input("Ostakko kiuaskiviä? joo(1) ei(2) ostat kiuashiekka(3): "))
    if jee == 1:
        print("Voitit pelin")
    elif jee == 3:
        print("ei tokmaninssa myydä kiuashiekkaa ja mitä se ees on wtf")
    else:
        print("Hävisit peli")
elif jee == 3:
    print("Löysit salaisen lopetuksen: Alexander Stubb tulee luoksesi ja antaa kiuaskivet ilmaiseksi! Voitit pelin!")
else:
    print("Hävisit pelin")
