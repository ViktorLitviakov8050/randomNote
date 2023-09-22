from django.apps import AppConfig


class RandomnoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'randomNote'

    def ready(self):
        import randomNote.signals