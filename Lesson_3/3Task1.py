Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''


def div(*args):

    try:
        arg1 = int(input("Введите делимое число:  "))
        arg2 = int(input("Введите делитель: "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Нельзя использовать 0 в делителе"

    return res

    '''
 if arg2 != 0:
 return arg1 / arg2
 else:
 print("Нельзя использовать ноль в делителе")
    '''


print(f'result {div()}')