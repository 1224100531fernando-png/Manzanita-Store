from app.database import get_connection


def obtener_productos():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT
            id,
            nombre,
            descripcion,
            precio,
            stock,
            stock_minimo
        FROM productos
        ORDER BY id DESC
        """
    )

    productos = cursor.fetchall()

    cursor.close()
    connection.close()

    return productos


def crear_producto(
    nombre,
    descripcion,
    precio,
    stock,
    stock_minimo
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO productos
        (
            nombre,
            descripcion,
            precio,
            stock,
            stock_minimo
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            nombre,
            descripcion,
            precio,
            stock,
            stock_minimo
        )
    )

    connection.commit()

    cursor.close()
    connection.close()
    