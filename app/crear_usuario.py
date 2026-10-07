from werkzeug.security import generate_password_hash

from app.database import get_connection


password = generate_password_hash("Admin123")

connection = get_connection()

cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO usuarios
    (
        nombre,
        usuario,
        password,
        rol_id
    )
    VALUES (%s, %s, %s, %s)
    """,
    (
        "Administrador Principal",
        "admin",
        password,
        1
    )
)

connection.commit()

cursor.close()
connection.close()

print("Usuario administrador creado correctamente.")