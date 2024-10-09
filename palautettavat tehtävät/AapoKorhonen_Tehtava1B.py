kuukausitulot = float(input("Paljonko sun keskimääräinen kuukausitulot on?: "))

ruokahinta = float(input("Paljonko kouluruoka hinta on?: "))

montako = float(input("montako kertaa syöt kuukaudessa kampuksella: "))

muut = float(input("Paljonko menee kaikkeen muuhun elämiseen: "))

print("")
print("----------------------------")
print("")

print(f'Sun vuositulot on: {round(kuukausitulot * 12, 2)}')

ruokaakk = float(ruokahinta) * float(montako)
print(f'Sulla menee kouluruokaan rahaa kuukaudessa: {round(ruokaakk, 2)} €')

kuukausimenot = float(muut) + float(ruokaakk)
print(f'Sun kuukaisimenot yhteensä: {round(kuukausimenot, 2)} €')

rahatkateen = float(kuukausitulot) - float(kuukausimenot)
print(f'Kätenejäävä osuus menojen jälkeen kuukaudessa: {round(rahatkateen, 2)} €')

print("")
print(f'4 vuodessa säästät näin paljon jos laitat 20% joka kk: {round(rahatkateen * 0.2 * 4 * 12, 2)} €')
print("")


print("")
print("----------------------------")
print("")

# output > vuositulot eli kuuakusi tulot * 12
# paljo rahaa menee kouluruokaan kuukaudessa eli 30 * 3?
# kuukausi menot yhteensä eli 