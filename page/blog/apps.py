from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        import blog.signals

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
