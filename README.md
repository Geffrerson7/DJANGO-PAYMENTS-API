# DJANGO-PAYMENTS-API

## Description
API de pagos de servicios de streaming. Tiene las funcionalidades de crear pagos y registrar automáticamente si es que está vencido, crear y actualizar servicios de streaming y crear un usuario con foto de perfil.

## Run Locally

Clonar el repositorio

```bash
 $ git clone https://github.com/Geffrerson7/DJANGO-PAYMENTS-API.git
```

Ir al directorio al proyecto

```bash
 $ cd DJANGO-PAYMENTS-API
```

Crear un entorno virtual

```sh
$ virtualenv venv
```

Activar el entorno virtual
```sh
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Luego, realizamos las migraciones.
```sh
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app
```sh
(env)$ python manage.py runserver
```
Y navegar a
```sh
http://127.0.0.1:8000/
```

* **Python** (v. 3.10.7) [Source](https://www.python.org/)
* **Django** (v. 4.1.7)  [Source](https://www.djangoproject.com/)
* **Django Rest Framework** (v. 3.14.0) [Source](https://www.django-rest-framework.org/)
* **django-cors-headers** (v. 3.14.0) [Source](https://pypi.org/project/django-cors-headers/)
* **drf-yasg** (v. 1.21.5) [Source](https://drf-yasg.readthedocs.io/en/stable/)
* **gunicorn** (v. 20.1.0) [Source](https://gunicorn.org/)
* **whitenoise** (v. 6.4.0) [Source](https://whitenoise.readthedocs.io/en/latest/)
* **Render**  [Source](https://render.com/docs/deploy-django)
## Documentación
Para la documentación del proyecto se utilizó Swagger por su capacidad para generar documentación dinámica y en tiempo real de los servicios web que se están construyendo.
La documentación del projecto en swagger está en este [Link](https://payments-api-yf4q.onrender.com/swagger/)


## Author
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)