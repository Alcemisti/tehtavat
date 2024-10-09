import random

def LuoKayttajatunnus(etunimi, sukunimi):
    etu = etunimi[:3].lower()
    suku = sukunimi[:3].lower()
    numerot = str(random.randint(100, 999))
    kayttajatunnus = etu + suku + numerot
    return kayttajatunnus

etunimi = input("Anna etunimesi: ")
sukunimi = input("Anna sukunimesi: ")

kayttajatunnus = LuoKayttajatunnus(etunimi, sukunimi)

print("Luotu käyttäjätunnus on:", kayttajatunnus)