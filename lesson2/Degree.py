
l = input("Введите числа через пробел: ").split()
degre = input("Введине степень: ")
result = []

try:
    degre = int(degre)
    for i in l:
        try:
            num = float(i)
            if num.is_integer():
                num = int(num)
            result.append(str(num ** degre))
        except ValueError:
            result.append(i * degre)
    print("Вывод:", " ".join(result))
except:
    print("Необходимо ввести число степени")



