#!/bin/bash

echo "El script eliminara contenedores antiguos del proyecto. ¿Continuar? (s/n): "
read -r confirm
if [[ "$confirm" != "s" && "$confirm" != "S" ]]; then
    exit 1
fi

docker compose down -v --remove-orphans

docker compose build
docker compose up -d

echo "Esperando a que la base de datos esté lista..."
docker compose exec ceragon-backend sh -c 'until nc -z db 3306; do sleep 1; done'


docker compose exec ceragon-backend python manage.py migrate

echo "Ejecutando tests..."
docker compose exec ceragon-backend pytest
if [[ $? -ne 0 ]]; then
  echo "Tests fallaron. Abortando despliegue."
  exit 1
fi

echo "Cargando datos iniciales..."
docker compose exec ceragon-backend python manage.py populate_data

echo "¿Querés crear un superusuario para el admin? (s/n): "
read -r create_admin
if [[ "$create_admin" == "s" || "$create_admin" == "S" ]]; then
    docker compose exec ceragon-backend python manage.py createsuperuser
else
    echo "Superusuario no creado."
fi

echo "Despliegue finalizado correctamente."
echo "Accedé a la app en: http://localhost:8000"
echo "Accedé al admin en http://localhost:8000/admin/"
echo "Accedé a la documentación de la API en http://localhost:8000/swagger/"