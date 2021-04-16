from django.apps import AppConfig
from django.core.management import call_command


class PagesConfig(AppConfig):

    name = 'pages'

    def ready(self):
        # code that run on startup
        call_command('migrate')
