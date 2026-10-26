from django.contrib import admin

# Register your models here.



from dynamic_models.models import ModelSchema, FieldSchema
from .models import Modelnames, CustomField
# from test2.models import DynamicModelsDept3

from django.contrib import admin
admin.site.register(Modelnames)
admin.site.register(ModelSchema)
admin.site.register(FieldSchema)
admin.site.register(CustomField)
# admin.site.register(DynamicModelsDept3)

# from .models import FieldSchema

# @admin.register(FieldSchema)
# class FieldSchemaAdmin(admin.ModelAdmin):
#     pass
import json

# models = Modelnames.objects.all()

# for model in models:
#     model_schema = ModelSchema.objects.get(name=model.modelname)
#     properties = json.loads(model_schema.properties)
    
#     fields = {}
#     for field_name, field_props in properties.items():
#         field_type = field_props['type']
#         max_length = int(field_props.get('max_length', 255))  # تحويل قيمة 'max_length' إلى عدد صحيح
#         # قم بتحديد المزيد من الخصائص الأخرى الخاصة بالحقل إذا كانت موجودة في JSON
        
#         if field_type == 'char':
#             field = models.CharField(max_length=max_length)
#         elif field_type == 'text':
#             field = models.TextField(max_length=max_length)
#         # قم بتعريف المزيد من أنواع الحقول الديناميكية إذا كانت مدعومة في تطبيقك
        
#         fields[field_name] = field
    
#     # قم بإنشاء نموذج الجدول الديناميكي باستخدام الحقول المعرفة
#     dynamic_model = type(model.modelname, (models.Model,), fields)
    
#     # قم بتسجيل النموذج في واجهة إدارة Django
#     admin.site.register(dynamic_model)# Register your models here.

# models = Modelnames.objects.all()
# for model in models:
#     reg_model = ModelSchema.objects.get(name=model.modelname).as_model()
#     admin.site.register(reg_model)
# admin.site.register(ModelSchema)
# admin.site.register(FieldSchema)

# admin.py

# from django.contrib import admin
from django.apps import apps

# استدعاء الدالة وتسجيل الجداول في ملف الإدارة
from django.contrib.admin.sites import AlreadyRegistered

from django.contrib.admin.sites import NotRegistered

def register_dynamic_models():
    # app_name = 'test2'
    app_name = 'dynamic_models'
    models = apps.get_models(app_name)
    for model in models:
        if model.__name__ not in ['Group', 'LogEntry']:
            try:
                admin.site.unregister(model)
            except NotRegistered:
                pass
            admin.site.register(model)

# def register_dynamic_models():
    
#     models = ModelSchema.objects.all()
#     for model in models:
#         # try:
#         #     print("fffffffffffffff")
#         #     admin.site.unregister(model.as_model())
#         # except NotRegistered:
#         #     pass
#         admin.site.register(model.as_model())

# استدعاء الدالة لتسجيل الجداول في ملف الإدارة
register_dynamic_models()
