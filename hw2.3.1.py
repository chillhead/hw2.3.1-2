user_input = list(input('Введите через пробел оператор и два числа: ').split(' '))
operator = user_input[0]
assert operator in ['+', '-', '*', '/'], 'Введен неверный оператор.'

digit1 = int(user_input[1])
digit2 = int(user_input[2])
result = 0
assert digit1 >= 0, 'Введено отрицательное число'
assert digit2 >= 0, 'Введено отрицательное число'
try:

    if operator == '+':
        result = digit1 + digit2
    elif operator == '-':
        result = digit1 - digit2
    elif operator == '*':
        result = digit1 * digit2
    elif operator == '/':
        result = digit1 / digit2

except ValueError:
    print('Похоже вы пытаетесь оперировать со строками.')
except ZeroDivisionError:
    print('Деление на 0 запрещено! Администрация.')
else:
    print(result)