import json

def get_user_info():
    with open("data/user.json", "r") as file:
        user_info = json.load(file)
        return user_info