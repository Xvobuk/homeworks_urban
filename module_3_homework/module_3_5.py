def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

try:
    result_3 = get_multiplied_digits('Абоба') # В такие программы можно добавлять исключения, но мы ещё их не прошли)))
except:
    result = get_multiplied_digits(40203)
    result_2 = get_multiplied_digits(88005553535)

    print(result)
    print(result_2)
