# Plataforma de Noticias - Backend 

Sistema de gestión de publicaciones periodísticas enfocado en la administración de artículos, autores y categorías. Este proyecto digitaliza el flujo de trabajo de un medio digital, permitiendo mantener un registro histórico y auditable de los estados de cada publicación. Desarrollado para la asignatura de Programación Backend en INACAP.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Framework:** Django
* **Base de Datos:** SQLite (entorno de desarrollo) / MariaDB (producción)
* **Herramientas:** Entorno virtual (venv), Git, VS Code en Linux

## 🚀 Instalación y Uso (Entorno Linux)

Sigue estos pasos para levantar el entorno de desarrollo de manera local:

1. Clonar este repositorio:
   `git clone https://github.com/martingabrieldroguett/plataforma-noticias-backend.git`
2. Ingresar al directorio del proyecto:
   `cd plataforma-noticias-backend`
3. Crear y activar el entorno virtual (usando Bash o Fish):
   `python -m venv ambiente_noticias`
   `source ambiente_noticias/bin/activate.fish`
4. Instalar las dependencias de Django:
   `pip install django`
5. Aplicar las migraciones a la base de datos:
   `python manage.py migrate`
6. Iniciar el servidor local:
   `python manage.py runserver`

## ⚙️ Características Principales

* **Panel de Administración Segurizado:** Gestión completa (CRUD) de Autores, Categorías y Noticias directamente desde `/admin/`.
* **Vistas Personalizadas:** Interfaz de bienvenida en la raíz del sitio y manejo global de errores para enlaces rotos (Error 404).
* **Auditoría de Estados:** Control estricto del ciclo de vida de los artículos periodísticos (Borrador, Publicado, Archivado).
