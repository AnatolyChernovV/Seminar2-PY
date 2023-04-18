# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
n = int(input())
count_reshka = 0
count_gerb = 0
for i in range(n):
    print('1 or 0:')
    x = int(input())
    if x == 0:
        count_reshka += 1
    else:
        count_gerb += 1
if count_gerb > count_reshka:
    print('reshka:',count_reshka)
else:
    print('gerb:',count_gerb)