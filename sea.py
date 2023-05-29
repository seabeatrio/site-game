counter1 = 0
counter2 = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1
if counter2 > 4:
    print('Было введено', counter2, 'нулей.')
if counter1 == 1:
    print('Было введено', counter1, 'число, больших 10.')
if counter1 > 1 and counter1 < 5:
    print('Было введено', counter1, 'числа, больших 10.')
if counter2 < 5:
    print('Было введено', counter2, 'нуля.')
if counter1 > 4:    
    print('Было введено', counter1, 'чисел, больших 10.')
