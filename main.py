from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea, Categoria
import datetime # Importamos el módulo datetime

app = Flask(__name__)  # En app se encuentra nuestro servidor web de Flask

# Raiz ("/") - index.html
@app.route("/")
def home():
    todas_las_tareas = db.session.query(Tarea).all() # Consultamos y almacenamos todas las tareas de la base de datos
    todas_las_categorias = db.session.query(Categoria).all()
    print(todas_las_tareas)
    # No pasamos tarea_a_editar por defecto, ya que es la vista principal de creación
    return render_template("index.html", lista_de_tareas = todas_las_tareas, lista_de_categorias = todas_las_categorias ) # Se carga el template index.html

# Nueva ruta para mostrar el formulario de edición
@app.route("/editar-tarea/<id>")
def editar(id):
    tarea_a_editar = db.session.query(Tarea).filter_by(id=int(id)).first()
    if not tarea_a_editar:
        # Si la tarea no existe, redirigir a la página principal o mostrar un error
        return redirect(url_for("home"))

    todas_las_tareas = db.session.query(Tarea).all()
    todas_las_categorias = db.session.query(Categoria).all()
    # Pasamos la tarea_a_editar al template para pre-rellenar el formulario
    return render_template("index.html",
                           lista_de_tareas = todas_las_tareas,
                           lista_de_categorias = todas_las_categorias,
                           tarea_a_editar = tarea_a_editar)

@app.route("/crear-tarea", methods=["POST"])
def crear():
    contenido = request.form["contenido_tarea"]
    categoria = request.form.get("categoria_tarea", None)
    fecha_limite_str = request.form.get("fecha_limite_tarea", None) # Obtenemos la fecha como string

    fecha_limite = None
    if fecha_limite_str: # Si se proporcionó una fecha, la convertimos a objeto date
        try:
            fecha_limite = datetime.datetime.strptime(fecha_limite_str, "%Y-%m-%d").date()
        except ValueError:
            # Aquí podrías manejar el error si el formato de la fecha no es correcto
            print(f"Advertencia: Formato de fecha inválido para: {fecha_limite_str}")

    print(f"Tarea: {contenido}, Categoría: {categoria}, Fecha Límite: {fecha_limite}")

    tarea = Tarea(
        contenido=contenido,
        hecha=False,
        categoria_id = int(categoria) if categoria else None,
        fecha_limite = fecha_limite # Pasamos la fecha límite al constructor
    )
    db.session.add(tarea)  # Añadir el objeto de Tarea a la base de datos
    db.session.commit()  # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for("home")) # Esto nos redirecciona a la función home()

# Nueva ruta para actualizar una tarea existente
@app.route("/actualizar-tarea/<id>", methods=["POST"])
def actualizar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    if not tarea:
        return redirect(url_for("home")) # Tarea no encontrada

    tarea.contenido = request.form["contenido_tarea"]
    categoria = request.form.get("categoria_tarea", None)
    tarea.categoria_id = int(categoria) if categoria else None

    fecha_limite_str = request.form.get("fecha_limite_tarea", None)
    tarea.fecha_limite = None # Resetear por si se vacía el campo
    if fecha_limite_str:
        try:
            tarea.fecha_limite = datetime.datetime.strptime(fecha_limite_str, "%Y-%m-%d").date()
        except ValueError:
            print(f"Advertencia: Formato de fecha inválido para: {fecha_limite_str} en actualización")

    db.session.commit()
    return redirect(url_for("home"))


@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    db.session.query(Tarea).filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    db.Base.metadata.create_all(bind=db.engine) # Creamos el modelo de datos

    # Crear algunas categorías si no existen
    if db.session.query(Categoria).count() == 0:
        categorias = ["Trabajo", "Estudio", "Personal", "Otros"]
        for nombre in categorias:
            db.session.add(Categoria(nombre=nombre))
        db.session.commit()

    app.run(debug=True)



