import json
from methods import load_file, save_file, delete_file, empty_file



data = {
    "name": "Milica",
    "age": 29,
    "height": 167,
    "gender": "female"
}



delete_file("data/test.json")

empty_file("data/user.json")