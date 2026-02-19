import csv

header = ['Животное', 'Среда обитания']
rows = [
    ['Медведь', 'Лес'],
    ['Дельфин', 'Океан'],
    ['Верблюд', 'Пустыня']
]

with open('animals.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("Файл animals.csv успешно создан.")
