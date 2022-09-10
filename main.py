# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11

# n = float(input('введите число '))
# sum = 0
# while n != 0:
#     sum = sum + n %10
#     n = n // 10
# print(int(sum))
    
# 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# prod = 1
# n = int(input('введите число '))
# list = []
# for i in range(1, n + 1):
#     list.append(prod * i)
#     prod = prod * i
# print(list)

# 3. Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму.

# n = int(input('введите число '))
# list = []
# sum = 0
# j = 0
# for i in range(1, n+1):
#     sum += ((1+1/i)**i)
# print(round(sum, 2))

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

## решение записала с урока, сама не совсем поняла его

# import random
# n = int(input())
# a = []
# for i in range(n):
#     a.append(random.randint(-n,n))
# print(a)

# m = open('file.txt', 'w')
# len_m = random.randint(2,n)
# for i in range(len_m):
#     m.write(str(random.randint(0, n-1)))
#     m.write('\n')
# prod = 1
# f = open('file.txt', 'r')
# for i in f.readline():
#     prod *= a[int(f.readline)]
# print(prod)

# 5. Реализуйте алгоритм перемешивания списка.

from random import * # импортируем все функции из библиотеки
list = [randint(-10, 10) for _ in range(randint(5, 10))]
print(list)
shuffle(list)
print(list)