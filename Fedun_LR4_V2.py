#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pickle

class students (list):
    
 
    def __init__(self,group, FName, Name, SName, oc):   #Конструктор класса
       
        self.group = group
        self.FName = FName
        self.Name = Name
        self.SName = SName
        self.oc = oc
        
      
    def Edit(self,group, FName, Name, SName, oc):       #Функция изменения параметров класса
        
        
        self.group = group
        self.FName = FName
        self.Name = Name
        self.SName = SName
        self.oc = oc
        print(self.group,self.FName,self.Name,self.SName,self.oc)
   
    def _Print(self):                                    #Функция вывода параметров экземпляра класса /Protected
        #Вывод
        print(self.group,self.FName,self.Name,self.SName,self.oc)
        
    def oc_x2_plus1(self):                               #Функция увеличивает параметр oc в 2 раза и прибавляет 1 (oc*2+1)/Public
         
        self.oc= self.oc*2
        print(self.group,self.FName,self.Name,self.SName,self.oc)
        self.__Plus_odin()
        print(self.group,self.FName,self.Name,self.SName,self.oc)
        
    def __Plus_odin(self):                               #Приватная функция увеличения параметра oc на 1 (oc+1)/Private
        self.oc = self.oc + 1
            
class kurs4 (students):                                  #Подкласс класса student
     
    def oc_x2_plus1(self):                               #Переопределение функции oc_x2_plus1 (ранее она выводила(oc*2+1)
        self.oc = self.oc *3                             # теперь будет выводить oc*3
        print(self.group,self.FName,self.Name,self.SName,self.oc)
    
id_1=students('A-04','Fedun','Oleg','Stepanovich', 100)  #создаем экземпляр класса student, id_1
id_1._Print()                                            #проверяем метод _Print
id_1.Edit('A-04','Fedun','Oleg','Stepanovich', 5)        #проверяем метод Edit
id_1.oc_x2_plus1()                                       #проверяем метод oc_x2_plus1
with open("A04Fedun.pkl", "wb") as fp:                   #Сохраняем класс в файл A04Fedun.pkl
    pickle.dump(id_1, fp)
with open("A04Fedun.pkl", "rb") as fp:                   #Загружаем в переменную test файл A04Fedun.pkl
    test = pickle.load(fp)
test._Print()                                            #проверяем метод _Print для загруженного экземпляра
test.Edit('A-04','Fedun','Oleg','Python3', 132321)

id_kurs4 = kurs4('A-06','Familiy','Imya','Otchestvo', 10)   #создаем экземпляр класса kurs4, он является подклассом students
id_kurs4._Print()                                           #Пробуем вызвать защищенный метод описанный в родительском классе
id_kurs4.oc_x2_plus1()                                      #Проверим переопределение функции oc_x2_plus1, ожидаем oc*3

id_1.__Plus_odin()                                          #Попробуем вызвать приватный класс для экземпляра класса
                                                            # Должны получить ошибку
    