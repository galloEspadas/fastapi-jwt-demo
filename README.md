# 🚀 FastAPI JWT + MongoDB Demo

API de autenticación simple construida con **FastAPI**, **MongoDB**, **Motor**, **Passlib** y **JWT**.  
Incluye registro, inicio de sesión, generación de tokens de acceso y endpoints protegidos.

---

## 📦 Tecnologías usadas
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web rápido para Python.
- [MongoDB](https://www.mongodb.com/) - Base de datos NoSQL.
- [Motor](https://motor.readthedocs.io/) - Driver async para MongoDB.
- [Passlib](https://passlib.readthedocs.io/) - Hash de contraseñas.
- [Python-JOSE](https://python-jose.readthedocs.io/) - Generación y validación de JWT.

---

## ⚙️ Instalación y uso

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/TU-USUARIO/fastapi-jwt-demo.git
cd fastapi-jwt-demo
```

### 2️⃣ Instalar dependencias
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Configurar variables de entorno

Edita el archivo `.env` con tus credenciales de MongoDB:

```env
MONGO_URI="mongodb+srv://usuario:contraseña@cluster.mongodb.net/?retryWrites=true&w=majority"
MONGO_DB_NAME="nombre_de_tu_db"
```

### 4️⃣ Ejecutar la API

```bash
uvicorn app.main:app --reload
```

---

## 🛣️ Endpoints principales

- `POST /auth/register` — Registro de usuario (requiere `username` y `password`)
- `POST /auth/login` — Login y obtención de token JWT
- `GET /protected` — Endpoint protegido, requiere token JWT
- `GET /users` — Listado de usuarios registrados (protegido)

---

## 🔒 Autenticación

La autenticación se realiza mediante JWT.  
Incluye protección de rutas usando el esquema Bearer.

---

## 🗄️ Estructura del proyecto

```
app/
    ├── auth.py         # Endpoints de autenticación
    ├── config.py       # Configuración de JWT
    ├── crud.py         # Operaciones con la base de datos
    ├── database.py     # Conexión a MongoDB
    ├── main.py         # Inicialización de FastAPI y rutas
    ├── schemas.py      # Modelos Pydantic
    └── utils.py        # Utilidades (hash, JWT, autenticación)
.env                    # Variables de entorno
requirements.txt        # Dependencias
users.db                # (No usado, puedes eliminarlo si solo usas MongoDB)
```

---

## 📬 Prueba con cURL

```bash
# Registro
curl -X POST http://localhost:8000/auth/register -H "Content-Type: application/json" -d '{"username":"usuario","password":"clave"}'

# Login
curl -X POST http://localhost:8000/auth/login -H "Content-Type: application/json" -d '{"username":"usuario","password":"clave"}'

# Acceso a endpoint protegido
curl -X GET http://localhost:8000/protected -H "Authorization: Bearer TU_TOKEN"
```

---

## 📝 Licencia

Este proyecto está bajo la licencia Apache