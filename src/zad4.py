alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
data = str(input("Podaj zdanie"))
print(data)

sorted_data = ''.join(sorted(data))
print(sorted_data)


for letter in sorted_data:
    print("indeks")
    int_data = alfabet.index(letter.lower())
    print(alfabet.index(letter.lower()))
    del alfabet[int_data]

print(alfabet)