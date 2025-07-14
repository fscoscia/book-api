# Api de libros y autores

Proyecto de ejemplo con Django, MySQL y Docker.
Incluye API para gestión de libros y autores, administración vía Django Admin y pruebas automatizadas.

## Requisitos

-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

## Instalación y despliegue

1. Clonar el repositorio:

2. Crear archivo .env con las variables de entorno necesarias:

    ```bash
    DEBUG=True
    SECRET_KEY=supersecretkey
    ALLOWED_HOSTS=localhost,127.0.0.1
    DB_NAME=dbname
    DB_USER=dbuser
    DB_PASSWORD=dbpassword
    DB_ROOT_PASSWORD=superrootpassword
    DB_HOST=db
    DB_PORT=3306
    ```

3. Ejecutar script de despliegue (asegurarse que tenga permisos de ejecución `chmod +x deploy.sh`):

    ```bash
    ./deploy.sh
    ```

## Estructura del proyecto

```bash
 ceragon/
 ├── core/                  # Aplicación principal con modelos, vistas y serializers
 ├── ceragon/               # Configuración Django (settings, urls, etc)
 ├── manage.py
 ├── Dockerfile
 ├── docker-compose.yml
 ├── deploy.sh              # Script  para desplegar la app
 ├── Pipfile
 ├── Pipfile.lock
 └── .env                   # Variables de entorno
```
