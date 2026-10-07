from app.database import get_connection


connection = get_connection()
cursor = connection.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS productos (

        id INT AUTO_INCREMENT PRIMARY KEY,

        nombre VARCHAR(100) NOT NULL,

        descripcion VARCHAR(255),

        precio DECIMAL(10,2) NOT NULL,

        stock INT NOT NULL DEFAULT 0,

        stock_minimo INT NOT NULL DEFAULT 5

    )
    """
)


connection.commit()

cursor.close()
connection.close()


print("Tabla productos creada correctamente.")
