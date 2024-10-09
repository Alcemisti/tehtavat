num1 = float(input("\nAnna ensimmäinen numero (pienempi): "))
num2 = float(input("Anna toinen numero (suurempi): "))


if num1 < num2:
    prosentti = (num1 / num2) * 100
    print(f"Luku {num1} on {prosentti:.2f}% luvusta {num2}")

    palkin_pituus = 25
    palkki = int((prosentti / 100) * palkin_pituus)

    palkki_visuaalisesti = "💥" * palkki + "🌕" * (palkin_pituus - palkki)
    print(f"latausbaari: {palkki_visuaalisesti}")
else:
    print("Virhe: Ensimmäisen luvun pitää olla pienempi kuin toisen.")