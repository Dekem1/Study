#!/usr/bin/env python
# coding: utf-8

# In[85]:


list = [1,False,'Федун','Олег','Вариант',9.0, 'и','это',True]
def main():
    
    choose = 7
    while choose != '0':
        print('ВЫБЕРИТЕ ДЕЙСТВИЕ\n' '1 - Вывести список\n'  '2 - добавить элемент в список\n' '3 - удалить элемент из списка\n'  '4 - переставить элемент в списке\n' '0 - Выход')
        choose = input()  #Получение символа с клавиатуры
        if choose == '1': 
            print(list)  #Вывод списка
            continue
            
        elif choose == '2':
            print('Введите позицую нового элемента')
            index = input()
            print('Введите элемент списка')
            element = input()
            list.insert(int(index)-1,element)  #удаление элемента по номеру
            print(list)
            continue
        elif choose == '3' :
            print('Введите номер элемента для удаления')
            index = input()
            list.pop(int(index)-1)
            print(list)
            continue
        elif choose =='4' :
            print('ВВедите номер элемента для перестановки')
            index_in = input()
            print('ВВедите с каким элементом поменять')
            index_to = input()
            boot = list[int(index_to)-1]                  #Буфер запоминания элемента
            list[int(index_to)-1]=list[int(index_in)-1]   #В элемент "В него" присвоить значение элемента "Из него"
            list[int(index_in)-1] = boot                  #В элемент "Из него" присваиваем значение из буфера
            print(list)
            continue
        elif choose == '0':
            flag = 0
            continue
        
    
        else:
            print('Необходимо ввести число 1- 4!!!!')
            continue
main()


# In[88]:


myStr1='Дана;1;строка;которая;содержит;1;слова;разделенные;символом;точки;2;с;запятой;строка;которая;содержит'
my_list=list(set(myStr1.split(";")))
print(my_list)


# In[ ]:




