from database import USERS_COLLECTION
from auth import get_password_hash

def user_exists(username):
    existing_user = USERS_COLLECTION.find_one({"username": username})
    if existing_user:
        return True

def create_user(username,password, role='user'):
    # Verificar si el usuario ya existe
    existing_user = user_exists(username)
    if existing_user:
        print("The user already exists.")
        return

    hashed_password = get_password_hash(password)

    new_user = {
        "username": username,
        "hashed_password": hashed_password,
        "role": role
    }

    USERS_COLLECTION.insert_one(new_user)
    print(f"Usuario con rol {role} creado exitosamente.")

create_user("tester","1234","tester")
