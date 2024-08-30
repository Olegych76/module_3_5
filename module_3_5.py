# определяем функцию:
def get_multiplied_digits(num):
    str_num = str(num)  # переводим число в строку, чтобы обращаться к цифрам по индексу
    first = int(str_num[0])  # извлекаем первую цифру числа

    if len(str_num) > 1:  # проверяем, содержит ли строка `str_num` более одной цифры
        # если да, то возвращаем произведение первой цифры и результата рекурсивного вызова функции
        # для оставшейся части числа:
        return first * get_multiplied_digits(int(str_num[1:]))
    #  если нет, возвращаем самое число first:
    else:
        return first


str_ = '40902080305'
print(get_multiplied_digits(str_))  # результат поразрядного умножения цифр строки '40902080305'
