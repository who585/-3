import json
import csv# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open(INPUT_FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        with open("output.json", "w") as m:
            for row in reader:
                json_data = json.dump(row,m, indent = 4)
        return json_data
        # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


for row in task():
    json_data += ','.join(row) + '\n'

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
