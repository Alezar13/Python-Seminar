

a = int(input("ВВедите минимальный элемент массива => "))
b = int(input("ВВедите максимальный элемент массива => "))
r = int(input("ВВедите длину массива => "))
from random import randint
list_1 = [randint(a, b) for i in range(r)] 
list_2 = []
min = int(input("ВВедите минимальное число диаппазона => "))
max = int(input("ВВедите максимальное число диаппазона => "))
print(f"Массив : {list_1}")
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(f"Индексы элементов входящих в заданный диапазон : {list_2}")