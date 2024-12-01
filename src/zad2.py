from audioop import reverse

imiona = ["Tomek", "Ala", "Jacek","Iza"]
imiona = sorted(imiona)
print(imiona)
imiona.append("Ryszard")
imiona.append("Henryk")
print(imiona.pop())
imiona.insert(2, "Jan")
print(imiona)
imiona.reverse()
imiona = imiona*2
print(imiona)