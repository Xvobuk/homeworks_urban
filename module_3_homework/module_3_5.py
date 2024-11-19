def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

# Валидация:
    if first == 0:
        if len(str_number) > 1:
            return get_multiplied_digits(int(str_number[1:]))
        else:
            return 1

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

#Проверяем разные значения
result_1 = get_multiplied_digits(40203)
result_2 = get_multiplied_digits(88005553535)
result_3 = get_multiplied_digits(240)

print(result_1)
print(result_2)
print(result_3)
