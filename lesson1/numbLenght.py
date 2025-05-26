print("Введите число:")
numb = input()

try:
    numb = int(numb)
    lenght = 0
    while (numb // 10 >= 1):
        lenght += 1
        numb = numb // 10
    print(f"В этом числе {lenght} цифры.")
except: print("Ошибка: данные не являются числом.")