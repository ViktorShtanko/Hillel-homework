#Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = {}
for i in keys:
    a[i] = i*i
print(a)