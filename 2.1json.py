import csv
import os


def print_employees_over_30(csv_file):
    if not os.path.exists(csv_file):
        print(f"Файл не найден по пути: {os.path.abspath(csv_file)}")
        return

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    age = int(row['Возраст'])
                    if age > 30:
                        print(row['Имя'])
                except ValueError:
                    continue
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


print_employees_over_30('employees.csv')
