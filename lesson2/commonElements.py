list1 = input("Введите первый список: ").split()
list2 = input("Введите второй список: ").split()


set1 = set(map(int, list1))
set2 = set(map(int, list2))

common_elements = set1.intersection(set2)


print(f"Общие элементы:", *sorted(common_elements))