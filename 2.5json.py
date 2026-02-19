import csv
import json


def convert_csv_to_json(csv_path: str, json_path: str) -> None:

    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        print(f"Конвертация завершена: {csv_path} -> {json_path}")
    except Exception as e:
        print(f"Ошибка при конвертации CSV в JSON: {e}")


def convert_json_to_csv(json_path: str, csv_path: str) -> None:

    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        if not data:
            print("JSON-файл пуст, CSV не создан.")
            return

        headers = data[0].keys()

        with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"Конвертация завершена: {json_path} -> {csv_path}")
    except Exception as e:
        print(f"Ошибка при конвертации JSON в CSV: {e}")


convert_csv_to_json('animals.csv', 'animals.json')
convert_json_to_csv('animals.json', 'animals_new.csv')
