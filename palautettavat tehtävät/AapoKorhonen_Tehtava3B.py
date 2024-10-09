#lisätään tuotteita ostoslistaan

#täs o ostoslista
ostoslista = []

#nyt käyttäjä saa lisata listaan tavaraa
while True:
    itemi = input(" mitä laitettaa(kirjotappa valmis jos et laita enemppää)")

    if itemi.lower() == 'valmis':
        break

    ostoslista.append(itemi)


#for looppia nyt käytetän kun tehtävässä sanotinn etät pitää käyttää nii käytetää sitä for looppia sitte tähä viimesee osioo nii

ostoslista.sort()

print("\ntäsäs lista:")
for itemi in ostoslista:
    print(itemi)