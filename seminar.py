# Задача 1
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num = float(input("Введите число: "))

sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("Сумма цифр данного числа равна: ", sum)

# Задача 2
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int(input("Введите число N: "))
prod = 1 
for i in range(1, N+1):
    prod *= i 
print("Произведение чисел от 1 до N = ", prod)

# Задача 3
#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
n = int(input("Введите число N: "))
sum = 0
for i in range(1, n+1):
    sum += (1 + 1/i) **i 
print("Сумма из последовательности", n, "чисел равна ", sum)

# Задача 4
#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint
from tkinter import W

n = (int(input('Введите количество элементов: ')))
list = []
for i in range(n):
    list.append(randint(-n, n+1))
print(list)

f = open("file.txt", 'w')
while True:
    pos = input("Укажите нужную вам позицию для вычисления: ")
    if pos == "":
        break
    f.write(pos+"\n")
f.close()

prod = 1
f = open("file.txt", 'r')
for line in f:
    if line == "":
        break
    prod *= list[int(line)]
f.close()
print(prod)

# Задача 5
#Реализуйте алгоритм перемешивания списка.
import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Изначальный список: ', list)
random.shuffle(list)
print('Перемешанный список: ', list)

#Заполнение листа пользователем
import random

def list(L):
    list = []
    for i in range(L):
        n = int(input(f"Введите {i+1} элемент: "))
        list.append(n)
    return list

m = int(input("Введите количество элементов: "))
new_list = list(m)
print('Изначальный список: ', new_list)
random.shuffle(new_list)
print('Перемешанный список: ', new_list)