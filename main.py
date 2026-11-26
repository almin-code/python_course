import json

with open("data/user.json", "r") as file:
    data = json.load(file)
    data.append({
        "name": "Marko Markovic",
        "age": 30,
        "height": 189,
        "gender": "male"
    })

with open("data/user.json", "w") as file:
    json.dump(data, file, indent=4)

    print(data)