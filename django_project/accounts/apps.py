from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
