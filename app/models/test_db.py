from app.database import get_connection


connection = get_connection()

print("Conexión a MySQL exitosa")

connection.close()