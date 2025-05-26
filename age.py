print("Введите ваш возраст: ");
age = input()

try:
    age = int(age);
    if age >= 18:
        print("Вы совершеннолетний.")
    else: print("Вы несовершеннолетний.")
except: print("Ошибка: введено не число!")