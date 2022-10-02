# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11

n = float(input('введите число: '))
sum = 0
while n != 0:
    sum = sum + n %10
    n = n // 10
print(int(sum))

# 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('введите число: '))
# prod = 1
# array = []
# for i in range(1, n + 1):
#     array.append(prod * i)
#     prod = prod * i
# print(array)

# 3. Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму.

# n = int(input('введите число: '))
# list = []
# sum = 0
# for i in range(1, n + 1):
#     sum += ((1 + 1 / i) ** i)
# print(round(sum, 2))

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# n = int(input('введите число N: '))
# a = []
# for i in range(-n, n + 1):
#     a.append(i)
# print(a)
#
# # попыталась по логике лекции написать программу, но она не работает. Помогите разобраться
# # ошибка здесь:  prod = prod * list[line] - unsupported operand type(s) for *: 'int' and 'types.GenericAlias'
#
# prod = 1
# data = open('file.txt', 'r')
# for line in data:
#     prod = prod * list[line]
# data.close()
# print(prod)

# 5. Реализуйте алгоритм перемешивания списка.
# не знаю, как написать алгоритм, нашла готовый метод shuffle

# from random import *
# array = [randint(0, 10) for _ in range(randint(0, 5))]
# print(array)
# shuffle(array)
# print(array)
