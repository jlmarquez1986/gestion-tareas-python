### App de Gestión de Tareas

### Autor: José Luis Márquez García 

### Curso: Programación en Python (Tokio School) 

### Fecha: 25/06/2025

--- 
### 📝 Descripción General

Esta aplicación es una herramienta de escritorio diseñada para ayudar a los usuarios a organizar sus flujos de trabajo mediante la creación y categorización de tareas con fechas límite. Permite un control total sobre las actividades pendientes, ofreciendo una interfaz visual intuitiva para gestionar el día a día de forma eficiente.

### ✨ Características Principales

* **Gestión de Tareas:** Permite escribir tareas, asignarles una categoría y establecer fechas límite.


* **Categorización Personalizada:** Organización por categorías como Trabajo, Estudio, Personal y Otros.


* **Control de Estado:** Funcionalidad para marcar tareas como realizadas, editarlas o eliminarlas definitivamente.


* **Persistencia de Datos:** Conexión a una base de datos local SQLite para asegurar que la información no se pierda al cerrar la app.


* **Interfaz Dinámica:** Listado de tareas actualizado en tiempo real en la parte inferior de la pantalla.

### 🛠️ Stack Tecnológico

* **Lenguaje:** Python.
  
* **Base de Datos: SQLite** (Motor de base de datos relacional estándar).
  
* **Gestión de Datos: DB Browser for SQLite** (Herramienta utilizada para el diseño, edición y depuración de la estructura de las tablas).

* **Interfaz Gráfica:** Tkinter / CustomTkinter.

### 📊 Estructura de la Base de Datos

La aplicación utiliza dos tablas principales para organizar la información:


* **Tabla categoria:** Almacena los tipos de tareas (id, nombre).


* **Tabla tarea:** Contiene el detalle de las actividades (id, contenido, hecha, fecha_limite, categoria_id).

### 🚀 Instalación y Ejecución

1. Clona el repositorio:
   git clone https://github.com/jlmarquez1986/gestion-tareas-python.git

2. Instala las dependencias necesarias (si utilizas librerías externas):
   pip install -r requirements.txt

3. Ejecuta la aplicación:
   python main.py


### 🏆 Conclusiones y Aprendizajes

Este proyecto me ha permitido profundizar en:

* El diseño de interfaces gráficas funcionales en Python.

* La implementación de operaciones **CRUD** (Crear, Leer, Actualizar, Borrar) sobre una base de datos SQL.

* La lógica de manejo de fechas y estados booleanos para el control de tareas completadas.

**🎓 Contexto Académico**

Este proyecto ha sido desarrollado como parte práctica del **Módulo 4: Manipulación y Almacenamiento de Datos** del Curso Superior de Programación con Python en **Tokio School. Objetivo:** Aplicar conocimientos de persistencia de datos y gestión de bases de datos relacionales en una aplicación real.
   

