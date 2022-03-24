# # 1.1) убрать из него повторяющиеся элементы
my_list1=[10,11,2,3,5,8,23,11,2,5,76,43,2,32,76,3,10,0,1]
print (list(set(my_list1)))
print(my_list1)

# 1.2) вывести 3 наибольших числа из исходного массива
my_list3=[10,11,2,3,5,8,23,11,2,5,76,43,2,32,76,3,10,0,1]
my_list4=list(set(my_list3))
my_list5=sorted(my_list4)
x=max(my_list5)
print(x)
del my_list5[-1]
y=max(my_list5)
print(y)
del my_list5[-1]
z=max(my_list5)
print(z)

# 1.3) вывести индекс минимального элемента массива
a=min(my_list1)
b=my_list1.index(a)
print(b)

#1.4) вывести исходный массив в обратном порядке
my_list2=list(reversed([10,11,2,3,5,8,23,11,2,5,76,43,2,32,76,3,10,0,1]))
print(my_list2)