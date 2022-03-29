#Найти общие ключи в двух словарях:
dict_one = {'a':1,'b':2,'c':3,'d':4}
dict_two = {'a':6,'b':7,'z':20,'x':40}
intersection = dict_one.keys() & dict_two.keys()
print(intersection)
