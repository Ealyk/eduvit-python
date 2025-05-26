from warnings import catch_warnings
while (True):
    print("Введите число: ")
    numb = input()
    if (numb == "exit"):
        break;


    try:
        numb = int(numb);
        if numb % 2 == 0:
            print(f"Число {numb} является чётным")
        else:
            print(f"Число {numb} не является чётным")
    except: (print("Ошибка: введено не число"))