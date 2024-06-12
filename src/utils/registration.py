# src/utils/registration.py
from utils.database import load_users, save_users

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
