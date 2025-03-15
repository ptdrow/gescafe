from database import DB
from auth import get_password_hash

USERS_COLLECTION = DB["users"]

def create_admin_user(password):
    username = "admin"

    # Verificar si el usuario ya existe
    existing_user = USERS_COLLECTION.find_one({"username": username})
    if existing_user:
        print("The user already exists.")
        return

    hashed_password = get_password_hash(password)

    new_user = {
        "username": username,
        "hashed_password": hashed_password,
        "role": "admin"
    }

    USERS_COLLECTION.insert_one(new_user)
    print("Usuario administrador creado exitosamente.")

create_admin_user("my_super_password")
