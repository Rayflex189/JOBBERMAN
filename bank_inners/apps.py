from django.apps import AppConfig


class BankInnersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bank_inners'
    
    def ready(self):
        import bank_inners.signals