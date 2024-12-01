imie = input("Podaj imie")
print(f"Witaj {imie}")
wiek = input("Podaj wiek")
print(f"Twoj wiek {wiek}")
nazwisko = input("Podaj nazwisko")
print(f"Inicjaly: {imie[0]} {nazwisko[0]}")
lancuch = input("Podaj lancuch")
print(lancuch*5)

lancuch2 = input("Podaj 2 lancuch")
lancuch3 = input("Podaj 3 lancuch")

lancuch4 = lancuch2+ lancuch3

print(lancuch4)
lancuch5= lancuch2[0:len(lancuch2)//2] + lancuch3[len(lancuch3)//2:]
print(lancuch5)