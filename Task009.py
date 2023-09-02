list_1 = [1,2,3,4,5] # список чисел
k = 4.2         # число к которому найти ближайшее
 

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)