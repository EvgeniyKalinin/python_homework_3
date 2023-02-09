# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# строка содержит число X.

n = int(input("Введите колличество элементов массива  -->   "))
list = []

for i in range(n):
    num = int(input(f"Введите [{i}] элемент массива -->   "))
    list.append(num)
print(list)
res = list[0]
len = len(list)

x = int(input("Какое число  -->   "))

k = list[0] - x
if k < 0:
    k *= -1
for i in range(len):
   
    
    k_1 = list[i] - x
    if k_1 < 0:
        k_1 *= -1
    if k_1 < k:
        k = k_1
        res = list[i]
    

print()
print(n)
print(list)
print(x)
print(res)
