#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
#Задание на отбор:
#N классов в школе программистов решили отпраздновать конец четверти и заказать пончиков 
#M видов. В ближайшей кофейне ученикам предложили выбрать один прайс-лист из 
#L разновидностей.
#Помогите ученикам написать код, который посчитает сколько денег на пончики по разным прайс-листам потратит каждый класс.

#ФОРМАТ ВВОДА
#Первая строка содержит числа 1≤N,M,L≤500.

#Далее идут N строк, содержащих M чисел - количества пончиков каждого вида, необходимые каждому классу.

#Далее идут M строк, содержащие список цен для каждого вида пончиков в каждом из L прайс-листов.

#ФОРМАТ ВЫВОДА
#Выведите N строк, содержащих стоимость всех пончиков для каждого класса для каждого из L прайс-листов.


# In[3]:


my_series_1 = pd.Series(['A','A','B','B'])
my_series_2 = pd.Series([10,14,12,23])
my_data=pd.DataFrame({'type':my_series_1,'value':my_series_2})


# In[4]:


B=[]
C=[]
H=()
A=input()
A=A.split(' ')
for i in range(int(A[0])):
    B.append(input())
    B[i]=list(map(int, B[i].split()))
for i in range(int(A[1])):
    C.append(input())
    C[i]=list(map(int, C[i].split()))


# In[278]:


B=[]
C=[]
H=''
A=input()
A=A.split(' ')
for i in range(int(A[0])):
    B.append(input())
    B[i]=list(map(int, B[i].split()))
for i in range(int(A[1])):
    C.append(input())
    C[i]=list(map(int, C[i].split()))
s=0
p=0
for j in range(len(B[0])):
    
    for k in range(len(C[0])):
        for i in range(len(B[0])):
           
            o=C[i][k]*B[k-p+j][i]
            
            s+=o
            
        p+=1
        H=H+str(s)+' '
        
        s=0
        
    p=0
    print(H)
    H=''
          
    


# In[203]:


for j in range(4):
    print(j)


# In[246]:


for i in range(int(A[0])):
    print(str(H[i*int(A[2]):(i+1)*int(A[2])])

