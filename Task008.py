"""
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.
"""
count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)
#Или
"""
list_1 = [1, 2, 3, 4, 5]
k = 3
print(list_1.count(k))
"""