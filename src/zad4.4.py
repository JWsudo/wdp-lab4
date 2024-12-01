def average(lista):
    counter = 0
    sum = 0
    for digit in lista:
        sum += digit
        counter +=1
    return sum/counter

print(average([1,2,3]))