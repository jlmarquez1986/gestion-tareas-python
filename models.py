import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship

'''
Creamos una clase llamada Tarea
Esta clase va a ser nuestro modelo de datos de la tarea (el cual nos servirá
luego para la base de datos)
Esta clase va a almacenar toda la información referente a una tarea
'''

# Clase TAREA
class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True) # Identificador único de cada tarea (no puede haber dos tareas con el mismo id, por eso es primary key)
    contenido = Column(String(200), nullable=False) # Contenido de la tarea, un texto de máximo 200 caracteres
    hecha = Column(Boolean) # Booleano que indica si una tarea ha sido hecha o no
    fecha_limite = Column(Date, nullable = True) # Nueva columna para la fecha límite, puede ser nula
    # Agregamos la clave foránea para la relación con Categoria
    categoria_id = Column(Integer, ForeignKey('categoria.id'), nullable=True)
    # Definimos la relación con Categoria
    categoria_obj = relationship("Categoria", back_populates="tareas")

    def __init__(self, contenido, hecha, categoria_id=None, fecha_limite=None):
    # Recordemos que el id no es necesario crearlo manualmente, lo añade la base de datos automaticamente
        self.contenido = contenido
        self.hecha = hecha
        self.categoria_id = categoria_id # Asignamos el valor de categoria_id
        self.fecha_limite = fecha_limite  # Asignamos el valor de fecha_limite

    def __repr__(self):
        # Asegurarse de que fecha_limite no es None antes de formatear
        fecha_str = self.fecha_limite.strftime("%Y-%m-%d") if self.fecha_limite else "Sin fecha"
        return "Tarea {}: {} ({}) - Fecha Límite: {}".format(self.id, self.contenido, self.hecha, fecha_str)

    def __str__(self):
        fecha_str = self.fecha_limite.strftime("%Y-%m-%d") if self.fecha_limite else "Sin fecha"
        return "Tarea {}: {} ({}) - Fecha Límite: {}".format(self.id, self.contenido, self.hecha, fecha_str)

# Clase CATEGORÍA

class Categoria(db.Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    # Definimos la relación inversa con Tarea
    tareas = relationship("Tarea", back_populates="categoria_obj")

    def __repr__(self):
        return f"Categoría {self.id}: {self.nombre}"

    def __init__(self, nombre):
        self.nombre = nombre