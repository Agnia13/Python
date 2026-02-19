LEVELS = (
    (1, "Комната с ключами", "Вы в маленькой комнате. На полу разбросаны ключи. В северной стене видна дверь."),
    (2, "Зал призрака", "Перед вами огромный зал. В центре парит призрачная фигура. В углу стоит старый сундук."),
    (3, "Комната загадок", "Вы в каменной комнате. На стене висит табличка с загадкой. Напротив – массивная дверь с кодовым замком.")
)

ITEM_DESCRIPTIONS = {
    "железный ключ": "Простой железный ключ, возможно от двери.",
    "серебряный ключ": "Изящный серебряный ключ, покрытый патиной.",
    "золотой ключ": "Маленький золотой ключик, блестит даже в темноте.",
    "амулет": "Священный амулет с изображением солнца. Он излучает слабое свечение.",
    "бумажка": "Клочок бумаги с числом 371."
}

MONSTERS = {
    "призрак": "амулет"
}

DOOR_CODES = {
    3: 371
}

inventory = []
collected_keys = set()
current_level = 1
game_running = True
monster_defeated = False
door_open = False

def show_help():
    print("\nДоступные команды:")
    print("  осмотреться         – осмотреть текущую локацию")
    print("  взять [предмет]     – поднять предмет")
    print("  инвентарь           – показать содержимое инвентаря")
    print("  использовать [предм]– применить предмет")
    print("  идти                – перейти в следующую локацию (если возможно)")
    print("  помощь              – показать эту подсказку")
    print("  выход               – завершить игру\n")

def show_inventory():
    if inventory:
        print("\nВаш инвентарь:")
        for item in inventory:
            print(f"  - {item}: {ITEM_DESCRIPTIONS.get(item, 'Нет описания.')}")
    else:
        print("\nИнвентарь пуст.")

def take_item(item_name):
    global collected_keys
    print("Неизвестная команда 'взять' в данном контексте.")

def use_item(item_name):
    global monster_defeated, door_open, game_running
    if item_name not in inventory:
        print(f"У вас нет предмета '{item_name}'.")
        return

    if current_level == 2 and item_name == MONSTERS.get("призрак"):
        if not monster_defeated:
            print("Вы поднимаете амулет над головой. Призрак вскрикивает и исчезает в облаке дыма!")
            inventory.remove(item_name)
            monster_defeated = True
        else:
            print("Призрак уже побеждён.")
    elif current_level == 3 and item_name == "бумажка":
        print("На клочке бумаги написано число 371. Похоже, это код от двери.")
    else:
        print("Нельзя применить этот предмет сейчас.")

def level1():
    global current_level, door_open, collected_keys, inventory, game_running
    print(f"\n=== Уровень {LEVELS[0][0]}: {LEVELS[0][1]} ===")
    print(LEVELS[0][2])
    keys_in_room = {"железный ключ", "серебряный ключ", "золотой ключ"}

    while current_level == 1 and game_running:
        command = input("\n> ").strip().lower()
        if command == "осмотреться":
            print("Вы видите три ключа, лежащих на полу: железный, серебряный и золотой.")
            if collected_keys:
                print(f"Вы уже подобрали: {', '.join(collected_keys)}.")
            else:
                print("Вы пока ничего не брали.")
            print("Дверь на севере закрыта.")
        elif command.startswith("взять "):
            item = command[5:].strip()
            if item in keys_in_room and item not in collected_keys:
                print(f"Вы подобрали {item}.")
                collected_keys.add(item)
                inventory.append(item)
                print(f"Теперь у вас есть {item}.")
            elif item in collected_keys:
                print("Этот ключ вы уже взяли.")
            else:
                print("Здесь нет такого предмета.")
        elif command == "инвентарь":
            show_inventory()
        elif command.startswith("использовать "):
            item = command[12:].strip()
            use_item(item)
        elif command == "идти":
            if collected_keys == keys_in_room:
                print("Вы вставляете все три ключа в замок. Дверь со скрежетом открывается!")
                door_open = True
                current_level = 2
                print("Вы переходите в следующий зал...")
            else:
                print("Дверь заперта. Похоже, нужны все три ключа.")
        elif command == "помощь":
            show_help()
        elif command == "выход":
            game_running = False
            break
        else:
            print("Неизвестная команда. Введите 'помощь' для списка команд.")

