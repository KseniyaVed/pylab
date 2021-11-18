Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# задание №1 (сумма ряда 0-100)

import numpy
x=numpy.array(range(100))
print(numpy.mean(x))

# Задание №2 (сумма ряда 0-инпут)

import numpy
a=int(input())
b=[int(c) for c in input().split()]
print(numpy.array(b))

# Задание №3 (среднее среди 100 случайных чисел)

import numpy as np
import random
x = np.array([random.random() for i in range(100)])
print(np.mean(x))
