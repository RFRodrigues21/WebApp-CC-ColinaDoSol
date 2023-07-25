from django.apps import AppConfig


class ColinadosolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ColinaDoSol'
    def ready(self):
        import ColinaDoSol.signals
