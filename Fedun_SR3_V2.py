#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list = (1,'Федун', 'Олег', 'В9',True,'ЭВМ',21,1,'ЭВМ',3.44,'Федун',False,True)
def main():
    
    choose = 7
    while choose != '0':
        print('ВЫБЕРИТЕ ДЕЙСТВИЕ\n' '1 - Вывести кортеж\n'  '2 - поиск элемента\n')
        choose = input()  #Получение символа с клавиатуры
        if choose == '1': 
            print(list)  #Вывод списка
            continue
            
        elif choose == '2':
            print('Введите элемент для поиска')
            index = input()
            try: print('Номер искомого элемента',list.index(index)+1)
            except ValueError :
                try:
                    index1 = float(index)
                    print('Номер искомого элемента',list.index(index1)+1)                                                            
                except ValueError :                                              
                        count = 0
                        index2 = str(index)
                        for i in list:                               
                            if(str(i)== index2):
                                print('Номер искомого элемента',count+1)
                                break
                            else:
                                    count=count+1                        
                        if (len(list)==count):
                            print('элемента нет в кортеже')                                
                
            continue        
        else:
            print('Необходимо ввести число 1- 2!!!!')
            continue
main()


# In[ ]:





# In[ ]:




