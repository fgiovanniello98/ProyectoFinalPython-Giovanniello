# Proyecto Final (Django) — Blog de Páginas

Aplicación web estilo blog hecha con **Django** que incluye:
- Home, About (/about/), Pages (/pages/)
- CRUD completo de páginas (con **CKEditor** y **carga de imágenes**)
- Registro, login, logout
- Perfil de usuario con avatar/biografía y edición + cambio de contraseña
- Mensajería entre usuarios (bandeja de entrada/enviados)

> **Importante:** este repo NO incluye la base de datos `db.sqlite3` ni la carpeta `media/` (están en `.gitignore`).

## Requisitos
- Python 3.10+ recomendado
- pip

## Instalación y ejecución
```bash
# 1) Crear y activar entorno virtual (Windows)
python -m venv .venv
.venv\Scripts\activate

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Migraciones (crea la DB local)
python manage.py makemigrations
python manage.py migrate

# 4) Crear superusuario para el admin
python manage.py createsuperuser

# 5) Levantar servidor
python manage.py runserver
```

Abrí el navegador en:
- Home: `http://127.0.0.1:8000/`
- About: `http://127.0.0.1:8000/about/`
- Pages: `http://127.0.0.1:8000/pages/`
- Admin: `http://127.0.0.1:8000/admin/`
- Mensajes: `http://127.0.0.1:8000/mensajes/`
- Perfil: `http://127.0.0.1:8000/cuentas/perfil/`

## Funcionalidades clave
- Si no hay páginas disponibles, en `/pages/` se muestra **"No hay páginas aún"**.
- Para **crear/editar/borrar** páginas necesitás estar logueado.
- En el detalle de una página podés ver el contenido enriquecido (CKEditor) y la imagen.
- La app de **mensajería** permite enviar mensajes a otros usuarios y ver bandejas.

## Estructura del proyecto
- `paginas/`: modelo principal `Pagina` + CRUD
- `cuentas/`: registro/login/perfil + avatar/biografía + cambio de password
- `mensajeria/`: mensajes entre usuarios
- `templates/`: herencia de templates con `base.html` y navegación (NavBar)

## Video (entrega)
Grabá un video (máx 10 min) mostrando:
- Registro/Login/Logout
- Perfil + edición + cambio de password
- Listado de páginas + detalle + crear/editar/borrar
- Mensajes (enviar y ver bandeja)

Sugerencias: OBS, Free Cam, Filmora, etc.
