from django.apps import AppConfig


class HomescreenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HomeScreen'

    def ready(self):
        import HomeScreen.signals
