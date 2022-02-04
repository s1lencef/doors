from random import choice
import pygal

hist = pygal.Bar()
hist.title = 'Проверка парадокса из тик-тока'
hist.y_title = 'Количество верно угаданных'

for k in range(0,2):
    if k == 0:
        title = 'НЕ МЕНЯЯ ВЫБОРА'
    else:
        title = 'ИЗМЕНЯЯ ВЫБОР'
    print(title)
    doors = [0, 0, 0]
    view = ['x', 'x', 'x']
    count_right = 0
    for i in range(0,10):
        doors[choice([0,1,2])] = 1
        print(view)
        first = int(input('Выберете дверь (0,1,2): '))
        for k in range(0,3):
            if (doors[k]==0) and (k!= first):
                view[k] = doors[k]
                break
        print(view)
        first = int(input('Выбете дверь (0,1,2): '))
        if doors[first] == 1:
            count_right +=1

        view =['x','x','x']
        doors = [0,0,0]

    print('Верно угаданных: '+str(count_right))
    print('Процент угаданных: '+ str((round(count_right/10, 2))*100)+'%')


    with open('doors_test.txt','a') as file:
        file.write(title+'\n')
        file.write('Верно угаданных: '+str(count_right)+'\n')
        file.write('Процент угаданных: '+ str((round(count_right/10, 2))*100)+'%\n')
        file.write('-------'*35+'\n')


    hist.add(title, count_right)

hist.render_to_file('doors_test.svg')