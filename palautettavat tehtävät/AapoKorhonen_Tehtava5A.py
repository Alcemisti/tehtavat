import datetime

valinta = int(input("Haluatko laskea päivät jouluun tästä hetkestä (1) vai laskea jouluun omasta syntymäpäivästä (2)"))


nyt = datetime.datetime.now()
joulu = datetime.datetime(nyt.year, 12, 24)
viimejoulu = datetime.datetime(nyt.year - 1, 12, 24)

if nyt > joulu:
    joulu = datetime.datetime(nyt.year + 1, 12, 24)

def paivatjouluun():
    if valinta == 1:
        ero = joulu - nyt
        paivina = ero.days
        return paivina
    
def paivatviimejoulusta():
    if valinta == 1:
        summa = nyt - viimejoulu
        paivina = summa.days
        return paivina

def synttareista_jouluun():
    if valinta == 2:
        while True:
            try:
                synttari_paiva = int(input("mikä päivä sun synttärit on "))
                synttari_kuu = int(input("mikä kuukausi synttärisi ovat "))

                synttärit = datetime.datetime(nyt.year, synttari_kuu, synttari_paiva)

                if synttärit > joulu:
                    uusi_joulu = datetime.datetime(nyt.year + 1, 12, 24)
                else:
                    uusi_joulu = joulu
                    
                
                ero = uusi_joulu - synttärit
                paivina = ero.days
                return paivina
            except ValueError:
                print("virhe")
            except Exception as e:
                print("virhe")

if valinta == 1:
    print(paivatjouluun())
    print(paivatviimejoulusta())
    if paivatjouluun() < paivatviimejoulusta():
        print("olet lähempänä ensi joulua kuin viime joulua")
    elif paivatviimejoulusta() < paivatjouluun():
        print("oot lähempänä viimejoulua kuin ensijoulua")
elif valinta == 2:
    print(synttareista_jouluun())
else:
    print("ERROR!")
