try:
    operator = input('Введите ператор(+ - * /): ')
    digit1 = int(input('Введите число: '))
    digit2 = int(input('Другое число: '))
    result = 0
    if operator == '+':
        result = digit1 + digit2
    elif operator == '-':
        result = digit1 - digit2
    elif operator == '*':
        result = digit1 * digit2
    elif operator == '/':
        result = digit1 / digit2
    try:
        assert operator in ['+', '-', '*', '/'], 'Введен неверный оператор.'
    except Exception as e:
        print(e)
except ValueError:
    print('Похоже вы пытаетесь оперировать со строками.')
except ZeroDivisionError:
    print('Деление на 0 запрещено! Администрация.')
else:
    print(result)
