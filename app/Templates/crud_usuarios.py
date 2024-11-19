import httpx
import requests

items = []

async def preload_items():
    global items
    print("Preload items...........................")
    items = await get_item1()
    return items

async def get_item1():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://127.0.0.1:8080/Usuariosockets/index")
        print(f"Entra a listar 1 {response.status_code}")

        if response.status_code == 200:
            users = response.json()
            print(f"Entra a listar{users}")

            data = response.json()
            return [{"id": user["id"], 
                     "nombre": user["nombre"],
                     "apellido": user["apellido"],
                     "celular": user["celular"],
                     "correo": user["correo"],
                     "password_hash": user["password_hash"],
                     "fecha_nacimiento": user["fecha_nacimiento"],
                     "rol": user["rol"]} 
                    for user in data]
        
        else:
            print("Error al obtener los datos:", response.status_code)
            return []
    except Exception as e:
        print("Error en la conexión:", e)
        return []
    
async def create_user(nombre, password_hash, celular, correo, apellido, fecha_nacimiento, rol):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("http://127.0.0.1:8080/Usuariosockets/add", json={"nombre":nombre, "password_hash": password_hash, "apellido": apellido, "correo": correo, "celular": celular, "fecha_nacimiento": fecha_nacimiento, "rol": rol})
        
        if response.status_code == 201:
            print("Usuario creado:", response.json())
        else:
            print("Error al crear el usuario:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)

async def update_user(user_id, new_nombre, new_password, new_apellido, new_celular, new_correo, new_nacimiento, new_rol):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(f"http://127.0.0.1:8080/Usuariosockets/update{user_id}", json={"nombre": new_nombre, "password": new_password, "apellido": new_apellido, "celular": new_celular, "correo": new_correo, "fecha_nacimiento": new_nacimiento, "rol": new_rol})
        
        if response.status_code == 200:
            print("Usuario actualizado:", response.json())
        else:
            print("Error al actualizar el usuario:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)

async def delete_user(user_id):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://127.0.0.1:8080/Usuariosockets/delete/{user_id}")
        
        if response.status_code == 200:
            print("Usuario eliminado:", response.json())
        else:
            print("Error al eliminar el usuario:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)


def get_items():
    return items

def add_item(item):
    items.append(item)
    
def edit_item(index, new_item):
    items[index] = new_item

def delete_item(index):
    items.pop(index)
