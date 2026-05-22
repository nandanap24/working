import json

with open("data/sample.json", "r") as file:
    data = json.load(file)

print(data)
print(type(data))