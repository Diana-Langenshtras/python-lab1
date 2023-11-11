# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as source, open(OUTPUT_FILENAME, "w") as destination:
        data = csv.DictReader(source, delimiter=",")
        json.dump(list(data), destination, indent=4, ensure_ascii=False)
        destination.close()
        source.close()

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
