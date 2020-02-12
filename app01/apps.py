from django.apps import AppConfig


class App01Config(AppConfig):
    name = 'app01'
    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules("xx")  #会自动执行各个app的xx文件