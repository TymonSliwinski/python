dane = {"jeden":1, "dwa":2, "trzy":3, "cztery":4, "pięć":5, "sześć":6, "siedem":7, "osiem":8, "dziewięć":9,
        "dziesięć":10, "jedenaście":11, "dwanaście":12, "trzynaście":13, "czternaście":14, "piętnaście":15,
        "szesnaście":16, "siedemnaście":17, "osiemnaście":18, "dziewiętnaście":19,"dwadzieścia":2, "trzydzieści":3,
        "czterdzieści":4, "pięćdziesiąt":5}

inp = input("wprowadź liczbę słownie w przedziale 1-59: ").split()

if len(inp) == 1:
    if inp[0] in list(dane)[:19]:
        print(dane[inp[0]])
    elif inp[0] in list(dane)[19:]:
        print(str(dane[inp[0]])+"0")
    else:
        print('error1')
elif len(inp) == 2:
    if inp[0] in list(dane)[19:] and inp[1] in list(dane)[:19]:
        print(str(dane[inp[0]]) + str(dane[inp[1]]))
    else:
        print('error2')
else:
    print('error3')
