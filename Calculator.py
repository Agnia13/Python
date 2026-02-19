def get_number(prompt, num_type=float):
    while True:
        try:
            return num_type(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def get_int(prompt):
    return get_number(prompt, int)

def get_list(prompt):
    while True:
        try:
            raw = input(prompt)
            items = [int(x.strip()) for x in raw.split(',') if x.strip()]
            return items
        except ValueError:
            print("Ошибка: введите целые числа через запятую.")

def arithmetic():
    ops = {
        '1': ('+', lambda x, y: x + y),
        '2': ('-', lambda x, y: x - y),
        '3': ('*', lambda x, y: x * y),
        '4': ('/', lambda x, y: x / y),
        '5': ('//', lambda x, y: x // y),
        '6': ('%', lambda x, y: x % y),
        '7': ('**', lambda x, y: x ** y)
    }
    print("\nАрифметика")
    for k, (op, _) in ops.items():
        print(f"{k}. {op}")
    print("0. Назад")
    choice = input("Выберите оператор: ")
    if choice == '0':
        return
    if choice not in ops:
        print("Неверный выбор.")
        return
    a = get_number("Первый операнд: ")
    b = get_number("Второй операнд: ")
    try:
        if ops[choice][0] in ('/', '//', '%') and b == 0:
            print("Ошибка: деление на ноль.")
            return
        result = ops[choice][1](a, b)
        print(f"{a} {ops[choice][0]} {b} = {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

def comparison():
    ops = {
        '1': ('==', lambda x, y: x == y),
        '2': ('!=', lambda x, y: x != y),
        '3': ('>', lambda x, y: x > y),
        '4': ('<', lambda x, y: x < y),
        '5': ('>=', lambda x, y: x >= y),
        '6': ('<=', lambda x, y: x <= y)
    }
    print("\nСравнение")
    for k, (op, _) in ops.items():
        print(f"{k}. {op}")
    print("0. Назад")
    choice = input("Выберите оператор: ")
    if choice == '0':
        return
    if choice not in ops:
        print("Неверный выбор.")
        return
    a = get_number("Первый операнд: ")
    b = get_number("Второй операнд: ")
    try:
        result = ops[choice][1](a, b)
        print(f"{a} {ops[choice][0]} {b} = {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

def logical():
    ops = {
        '1': ('and', lambda x, y: x and y),
        '2': ('or', lambda x, y: x or y)
    }
    print("\nЛогика")
    print("1. and")
    print("2. or")
    print("3. not")
    print("0. Назад")
    choice = input("Выберите оператор: ")
    if choice == '0':
        return
    if choice == '3':
        a = input("Операнд: ")
        try:
            if a.replace('.', '', 1).replace('-', '', 1).isdigit():
                a = float(a)
            result = not a
            print(f"not {a} = {result}")
        except Exception as e:
            print(f"Ошибка: {e}")
    elif choice in ops:
        a = input("Первый операнд: ")
        b = input("Второй операнд: ")
        try:
            for v in (a, b):
                if v.replace('.', '', 1).replace('-', '', 1).isdigit():
                    v = float(v)
            result = ops[choice][1](a, b)
            print(f"{a} {ops[choice][0]} {b} = {result}")
        except Exception as e:
            print(f"Ошибка: {e}")
    else:
        print("Неверный выбор.")

def bitwise():
    ops = {
        '1': ('&', lambda x, y: x & y),
        '2': ('|', lambda x, y: x | y),
        '3': ('^', lambda x, y: x ^ y),
        '4': ('~', lambda x: ~x),
        '5': ('<<', lambda x, y: x << y),
        '6': ('>>', lambda x, y: x >> y)
    }
    print("\nПобитовые")
    for k, (op, _) in ops.items():
        print(f"{k}. {op}")
    print("0. Назад")
    choice = input("Выберите оператор: ")
    if choice == '0':
        return
    if choice not in ops:
        print("Неверный выбор.")
        return
    if choice == '4':
        a = get_int("Операнд: ")
        try:
            result = ops[choice][1](a)
            print(f"~{a} = {result}")
        except Exception as e:
            print(f"Ошибка: {e}")
    else:
        a = get_int("Первый операнд: ")
        b = get_int("Второй операнд: ")
        try:
            result = ops[choice][1](a, b)
            print(f"{a} {ops[choice][0]} {b} = {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

def membership():
    print("\nПринадлежность")
    print("1. in")
    print("2. not in")
    print("0. Назад")
    choice = input("Выберите оператор: ")
    if choice == '0':
        return
    elem = get_int("Элемент (целое число): ")
    lst = get_list("Список целых чисел через запятую: ")
    try:
        if choice == '1':
            result = elem in lst
            op = 'in'
        elif choice == '2':
            result = elem not in lst
            op = 'not in'
        else:
            print("Неверный выбор.")
            return
        print(f"{elem} {op} {lst} = {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

def identity():
    print("\nТождественность")
    print("1. is")
    print("2. is not")
    print("0. Назад")
    choice = input("Выберите оператор: ")
    if choice == '0':
        return
    a = input("Первый объект: ")
    b = input("Второй объект: ")
    try:
        if choice == '1':
            result = a is b
            op = 'is'
        elif choice == '2':
            result = a is not b
            op = 'is not'
        else:
            print("Неверный выбор.")
            return
        print(f"{a} {op} {b} = {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    categories = {
        '1': ("Арифметические", arithmetic),
        '2': ("Сравнения", comparison),
        '3': ("Логические", logical),
        '4': ("Побитовые", bitwise),
        '5': ("Принадлежности", membership),
        '6': ("Тождественности", identity)
    }
    while True:
        print("\nКАЛЬКУЛЯТОР")
        for k, (name, _) in categories.items():
            print(f"{k}. {name}")
        print("0. Выход")
        choice = input("Ваш выбор: ")
        if choice == '0':
            print("До свидания!")
            break
        if choice in categories:
            categories[choice][1]()
        else:
            print("Неверный выбор. Попробуйте снова.")

main()