def level2():
    global current_level, monster_defeated, inventory, game_running
    print(f"\n=== Уровень {LEVELS[1][0]}: {LEVELS[1][1]} ===")
    print(LEVELS[1][2])
    amulet_taken = False

    while current_level == 2 and game_running:
        command = input("\n> ").strip().lower()
        if command == "осмотреться":
            print("В центре зала парит призрачная фигура. В углу стоит старый деревянный сундук.")
            if monster_defeated:
                print("Призрак исчез, теперь ничто не мешает пройти дальше.")
            else:
                print("Призрак покачивается в воздухе, как будто ждёт ваших действий.")
        elif command == "открыть сундук":
            if not amulet_taken:
                print("Вы открываете сундук и находите внутри старинный амулет!")
                amulet_taken = True
                inventory.append("амулет")
                print("Амулет добавлен в инвентарь.")
            else:
                print("Сундук уже открыт и пуст.")

        elif command == "инвентарь":
            show_inventory()
        elif command.startswith("использовать "):
            item = command[12:].strip()
            use_item(item)
        elif command == "идти":
            if monster_defeated:
                print("Вы проходите через зал и подходите к двери на востоке. Она ведёт дальше.")
                current_level = 3
            else:
                print("Призрак преграждает путь. Надо что-то сделать с ним.")
        elif command == "помощь":
            show_help()
        elif command == "выход":
            game_running = False
            break
        else:
            print("Неизвестная команда.")

def level3():
    global current_level, door_open, game_running, inventory
    print(f"\n=== Уровень {LEVELS[2][0]}: {LEVELS[2][1]} ===")
    print(LEVELS[2][2])
    hint_taken = False

    while current_level == 3 and game_running:
        command = input("\n> ").strip().lower()
        if command == "осмотреться":
            print("На стене табличка с загадкой:\n"
                  " 'Число, что меньше ста, но больше трёх,\n"
                  "  Если его перевернуть – получишь 173.'\n"
                  "Рядом дверь с кодовым замком, требующим трёхзначный код.\n"
                  "На полу лежит бумажка.")
            if "бумажка" in inventory:
                print("У вас есть клочок бумаги с числом 371.")
        elif command.startswith("взять "):
            item = command[5:].strip()
            if item == "бумажка" and not hint_taken:
                print("Вы замечаете на полу обрывок бумаги и поднимаете его.")
                inventory.append("бумажка")
                hint_taken = True
            elif item == "бумажка" and hint_taken:
                print("Вы уже взяли подсказку.")
            else:
                print("Здесь нет такого предмета.")
        elif command == "инвентарь":
            show_inventory()
        elif command.startswith("использовать "):
            item = command[12:].strip()
            use_item(item)
        elif command == "идти":
            if door_open:
                print("Вы выходите через открытую дверь и оказываетесь снаружи замка. Поздравляем, вы выбрались!")
                print("Игра пройдена!")
                game_running = False
            else:
                print("Дверь заперта на кодовый замок.")
        elif command.isdigit() and len(command) == 3:
            code_attempt = int(command)
            if code_attempt == DOOR_CODES[3]:
                print("Замок щёлкает, дверь открывается!")
                door_open = True
            else:
                print("Неверный код. Замок не реагирует.")
        elif command == "помощь":
            show_help()
        elif command == "выход":
            game_running = False
            break
        else:
            print("Неизвестная команда.")

def main():
    print("=" * 50)
    print("         Добро пожаловать в замок!")
    print("=" * 50)
    print("Вы оказались в древнем замке. Нужно выбраться наружу.")
    show_help()

    global game_running
    while game_running:
        if current_level == 1:
            level1()
        elif current_level == 2:
            level2()
        elif current_level == 3:
            level3()
        else:
            break

    print("\nСпасибо за игру!")

main()