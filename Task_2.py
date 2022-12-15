# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
numbers = [1.05, 1.045, 3.3, 10.1]
def f (x):
    k = round(x % 1,4)
    return k

data = list(map(f,numbers))

#while i < len(numbers):
#    ls.append(f(numbers[i]))
#    i += 1

num_min = data[0]
num_max = 0
for j in data:
    if j > num_max:
        num_max = j
    elif j < num_min:
        num_min = j
print(round(num_max - num_min,4))