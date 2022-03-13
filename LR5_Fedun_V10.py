#!/usr/bin/env python
# coding: utf-8

# In[56]:



import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from math import pi
#Задаие 1
print('--------------------------ЗАДАНИЕ 1-----------------------')
A = np.array([[2, -5, 1, 2],[-3, 7, -1, 4],[5, -9, 2, 7],[4, -6, 1, 2]])
print(A)
print('Минимальный элемент',np.amin(A))
t1=np.nanmin(A,1)
t2=np.argmin(t1)
print('Строка с минимальным элементом',t2+1)
k1=np.take(A,[0,4,8,12])
print('1-ый столбец',k1)
k2=np.take(A,[8,9,10,11])
print('Строка с минимальным элементом',k2)
for i in range(0,4,1):
    A[2,i]=k1[i]
for i in range(0,4,1):
    A[i,0]=k2[i]
print('Результат перестановки\n',A)



#ЗАДАНИЕ 2
print('--------------------------ЗАДАНИЕ 2-----------------------')
x=np.linspace(-10,10,20)
y1=abs(abs(x)-3) #задание первой функии
y2=x-9           #задание второй функии
y3=-(x-9)        #задание третьей функии
y4=-(x-9)/3      #задание четвертой функии
plt.subplot()
plt.plot(x,y1,'g-',linewidth=1,marker = 'o')   #построение первой функии
plt.plot(x,y2,'b--',linewidth=2,marker = 'd')  #построение второй функии
plt.plot(x,y3,'r-.',linewidth=3,marker = 'X')  #построение третьей функии
plt.plot(x,y4,'k-',linewidth=4,marker = 's')   #построение четвертой функии
plt.grid('on')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Задание 2')
plt.legend(['y1','y2','y3','y4'])
plt.show()
print('Максимум y1:',max(y1),'Минимум y1:',min(y1))     #поиск максимума и минимума первой функии
print('Максимум y2:',max(y2),'Минимум y2:',min(y2))     #поиск максимума и минимума второй функии
print('Максимум y3:',max(y3),'Минимум y3:',min(y3))     #поиск максимума и минимума третьей функии
print('Максимум y4:',max(y4),'Минимум y4:',min(y4))     #поиск максимума и минимума четвертой функии



#Задание 3
print('--------------------------ЗАДАНИЕ 3-----------------------')
f3=lambda x: 1/(5*x+11)**3
import scipy.integrate as integrate
print('Интеграл',integrate.quadrature(f3,-2, -1))



#Задание 4
print('--------------------------ЗАДАНИЕ 4-----------------------')
x=np.linspace(0,2*pi)
f4=(3*x**2+5)*np.cos(2*x)
print('Интеграл методом трапеции',integrate.trapezoid(f4,x))
print('Интеграл методом Симпсона',integrate.simpson(f4,x))



#Задание 5
print('--------------------------ЗАДАНИЕ 5-----------------------')
f5 = lambda y, x: 1+(2*y/x)+(np.cos(x))**2
print('Решение повторного интеграла:',integrate.dblquad(f5, 1, 3, lambda x: 1, lambda x: 2))
print('--------------------------ЗАДАНИЕ 6-----------------------')


# In[ ]:




