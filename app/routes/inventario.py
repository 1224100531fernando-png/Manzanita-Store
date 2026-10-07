from flask import Blueprint, render_template, request, redirect, url_for, session

from app.models.producto import obtener_productos, crear_producto


inventario = Blueprint(
    "inventario",
    __name__,
    url_prefix="/inventario"
)


@inventario.route("/")
def lista():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    productos = obtener_productos()

    return render_template(
        "inventario/lista.html",
        productos=productos
    )


@inventario.route("/nuevo", methods=["GET", "POST"])
def nuevo():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        nombre = request.form.get("nombre", "").strip()
        descripcion = request.form.get("descripcion", "").strip()
        precio = request.form.get("precio")
        stock = request.form.get("stock")
        stock_minimo = request.form.get("stock_minimo")

        crear_producto(
            nombre,
            descripcion,
            precio,
            stock,
            stock_minimo
        )

        return redirect(
            url_for("inventario.lista")
        )

    return render_template(
        "inventario/nuevo.html"
    )
