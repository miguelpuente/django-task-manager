import os
from celery import Celery

# Establecer el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

celery_app = Celery("core")

# Cargar configuración desde settings.py
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Autodiscover tasks en las apps de Django
celery_app.autodiscover_tasks()
