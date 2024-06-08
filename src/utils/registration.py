import json
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '../database.json')

def register_user(name, email, tickets):
    users = load_users()
    user_id = len(users) + 1
    user = {'id': user_id, 'name': name, 'email': email, 'tickets': tickets}
    users.append(user)
    save_users(users)
    return user

def get_user_by_email(email):
    users = load_users()
    for user in users:
        if user['email'] == email:
            return user
    return None

def load_users():
    if not os.path.exists(DATABASE_PATH):
        return []
    with open(DATABASE_PATH, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(DATABASE_PATH, 'w') as file:
        json.dump(users, file)
