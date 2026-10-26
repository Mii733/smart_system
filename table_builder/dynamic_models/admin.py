# from django.contrib import admin

# # Register your models here.



# from dynamic_models.models import ModelSchema, FieldSchema
# # from .models import Modelnames, CustomField
# # from test2.models import DynamicModelsDept3

# from django.contrib import admin
# # admin.site.register(Modelnames)
# admin.site.register(ModelSchema)
# admin.site.register(FieldSchema)
# # admin.site.register(CustomField)

# # from django.contrib import admin
# from django.apps import apps

# # استدعاء الدالة وتسجيل الجداول في ملف الإدارة
# from django.contrib.admin.sites import AlreadyRegistered

# from django.contrib.admin.sites import NotRegistered

# def register_dynamic_models():
#     # app_name = 'test2'
#     app_name = 'dynamic_models'
#     models = apps.get_models(app_name)
#     for model in models:
#         if model.__name__ not in ['Group', 'LogEntry']:
#             try:
#                 admin.site.unregister(model)
#             except NotRegistered:
#                 pass
#             admin.site.register(model)

# # استدعاء الدالة لتسجيل الجداول في ملف الإدارة
# register_dynamic_models()
