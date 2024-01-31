import json# TODO решите задачу
FILENAME = "input.json"
def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)
        x = [i["score"]*i["weight"] for i in data]
        summ = round(sum(x), 4)

        return summ
print(task())
