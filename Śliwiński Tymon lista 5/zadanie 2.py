ones = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziewięć"}
twos = {0:"dziesięć", 1:"jedenaście", 2:"dwanaście", 3:"trzynaście", 4:"czternaście", 5:"piętnaście",
        6:"szesnaście", 7:"siedemnaście", 8:"osiemnaście", 9:"dziewiętnaście"}
tens = {2:"dwadzieścia", 3:"trzydzieści", 4:"czterdzieści", 5:"pięćdziesiąt", 6:"sześćdziesiąt", 7:"siedemdziesiąt", 8:"osiemdziesiąt", 9:"dziewięćdziesiąt"}
hundrets = {1:"sto", 2:"dwieście", 3:"trzysta", 4:"czterysta", 5:"pięćset", 6:"sześćset", 7:"siedemset", 8:"osiemset", 9:"dziewięćset"}

inp = input("liczba 1-1999: ")

inp_length = len(inp)

if inp_length == 1:
    print(ones[int(inp)])
elif inp_length == 2 and inp[0] == 1:
    print(twos[int(inp[1])])
elif inp_length == 2:
    print(tens[int(inp[0])], ones[int(inp[1])])
elif inp_length == 3:
    print(hundrets[int(inp[0])], tens[int(inp[1])], ones[int(inp[2])])
elif inp_length == 4:
    print('tysiąc', hundrets[int(inp[1])], tens[int(inp[2])], ones[int(inp[3])])
else:
    print('nieprawidłowy input')
