""" 
Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

Функция не должна ничего выводить, только возвращать значение.

Пример:


a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8 

"""

a = 2
b = 3

def f(a, b):
    if b == 0:
        return 1
    else:
        return a * f(a, b - 1)
       
    
print(f(a, b))