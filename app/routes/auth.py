from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash

from app.database import get_connection


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form.get("usuario", "").strip()
        password = request.form.get("password", "")

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT
                u.id,
                u.nombre,
                u.usuario,
                u.password,
                u.activo,
                r.nombre AS rol
            FROM usuarios u
            INNER JOIN roles r
                ON u.rol_id = r.id
            WHERE u.usuario = %s
            """,
            (usuario,)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user is None:
            return render_template(
                "auth/login.html",
                error="Usuario o contraseña incorrectos."
            )

        if not user["activo"]:
            return render_template(
                "auth/login.html",
                error="El usuario se encuentra desactivado."
            )

        if not check_password_hash(user["password"], password):
            return render_template(
                "auth/login.html",
                error="Usuario o contraseña incorrectos."
            )

        session["usuario_id"] = user["id"]
        session["nombre"] = user["nombre"]
        session["usuario"] = user["usuario"]
        session["rol"] = user["rol"]

        return redirect(url_for("auth.dashboard"))

    return render_template("auth/login.html")


@auth.route("/dashboard")
def dashboard():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template(
        "auth/dashboard.html",
        nombre=session["nombre"],
        rol=session["rol"]
    )


@auth.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))