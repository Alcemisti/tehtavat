def jarjesta():
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] >= list[j]:
                list[i], list[j] = list[j], list[i]
    
    print("Numerot pienimmästä suurimpaan:", list)
list = []
kysy = input("Anna jokin kokonaisluku (jätä tyhjäksi lopettaaksesi): ")

while kysy != "":
    list.append(int(kysy))
    kysy = input("Anna jokin toinen kokonaisluku (jätä tyhjäksi lopettaaksesi): ")
    
jarjesta()
