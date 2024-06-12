# src/utils/database.py
import json
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '../database.json')

def load_users():
    if not os.path.exists(DATABASE_PATH):
        return []
    with open(DATABASE_PATH, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(DATABASE_PATH, 'w') as file:
        json.dump(users, file)
