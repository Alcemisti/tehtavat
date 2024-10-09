#tarvitaan 2 floattia
#tarvitaan iffilauseita joissa on + - * ja / laskut
#käytätjä valitsee minkä noista lasketaan

print("Laitappa numeroita, jos laitat kirjaime nii ei toimi t. Alexander Stubb elikkäs presidentti")
arvo1 = float(input("anna eka arvo: "))
arvo2 = float(input("annappa toine arvo: "))


print("annoit arvot",arvo1, "ja",arvo2)


laskutoimitus = input("mikä laskutoimitus tehää? ( + - * / ): ")

if laskutoimitus == "+":
    print(arvo1 + arvo2)
elif laskutoimitus == "-":
    print(arvo1 - arvo2)
elif laskutoimitus == "*":
    print(arvo1 * arvo2)
elif laskutoimitus == "/":
    print(arvo1 / arvo2)
else:
    print("virhe")