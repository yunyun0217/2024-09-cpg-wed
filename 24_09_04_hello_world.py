# -*- coding: utf-8 -*-
"""24-09-04-hello-world.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Vn1EgEZnkEhIUt1BTswLCnw6Xd8jsnWI
"""

print("Hello World")

print("Hello Python")

a = 1
a = a + 1  # a + 1로 계산된 값을 다시 a에 대입한다.
print(a)

a = 1
a -= 3
  # a + 1로 계산된 값을 다시 a에 대입한다.
print(a)

#복합연산자 +=, -=, *=, /=, //=, %=, **=

import pylab as py

x_deg = py.arange(-180, 180+1,)
x_rad = py.deg2rad(x_deg)
y = py.sin(x_rad)

py.plot(x_deg, y)

py.xlabel('x(def)')
py.ylabel('sin(x)')
py.grid(True)