word = input("ANNA SANA! ")
reversed_word = ""
for käännettysana in range(len(word) - 1, -1, -1):
    reversed_word += word[käännettysana].swapcase()
print("Käännettynä:", reversed_word)