romdict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

roman = list(input("enter a roman number: "))
translated = []  # lista przechowująca przetłumaczone liczby
result = 0  # wynik końcowy

for num in roman:
    if num in romdict:  # jeżeli liczba jest rzymska
        translated.append(romdict[num])  # przetłumacz
    else:
        print("wrong input")

for num in translated:
    idx = translated.index(num)  # aktualna pozycja
    # jeżeli liczba jest ostatnia lub większa od następnej zwiększ wynik
    if idx == len(translated)-1 or (idx != len(translated)-1 and num >= translated[idx+1]):
        result += num
    else:  # jeżeli liczba jest mniejsza od następnej zmniejsz wynik o jej wartość
        result -= num

print(result)
