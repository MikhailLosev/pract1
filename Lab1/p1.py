'''Открываем текстовый файл'''
with open('p1.txt') as f:
    a = f.read()
    ''' Закрываем'''
    f.close()

'''Объявляем переменные:
    n - колл-во цирф
    s - наш рузультат
    x - массив наших чисел
    sum_ - сумма наших цифр из массива'''
n = int(a.split()[0])
s = int(a.split()[-1])
x = [int(i) for i in a.split()[1:-1]]
sum_ = sum(x)

''' Объявляем функцию, которая рекурсивно перебирает знаки '''
def recurce_func(k, summ):

    if summ == s:
        return True
    if k == 0:
        return summ == s
    '''Меняем знаки'''
    x[k] = -x[k]
    if recurce_func(k-1, summ+2*x[k]):
         return True
    x[k] = -x[k]
    if recurce_func(k-1, summ):
        return True
    return False

''' Объявляем функцию, которая формирует ответ '''
def result_string(mas, res):
    if not res:
        return "No solution"
    string = str(mas[0])
    for elem in range(1, len(mas)):
        if mas[elem] >= 0:
            string += '+' + str(mas[elem])
        else:
            string += str(mas[elem])
    return string+'='+str(s)

''' Вызываем рекурсивную функцию'''
res = recurce_func(n-1, sum_)
''' Выводим ответ'''
print(result_string(x, res))







