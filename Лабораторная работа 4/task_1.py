import json

FILENAME = "input.json"

# TODO решите задачу
def task() -> float:
    count = 0
    with open(FILENAME) as f:
        json_data = json.load(f)
    count = sum([dict_["score"] * dict_["weight"] for dict_ in json_data])
    return round(count, 3)


print(task())
