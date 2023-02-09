from random import randint

n = int(input("Введите колличество элементов массива  -->   "))
list = []


for i in range(n):
    num = int(input(f"Введите [{i}] элемент массива -->   "))
    list.append(num)
print(list)

x = int(input("Какое число посчитать в массиве? -->   "))

count = 0
for i in list:
    if i == x:
        count += 1
print(f"В массиве число '{x}' повторяется {count} раз(а).")

print()
print()
print(n)
print(list)
print(x)
print(count)