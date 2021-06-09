import json
slownik = [["e","l","o"], ["e1", "l1", "o1"]]

with open("data_file.json", "w") as write_file:
    json.dump(slownik, write_file)

with open("data_file.json", "r") as write_file:
    x = list(json.load(write_file))
    print(x[1][2])
