import json
import os

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def signup_user(email, password):
    users = load_users()
    if email in users:
        return False
    users[email] = {"password": password, "data": []}
    save_users(users)
    return True

def login_user(email, password):
    users = load_users()
    return users.get(email, {}).get("password") == password