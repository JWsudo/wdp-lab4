import math

def pole(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Boki musza byc dluzsze niz zero.")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Taki trojkat nie istenieje.")

    s = (a + b + c) / 2
    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return pole


try:
    a = 5
    b = 4
    c = 8
    print(f"Pole trójkąta o bokach {a}, {b}, {c}: {pole(a, b, c)}")
except ValueError as e:
    print(f"Wyjątek: {e}")