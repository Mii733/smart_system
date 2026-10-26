from .validators import validate_identifier, is_safe_identifier






from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.db import models
from django import forms
from django.db import transaction
from django.db import connection
# from .models import Modelnames, TblSystem, CustomUser, UserAction
from .models import Modelnames, TblSystem, CustomUser, CustmReportHeader, UserAction
from .forms import CustomFieldForm, FieldSchemaForm, CustmReportHeaderForm, UserActionForm, create_dynamic_formset, create_dynamic_form_for_formset
from django.apps import apps
import psycopg2
# في ملف views.py

from django.shortcuts import render, redirect
from .forms import TblSystemForm, FieldConditionForm, create_dynamic_form, get_dynamic_model, create_dynamic_form_for_seach
from django.db import connection

from .models import CustomField
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse , HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from django.db import models
# from dynamic_models.models import ModelSchema, FieldSchema
from django.urls import clear_url_caches
from importlib import import_module,reload
from django.contrib import admin
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.db.models.base import ModelBase
from dynamic_models.models import ModelSchema, FieldSchema, ModelBuilder
from dynamic_models.factory import FieldFactory, ModelFactory
# import pytest
from django.test import TestCase
# from django.db.models.fields.related import ForeignKey
from django.core.exceptions import ObjectDoesNotExist
from dynamic_models import utils
from dynamic_models.exceptions import InvalidFieldNameError, NullFieldChangedError
import json
import subprocess
from contextlib import contextmanager
import pandas as pd
from django.apps import apps
from django.forms import Form, fields
from django.template import Template, Context
from django.http import JsonResponse
from django.db import connections
import json
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Field
from django.template import Template
from psycopg2.extensions import string_types

from django import forms
from django.forms import modelform_factory
# from dynamic_forms.models import FieldDefinition
from django.db import connection
import subprocess
from django.core.management import call_command
from django.db import migrations, models
import fileinput
import types
import subprocess
import re
from googletrans import Translator
from django.http import QueryDict

# from transliterate import translit

# def arabic_to_english(word):
#     return translit(word, 'ar', reversed=True)

from django.shortcuts import render
from django.db import connection
# from .models import DynamicModel
from django.shortcuts import render
# from .forms import DynamicForm
import psycopg2
from django import forms
from django.db import models
from django.forms import ModelForm
from test2.models import *


import os
import sys
from django.core.management import call_command


def make_migrations_and_migrate1(app_label):
    try:

        print("Current working directory:", os.getcwd())

        # الحصول على مسار التطبيق
        app_config = apps.get_app_config(app_label)
        app_path = os.path.dirname(app_config.path)

        # طباعة مسار التطبيق
        print(f"App path for '{app_label}': {app_path}")
        
        # إنشاء المهاجرات للتطبيق المحدد
        call_command('makemigrations', app_label, settings='table_builder.settings')

        # تطبيق المهاجرات للتطبيق المحدد
        call_command('migrate', app_label, settings='table_builder.settings')

        print(f"Migration for app '{app_label}' has been successfully applied.")

    except Exception as e:
        print(f"An error occurred while making migrations for app '{app_label}': {str(e)}")



# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
#     try:
#         # تأكد من تحميل إعدادات Django قبل تنفيذ الأوامر
#         import django
#         django.setup()
        
#         # تشغيل الدالة لإنشاء وتطبيق المهاجرات لتطبيق تيست2
#         app_label = 'test2'
#         make_migrations_and_migrate(app_label)
        
#         print("Migrations created and applied successfully for app 'test2'.")
#     except Exception as e:
#         print("An error occurred:", e)

# def makemigrations_migrate():
#     call_command('makemigrations')
#     call_command('migrate')

# تشغيل الدالة لإنشاء وتطبيق المهاجرات
# makemigrations_migrate()

# if not os.path.exists()



def dynamic_form(request, model_name):
    dynamic_form = DynamicForm()
    return render(request, 'dynamic_form.html', {'form': dynamic_form})
    
def translate_to_en(text):
    translator = Translator()
    translation = translator.translate(text, src='ar', dest='en')
    translated_text = translation.text
    return translated_text

def translate_to_ar(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='ar')
    translated_text = translation.text
    return translated_text

def run_inspectdb_command():
    try:
        result = subprocess.run(["python", "manage.py", "inspectdb"], capture_output=True, text=True, check=True)
        print("Command executed successfully.")
        print("Modifying delete behavior...")
        output = result.stdout
        # print(output)
        # تحديد نمط الخط الذي يحتوي على تعريف الحقول في الناتج المولد
        field_definition_pattern = re.compile(r"(\w+)\s+=\s+models\.(\w+)\(")

        # الحقول المتوقعة في التعريف
        expected_fields = ["CharField", "IntegerField", "BooleanField", "DateField", "DateTimeField", "ForeignKey", "ManyToManyField"]

        # تحليل الناتج المولد وتعديله لإضافة verbose_name للحقول

        for line in output.splitlines():
            if line.startswith('class '):
                class_name = line.split(' ')[1].split('(')[0]
                app_label = "test2"  # استبدل "myapp" بالتطبيق الخاص بك
                model = apps.get_model(app_label=app_label, model_name=class_name, require_ready=False)
                if model:
                    # تحديث verbose_name لكل حقل في النموذج
                    updated_line = line
                    for field in model._meta.fields:
                        updated_line = updated_line.replace(field.attname, field.verbose_name)
                    # طباعة السطر المعدل
                    print(updated_line)


    except subprocess.CalledProcessError as e:
        print("Command execution failed.")
        print("Error message:")
        print(e.stderr)

from django.db.models.base import ModelBase
def run_makemigrations():
    try:
        call_command('makemigrations')
        print("تم تنفيذ الأمر makemigrations بنجاح.")
    except Exception as e:
        print("حدث خطأ أثناء تنفيذ الأمر makemigrations:")
        print("fffffffffffffffffffffff")
        print(str(e))

def my_view2(request, model_name):
    table_name = model_name
    # table_name = 'DynamicModelsEmp3'
    form_class = create_dynamic_form(table_name)
    # model_class, form_class = generate_model_and_form(table_name)
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = form_class()
    
    return render(request, 'my_view2.html', {'form': form})


def my_view(request):
    # الحصول على النماذج الموجودة في المشروع 
    # all_models = {f"{model._meta.app_label}.{model.__name__}": model._meta.verbose_name for model in apps.get_models()}
    all_models = {f"{model.__name__}": model._meta.verbose_name for model in apps.get_models()}
    all_models2 = ModelSchema.objects.all()
    return render(request,"dynamic_form.html", {'all_models': all_models , 'all_models2': all_models2})

def my_view1(request):
    model_name = request.GET.get('model')
    model_name = 'test2.DynamicModels' + model_name.replace("_", "")
    if not model_name:
        return HttpResponseBadRequest("NO model name provided.")
    try:
        Model = apps.get_model(app_label=model_name.split('.')[0], model_name=model_name.split('.')[1])
        # print(Model,"lllllllllllllllllll")
    except (LookupError, IndexError):
        return HttpResponseBadRequest("Invalid model name")

    ModelForm = modelform_factory(Model, fields='__all__')  # تحريك هذا السطر إلى هنا
    # print(ModelForm,"lllllllllllllllllll")
    if request.method == 'POST':
        form_instance = ModelForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            # يمكنك إجراء أي إجراءات أخرى بعد حفظ البيانات
    else:
        form_instance = ModelForm()  # وهنا

    return render(request, "my_view1.html", {'form': form_instance})

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from django.core.exceptions import AppRegistryNotReady


from django.db import IntegrityError

def delete_custom_permissions_for_all_models():
    try:
        apps.check_models_ready()  # تأكد من أن النماذج جاهزة
    except AppRegistryNotReady:
        return  # إذا لم تكن النماذج جاهزة، لا تتابع

    all_models = apps.get_models()  # الحصول على جميع النماذج

    custom_permissions = [
        {'codename': 'import_data', 'name': 'Can Import Data'},
        {'codename': 'export_data', 'name': 'Can Export Data'},
        {'codename': 'print_data', 'name': 'Can Print Data'},
        {'codename': 'create_field', 'name': 'Can Create Field'},
        {'codename': 'drop_field', 'name': 'Can Drop Field'},
        {'codename': 'edit_field', 'name': 'Can Edit Field'},
        {'codename': 'delete_model', 'name': 'Can Delete Model'},
        {'codename': 'edit_model', 'name': 'Can Edit Model'},
        {'codename': 'view_model', 'name': 'Can View Model'},
        {'codename': 'drop_model', 'name': 'Can Drop Model'},
        {'codename': 'edit_model', 'name': 'Can Edit Model'},
        {'codename': 'manage_model', 'name': 'Can Manage Model'},
        {'codename': 'model_report', 'name': 'Can Report Model'},
        {'codename': 'import_data', 'name': 'Can Import Data'},
        {'codename': 'export_data', 'name': 'Can Export Data'},
        {'codename': 'print_data', 'name': 'Can Print Data'},
        {'codename': 'add_field', 'name': 'Can Add Field'},
        {'codename': 'delete_field', 'name': 'Can Delete Field'},
        {'codename': 'edit_field', 'name': 'Can Edit Field'},
        {'codename': 'delete_model', 'name': 'Can Delete Model'},
        {'codename': 'edit_model', 'name': 'Can Edit Model'},
        {'codename': 'view_model', 'name': 'Can View Model'},

    ]
    
    for model in all_models:
        model_content_type = ContentType.objects.get_for_model(model)

        for permission_data in custom_permissions:
            # استخدم codename فقط من القاموس
            codename = f"{permission_data['codename']}_{model._meta.model_name}"

            try:
                # العثور على الصلاحية حسب الـ codename
                permission = Permission.objects.get(codename=codename, content_type=model_content_type)
                permission.delete()
                print(f"Deleted permission with codename '{codename}' for model '{model._meta.model_name}'.")
            except Permission.DoesNotExist:
                print(f"Permission with codename '{codename}' for model '{model._meta.model_name}' does not exist.")

def create_custom_permissions_for_all_models():
    try:
        apps.check_models_ready()  # تأكد من أن النماذج جاهزة
    except AppRegistryNotReady:
        return  # إذا لم تكن النماذج جاهزة، لا تتابع

    all_models = apps.get_models()  # الحصول على جميع النماذج

    custom_permissions = [
        {'codename': 'import_data', 'name': 'Can Import Data'},
        {'codename': 'export_data', 'name': 'Can Export Data'},
        {'codename': 'print_data', 'name': 'Can Print Data'},
        {'codename': 'add_field', 'name': 'Can Add Field'},
        {'codename': 'delete_field', 'name': 'Can Delete Field'},
        {'codename': 'edit_field', 'name': 'Can Edit Field'},
        {'codename': 'delete_model', 'name': 'Can Delete Model'},
        {'codename': 'edit_model', 'name': 'Can Edit Model'},
        {'codename': 'view_model', 'name': 'Can View Model'},
    ]

    for model in all_models:
        model_content_type = ContentType.objects.get_for_model(model)

        for permission_data in custom_permissions:
            codename = f"{permission_data['codename']}_{model._meta.model_name}"
            name = f"{permission_data['name']} ({model._meta.model_name})"
            
            # تحقق إذا كانت الصلاحية موجودة مسبقًا
            existing_permission = Permission.objects.filter(
                codename=codename,
                content_type=model_content_type
            ).first()

            if existing_permission:
                print(f"الصلاحية '{codename}' موجودة بالفعل للنموذج '{model._meta.model_name}'.")
            else:
                # إذا كانت الصلاحية غير موجودة، يتم إنشاؤها
                try:
                    permission = Permission.objects.create(
                        codename=codename,
                        name=name,
                        content_type=model_content_type
                    )
                    # print(f"Created permission with codename '{permission.codename}' for model '{model._meta.model_name}'.")
                except IntegrityError:
                    print(f"حدث خطأ في إنشاء صلاحية '{codename}' للنموذج '{model._meta.model_name}' بسبب تكرار المفتاح.")


def create_custom_permissions_for_app(app_label):
    try:
        apps.check_models_ready()  # تأكد من أن النماذج جاهزة
    except AppRegistryNotReady:
        return  # إذا لم تكن النماذج جاهزة، لا تتابع

    # الحصول على جميع النماذج في التطبيق المحدد
    app_config = apps.get_app_config(app_label)
    all_models = app_config.get_models()  # نماذج التطبيق المحدد

    
    custom_permissions = [
        {'codename': 'import_data', 'name': 'Can Import Data'},
        {'codename': 'export_data', 'name': 'Can Export Data'},
        {'codename': 'print_data', 'name': 'Can Print Data'},
        {'codename': 'create_field', 'name': 'Can Create Field'},
        {'codename': 'drop_field', 'name': 'Can Drop Field'},
        {'codename': 'edit_field', 'name': 'Can Edit Field'},
        # {'codename': 'drop_model', 'name': 'Can Drop Model'},
        # {'codename': 'edit_model', 'name': 'Can Edit Model'},
        {'codename': 'manage_model', 'name': 'Can Manage Model'},
        {'codename': 'model_report', 'name': 'Can Report Model'},
    ]

    for model in all_models:
        model_content_type = ContentType.objects.get_for_model(model)

        for permission_data in custom_permissions:
            codename = f"{permission_data['codename']}_{model._meta.model_name}"
            name = f"{permission_data['name']} ({model._meta.model_name})"
            
            # تحقق إذا كانت الصلاحية موجودة مسبقًا
            existing_permission = Permission.objects.filter(
                codename=codename,
                content_type=model_content_type
            ).first()

            if existing_permission:
                pass
                # print(f"الصلاحية '{codename}' موجودة بالفعل للنموذج '{model._meta.model_name}'.")
            else:
                # إذا كانت الصلاحية غير موجودة، يتم إنشاؤها
                try:
                    Permission.objects.create(
                        codename=codename,
                        name=name,
                        content_type=model_content_type
                    )
                    # print(f"تم إنشاء الصلاحية '{codename}' للنموذج '{model._meta.model_name}'.")
                except IntegrityError:
                    pass
                    # print(f"حدث خطأ في إنشاء صلاحية '{codename}' للنموذج '{model._meta.model_name}' بسبب تكرار المفتاح.")


def delete_custom_permissions_for_app(app_label):
    try:
        apps.check_models_ready()  # تأكد من أن النماذج جاهزة
    except AppRegistryNotReady:
        return  # إذا لم تكن النماذج جاهزة، لا تتابع

    # الحصول على جميع النماذج في التطبيق المحدد
    app_config = apps.get_app_config(app_label)
    all_models = app_config.get_models()  # نماذج التطبيق المحدد

    custom_permissions = [
        'import_data',
        'export_data',
        'print_data',
        'create_field',
        'drop_field',
        'edit_field',
        'manage_model',
        'model_report',
    ]

    for model in all_models:
        model_content_type = ContentType.objects.get_for_model(model)

        for permission_codename in custom_permissions:
            codename = f"{permission_codename}_{model._meta.model_name}"
            
            # البحث عن الصلاحية وحذفها إذا وجدت
            try:
                permission = Permission.objects.get(
                    codename=codename,
                    content_type=model_content_type
                )
                permission.delete()
                print(f"تم حذف الصلاحية '{codename}' للنموذج '{model._meta.model_name}'.")
            except Permission.DoesNotExist:
                print(f"الصلاحية '{codename}' غير موجودة للنموذج '{model._meta.model_name}'.")

import subprocess
import re


import os
import sys

from django.core.management import execute_from_command_line
import os
import sys
from django.core.management import call_command
from django.conf import settings
import os
from django.core.management import call_command
from io import StringIO
import sys

# في ملف utils.py داخل مشروع Django
import os
import sys
from django.core.management import call_command
from django.apps import apps
from django.core.management import call_command
import os
import sys

import os
import sys
from django.core.management import call_command
from django.apps import apps

def make_migrations_and_migrate1(app_name):
    """
    دالة لعمل Migrations لتطبيق معين فقط.
    يتم تمرير اسم التطبيق الذي تريد عمل المراجعة والتطبيق له.
    """
    try:
        # التأكد من إعداد البيئة بشكل صحيح
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_builder.settings')

        print("Current working directory:", os.getcwd())

        # الحصول على مسار التطبيق
        app_config = apps.get_app_config(app_name)
        app_path = os.path.dirname(app_config.path)

        # طباعة مسار التطبيق
        print(f"App path for '{app_name}': {app_path}")
        
        # طباعة المسار لكل موديل في التطبيق
        # models = app_config.get_models()
        # for model in models:
        #     model_file_path = os.path.abspath(model._meta.app_label + '/models.py')
        #     print(f"Model: {model.__name__}, Model file path: {model_file_path}")

        # في حال كان المشروع قد تم تحويله إلى EXE باستخدام PyInstaller
        if getattr(sys, 'frozen', False):
            # إذا كان PyInstaller قد قام بتجميد المشروع، يجب استخدام `call_command` لتشغيل `makemigrations`
            print(f"Running migrations for frozen app: {app_name}")
            call_command('makemigrations', app_name)  # إنشاء migrations للتطبيق المعين
            call_command('migrate', app_name)         # تطبيق التغييرات على قاعدة البيانات للتطبيق المعين
            print("99999999999999999999999999")
        else:
            # إذا كان المشروع في بيئة تطوير عادية
            print(f"Running migrations for development app: {app_name}")
            call_command('makemigrations', app_name)  # إنشاء migrations للتطبيق المعين
            call_command('migrate', app_name)         # تطبيق التغييرات على قاعدة البيانات للتطبيق المعين
            print("00000000000000000000")
        
        print(f"Command executed successfully for {app_name}")

    except Exception as e:
        print(f"An error occurred while processing {app_name}: {str(e)}")



def make_migrations_and_migrate(app_name):
    """
    دالة لعمل Migrations لتطبيق معين فقط.
    يتم تمرير اسم التطبيق الذي تريد عمل المراجعة والتطبيق له.
    """
    try:
        # التأكد من إعداد البيئة بشكل صحيح
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_builder.settings')

        print("Current working directory:", os.getcwd())

        # الحصول على مسار التطبيق
        app_config = apps.get_app_config(app_name)
        app_path = os.path.dirname(app_config.path)

        # طباعة مسار التطبيق
        print(f"App path for '{app_name}': {app_path}")
        
        # التأكد من أن البيئة في وضع frozen أو تطوير
        if getattr(sys, 'frozen', False):
            print("Running in frozen mode")
            base_path = os.path.dirname(sys.executable)
            # تأكد من أن المجلدات تم تضمينها بشكل صحيح داخل EXE
            print(f"Base path for frozen app: {base_path}")
            
            # هنا تحقق من أن مجلد migrations موجود في البيئة المجمدة
            app_migrations_path = os.path.join(base_path, '_internal', app_name, 'migrations')
            print(f"App migrations path: {app_migrations_path}")
            
            # تحقق من أن PyInstaller قام بتضمين الملفات بشكل صحيح
            if not os.path.exists(app_migrations_path):
                print(f"Warning: Migrations directory not found at {app_migrations_path}")

            # تنفيذ الأوامر الخاصة بالمجمد
            call_command('makemigrations', app_name)
            call_command('migrate', app_name)
        else:
            print("Running in development mode")
            call_command('makemigrations', app_name)
            call_command('migrate', app_name)
        
        print(f"Command executed successfully for {app_name}")

    except Exception as e:
        print(f"An error occurred while processing {app_name}: {str(e)}")


def make_migrations_and_migrate2(app_name):
    """
    دالة لعمل Migrations لتطبيق معين فقط.
    يتم تمرير اسم التطبيق الذي تريد عمل المراجعة والتطبيق له.
    """
    try:
        # التأكد من إعداد البيئة بشكل صحيح
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_builder.settings')

        # الحصول على مسار التطبيق
        app_config = apps.get_app_config(app_name)
        
        # إذا كان المشروع قد تم تجميعه باستخدام PyInstaller
        if getattr(sys, 'frozen', False):
            # استخدام sys._MEIPASS للوصول إلى الملفات المجمعة
            app_path = os.path.join(sys._MEIPASS, app_name)  # استخدام _MEIPASS للوصول إلى المسار الصحيح
        else:
            # إذا كان في بيئة تطوير عادية
            app_path = os.path.dirname(app_config.path)
        
        # طباعة المسار الذي سيتم استخدامه
        print(f"App path for '{app_name}': {app_path}")
        
        # في حال كان المشروع قد تم تحويله إلى EXE باستخدام PyInstaller
        if getattr(sys, 'frozen', False):
            # إذا كان PyInstaller قد قام بتجميد المشروع، يجب استخدام `call_command` لتشغيل `makemigrations`
            print(f"Running migrations for frozen app: {app_name}")
            call_command('makemigrations', app_name)  # إنشاء migrations للتطبيق المعين
            call_command('migrate', app_name)         # تطبيق التغييرات على قاعدة البيانات للتطبيق المعين
            print("Migrations applied for frozen app.")
        else:
            # إذا كان المشروع في بيئة تطوير عادية
            print(f"Running migrations for development app: {app_name}")
            call_command('makemigrations', app_name)  # إنشاء migrations للتطبيق المعين
            call_command('migrate', app_name)         # تطبيق التغييرات على قاعدة البيانات للتطبيق المعين
            print("Migrations applied for development app.")
        
        print(f"Command executed successfully for {app_name}")

    except Exception as e:
        print(f"An error occurred while processing {app_name}: {str(e)}")


import os
import sys
from django.core.management import call_command
from django.apps import apps
import django

def make_migrations_and_migrate2(app_name):
    """
    دالة لعمل Migrations لتطبيق معين فقط.
    يتم تمرير اسم التطبيق الذي تريد عمل المراجعة والتطبيق له.
    """
    try:
        # التأكد من إعداد البيئة بشكل صحيح
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_builder.settings')

        # إذا كان المشروع قد تم تحويله إلى EXE باستخدام PyInstaller
        if getattr(sys, 'frozen', False):
            # إذا كان PyInstaller قد قام بتجميد المشروع، يجب استخدام `call_command` لتشغيل `makemigrations`
            print(f"Running migrations for frozen app: {app_name}")

            # تحديد المسار الصحيح في بيئة EXE
            app_path = os.path.dirname(sys.executable)  # الحصول على المسار الفعلي للـ EXE
            os.chdir(app_path)  # تغيير الدليل الحالي ليكون داخل المجلد الذي يحتوي على EXE
            print(f"Changed directory to: {os.getcwd()}")

            # إعادة تحميل إعدادات Django
            django.setup()

            # تنفيذ الأوامر داخل EXE
            call_command('makemigrations', app_name)  # إنشاء migrations للتطبيق المعين
            call_command('migrate', app_name)         # تطبيق التغييرات على قاعدة البيانات للتطبيق المعين
            print("99999999999999999999999999")
        else:
            # إذا كان المشروع في بيئة تطوير عادية
            print(f"Running migrations for development app: {app_name}")
            call_command('makemigrations', app_name)  # إنشاء migrations للتطبيق المعين
            call_command('migrate', app_name)         # تطبيق التغييرات على قاعدة البيانات للتطبيق المعين
            print("00000000000000000000")
        
        print(f"Command executed successfully for {app_name}")

    except Exception as e:
        print(f"An error occurred while processing {app_name}: {str(e)}")



def make_migrations_and_migrate3(app_name):
    """
    دالة لعمل Migrations لتطبيق معين فقط.
    يتم تمرير اسم التطبيق الذي تريد عمل المراجعة والتطبيق له.
    """
    try:
        # التأكد من إعداد البيئة بشكل صحيح
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_builder.settings')

        print("Current working directory:", os.getcwd())

        # الحصول على مسار التطبيق
        app_config = apps.get_app_config(app_name)
        app_path = os.path.dirname(app_config.path)

        # طباعة مسار التطبيق
        print(f"App path for '{app_name}': {app_path}")
        
        # في حال كان المشروع قد تم تحويله إلى EXE باستخدام PyInstaller
        if getattr(sys, 'frozen', False):
            # إذا كان PyInstaller قد قام بتجميد المشروع، يجب استخدام `sys._MEIPASS` للوصول إلى الملفات المدمجة
            base_path = sys._MEIPASS
            print(f"Frozen environment detected. Using base path: {base_path}")

            # تأكد من أن المسار إلى تطبيقك صحيح بعد تجميعه باستخدام PyInstaller
            app_path = os.path.join(base_path, os.path.relpath(app_path, os.getcwd()))
            print(f"App path after adjustment: {app_path}")

            # تأكد من أن المجلدات التي تحتوي على النماذج والمهاجرات موجودة في البيئة المجمعَّة
            models_path = os.path.join(app_path, "models.py")
            print(f"Models path: {models_path}")

            # تأكد من أن الملف models.py موجود في البيئة المجمعَّة
            if not os.path.exists(models_path):
                print(f"Warning: {models_path} does not exist in EXE environment.")

            # تشغيل makemigrations و migrate في بيئة EXE
            call_command('makemigrations', app_name)  # إنشاء migrations للتطبيق المعين
            call_command('migrate', app_name)         # تطبيق التغييرات على قاعدة البيانات للتطبيق المعين

            print("Migrations and migrations applied successfully in EXE environment.")

        else:
            # إذا كان المشروع في بيئة تطوير عادية
            call_command('makemigrations', app_name)  # إنشاء migrations للتطبيق المعين
            call_command('migrate', app_name)         # تطبيق التغييرات على قاعدة البيانات للتطبيق المعين
            print("Migrations and migrations applied successfully in development environment.")

        print(f"Command executed successfully for app: {app_name}")

    except Exception as e:
        print(f"An error occurred in {app_name}: {str(e)}")

import os
import sys
from django.core.management import call_command
from io import StringIO

def modify_delete_behavior2():
    try:
        # تأكد من أنك في بيئة Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_builder.settings')

        # استخدام StringIO لالتقاط المخرجات
        output = StringIO()
        
        # تنفيذ أمر inspectdb داخل نفس العملية
        print("Running inspectdb...")

        # إعادة توجيه المخرجات إلى output
        call_command('inspectdb', stdout=output)

        # الحصول على المخرجات من StringIO
        models_output = output.getvalue()

        print("Command executed successfully.")
        print("Modifying delete behavior...")

        # تعديل سلوك الحذف من DO_NOTHING إلى CASCADE
        models_output = models_output.replace('models.DO_NOTHING', 'models.CASCADE')

        # تعديل الحقول من نوع CharField إلى FileField إذا كانت مناسبة
        models_output = modify_file_fields(models_output)

        # تحديد المسار الصحيح بناءً على البيئة (EXE أو تطوير)
        if getattr(sys, 'frozen', False):
            # في بيئة EXE، استخدم sys._MEIPASS للوصول إلى المجلد المؤقت
            base_path = sys._MEIPASS
            print(f"Frozen environment detected. Using base path: {base_path}")
            
            # التأكد من عدم تكرار _internal في المسار
            models_dir = os.path.join(base_path, "_internal", "test2")
        else:
            # في بيئة التطوير العادية
            models_dir = os.path.join(os.getcwd(), "_internal", "test2")

        # التأكد من وجود الدليل test2
        os.makedirs(models_dir, exist_ok=True)

        # تحديد مسار models.py داخل الدليل
        models_path = os.path.join(models_dir, "models.py")
        print(f"Saving models to: {models_path}")
        
        # كتابة النماذج المعدلة إلى ملف models.py
        with open(models_path, "w", encoding='utf-8') as file:
            file.write(models_output)

        print("Delete behavior modified successfully. Models written to models.py.")

    except Exception as e:
        print("An error occurred:", str(e))
        raise


def modify_delete_behavior1():
    try:
        # تأكد من أنك في بيئة Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_builder.settings')

        # استخدام StringIO لالتقاط المخرجات
        output = StringIO()
        
        # تنفيذ أمر inspectdb داخل نفس العملية
        print("Running inspectdb...")

        # إعادة توجيه المخرجات إلى output
        call_command('inspectdb', stdout=output)

        # الحصول على المخرجات من StringIO
        models_output = output.getvalue()

        print("Command executed successfully.")
        print("Modifying delete behavior...")

        # تعديل سلوك الحذف من DO_NOTHING إلى CASCADE
        models_output = models_output.replace('models.DO_NOTHING', 'models.CASCADE')

        # تعديل الحقول من نوع CharField إلى FileField إذا كانت مناسبة
        models_output = modify_file_fields(models_output)

        # التأكد من وجود الدليل test2
        # os.makedirs(os.path.join(os.getcwd(), "_internal/test2"), exist_ok=True)

        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # models_path = os.path.join(script_dir, "_internal/test2", "models.py")


        # كتابة النماذج المعدلة إلى ملف models.py
        models_path = os.path.join(os.getcwd(), "test2", "models.py")
        # models_path = os.path.join(os.getcwd(), "_internal/test2", "models.py")
        print(f"Saving models to: {models_path}")
        with open(models_path, "w", encoding='utf-8') as file:
            file.write(models_output)

        print("Delete behavior modified successfully. Models written to models.py.")

    except Exception as e:
        print("An error occurred:", str(e))
        raise


def modify_delete_behavior():
    try:
        # تأكد من أنك في بيئة Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_builder.settings')

        output = StringIO()
        app_name = 'test2'

        # تنفيذ أمر inspectdb داخل نفس العملية
        print("Running inspectdb...")
        call_command('inspectdb', stdout=output)

        models_output = output.getvalue()

        print("Command executed successfully.")
        print("Modifying delete behavior...")

        # تعديل سلوك الحذف
        models_output = models_output.replace('models.DO_NOTHING', 'models.CASCADE')

        # تعديل الحقول إذا لزم الأمر
        models_output = modify_file_fields(models_output)

        # التحقق من المسار في بيئة frozen
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
            models_path = os.path.join(base_path, "_internal", "test2", "models.py")
            print(f"Saving models to: {models_path}")
        else:
            models_path = os.path.join(os.getcwd(), "test2", "models.py")
            print(f"Saving models to: {models_path}")

        # كتابة النماذج المعدلة
        with open(models_path, "w", encoding='utf-8') as file:
            file.write(models_output)

        print("Delete behavior modified successfully. Models written to models.py.")
    except Exception as e:
        print("An error occurred:", str(e))
        raise

# تعمل بنجاح
def modify_delete_behavior1():
    try:
        # تأكد من أنك في بيئة Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table_builder.settings')

        # استخدام StringIO لالتقاط المخرجات
        output = StringIO()
        app_name = 'test2'
        
        # تنفيذ أمر inspectdb داخل نفس العملية
        print("Running inspectdb...")

        # إعادة توجيه المخرجات إلى output
        call_command('inspectdb', stdout=output)

        # الحصول على المخرجات من StringIO
        models_output = output.getvalue()

        print("Command executed successfully.")
        print("Modifying delete behavior...")

        # تعديل سلوك الحذف من DO_NOTHING إلى CASCADE
        models_output = models_output.replace('models.DO_NOTHING', 'models.CASCADE')

        # تعديل الحقول من نوع CharField إلى FileField إذا كانت مناسبة
        models_output = modify_file_fields(models_output)

        # التأكد من وجود الدليل test2
        # os.makedirs(os.path.join(os.getcwd(), "test2"), exist_ok=True)
        # os.makedirs(os.path.join(os.getcwd(), "_internal/test2"), exist_ok=True)

        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # models_path = os.path.join(script_dir, "_internal/test2", "models.py")
        # في حال كان المشروع قد تم تحويله إلى EXE باستخدام PyInstaller
        if getattr(sys, 'frozen', False):
            # إذا كان PyInstaller قد قام بتجميد المشروع، يجب استخدام `call_command` لتشغيل `makemigrations`
            print(f"Running  for frozen app: test2")
            models_path = os.path.join(os.getcwd(), "_internal/test2", "models.py")
            print(f"Saving models to: {models_path}")
            with open(models_path, "w", encoding='utf-8') as file:
                file.write(models_output)
        else:
            # إذا كان المشروع في بيئة تطوير عادية
            print(f"Running  for development app: test2")
            models_path = os.path.join(os.getcwd())
            print(f"Saving models to: {models_path}")
            # كتابة النماذج المعدلة إلى ملف models.py
            with open("test2/models.py", "w", encoding='utf-8') as file:
                file.write(models_output)
        

        # كتابة النماذج المعدلة إلى ملف models.py
        # models_path = os.path.join(os.getcwd(), "test2", "models.py")
        # models_path = os.path.join(os.getcwd(), "_internal/test2", "models.py")
        # print(f"Saving models to: {models_path}")
        # with open(models_path, "w", encoding='utf-8') as file:
        #     file.write(models_output)

        print("Delete behavior modified successfully. Models written to models.py.")

    except Exception as e:
        print("An error occurred:", str(e))
        raise




def modify_delete_behavior2():
    try:
        # الحصول على المسار الحالي (مجلد الـ EXE)
        base_dir = os.path.dirname(sys.executable)
        
        # المسار المطلق لـ manage.py
        manage_path = os.path.join(base_dir, "manage.py")
        
        # التحقق من وجود manage.py
        if not os.path.exists(manage_path):
            print(f"File not found: {manage_path}")
            return
        
        # تنفيذ أمر inspectdb
        models_output = subprocess.check_output(
            [sys.executable, manage_path, "inspectdb"],
            text=True,
            stderr=subprocess.STDOUT
        )
        
        print("Command executed successfully.")
        print("Modifying delete behavior...")

        # تعديل سلوك الحذف من DO_NOTHING إلى CASCADE
        models_output = models_output.replace('models.DO_NOTHING', 'models.CASCADE')

        # تعديل الحقول من نوع CharField إلى FileField إذا كانت مناسبة
        models_output = modify_file_fields(models_output)
        
        # المسار المطلق لملف models.py
        models_dir = os.path.join(base_dir, "test2")
        os.makedirs(models_dir, exist_ok=True)  # إنشاء المجلد إذا لم يكن موجودًا
        models_path = os.path.join(models_dir, "models.py")
        
        # كتابة النماذج المعدلة إلى ملف models.py
        with open(models_path, "w", encoding='utf-8') as file:
            file.write(models_output)

        print("Delete behavior modified successfully. Models written to models.py.")

    except subprocess.CalledProcessError as e:
        print("Command execution failed.")
        print("Error message:")
        print(e.output)
    except Exception as e:
        print("An unexpected error occurred:")
        print(str(e))



# اشتغلة بعد التحويل لاكن تقوم بفتح تبويبة جديدة ولا تقوم با الغرض المطلوب منها
def modify_delete_behavior1():
    try:
        # الحصول على المسار المطلق لـ manage.py
        manage_path = os.path.join(os.getcwd(), "manage.py")
        
        # تنفيذ أمر inspectdb
        models_output = subprocess.check_output([sys.executable, manage_path, "inspectdb"], text=True, stderr=subprocess.STDOUT)
        
        print("Command executed successfully.")
        print("Modifying delete behavior...")

        # تعديل سلوك الحذف من DO_NOTHING إلى CASCADE
        models_output = models_output.replace('models.DO_NOTHING', 'models.CASCADE')

        # تعديل الحقول من نوع CharField إلى FileField إذا كانت مناسبة
        models_output = modify_file_fields(models_output)
        
        # كتابة النماذج المعدلة إلى ملف models.py
        models_path = os.path.join(os.getcwd(), "test2", "models.py")
        with open(models_path, "w", encoding='utf-8') as file:
            file.write(models_output)

        print("Delete behavior modified successfully. Models written to models.py.")

    except subprocess.CalledProcessError as e:
        print("Command execution failed.")
        print("Error message:")
        print(e.output)
    except Exception as e:
        print("An unexpected error occurred:")
        print(str(e))


def modify_delete_behavior1():
    # print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    try:
        
        # تنفيذ أمر inspectdb للحصول على تعريفات النماذج من قاعدة البيانات
        models_output = subprocess.check_output(["python", "manage.py", "inspectdb"], text=True)
        
        # print("Command executed successfully.")
        # print("Modifying delete behavior...")

        # تعديل سلوك الحذف من DO_NOTHING إلى CASCADE
        models_output = models_output.replace('models.DO_NOTHING', 'models.CASCADE')

        # تعديل الحقول من نوع CharField إلى FileField إذا كانت مناسبة
        # البحث عن الحقول التي قد تكون من نوع CharField والتي يجب أن تكون FileField
        models_output = modify_file_fields(models_output)
        
        # كتابة النماذج المعدلة إلى ملف models.py
        with open("test2/models.py", "w", encoding='utf-8') as file:
            file.write(models_output)

        print("Delete behavior modified successfully. Models written to models.py.")

    except subprocess.CalledProcessError as e:
        # print("Command execution failed.")
        print("Error message:")
        print(e.output)

def modify_file_fields(models_output):
    """
    تقوم هذه الدالة بتحويل الحقول من نوع CharField إلى FileField إذا كانت مناسبة،
    وإضافة حقول ManyToManyField من CustomField إلى النموذج الذي يحتوي عليها فقط.
    """
    lines = models_output.splitlines()
    modified_lines = []
    
    # استرجاع جميع الحقول من جدول CustomField
    fields = CustomField.objects.all()
    
    # إنشاء قاموس لتخزين حقول ManyToManyField لكل نموذج
    many_to_many_fields = {}
    
    # تجميع حقول ManyToManyField لكل نموذج
    for field in fields:
        if field.field_type == "ManyToManyField":
            if field.table not in many_to_many_fields:
                model_name = 'DynamicModels' + field.table.replace("_", "").capitalize()
                many_to_many_fields[model_name] = []
                # many_to_many_fields[field.table] = []
            many_to_many_fields[model_name].append(field)
            # many_to_many_fields[field.table].append(field)
    
    # التكرار على كل سطر من سطور النموذج
    for line in lines:
        # التحقق من بداية تعريف نموذج
        if line.strip().startswith("class "):
            # استخراج اسم النموذج
            model_name = line.split("class ")[1].split("(")[0].strip()
            
            # إضافة السطر إلى القائمة المعدلة
            modified_lines.append(line)
            
            # التحقق من وجود حقول ManyToManyField لهذا النموذج
            if model_name in many_to_many_fields:
                for field in many_to_many_fields[model_name]:
                    # إنشاء السطر الخاص بحقل ManyToManyField
                    field_line = f"    {field.field_name} = models.ManyToManyField("
                    related_model = 'DynamicModels' + field.related_table.replace("_", "").capitalize()
                    # إضافة النموذج المرتبط (to)
                    field_line += f"'{related_model}', "
                    # field_line += f"to='{field.related_table}', "
                    
                    # إضافة related_name إذا كان موجودًا
                    # if field.related_name:
                    #     field_line += f"related_name='{field.related_name}', "
                    
                    # إضافة through إذا كان موجودًا
                    # if field.through_model:
                    through_model = 'DynamicModels' + field.table.replace("_", "").capitalize()+ field.field_name.capitalize()
                    field_line += f"through='{through_model}', "
                    # field_line += f"through='{field.through_model}', "
                    
                    # إضافة verbose_name إذا كان موجودًا
                    if field.verbose_name:
                        field_line += f"verbose_name='{field.verbose_name}', "
                    
                    # إغلاق السطر
                    field_line = field_line.rstrip(", ") + ")"
                    
                    # إضافة السطر إلى القائمة المعدلة
                    modified_lines.append(field_line)
        else:
            # التكرار على الحقول في CustomField للتحقق إذا كانت من نوع "FileField" أو "ImageField"
            for field in fields:
                # إذا كان field_type هو "FileField" وكان السطر يحتوي على "CharField" لتمثيل ملف
                if field.field_type == "FileField" and "CharField" in line and field.field_name in line:
                    # تعديل السطر ليصبح من نوع FileField
                    line = line.replace('CharField', 'FileField')
                    
                    # إضافة upload_to, null, blank داخل الأقواس إذا لم تكن موجودة
                    if "upload_to" not in line:
                        line = line.replace(")", ", upload_to='media/')", 1)
                    # بمجرد تعديل السطر، يمكننا التوقف عن التكرار على الحقول لهذا السطر
                    break
                
                # إذا كان field_type هو "ImageField" وكان السطر يحتوي على "CharField" لتمثيل صورة
                elif field.field_type == "ImageField" and "CharField" in line and field.field_name in line:
                    # تعديل السطر ليصبح من نوع ImageField
                    line = line.replace('CharField', 'ImageField')
                    
                    # إضافة upload_to, null, blank داخل الأقواس إذا لم تكن موجودة
                    if "upload_to" not in line:
                        line = line.replace(")", ", upload_to='media/images')", 1)
                    # بمجرد تعديل السطر، يمكننا التوقف عن التكرار على الحقول لهذا السطر
                    break
            
            # إضافة السطر المعدل إلى القائمة
            modified_lines.append(line)
    
    # إرجاع النتيجة المعدلة
    return "\n".join(modified_lines)

def modify_file_fields1(models_output):
    # هذا الكود يبحث عن الحقول المحتملة التي من المفترض أن تكون FileField بدلاً من CharField
    lines = models_output.splitlines()
    modified_lines = []
    
    # استرجاع جميع الحقول من جدول CustomField
    fields = CustomField.objects.all()
    
    # التكرار على كل سطر من سطور النموذج
    for line in lines:
        # التكرار على الحقول في CustomField للتحقق إذا كانت من نوع "FileField"
        for field in fields:
            # إذا كان field_type هو "FileField" وكان السطر يحتوي على "CharField" لتمثيل ملف
            if field.field_type == "FileField" and "CharField" in line and field.field_name in line:
                # تعديل السطر ليصبح من نوع FileField
                line = line.replace('CharField', 'FileField')
                
                # إضافة upload_to, null, blank داخل الأقواس إذا لم تكن موجودة
                if "upload_to" not in line:
                    line = line.replace(")", ",upload_to='media/')", 1)
                # بمجرد تعديل السطر، يمكننا التوقف عن التكرار على الحقول لهذا السطر
                break
            elif field.field_type == "ImageField" and "CharField" in line and field.field_name in line:
                # تعديل السطر ليصبح من نوع FileField
                line = line.replace('CharField', 'ImageField')
                
                # إضافة upload_to, null, blank داخل الأقواس إذا لم تكن موجودة
                if "upload_to" not in line:
                    line = line.replace(")", ",upload_to='media/images')", 1)
                # بمجرد تعديل السطر، يمكننا التوقف عن التكرار على الحقول لهذا السطر
                break
            
        
        # إضافة السطر المعدل إلى القائمة
        modified_lines.append(line)

    # إرجاع النتيجة المعدلة
    return "\n".join(modified_lines)


# def get_field_class(data_type):
#     # تعيين نوع الحقل بناءً على نوع البيانات في قاعدة البيانات
#     if data_type == 'integer':
#         return forms.IntegerField
#     elif data_type == 'float':
#         return forms.FloatField
#     elif data_type == 'boolean':
#         return forms.BooleanField
#     elif data_type == 'date':
#         return forms.DateField
#     elif data_type == 'datetime':
#         return forms.DateTimeField
#     elif data_type == 'foreign_key':
#         return forms.models.ForeignKey()
#         # related_model = YourRelatedModel
#         # return forms.ModelChoiceField(queryset=related_model.objects.all()) # يمكن استخدام ForeignKey بدلاً من CharField إذا تطلب الأمر
#     else:
#         return forms.CharField

def custm_conncetion():
    conn = psycopg2.connect(database="s19", user="postgres", password="postgres", host="localhost", port="5432")
    cur = conn.cursor()
    return cur

# مستخدمة
def db_table_exists(table_name):
    with _db_cursor() as c:
        table_names = connection.introspection.table_names(c)
        return table_name in table_names

@contextmanager
def _db_cursor():
    cursor = connection.cursor()
    yield cursor
    cursor.close()

def addModelEntries(request):
    return redirect('/admin')

def base(request):
    return render(request,'base.html')

# مستخدمة
def add_related_field_sql(table_name, field_name, related_table_name, related_field_name, data_type):
    # Validate identifiers against SQL injection
    validate_identifier(table_name, "table_name")
    validate_identifier(field_name, "field_name")
    validate_identifier(related_table_name, "related_table_name")
    validate_identifier(related_field_name, "related_field_name")

    # Use Django connection instead of hardcoded external connection
    with connection.cursor() as cur:
        create_field_query = f"ALTER TABLE {table_name} ADD COLUMN {field_name} {data_type};"
        cur.execute(create_field_query)
        create_relation_query = f"ALTER TABLE {table_name} ADD FOREIGN KEY ({field_name}) REFERENCES {related_table_name}({related_field_name});"
        cur.execute(create_relation_query)


# def add_related_field2(table_name, field_name, related_table_name, related_field_name, data_type):
#     # اتصال بقاعدة البيانات
#     # conn = psycopg2.connect(database="s11", user="postgres", password="postgres", host="localhost", port="5432")
#     conn = custm_conncetion()
#     cur = conn.cursor()

#     # إنشاء الحقل في الجدول الأول
#     create_field_query = f"ALTER TABLE {table_name} ADD COLUMN {field_name} {data_type};"
#     cur.execute(create_field_query)

#     # إنشاء العلاقة بين الجدولين مع خاصية ON DELETE CASCADE
#     create_relation_query = f"ALTER TABLE {table_name} ADD CONSTRAINT fk_{field_name}_{related_table_name}_{related_field_name} FOREIGN KEY ({field_name}) REFERENCES {related_table_name}({related_field_name}) ON DELETE CASCADE;"
#     cur.execute(create_relation_query)

#     # إغلاق الاتصال بقاعدة البيانات
#     cur.close()
#     conn.commit()
#     conn.close()

# استدعاء الدالة
# add_related_field('table1', 'field1', 'related_table', 'related_field', 'INTEGER')

def create_subproject(request):
    if request.method == 'POST':
        form = TblSystemForm(request.POST)
        if form.is_valid():
            subproject = form.save()
            return redirect('index')
    else:
        form = TblSystemForm()
    
    return render(request, 'index.html', {'form': form})

# def create_subproject(request):
#     if request.method == 'POST':
#         form = TblSystemForm(request.POST)
#         if form.is_valid():
#             subproject = form.save()
#             return redirect('subproject_detail', sys_name_id=subproject.id)
#     else:
#         form = TblSystemForm()
    
#     return render(request, 'create_subproject.html', {'form': form})


# def get_fields(request, table_name):
#     get_fields = CustomField.filter(tabel=table_name)

#     return render(request,'createModels.html', context = {'get_fields': get_fields})

# في ملف views.py

def get_fields(request):
    table_name = request.GET.get('table', None)
    table_name = arabic_to_english(table_name)
    # print(table_name,"ttttttttttt")
    
    if table_name:
        # استعلام لاسترداد حقول الجدول معين
        fields = CustomField.objects.filter(table=table_name)
        field_list = []
        for field in fields:
            field_list.append({
                'name': field.verbose_name,
            })
        # print(field_list)
        return JsonResponse(field_list, safe=False)
    else:
        return JsonResponse({'error': 'No table name provided'}, status=400)    




# مشهد Django لعرض تشيك بوكس لحقول النموذج

def display_fields(request, table_name):

    model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
    model = apps.get_model(app_label='test2', model_name=model_name)

    fields = CustomField.objects.filter(table=table_name)
    
    if request.method == 'POST':
        selected_fields = request.POST.getlist('selected_fields')
        # print(selected_fields)
        request.session['selected_fields'] = selected_fields
        
        search_query = {}
        for field in selected_fields:
            field_name = CustomField.objects.get(field_name=field).field_name
            search_query[field_name] = request.POST.get(field_name)
            # print(search_query)
        
        results = model.objects.filter(**search_query)
        # selected_fields = ['alaqsamasm_alqsm', 'alaqsamalmwqa', 'alaqsamalmswl']
        # results = model.objects.all()
        print(results)
        # print(selected_fields)
        return render(request, 'fields.html', {'fields': fields, 'results': results, 'selected_fields': selected_fields, 'model_name': model_name})
    
    # selected_fields = ['alaqsamasm_alqsm', 'alaqsamalmwqa', 'alaqsamalmswl']
    selected_fields = request.session.get('selected_fields', [])
    
    return render(request, 'fields.html', {'fields': fields, 'selected_fields': selected_fields, 'model_name': model_name})

def run_server():
    call_command('runserver')

def createModels(request,sys_name_id):
    sys_name = TblSystem.objects.get(id=sys_name_id).name
    if not request.user.has_perm(f'dynmic_table.add_{sys_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        sys_name_id = sys_name_id
        subproject = get_object_or_404(TblSystem, id=sys_name_id)
        tables = ModelSchema.objects.all()
        modelExists = False
        modelCreated = False
        modelName = ''
        if request.POST:
            try:
                model_schema = arabic_to_english(request.POST['modelname'])
                model_schema = ModelSchema.objects.create(name=arabic_to_english(request.POST['modelname']).replace(" ", ""))
                
                Modelnames.objects.create(modelname=arabic_to_english(request.POST['modelname']).replace(" ", ""), modelnameAr=request.POST['modelname'], sys_name=subproject, model_type=request.POST['model_type'])
                modify_delete_behavior()
               
                make_migrations_and_migrate('test2')
                # run_migrations_for_app('test2')

                # make_migrations_and_migrate('dynamic_models')

                # create_custom_permissions_for_all_models()
                modelCreated = True
                return redirect('subproject_detail', sys_name_id=sys_name_id)

            except Exception as e:
                modelExists = True
                return render(request,'create_table.html', context={'sys_name_id': sys_name_id,'modelExists' : modelExists, 'modelCreated' : modelCreated, 'modelName' : modelName})
            
        return render(request,'create_table.html', context = {'sys_name_id': sys_name_id,'modelExists' : modelExists, 'modelCreated' : modelCreated, 'modelName' : modelName, 'tables': tables})

# تحت التطوير وليست مستخدمة

def update_table(request, model_id, sys_name_id):
    sys_name_id = sys_name_id
    subproject = get_object_or_404(TblSystem, id=sys_name_id)
    tables = ModelSchema.objects.all()
    modelExists = False
    modelCreated = False
    modelName = ''
    model_schema_instance = Modelnames.objects.get(id=model_id)
    model_schema_instance1 = ModelSchema.objects.get(id=model_id).as_model()
    if request.POST:
        try:
            print("eeeeeeeeeeee")
            # model_schema_instance = ModelSchema.objects.get(id=model_id)
            # تحديث الجدول بناءً على المدخلات الجديدة
            new_model_schema_name = arabic_to_english(request.POST['modelname']).replace(" ",""),

            if model_schema_instance.name != new_model_schema_name:
                model_schema_instance.name = new_model_schema_name

            # model_schema_instance.save()

            # model_schema = arabic_to_english(request.POST['modelname'])
            # model_schema = ModelSchema.objects.create(name=arabic_to_english(request.POST['modelname']))
            print("bbbbbbbbbbbbbbbbb")
            modelCreated = True
            # Modelnames.objects.create(modelname=arabic_to_english(request.POST['modelname']), modelnameAr=request.POST['modelname'], sys_name=subproject, model_type=request.POST['model_type'])
           
            # modify_delete_behavior()
            # make_migrations_and_migrate('test2')
            # create_custom_permissions_for_all_models()
            messages.success(request,"تم التعديل بنجاح")
            return redirect('subproject_detail', sys_name_id=sys_name_id)

        except Exception as e:
            modelExists = True
            return render(request,'update_table.html', context={'sys_name_id': sys_name_id,'modelExists' : modelExists, 'modelCreated' : modelCreated, 'modelName' : model_schema_instance})
        
    return render(request,'update_table.html', context = {'sys_name_id': sys_name_id,'modelExists' : modelExists, 'modelCreated' : modelCreated, 'modelName' : model_schema_instance, 'tables': tables})

# تحت التطوير

def add_related_field2(model_name, field_name, to, related_name,verbose_name):
    field_name = model_name + field_name
    relatedField = to + related_name
    
    another_model_schema1 = ModelSchema.objects.get(name=model_name).as_model()
    # print(another_model_schema1)
    # another_model_schema = get_dynamic_model(to)
    another_model_schema = 'test2.DynamicModels' + to.replace("_", "").capitalize()
    # print(another_model_schema)
    # another_model_schema = ModelSchema.objects.get(name=to)

    model_schema_instance = ModelSchema.objects.get(name=model_name)
    
    try:
        FieldSchema.objects.create(
            name=field_name,
            model_schema=model_schema_instance,
            class_name="django.db.models.ForeignKey",
            kwargs={
                "to": another_model_schema,
                "on_delete": models.CASCADE,  # استخدم models.CASCADE هنا
                "related_name": f'{relatedField}',
                "null": True,  # يجب أن تكون القيمة True أو False
                "blank": True,  # يجب أن تكون القيمة True أو False
                "verbose_name": f'{verbose_name}',
            },
        )
    except Exception as e:
        print("sssss")
        print(e)


def add_many_to_many_related_field(request,sys_name_id,model_name, field_name, to, related_name,verbose_name):
    field_name = model_name + field_name
    relatedField = to + related_name

    another_model_schema1 = ModelSchema.objects.get(name=to)
    another_model_schema2 = ModelSchema.objects.get(name=model_name).as_model()

    another_model_schema = 'test2.DynamicModels' + to.replace("_", "").capitalize()
    through = 'DynamicModels'+model_name.replace("_", "").capitalize()
    
    model_schema_instance = ModelSchema.objects.get(name=model_name)

    columns = FieldSchema.objects.filter(model_schema=model_schema_instance)
    for field in columns:
        if field.kwargs.get('to')==another_model_schema:
            messages.error(request,'يوجد حقل مرتبط بهذا النموذج',{another_model_schema})
            return redirect('add_field',model_name,sys_name_id)

    try:
        FieldSchema.objects.create(
            name=field_name,
            model_schema=model_schema_instance,
            class_name="django.db.models.ManyToManyField",
            kwargs={
                "to": another_model_schema,
                "on_delete": models.CASCADE,  # استخدم models.CASCADE هنا
                # "through": through2,
                "related_name": f'{relatedField}',
                "null": True,  # يجب أن تكون القيمة True أو False
                "blank": True,  # يجب أن تكون القيمة True أو False
                "verbose_name": f'{verbose_name}',
            },
        )
        CustomField.objects.create(
            table=model_name,
            field_name=model_name + arabic_to_english(request.POST['field']).replace(" ",""),
            # field_name=  arabic_to_english(request.POST['to']) + arabic_to_english(request.POST['relatedField']).replace(" ",""),
            field_type=request.POST['datatype'].replace("django.db.models.", ""),
            null_or_not=request.POST['null'], 
            unique_or_not=request.POST['unique'],
            blank_or_not=request.POST['null'],
            verbose_name=request.POST['field'],
            is_related= True,
            related_table=arabic_to_english(request.POST['to']),
            related_name= arabic_to_english(request.POST['to']) + arabic_to_english(request.POST['relatedField']).replace(" ",""),
        )

        # تحديث الحقل is_related ليكون True للسجلات التي تلبي الشرط المحدد
        CustomField.objects.filter(table=arabic_to_english(request.POST['to']).replace(" ",""), field_name= arabic_to_english(request.POST['to'])+ arabic_to_english(request.POST['relatedField'])).update(is_related=True)
        modify_delete_behavior()
    except Exception as e:
        messages.error(request, str(e))
        # print("sssss")
        # print(e)

def add_many_to_many_related_field2(request,sys_name_id,model_name, field_name,class_name, is_unique, is_null, to, related_name,verbose_name):
    field_name = model_name + field_name
    relatedField = to + related_name
    another_model_schema1 = ModelSchema.objects.get(name=to)
    another_model_schema2 = ModelSchema.objects.get(name=model_name).as_model()

    another_model_schema = 'test2.DynamicModels' + to.replace(" ", "").capitalize()
   
    model_schema_instance = ModelSchema.objects.get(name=model_name)

    columns = FieldSchema.objects.filter(model_schema=model_schema_instance)
    for field in columns:
        if field.kwargs.get('to')==another_model_schema:
            messages.error(request,'يوجد حقل مرتبط بهذا النموذج',{another_model_schema})
            return redirect('add_field',model_name,sys_name_id)

    try:

        if class_name=="django.db.models.ManyToManyField":

            FieldSchema.objects.create(
                name=field_name,
                model_schema=model_schema_instance,
                class_name=class_name,
                # class_name="django.db.models.ManyToManyField",
                kwargs={
                    "to": another_model_schema,
                    "related_name": f'{relatedField}',
                    "null": is_null,  # يجب أن تكون القيمة True أو False
                    "blank": is_null,  # يجب أن تكون القيمة True أو False
                    "verbose_name": f'{verbose_name}',
                },
            )

        elif class_name =="django.db.models.ForeignKey":

            FieldSchema.objects.create(
                name=field_name,
                model_schema=model_schema_instance,
                class_name=class_name,
                # class_name="django.db.models.ManyToManyField",
                kwargs={
                    "to": another_model_schema,
                    "on_delete": models.CASCADE,  # استخدم models.CASCADE هنا
                    "related_name": f'{relatedField}',
                    "null": is_null,  # يجب أن تكون القيمة True أو False
                    "blank": is_null,  # يجب أن تكون القيمة True أو False
                    "verbose_name": f'{verbose_name}',
                },
            )
        
        CustomField.objects.create(
            table=model_name,
            field_name=field_name,
            field_type=class_name.replace("django.db.models.", ""),
            null_or_not=is_null, 
            unique_or_not=is_unique,
            blank_or_not=is_null,
            verbose_name=verbose_name,
            is_related= True,
            related_table=to,
            related_name= relatedField,
        )
        # تفعيل الحقل الذي تم الارتباط بة من اجل من حذفة اذا حاول المستخدم حذفة
        CustomField.objects.filter(table=to, field_name= relatedField).update(is_related=True)
        modify_delete_behavior()
    except Exception as e:
        messages.error(request, str(e))
        # print("sssss")
        # print(e)


def create_through_table(through_table_name, from_model, to_model):
    """
    ينشئ جدول وسيط ManyToMany بين نموذجين إذا لم يكن موجودًا
    """
    try:
        # التحقق مما إذا كان الجدول الوسيط موجودًا بالفعل
        if through_table_name in connection.introspection.table_names():
            print(f"⚠️ الجدول الوسيط {through_table_name} موجود بالفعل.")
            return apps.get_model('test2', through_table_name)

        class Meta:
            db_table = through_table_name
            unique_together = (('from_model', 'to_model'),)

        # إنشاء النموذج الوسيط ديناميكيًا
        through_model = type(through_table_name, (models.Model,), {
            '__module__': 'test2.models',  # تحديد التطبيق الصحيح
            'id': models.BigAutoField(primary_key=True),
            'from_model': models.ForeignKey(from_model, on_delete=models.CASCADE),
            'to_model': models.ForeignKey(to_model, on_delete=models.CASCADE),
            'Meta': Meta
        })

        # تسجيل النموذج الوسيط
        apps.all_models['test2'][through_table_name.lower()] = through_model
        # print(f"✅ تم إنشاء الجدول الوسيط {through_table_name} بنجاح.")
        return through_model

    except Exception as e:
        print(f"❌ خطأ أثناء إنشاء الجدول الوسيط: {e}")
        return None

# السليمة 100%
def add_field1(request, model_name, sys_name_id ):
    modelss = apps.get_models('test2')
    # print(modelss,"fffffffffffffffffffffffffffff")
    # reload_dynamic_models()
    if not request.user.has_perm(f'test2.create_field_dynamicmodels{model_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        fieldExists = False
        fieldcreated = False
        modelName = Modelnames.objects.exclude(modelname=model_name)
        field_names = CustomField.objects.all()
        
        if request.POST:
            properties = check_field_property(request.POST['datatype'], request.POST['null'], request.POST['maxlen'], request.POST['unique'], request.POST['field'])
            if not "null" in properties and is_model_has_data(model_name)== True:
                messages.error(request, f" حدث خطأ لا يمكن انشاء حقل لا يقبل ان يكون فارغ وقد تم ادخال بيانات في الجدول: ")
            else:
                class_name=request.POST['datatype']
                if class_name == "django.db.models.ForeignKey":
                    try:
                        dynamic_models= 'dynamic_models_'+ request.POST['to']
                        # add_related_field('dynamic_models_'+ model_name, arabic_to_english(request.POST['to']) + arabic_to_english(request.POST['relatedField']).replace(" ",""), 'dynamic_models_'+ arabic_to_english(request.POST['to']).replace(" ","") , "id", "INTEGER")
                        # add_related_field3( model_name,arabic_to_english(request.POST['field'] ),arabic_to_english(request.POST['to']), arabic_to_english(request.POST['relatedField']),request.POST['field'])
                        add_related_field2( model_name,arabic_to_english(request.POST['field'] ),arabic_to_english(request.POST['to']), arabic_to_english(request.POST['relatedField']),request.POST['field'])
                        CustomField.objects.create(
                                    table=model_name,
                                    field_name=model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                                    # field_name=  arabic_to_english(request.POST['to']) + arabic_to_english(request.POST['relatedField']).replace(" ",""),
                                    field_type=request.POST['datatype'].replace("django.db.models.", ""),
                                    null_or_not=request.POST['null'], 
                                    unique_or_not=request.POST['unique'],
                                    blank_or_not=request.POST['null'],
                                    verbose_name=request.POST['field'],
                                    is_related= True,
                                    related_table=arabic_to_english(request.POST['to']),
                                    related_name= arabic_to_english(request.POST['to']) + arabic_to_english(request.POST['relatedField']).replace(" ",""),
                                )
                        
                        # تحديث الحقل is_related ليكون True للسجلات التي تلبي الشرط المحدد
                        CustomField.objects.filter(table=arabic_to_english(request.POST['to']).replace(" ",""), field_name= arabic_to_english(request.POST['to'])+ arabic_to_english(request.POST['relatedField'])).update(is_related=True)
                        modify_delete_behavior()
                        return redirect('manage_models', model_name, sys_name_id )
                    except Exception as e:
                        # إضافة رسالة خطأ للـ messages
                        messages.error(request, f"حدث خطأ: {str(e)}")
                        fieldExists = True
                        return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name,'sys_name_id':sys_name_id, 'error_message': e})
                
                elif class_name=="django.db.models.ManyToManyField":

                    try:
                        dynamic_models= 'dynamic_models_'+ request.POST['to']
                        
                        add_many_to_many_related_field2(request,sys_name_id,model_name,arabic_to_english(request.POST['field']).replace(" ",""), class_name, request.POST['unique'], request.POST['null'], arabic_to_english(request.POST['to']).replace(" ",""), arabic_to_english(request.POST['relatedField']).replace(" ",""),request.POST['field'])
                        # CustomField.objects.create(
                        #             table=model_name,
                        #             field_name=model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                        #             # field_name=  arabic_to_english(request.POST['to']) + arabic_to_english(request.POST['relatedField']).replace(" ",""),
                        #             field_type=request.POST['datatype'].replace("django.db.models.", ""),
                        #             null_or_not=request.POST['null'], 
                        #             unique_or_not=request.POST['unique'],
                        #             blank_or_not=request.POST['null'],
                        #             verbose_name=request.POST['field'],
                        #             is_related= True,
                        #             related_table=arabic_to_english(request.POST['to']),
                        #             related_name= arabic_to_english(request.POST['to']) + arabic_to_english(request.POST['relatedField']).replace(" ",""),
                        #         )
                        
                        # # تحديث الحقل is_related ليكون True للسجلات التي تلبي الشرط المحدد
                        # CustomField.objects.filter(table=arabic_to_english(request.POST['to']).replace(" ",""), field_name= arabic_to_english(request.POST['to'])+ arabic_to_english(request.POST['relatedField'])).update(is_related=True)
                        # modify_delete_behavior()
                        return redirect('manage_models', model_name, sys_name_id )
                    except Exception as e:
                        # إضافة رسالة خطأ للـ messages
                        messages.error(request, f"حدث خطأ: {str(e)}")
                        fieldExists = True
                        return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name,'sys_name_id':sys_name_id, 'error_message': e})
                
                elif class_name == "django.db.models.BooleanField" or class_name == "django.db.models.DateTimeField" or class_name == "django.db.models.ImageField" or class_name == "django.db.models.FileField":
                    try:
                        
                        # properties = check_field_property(request.POST['datatype'], request.POST['null'],request.POST['maxlen'], request.POST['unique'], request.POST['field'])
                        model_schema_instance = ModelSchema.objects.get(name=model_name)
                        FieldSchema.objects.create(
                            name=model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                            class_name=request.POST['datatype'],
                            model_schema=model_schema_instance,
                            kwargs = properties
                            )

                        CustomField.objects.create(
                            table=model_name,
                            field_name=model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                            field_type=request.POST['datatype'].replace("django.db.models.", ""),
                            null_or_not=request.POST['null'], 
                            unique_or_not=request.POST['unique'],
                            blank_or_not=request.POST['null'],
                            # max_length=request.POST['maxlen'],
                            verbose_name=request.POST['field'],
                            related_table=request.POST['to'],
                            related_name= arabic_to_english(request.POST['to'])+ request.POST['relatedField'],
                        )
                        fieldcreated = True
                        modify_delete_behavior()
                        return redirect('manage_models', model_name, sys_name_id )

                    except Exception as e:
                        # إضافة رسالة خطأ للـ messages
                        messages.error(request, f"حدث خطأ: {str(e)}")
                        fieldExists = True
                        return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name,'sys_name_id':sys_name_id, 'error_message': e})
                else:

                    try:
                        # properties = check_field_property(request.POST['datatype'], request.POST['null'], request.POST['maxlen'], request.POST['unique'], request.POST['field'])
                        # print( model_name + arabic_to_english(request.POST['field']))
                        model_schema_instance = ModelSchema.objects.get(name=model_name)
                        FieldSchema.objects.create(
                            name= model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                            class_name=request.POST['datatype'],
                            model_schema=model_schema_instance,
                            kwargs = properties
                            )
                        CustomField.objects.create(
                            table=model_name,
                            field_name= model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                            field_type=request.POST['datatype'].replace("django.db.models.", ""),
                            null_or_not=request.POST['null'], 
                            unique_or_not=request.POST['unique'],
                            blank_or_not=request.POST['null'],
                            max_length=request.POST['maxlen'],
                            verbose_name=request.POST['field'],
                            related_table=request.POST['to'],
                            related_name= arabic_to_english(request.POST['to']) + request.POST['relatedField'],
                        )
                        fieldcreated = True
                        modify_delete_behavior()
                        return redirect('manage_models', model_name,sys_name_id )
                    except Exception as e:
                        # إضافة رسالة خطأ للـ messages
                        messages.error(request, f" حدث خطأ  {str(e)}")
                        fieldExists = True
                        return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name,'sys_name_id':sys_name_id, 'error_message': e})

        return render(request,'add_field.html', context = {'model_name': model_name, 'modelName' : modelName, 'field_names': field_names, 'sys_name_id':sys_name_id})

def add_field(request, model_name, sys_name_id ):
    modelss = apps.get_models('test2')
    
    if not request.user.has_perm(f'test2.create_field_dynamicmodels{model_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        fieldExists = False
        fieldcreated = False
        modelName = Modelnames.objects.exclude(modelname=model_name)
        field_names = CustomField.objects.all()
        
        if request.POST:
            properties = check_field_property(request.POST['datatype'], request.POST['null'], request.POST['maxlen'], request.POST['unique'], request.POST['field'])
            if not "null" in properties and is_model_has_data(model_name)== True:
                messages.error(request, f" حدث خطأ لا يمكن انشاء حقل لا يقبل ان يكون فارغ وقد تم ادخال بيانات في الجدول: ")
            else:
                class_name=request.POST['datatype']
                if class_name == "django.db.models.ForeignKey" or class_name=="django.db.models.ManyToManyField":
                    try:

                        add_many_to_many_related_field2(request,sys_name_id,model_name,arabic_to_english(request.POST['field']).replace(" ",""), class_name, request.POST['unique'], request.POST['null'], arabic_to_english(request.POST['to']).replace(" ",""), arabic_to_english(request.POST['relatedField']).replace(" ",""),request.POST['field'])
                        
                        return redirect('manage_models', model_name, sys_name_id )
                    except Exception as e:
                        # إضافة رسالة خطأ للـ messages
                        messages.error(request, f"حدث خطأ: {str(e)}")
                        fieldExists = True
                        return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name,'sys_name_id':sys_name_id, 'error_message': e})
               
                elif class_name == "django.db.models.BooleanField" or class_name == "django.db.models.DateTimeField" or class_name == "django.db.models.ImageField" or class_name == "django.db.models.FileField":
                    try:  
                        # properties = check_field_property(request.POST['datatype'], request.POST['null'],request.POST['maxlen'], request.POST['unique'], request.POST['field'])
                        model_schema_instance = ModelSchema.objects.get(name=model_name)
                        FieldSchema.objects.create(
                            name=model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                            class_name=request.POST['datatype'],
                            model_schema=model_schema_instance,
                            kwargs = properties
                            )

                        CustomField.objects.create(
                            table=model_name,
                            field_name=model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                            field_type=request.POST['datatype'].replace("django.db.models.", ""),
                            null_or_not=request.POST['null'], 
                            unique_or_not=request.POST['unique'],
                            blank_or_not=request.POST['null'],
                            # max_length=request.POST['maxlen'],
                            verbose_name=request.POST['field'],
                            related_table=request.POST['to'],
                            related_name= arabic_to_english(request.POST['to'])+ request.POST['relatedField'],
                        )
                        fieldcreated = True
                        modify_delete_behavior()
                        return redirect('manage_models', model_name, sys_name_id )

                    except Exception as e:
                        # إضافة رسالة خطأ للـ messages
                        messages.error(request, f"حدث خطأ: {str(e)}")
                        fieldExists = True
                        return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name,'sys_name_id':sys_name_id, 'error_message': e})
                else:

                    try:
                        # properties = check_field_property(request.POST['datatype'], request.POST['null'], request.POST['maxlen'], request.POST['unique'], request.POST['field'])
                        # print( model_name + arabic_to_english(request.POST['field']))
                        model_schema_instance = ModelSchema.objects.get(name=model_name)
                        FieldSchema.objects.create(
                            name= model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                            class_name=request.POST['datatype'],
                            model_schema=model_schema_instance,
                            kwargs = properties
                            )
                        CustomField.objects.create(
                            table=model_name,
                            field_name= model_name + arabic_to_english(request.POST['field']).replace(" ",""),
                            field_type=request.POST['datatype'].replace("django.db.models.", ""),
                            null_or_not=request.POST['null'], 
                            unique_or_not=request.POST['unique'],
                            blank_or_not=request.POST['null'],
                            max_length=request.POST['maxlen'],
                            verbose_name=request.POST['field'],
                            related_table=request.POST['to'],
                            related_name= arabic_to_english(request.POST['to']) + request.POST['relatedField'],
                        )
                        fieldcreated = True
                        modify_delete_behavior()
                        return redirect('manage_models', model_name,sys_name_id )
                    except Exception as e:
                        # إضافة رسالة خطأ للـ messages
                        messages.error(request, f" حدث خطأ  {str(e)}")
                        fieldExists = True
                        return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name,'sys_name_id':sys_name_id, 'error_message': e})

        return render(request,'add_field.html', context = {'model_name': model_name, 'modelName' : modelName, 'field_names': field_names, 'sys_name_id':sys_name_id})



def create_custom_field(model_name, field_name, field_type, pro_null, pro_unique, pro_blank, pro_max_len, pro_verbose_name, related_table=None, related_name=None):
    try:
        CustomField.objects.create(
            table=model_name,
            field_name=field_name,
            field_type=field_type.replace("django.db.models.", ""),
            null_or_not=pro_null, 
            unique_or_not=pro_unique,
            blank_or_not=pro_null,
            max_length=pro_max_len,
            verbose_name=pro_verbose_name,
            related_table=related_table,
            related_name=related_name,
        )
    except Exception as e:
        raise Exception(f"حدث خطأ أثناء إنشاء الحقل: {str(e)}")

def create_field_schema(model_name, field_name, class_name, properties):
    try:
        model_schema_instance = ModelSchema.objects.get(name=model_name)
        FieldSchema.objects.create(
            name=field_name,
            class_name=class_name,
            model_schema=model_schema_instance,
            kwargs=properties
        )
    except Exception as e:
        raise Exception(f"حدث خطأ أثناء إنشاء FieldSchema: {str(e)}")

def add_field1(request, model_name, sys_name_id):
    if not request.user.has_perm(f'test2.add_field_{model_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')

    fieldExists = False
    fieldcreated = False
    modelName = Modelnames.objects.exclude(modelname=model_name)
    field_names = CustomField.objects.all()

    if request.POST:
        properties = check_field_property(request.POST['datatype'], request.POST['null'], request.POST['maxlen'], request.POST['unique'], request.POST['field'])

        if "null" not in properties and is_model_has_data(model_name):
            messages.error(request, f"حدث خطأ لا يمكن انشاء حقل لا يقبل ان يكون فارغ وقد تم ادخال بيانات في الجدول:")
            # print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        else:
            class_name = request.POST['datatype']
            field_name = model_name + arabic_to_english(request.POST['field'])

            # التعامل مع ForeignKey
            if class_name == "django.db.models.ForeignKey":
                try:
                    dynamic_models = f'dynamic_models_{request.POST["to"]}'
                    related_field = arabic_to_english(request.POST["to"]) + arabic_to_english(request.POST["relatedField"])
                    add_related_field(dynamic_models, related_field, f'dynamic_models_{arabic_to_english(request.POST["to"])}', "id", "INTEGER")

                    create_custom_field(model_name, related_field, request.POST['datatype'], request.POST['null'], request.POST['unique'], request.POST['null'], None, request.POST['field'], arabic_to_english(request.POST['to']), related_field)
                    create_field_schema(model_name, related_field, request.POST['datatype'], properties)

                    modify_delete_behavior()
                    return redirect('manage_models', model_name, sys_name_id)

                except Exception as e:
                    messages.error(request, f"حدث خطأ: {str(e)}")
                    fieldExists = True
                    return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name, 'sys_name_id': sys_name_id, 'error_message': e})

            # التعامل مع الأنواع الأخرى
            elif class_name in ["django.db.models.BooleanField", "django.db.models.DateTimeField", "django.db.models.ImageField", "django.db.models.FileField"]:
                try:
                    create_custom_field(model_name, field_name, request.POST['datatype'], request.POST['null'], request.POST['unique'], request.POST['blank'], request.POST['maxlen'], request.POST['field'])
                    create_field_schema(model_name, field_name, request.POST['datatype'], properties)

                    fieldcreated = True
                    modify_delete_behavior()
                    return redirect('manage_models', model_name, sys_name_id)

                except Exception as e:
                    messages.error(request, f"حدث خطأ: {str(e)}")
                    fieldExists = True
                    return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name, 'sys_name_id': sys_name_id, 'error_message': e})

            else:
                try:
                    create_custom_field(model_name, field_name, request.POST['datatype'], request.POST['null'], request.POST['unique'], request.POST['null'], request.POST['maxlen'], request.POST['field'])
                    create_field_schema(model_name, field_name, request.POST['datatype'], properties)

                    fieldcreated = True
                    modify_delete_behavior()
                    return redirect('manage_models', model_name, sys_name_id)

                except Exception as e:
                    messages.error(request, f"حدث خطأ لا يمكن انشاء حقل لا يقبل ان يكون فارغ وقد تم ادخال بيانات في الجدول: {str(e)}")
                    fieldExists = True
                    return render(request, 'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name, 'sys_name_id': sys_name_id, 'error_message': e})

    return render(request, 'add_field.html', context={'model_name': model_name, 'modelName': modelName, 'field_names': field_names, 'sys_name_id': sys_name_id})


# def get_dynamic_model(model_name):
#     # طريقة الاستدعا
#     # model_schema = ModelSchema.objects.get(name=model_name)
#     #     modelss=[]
#     #     for model in model_schema:
#     #         modelss.append(model.as_model())
#     #     print(modelss)
#     try:
#         # model = apps.get_model('dynamic_models', model_name = model_schema)
#         # model = apps.get_model('dynamic_models', model_name = model_name.lower())
#         model = apps.get_model('test2', model_name = 'DynamicModels' + model_name.replace("_", "").capitalize())
#         if model:
#             return model
#     except LookupError:
#         print(f"Model {model_name} not found.")
#     return None


def update_field2(request, model_name, field_id, sys_name_id):
    field_name = FieldSchema.objects.get(id=field_id)
            
    if not check_field_is_related(model_name, field_name):
    
        try:
            # الحصول على ModelSchema المرتبط بالنموذج
            model_schema_instance = ModelSchema.objects.get(name=model_name)

            # البحث عن الحقل باستخدام ID الحقل
            field_schema_instance1 = FieldSchema.objects.get(id=field_id)._get_model_with_field()
            field_schema_instance = FieldSchema.objects.get(id=field_id)
            # print(f"Name from DB: {field_schema_instance1}")  # تحقق من الاسم الذي يتم استرجاعه من قاعدة البيانات
        
        except Exception as e:
            result={'status':1,'message':"  لايمكن تعديل هذا الحقل كونة مرتبط بجدول اخر"}
            return JsonResponse(result)
            return redirect('manage_models', model_name, sys_name_id)
   
        if request.method == 'POST':
            # تحديد الخصائص الجديدة للحقل بناءً على القيم المدخلة
            properties = check_field_property(request.POST['datatype'], request.POST['null'], request.POST.get('blank', False), request.POST['maxlen'], request.POST.get('unique', False), request.POST['field'])

            try:
                
                # تحديث الحقل بناءً على المدخلات الجديدة
                new_field_name = model_name + arabic_to_english(request.POST['field'])

                if field_schema_instance.name != new_field_name:
                    field_schema_instance.name = new_field_name
                
                # تحديث الخصائص
                field_schema_instance.model_schema = model_schema_instance
                field_schema_instance.kwargs = properties

                # حفظ التعديلات في الحقل الحالي
                field_schema_instance.save()

                modify_delete_behavior()
                # make_migrations_and_migrate('test2')

                return redirect('manage_models', model_name, sys_name_id)

            except Exception as e:
                print(f"Error while updating field in model: {e}")
                return render(request, 'update_field.html', {'field': field_schema_instance, 'model_name': model_name, 'sys_name_id': sys_name_id})

    return render(request, 'update_field.html', {'field': field_schema_instance, 'model_name': model_name, 'sys_name_id': sys_name_id})

def update_field(request, model_name, field_id, sys_name_id):
    try:
        # استرجاع الحقل بناءً على الـ ID
        field_name1 = FieldSchema.objects.get(id=field_id)
        table_name = Modelnames.objects.get(modelname=model_name).modelnameAr
        model_schema_instance = ModelSchema.objects.get(name=model_name)
        field_name = FieldSchema.objects.filter(model_schema=model_schema_instance, name=field_name1).first()
        # print(field_name)
        # التحقق مما إذا كان الحقل مرتبطًا بجدول آخر
        if not check_field_is_related(model_name, field_name):
            # استرجاع ModelSchema المرتبط بالنموذج
            model_schema_instance = ModelSchema.objects.get(name=model_name)
            
            field_schema_instance1 = FieldSchema.objects.get(id=field_id)._get_model_with_field()

            # البحث عن الحقل باستخدام ID الحقل واسترجاع النموذج المرتبط به
            field_schema_instance = FieldSchema.objects.get(id=field_id)
            
            if request.method == 'POST':
                try:
                    # الحصول على الخصائص الجديدة التي سيتم تحديث الحقل بها
                    properties = check_field_property(
                        request.POST['datatype'], 
                        request.POST['null'], 
                        # request.POST.get('blank', False), 
                        request.POST['maxlen'], 
                        request.POST['unique'], 
                        request.POST['field']
                    )
                    
                    # تحديث الحقل بناءً على المدخلات الجديدة
                    new_field_name = model_name + arabic_to_english(request.POST['field']).replace(" ","")
                    
                    # إذا كان الاسم الجديد مختلفًا عن الاسم الحالي
                    if field_schema_instance.name != new_field_name:
                        field_schema_instance.name = new_field_name
                    
                    # تحديث الخصائص الأخرى
                    field_schema_instance.model_schema = model_schema_instance
                    if (field_name.kwargs["max_length"] < properties["max_length"]) or (field_name.kwargs["max_length"] == properties["max_length"]) :
                        field_schema_instance.kwargs = properties
                        # حفظ التعديلات في الحقل
                        field_schema_instance.save()

                        update_custom_field(request,model_name,new_field_name)

                        UserAction.objects.create(user=request.user,action="تعديل حقل ",model_name=table_name, details=properties)

                        # تنفيذ أي سلوكيات إضافية بعد التعديل (مثل تعديل الحقل في قاعدة البيانات)
                        modify_delete_behavior()

                        # إعادة التوجيه إلى الصفحة التي تعرض النماذج
                        return redirect('manage_models', model_name, sys_name_id)
                    else:
                        messages.error(request, "طول الحقل اسغر من القيمة السابقة")
                        return render(request, 'update_field.html', {'field': field_schema_instance, 'model_name': model_name, 'sys_name_id': sys_name_id})

                except Exception as e:
                    messages.error(request, e)
                    return render(request, 'update_field.html', {'field': field_schema_instance, 'model_name': model_name, 'sys_name_id': sys_name_id})

        else:
            # إذا كان الحقل مرتبطًا بجدول آخر
            messages.error(request, "لا يمكن تعديل هذا الحقل لأنه مرتبط بجدول آخر" )
            return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)
        
    except Exception as e:
        # التقاط أي أخطاء غير متوقعة
        
        messages.error(request, "حدث خطأ أثناء تحديث الحقل" )
        return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)

    # في حالة عدم وجود POST (عند التحميل الأولي للصفحة)
    return render(request, 'update_field.html', {'field': field_schema_instance, 'model_name': model_name, 'sys_name_id': sys_name_id})



def update_custom_field(request, model_name, custom_field_id):
    """
    دالة لتعديل بيانات نموذج CustomField بناءً على البيانات التي يتم إرسالها عبر request.POST.
    
    :param request: الكائن الذي يحتوي على البيانات المرسلة من النموذج
    :param custom_field_id: معرف السجل الذي تريد تعديله
    :return: السجل المعدل
    """
    # الحصول على السجل بناءً على ID
    # custom_field = get_object_or_404(CustomField, id=custom_field_id)
    custom_field = CustomField.objects.filter(table=model_name, field_name=custom_field_id).first()

    # استرجاع البيانات من request.POST مع التحقق من القيم
    field_name = model_name + arabic_to_english(request.POST['field']).replace(" ","")
    field_type = request.POST['datatype'].replace("django.db.models.", ""),
    max_length = request.POST['maxlen']
    null_or_not = request.POST['null']
    verbose_name = request.POST['field']
    unique_or_not = request.POST['unique']
    
    # تحديث الحقول إذا كانت موجودة في request.POST
    if field_name:
        custom_field.field_name = field_name
    if verbose_name:
        custom_field.verbose_name = verbose_name
    if field_type:
        custom_field.field_type = field_type
    if max_length:
        custom_field.max_length = int(max_length)  # تحويل القيمة إلى عدد صحيح إذا كانت موجودة
    if null_or_not is not None:
        custom_field.null_or_not = null_or_not  # تحويل القيمة إلى True أو False
    # if blank_or_not is not None:
    #     custom_field.blank_or_not = blank_or_not.lower() == 'true'  # نفس الشيء مع blank
    if unique_or_not is not None:
        custom_field.unique_or_not = unique_or_not  # نفس الشيء مع unique
    
    # حفظ التعديلات
    custom_field.save()

    return custom_field


from django.contrib import messages



# def create_field(request, model_name, field_type, field_properties):
#     try:
#         # استخراج الخصائص من الفورم
#         properties = check_field_property(field_properties['datatype'], field_properties['null'], field_properties['blank'],
#                                           field_properties['maxlen'], field_properties['unique'], field_properties['field'])

#         # استرجاع ModelSchema
#         model_schema_instance = ModelSchema.objects.get(name=model_name)

#         # إنشاء FieldSchema
#         FieldSchema.objects.create(
#             name=model_name + arabic_to_english(field_properties['field']),
#             class_name=field_properties['datatype'],
#             model_schema=model_schema_instance,
#             kwargs=properties
#         )

#         # إنشاء CustomField
#         CustomField.objects.create(
#             table=model_name,
#             field_name=model_name + arabic_to_english(field_properties['field']),
#             field_type=field_properties['datatype'].replace("django.db.models.", ""),
#             null_or_not=field_properties['null'],
#             unique_or_not=field_properties['unique'],
#             blank_or_not=field_properties['blank'],
#             max_length=field_properties.get('maxlen', None),
#             verbose_name=field_properties['field'],
#             related_table=field_properties.get('to', None),
#             related_name=arabic_to_english(field_properties.get('to', '')) + arabic_to_english(field_properties.get('relatedField', '')),
#         )
        
#         return True, None
#     except Exception as e:
#         return False, str(e)

# def add_field(request, model_name):
#     if not request.user.has_perm('dynamic_models.add_fieldschema'):
#         messages.error(request, 'لايوجد لديك صلاحية')
#         return redirect('confirm_perm')

#     modelName = Modelnames.objects.all()
#     field_names = CustomField.objects.all()
    
#     if request.POST:
#         class_name = request.POST['datatype']
#         field_properties = {
#             'datatype': class_name,
#             'null': request.POST['null'],
#             'unique': request.POST['unique'],
#             'blank': request.POST['blank'],
#             'field': request.POST['field'],
#             'maxlen': request.POST.get('maxlen', None),
#             'to': request.POST.get('to', None),
#             'relatedField': request.POST.get('relatedField', None)
#         }

#         # التعامل مع الأنواع المختلفة للحقول
#         if class_name == "django.db.models.ForeignKey":
#             fieldExists, error_message = create_field(request, model_name, class_name, field_properties)
#             if fieldExists:
#                 modify_delete_behavior()
#                 return redirect('manage_models', model_name)
#             else:
#                 messages.error(request, f"حدث خطأ: {error_message}")
#                 return render(request, 'add_field.html', context={"fieldExists": True, 'model_name': model_name, 'error_message': error_message})

#         elif class_name in ["django.db.models.BooleanField", "django.db.models.DateTimeField", "django.db.models.ImageField", "django.db.models.FileField"]:
#             fieldExists, error_message = create_field(request, model_name, class_name, field_properties)
#             if fieldExists:
#                 modify_delete_behavior()
#                 return redirect('manage_models', model_name)
#             else:
#                 messages.error(request, f"حدث خطأ: {error_message}")
#                 return render(request, 'add_field.html', context={"fieldExists": True, 'model_name': model_name, 'error_message': error_message})

#         else:
#             fieldExists, error_message = create_field(request, model_name, class_name, field_properties)
#             if fieldExists:
#                 modify_delete_behavior()
#                 return redirect('manage_models', model_name)
#             else:
#                 messages.error(request, f"حدث خطأ: {error_message}")
#                 return render(request, 'add_field.html', context={"fieldExists": True, 'model_name': model_name, 'error_message': error_message})

#     return render(request, 'add_field.html', context={'model_name': model_name, 'modelName': modelName, 'field_names': field_names})


# سليمة
# def add_field(request, model_name):
#     if not request.user.has_perm('dynamic_models.add_fieldschema'):
#         messages.error(request, 'لايوجد لديك صلاحية')
#         return redirect('confirm_perm')
#     else:
#         fieldExists = False
#         fieldcreated = False
#         modelName = Modelnames.objects.all()
#         field_names = CustomField.objects.all()
#         if request.POST:
#             class_name=request.POST['datatype']
#             if class_name == "django.db.models.ForeignKey":
#                 try:

#                     dynamic_models= 'dynamic_models_'+ request.POST['to']
#                     add_related_field('dynamic_models_'+ model_name, arabic_to_english(request.POST['relatedField']), 'dynamic_models_'+ arabic_to_english(request.POST['to']) , "id", "INTEGER")
#                     CustomField.objects.create(
#                                 table=model_name,
#                                 field_name=arabic_to_english(request.POST['relatedField']),
#                                 field_type=request.POST['datatype'].replace("django.db.models.", ""),
#                                 null_or_not=request.POST['null'], 
#                                 unique_or_not=request.POST['unique'],
#                                 blank_or_not=request.POST['blank'],
#                                 # max_length=request.POST['maxlen'],
#                                 verbose_name=request.POST['field'],
#                                 is_related= True,
#                                 related_table=arabic_to_english(request.POST['to']),
#                                 related_name=arabic_to_english(request.POST['relatedField']),
#                             )
                    
#                     # تحديث الحقل is_related ليكون True للسجلات التي تلبي الشرط المحدد
#                     CustomField.objects.filter(table=arabic_to_english(request.POST['to']), field_name=arabic_to_english(request.POST['relatedField'])).update(is_related=True)
#                     modify_delete_behavior()
#                     return redirect('manage_models', model_name)
#                 except Exception as e: 
#                     fieldExists = True
#                     return render(request,'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated, 'model_name': model_name})
#                     print(e)

#             elif class_name == "django.db.models.BooleanField" or class_name == "django.db.models.DateTimeField" or class_name == "django.db.models.FileField" :
#                 try:
#                     properties = check_field_property(request.POST['unique'], request.POST['null'], request.POST['blank'],request.POST['maxlen'], request.POST['datatype'], request.POST['field'])
#                     model_schema_instance = ModelSchema.objects.get(name=model_name)
#                     FieldSchema.objects.create(
#                         name=arabic_to_english(request.POST['field']),
#                         class_name=request.POST['datatype'],
#                         model_schema=model_schema_instance,
#                         kwargs = properties
#                         )
#                     CustomField.objects.create(
#                         table=model_name,
#                         field_name=arabic_to_english(request.POST['field']),
#                         field_type=request.POST['datatype'].replace("django.db.models.", ""),
#                         null_or_not=request.POST['null'], 
#                         unique_or_not=request.POST['unique'],
#                         blank_or_not=request.POST['blank'],
#                         # max_length=request.POST['maxlen'],
#                         verbose_name=request.POST['field'],
#                         # on_delete=request.POST['on_delete' + str(count)],
#                         related_table=request.POST['to'],
#                         related_name=request.POST['relatedField'],
#                     )
#                     fieldcreated = True
#                     modify_delete_behavior()
#                     return redirect('manage_models', model_name)

#                 except Exception as e:
#                     fieldExists = True
#                     return render(request,'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated})
            
#             else: 
#                 try:
#                     properties = check_field_property(request.POST['unique'], request.POST['null'], request.POST['blank'],request.POST['maxlen'], request.POST['datatype'], request.POST['field'])
#                     model_schema_instance = ModelSchema.objects.get(name=model_name)
#                     FieldSchema.objects.create(
#                         name=arabic_to_english(request.POST['field']),
#                         class_name=request.POST['datatype'],
#                         model_schema=model_schema_instance,
#                         kwargs = properties
#                         )
#                     CustomField.objects.create(
#                         table=model_name,
#                         field_name=arabic_to_english(request.POST['field']),
#                         field_type=request.POST['datatype'].replace("django.db.models.", ""),
#                         null_or_not=request.POST['null'], 
#                         unique_or_not=request.POST['unique'],
#                         blank_or_not=request.POST['blank'],
#                         max_length=request.POST['maxlen'],
#                         verbose_name=request.POST['field'],
#                         # on_delete=request.POST['on_delete' + str(count)],
#                         related_table=request.POST['to'],
#                         related_name=request.POST['relatedField'],
#                     )
#                     fieldcreated = True
#                     modify_delete_behavior()
#                     return redirect('manage_models', model_name)

#                 except Exception as e:
#                     fieldExists = True
#                     return render(request,'add_field.html', context={"fieldExists": fieldExists, 'fieldcreated': fieldcreated})
    
#         return render(request,'add_field.html', context = {'model_name': model_name, 'modelName' : modelName, 'field_names': field_names})


# def create_migration_for_dynamic_model(model_class):
#     # إنشاء ملف migration يدويًا
#     call_command('makemigrations', model_class._meta.app_label)
#     call_command('migrate')

# مستخدمة
def is_model_has_data(model_name):
    model = get_dynamic_model(model_name)
    if model is None:
        return HttpResponse("الجدول غير موجود او ان هناك خطاء ما", status=404)
    
    model_data = model.objects.all()
    if model_data:
        return True
    else:
        return False
    # return model_data

def check_field_property2(pro_field_type, pro_unique, pro_null, pro_blank, pro_max_length, pro_verbose_name):
    kwargs = {}

    # إذا كان الحقل ليس من الأنواع الخاصة (BooleanField, DateTimeField, FileField, ImageField)
    if pro_field_type not in ["django.db.models.BooleanField", "django.db.models.DateTimeField", "django.db.models.FileField", "django.db.models.ImageField"]:
        kwargs["max_length"] = pro_max_length

    # إذا كان نوع الحقل ImageField، نحدد مكان التحميل
    if pro_field_type == "django.db.models.ImageField":
        kwargs["upload_to"] = 'media/images/'

    # إذا كان نوع الحقل FileField، نحدد مكان التحميل
    if pro_field_type == "django.db.models.FileField":
        kwargs["upload_to"] = 'media/'

    # إذا كان pro_unique هو True، نحدد الخاصية unique
    if pro_unique:  # من المفترض أن تكون قيمة منطقية، لذا لا تقارن مع السلسلة "True"
        kwargs["unique"] = True

    # إذا كان pro_null هو True، نحدد الخاصية null
    if pro_null:
        kwargs["null"] = True

    # إذا كان pro_blank هو True، نحدد الخاصية blank
    if pro_blank:
        kwargs["blank"] = True

    # إضافة verbose_name
    kwargs["verbose_name"] = pro_verbose_name

    return kwargs


def check_field_property(pro_field_type, pro_null, pro_max_lenth, pro_unique, pro_verbose_name):
    kwargs = {}
    
    # إذا كان الحقل ليس من الأنواع الخاصة (BooleanField, DateTimeField, FileField, ImageField)
    if pro_field_type not in ["django.db.models.BooleanField", "django.db.models.DateTimeField", "django.db.models.FileField", "django.db.models.ImageField"]:
        kwargs["max_length"] = pro_max_lenth

    # إذا كان نوع الحقل ImageField، نحدد مكان التحميل
    if pro_field_type == "django.db.models.ImageField":
        kwargs["upload_to"] = 'media/images/'

    # إذا كان نوع الحقل FileField، نحدد مكان التحميل
    if pro_field_type == "django.db.models.FileField":
        kwargs["upload_to"] = 'media/'

    # إذا كان pro_unique هو "True"، نحدد الخاصية unique
    if pro_unique == "False":
        kwargs["unique"] = True

    # إذا كان pro_null هو "True"، نحدد الخاصية null
    if pro_null == "True":
        kwargs["null"] = True
        kwargs["blank"] = True


    # إذا كان pro_blank هو "True"، نحدد الخاصية blank
    # if pro_blank == "True":
    #     kwargs["blank"] = True

    # إضافة verbose_name
    kwargs["verbose_name"] = pro_verbose_name

    return kwargs

def arabic_to_english(word):
    translation_dict = {
        'ا': 'a',
        'ب': 'b',
        'ت': 't',
        'ث': 'th',
        'ج': 'j',
        'ح': 'h',
        'خ': 'kh',
        'د': 'd',
        'ذ': 'th',
        'ر': 'r',
        'ز': 'z',
        'س': 's',
        'ش': 'sh',
        'ص': 's',
        'ض': 'd',
        'ط': 't',
        'ظ': 'th',
        'ع': 'a',
        'غ': 'gh',
        'ف': 'f',
        'ق': 'q',
        'ك': 'k',
        'ل': 'l',
        'م': 'm',
        'ن': 'n',
        'ه': 'h',
        'و': 'w',
        'ي': 'y',
        'ة': 'h',
        'لا': 'la',
        'ؤ': 'w',
        'ء': 'a',
        'ئ': 'y',
        'ى': 'a',
        'إ': 'i',
        'أ': 'a',
        'آ': 'a',
        # ' ': '_',
    }
    
    translated_word = ''
    for char in word:
        if char in translation_dict:
            translated_word += translation_dict[char]
        else:
            translated_word += char
    
    return translated_word

def english_to_arabic(word):
    translation_dict = {
        'a': 'ا',
        'b': 'ب',
        't': 'ت',
        'th': 'ث',
        'j': 'ج',
        'h': 'ح',
        'kh': 'خ',
        'd': 'د',
        'r': 'ر',
        'z': 'ز',
        's': 'س',
        'sh': 'ش',
        's': 'ص',
        'd': 'ض',
        't': 'ط',
        'th': 'ظ',
        'a': 'ع',
        'gh': 'غ',
        'f': 'ف',
        'q': 'ق',
        'k': 'ك',
        'l': 'ل',
        'm': 'م',
        'n': 'ن',
        'h': 'ه',
        'w': 'و',
        'y': 'ي',
        'h': 'ة',
        'la': 'لا',
        'w': 'ؤ',
        'a': 'ء',
        'y': 'ئ',
        'a': 'ى',
        'i': 'إ',
        'a': 'أ',
        'a': 'آ',
        '_': ' ',
    }

    translated_word = ''
    for char in word:
        if char in translation_dict:
            translated_word += translation_dict[char]
        else:
            translated_word += char
    
    return translated_word

from django.contrib.auth.models import Permission
 
def index1(request):
    models = Modelnames.objects.all()
    tables = ModelSchema.objects.all()
    # modify_delete_behavior()
    # make_migrations_and_migrate('test2')
    
    # delete_custom_permissions_for_all_models()
    systems = TblSystem.objects.all()
    if request.method == 'POST':
        form = TblSystemForm(request.POST)
        if form.is_valid():
            subproject = form.save()
            return redirect('index')
    else:
        form = TblSystemForm()
    
    return render(request, 'base.html', {'form': form, 'systems': systems, 'tables': tables, 'models': models})
   

# view_المخازن'

# @login_required
def index(request):
    # print(request.user.get_all_permissions())
    # modify_delete_behavior()
    # delete_custom_permissions_for_all_models()

    models = Modelnames.objects.all()
    tables = ModelSchema.objects.all()

    # تصفية الأنظمة بناءً على صلاحيات المستخدم
    systems = TblSystem.objects.filter(
        id__in=[system.id for system in TblSystem.objects.all() if request.user.has_perm('dynmic_table.'+system.name+'_view')]
    )

    if request.method == 'POST':
        form = TblSystemForm(request.POST)
        if form.is_valid():
            subproject = form.save()
            return redirect('index')
    else:
        form = TblSystemForm()

    return render(request, 'base.html', {'form': form, 'systems': systems, 'tables': tables, 'models': models})

def system_manage(request):
    if not request.user.has_perm('dynmic_table.view_tblsystem'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        if request.method == 'POST':
            form = TblSystemForm(request.POST)
            if form.is_valid():
                subproject = form.save()
                return redirect('index')
        else:
            form = TblSystemForm()
            systems = TblSystem.objects.all()
            users = User.objects.all()

        return render(request, 'system_manage.html', {'form': form,})

def subproject_detail(request, sys_name_id):
    # modify_delete_behavior()
    # make_migrations_and_migrate('test2')
    # delete_custom_permissions_for_all_models()
    
    sys_name = TblSystem.objects.get(id=sys_name_id).name
    # print('dynmic_table.'+sys_name+'_view')
    # if not request.user.has_perm('dynmic_table.'+sys_name+'_view'):
    if not request.user.has_perm('dynmic_table.view_'+sys_name):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        subproject = get_object_or_404(TblSystem, id=sys_name_id)
        make_migrations_and_migrate('test2')
        # run_migrations_for_app('test2')
        # make_migrations_and_migrate('dynamic_models')


        # models = Modelnames.objects.all()
        # print(subproject)
        model_schema = ModelSchema.objects.all()
        # modelss = ModelSchema.objects.all()
        models = Modelnames.objects.filter(sys_name=subproject)
        # print(models)
        
        # for model in models:
        #     models2.append(get_dynamic_model(model.modelname)) 
        # print(models2)
        return render(request, 'subproject_detail.html', {'subproject': subproject, 'models': models, 'sys_name_id':sys_name_id})

def subprojects_manage(request):
    if not request.user.has_perm('dynmic_table.view_tblsystem'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        systems = TblSystem.objects.all()

        return render(request, 'subprojects_manage.html', {'systems': systems})

def subprojects_edit(request,sys_name_id):
    if not request.user.has_perm('dynmic_table.change_tblsystem'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        system = TblSystem.objects.get(id=sys_name_id)
        if request.method == 'POST':
            form = TblSystemForm(request.POST, request.FILES, instance=system)
            if form.is_valid():
                # الحصول على البيانات المدخلة في الفورم
                form_data = form.cleaned_data
                form.save()
                # subproject = form.save()
                return redirect('subprojects_manage')
        else:
            form = TblSystemForm(instance=system)

        return render(request, 'subprojects_edit.html',{'form': form} )


def subprojects_delete(request, sys_name_id):
    if not request.user.has_perm('dynmic_table.delete_tblsystem'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        # استرجاع الـ system (subproject) بناءً على ID
        system = get_object_or_404(TblSystem, id=sys_name_id)
        
        # التحقق إذا كان هناك نماذج مرتبطة بالـ subproject
        related_models = Modelnames.objects.filter(sys_name=sys_name_id)
        
        if related_models.exists():
            # إذا كان هناك نماذج مرتبطة بالـ subproject، منع الحذف
            messages.error(request, "لا يمكن حذف هذا الـنظام لأنه يحتوي على نماذج مرتبطة.")
            return redirect('subprojects_manage')
        
        # إذا لم يكن هناك نماذج مرتبطة، استكمال عملية الحذف
        try:
            system.delete()
            # يمكنك أيضًا إضافة سجل في جدول الإجراءات للمستخدم
            UserAction.objects.create(
                user=request.user,
                action="حذف نظام",
                model_name=system.name,
                details=str(system)
            )
            messages.success(request, "تم الحذف بنجاح")
            return redirect('subprojects_manage')
        except Exception as e:
            messages.error(request, f"حدث خطأ أثناء الحذف: {e}")
            return redirect('subprojects_manage')

        
        # return render(request, 'subprojects_manage.html')

# def models_manage(request, model_name):
#     if not request.user.has_perm('test2.can_view_model_dynamicmodels'+model_name):
#         messages.error(request, 'لايوجد لديك صلاحية')
#         return redirect('confirm_perm')
#     else:
#         fields = CustomField.objects.filter(table=model_name)
#         # fields = FieldSchema.objects.filter(model_schema=2)
#         # modify_delete_behavior()
#         return render(request, 'manage_models.html', {'model_name': model_name, 'fields': fields})


from django.shortcuts import render
from .forms import PermissionForm
from django.http import HttpResponse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps


def get_model_with_field(table_name):
    model = table_name.as_model()
    try:
        # field = model._meta.get_field(self.db_column)
        field = model._meta.get_fields()
    except FieldDoesNotExist:
        field = None
    return model, field

import json
from dynamic_models.schema import FieldSchemaEditor, ModelSchemaEditor
from dynamic_models.utils import db_table_exists, db_table_has_field
from .utils import alter_column
from django.db import connection

def alter_column_view(model_name, field_name):
    try:
        # تنفيذ استعلام SQL لتغيير خصائص الحقل ليقبل القيمة NULL
        with connection.cursor() as cursor:
            cursor.execute(f"ALTER TABLE your_table_name ALTER COLUMN {field_name} DROP NOT NULL;")
        
        print(f"تم تغيير خصائص الحقل {field_name} بنجاح ليقبل القيمة NULL")
        
    except Exception as e:
        print("حدث خطأ أثناء تعديل الحقل:", e)

def alter_column_name(model_name, old_field, new_field_name):
    validate_identifier(model_name, "model_name")
    validate_identifier(old_field, "old_field")
    validate_identifier(new_field_name, "new_field_name")
    table_name = 'dynamic_models_' + model_name
    try:
        # تنفيذ استعلام SQL لتغيير اسم الحقل
        with connection.cursor() as cursor:
            cursor.execute(f"ALTER TABLE {table_name} RENAME COLUMN {old_field} TO {new_field_name};")

        modify_delete_behavior()
    except Exception as e:
        print("alter_column_name error:", e)


def update_field_allow_null(model_name, field_name):
    validate_identifier(model_name, "model_name")
    validate_identifier(field_name, "field_name")
    table_name = 'dynamic_models_' + model_name
    try:
        # تنفيذ استعلام SQL لتغيير خصائص الحقل ليقبل القيمة NULL
        with connection.cursor() as cursor:
            cursor.execute(f"ALTER TABLE {table_name} ALTER COLUMN {field_name} DROP NOT NULL;")
        
        # الحصول على اسم القيد الفريد المرتبط بالحقل المعطى
        unique_constraint_name = f"{table_name}_{field_name}_key"
        
        # تنفيذ استعلام SQL لإزالة القيد الفريد (Unique Constraint) باستخدام اسم الحقل المعطى
        with connection.cursor() as cursor:
            cursor.execute(f"ALTER TABLE {table_name} DROP CONSTRAINT {unique_constraint_name};")
        
        modify_delete_behavior()
        print(f"تم تغيير خصائص الحقل {field_name} بنجاح ليقبل القيمة NULL ويكون فلزًا (non-unique)")
        
    except Exception as e:
        print("update_field_allow_null error:", e)



gid=0
def display_data(request,id,sys_name_id):
    global gid
    gid = id
    print(id,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    # modify_delete_behavior()
    # make_migrations_and_migrate('dynamic_models')
    if not request.user.has_perm(f'test2.view_dynamicmodels{id}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
    # print(request.user.get_all_permissions())
        model_schema = ModelSchema.objects.get(name=id)

        model_na = ModelSchema.objects.get(name=id)
        model_name = model_na.name
        model_name2 = model_name
        model_name_for_data = 'DynamicModels' + model_name.replace("_", "").capitalize()
        # model = model_schema.as_model()
        model = get_dynamic_model(model_name)
        if model is None:
            messages.error(request,"الجدول غير موجود او ان هناك خطاء ما")
            return redirect('index')

    
        queryset = model.objects.all()
        fields = CustomField.objects.filter(table=model_name2)
        models = Modelnames.objects.all()
        modelnamear = Modelnames.objects.get(modelname=model_name2)
        
        # systems = TblSystem.objects.all()
        # df = select_columns_name(model_name2)
        table_html = generate_table(queryset, model_name2,sys_name_id)
        
        return render(request, 'display_data.html', { 'sys_name_id':sys_name_id,'modelnamear': modelnamear, 'fields': fields, 'table_html': table_html,'model_name': model_name, 'models': models})  
        # return render(request, 'display_data.html', { 'sys_name_id':sys_name_id,'modelnamear': modelnamear, 'model_data': model_data, 'fields': fields, 'df': df, 'table_html': table_html, 'dynamic_form': dynamic_form, 'model_name': model_name, 'systems': systems, 'models': models})  

from django.db.models import Q

def report_view2(request, table_name):
    form_class = create_dynamic_form(table_name)
    model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
    model = apps.get_model(app_label='test2', model_name=model_name)
    queryset = model.objects.all()
    table_html = generate_table(queryset, table_name)
    fields = CustomField.objects.filter(table=table_name)
    # print(fields)
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            search_query = {}
            for field_name, field_value in form.cleaned_data.items():
                if field_value:
                    search_query[field_name] = field_value

            if search_query:
                query = Q(**search_query)
                queryset = model.objects.filter(query)

                selected_columns = request.POST.getlist('selected_columns')
                table_html = generate_table(queryset, table_name, selected_columns=selected_columns)
    else:
        form = form_class()

    return render(request, 'report_page.html', {'form': form, 'table_html': table_html, 'table_columns': fields})


def report_view1(request, table_name, sys_name_id):
    form_class = create_dynamic_form(table_name)
    model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
    model = get_dynamic_model(table_name)
    # model = apps.get_model(app_label='test2', model_name=model_name)
    queryset = model.objects.all()
    table_html = create_report_table(queryset, table_name,sys_name_id)
    fields = CustomField.objects.filter(table=table_name)
    data_report_header = CustmReportHeader.objects.all()

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            search_query = {}
            for field_name, field_value in form.cleaned_data.items():
                if field_value:
                    search_query[field_name] = field_value

            if search_query:
                query = Q(**search_query)
                queryset = model.objects.filter(query)
                table_html = create_report_table(queryset, table_name,sys_name_id)

    else:
        form = form_class()

    return render(request, 'report_page.html', {'sys_name_id':sys_name_id,'table_name':table_name, 'form': form, 'table_html': table_html, 'table_columns':fields, 'data_report_header': data_report_header})


def report_view(request, table_name, sys_name_id):
    # استرجاع النموذج الديناميكي
    form_class = create_dynamic_form_for_seach(table_name)
    model = get_dynamic_model(table_name)  

    # استرجاع جميع السجلات بشكل افتراضي
    queryset = model.objects.all()
    
    # إنشاء الجدول المبدئي
    table_html = create_report_table(queryset, table_name, sys_name_id)
    
    # استرجاع الحقول المخصصة
    fields = CustomField.objects.filter(table=table_name)
    data_report_header = CustmReportHeader.objects.all()

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            search_query = Q()  # إنشاء كائن البحث المتعدد

            for field_name, field_value in form.cleaned_data.items():
                if field_value:
                    try:
                        field = model._meta.get_field(field_name)  # الحصول على معلومات الحقل

                        # ✅ إذا كان الحقل `ForeignKey`
                        if field.is_relation and isinstance(field, models.ForeignKey):
                            search_query &= Q(**{f"{field_name}__exact": field_value})
                        
                        # ✅ إذا كان الحقل `ManyToManyField`
                        elif field.is_relation and isinstance(field, models.ManyToManyField):
                            search_query &= Q(**{f"{field_name}__in": field_value})

                        # ✅ إذا كان الحقل نصيًا أو عددًا عاديًا
                        else:
                            search_query &= Q(**{f"{field_name}__icontains": field_value})

                    except FieldDoesNotExist:
                        messages.error(f"⚠️ الحقل {field_name} غير موجود في الجدول {table_name}")
                        # print(f"⚠️ الحقل {field_name} غير موجود في الجدول {table_name}")

            # تنفيذ البحث
            queryset = model.objects.filter(search_query)
            table_html = create_report_table(queryset, table_name, sys_name_id)

    else:
        form = form_class()

    return render(request, 'report_page.html', {
        'sys_name_id': sys_name_id,
        'table_name': table_name,
        'form': form,
        'table_html': table_html,
        'table_columns': fields,
        'data_report_header': data_report_header
    })


def user_action(request):
    form = UserActionForm()
    actions = UserAction.objects.all()

    if request.method == 'POST':
        form = UserActionForm(request.POST)
        if form.is_valid():
            search_query = {}

            # إضافة الحقول التي تم ملؤها في الاستعلام
            for field_name, field_value in form.cleaned_data.items():
                if field_value:
                    if field_name in ['action', 'model_name', 'user']:  # البحث في الحقول المناسبة
                        search_query[field_name] = field_value

            # إضافة البحث بين تاريخين إذا كان هناك قيم للتواريخ
            timestamp_from = form.cleaned_data.get('timestamp_from')
            timestamp_to = form.cleaned_data.get('timestamp_to')

            if timestamp_from:
                search_query['timestamp__gte'] = timestamp_from  # >= للتاريخ من
            if timestamp_to:
                search_query['timestamp__lte'] = timestamp_to  # <= للتاريخ إلى

            if search_query:
                actions = UserAction.objects.filter(Q(**search_query))

        return render(request, 'user_action.html', {'form': form, 'actions': actions})
    
    return render(request, 'user_action.html', {'form': form, 'actions': actions})


def user_action1(request,table_name):
    form_class = UserActionForm()
    actions = UserAction.objects.all()
    
    if request.method == 'POST':
        form = UserActionForm(request.POST)
        if form.is_valid():
            search_query = {}
            for field_name, field_value in form.cleaned_data.items():
                if field_value:
                    search_query[field_name] = field_value

            if search_query:
                query = Q(**search_query)
                actions = UserAction.objects.filter(query)

        return render(request, 'user_action.html', {'form': form,  'actions': actions})
                
    else:
        form =  UserActionForm()

    return render(request, 'user_action.html', {'form': form,  'actions': actions})


from django.db import models

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm

def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_user')  
    else:
        form = CustomUserCreationForm()
        # per = CustomUserCreationForm().clean
        # print(per)
        # form = UserCreationForm()
    return render(request, 'add_user.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             # print(username)
#             # print("eeeeeeeeeeeeee")
#             password = form.cleaned_data['password']
#             # print(password)
#             # print("pppppppppppppp")
#             user = CustomUser.objects.filter(username=username, password=password)
#             print(user,"gggggggggggggggggggggggggggggggggggggg")
#             # user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 # Redirect to a success page
#                 return redirect('index')
#             else:
#                 # Return an 'invalid login' error message
#                 messages.error(request, 'Invalid email or password. Please try again.')
#         else:
#             # Handle form validation errors
#             messages.error(request, 'Invalid form data. Please correct the errors.')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout



from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser  # استيراد نموذج CustomUser

from django.contrib.auth.models import User


def manage_user(request):
    # user = CustomUser.objects.all()
    users = User.objects.all()
    return render(request, 'manage_user.html', {'users': users})



def confirm_perm(request):
    if messages.error:
        return render(request, 'confirm_perm.html',{'': ''})
    else:
        messages.error(request, 'لايوجد لديك صلاحية')
        return render(request, 'confirm_perm.html',{'': ''})


def select_columns_name(model_name):
    table = 'dynamic_models_'+ model_name
    fields = CustomField.objects.filter(table=model_name)
    column_names = {'id': 'id'} 
    for col in fields:
        column_names[col.field_name] = col.verbose_name

    # print(column_names, "ffffffffff")
    cursor = custm_conncetion()
    query = "SELECT * FROM " + table + " ;"
    cursor.execute(query)
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

     # القاموس الذي يحتوي على الأسماء بالعربية والإنجليزية
    arabic_to_english_dict = column_names

    # القائمة التي تحتوي على البيانات الأصلية
    original_data = columns

    # قائمة جديدة لتخزين البيانات المحدثة
    updated_data = []

    # تحديث البيانات بناءً على القاموس
    for item in original_data:
        updated_data.append(arabic_to_english_dict.get(item, item))

    columns = updated_data
    
    df = pd.DataFrame(results, columns=columns)

    return df

def select_columns_name2(model_name):
    table = 'dynamic_models_'+ model_name
    fields = CustomField.objects.filter(table=model_name)
    column_names = {'id': 'id'} 
    for col in fields:
        column_names[col.field_name.replace("_", "")] = col.verbose_name

    # print(column_names, "ffffffffff")
    cursor = custm_conncetion()
    query = "SELECT * FROM " + table + " ;"
    cursor.execute(query)
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

     # القاموس الذي يحتوي على الأسماء بالعربية والإنجليزية
    arabic_to_english_dict = column_names
    print(arabic_to_english_dict)
    print(columns)

    # القائمة التي تحتوي على البيانات الأصلية
    original_data = columns

    # قائمة جديدة لتخزين البيانات المحدثة
    updated_data = []

    # تحديث البيانات بناءً على القاموس
    for item in original_data:
        # print(item)
        updated_data.append(arabic_to_english_dict.get(item, item))

    columns = updated_data

    return columns

from django.db.models.fields.related import ForeignKey

def create_report_table1(queryset, model_name, sys_name_id):
    # model_name_for_data = 'DynamicModels' + model_name.replace("_", "").capitalize()
    model = get_dynamic_model(model_name)
    # model = apps.get_model(app_label = 'test2', model_name = model_name_for_data)
    # columns = select_columns_name2(model_name)
    model_schema = ModelSchema.objects.get(name=model_name)
    columns = FieldSchema.objects.filter(model_schema=model_schema)
    # إنشاء الجدول
    # html_output = '<table id="example1" class="table table-bordered"><thead>'
    html_output = '<table id="example1" class="table table-bordered table-striped"><thead>'

    # إنشاء الرأس
    html_output += '<tr>'
    html_output += f'<th style="text-align: center;">id</th>'

    for field in columns:
        html_output += f'<th style="text-align: center;">{ field.kwargs["verbose_name"] }</th>'
        # html_output += f'<th style="text-align: center;">{ field }</th>'
    # html_output += '<th style="text-align: center;">الحدث</th>'
    html_output += '</tr></thead><tbody>'
    
    
    for item in queryset:
        html_output += '<tr>'
        
        for field in model._meta.get_fields():
            if not hasattr(item, field.name):
                # html_output += '<td></td>'
                continue

            # if not field.is_relation or field.many_to_many or field.one_to_one:
            #     continue
            
            if field.related_model and field.related_model == models.ManyToOneRel:
                # print(field.name)
                continue

            # اذا احتجتاة
            # if isinstance(field, ForeignKey):

            if field.is_relation:
                field_name = field.name
                related_name = CustomField.objects.get(table=model_name , field_name=field_name)
                related_name2= related_name.related_name
                # print(related_name2,"pppppppppppppppppppppppp")

                # related_object = getattr(item, related_name2)
                # print(related_object,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
                related_object = getattr(item, field.name)
                if related_object:
                    related_field_name = f"{related_name.related_name}"
                    # field_name = f"{field.name}"
                    html_output += f'<td style="text-align: center;">{getattr(related_object, related_field_name)}</td>'
                    # html_output += f'<td style="text-align: center;">{getattr(related_object, field_name)}</td>'
                else:
                    html_output += '<td>لايوجد</td>'

            elif isinstance(field, (models.ImageField, models.FileField)):
                file_value = getattr(item, field.name)
                
                if file_value:
                    # إذا كان الحقل يحتوي على قيمة (صورة أو ملف)
                    if hasattr(file_value, 'url'):
                        # عرض الصورة إذا كان الحقل هو ImageField
                        html_output += f'<td style="text-align: center;"><img src="{file_value.url}" alt="Image" style="max-width: 50px; max-height: 50px;"></td>'
                    else:
                        # عرض رابط التنزيل إذا كان الملف من نوع آخر
                        html_output += f'<td style="text-align: center;"><a href="{file_value.url}" download>Download</a></td>'
                else:
                    # إذا لم يكن هناك ملف
                    html_output += f'<td style="text-align: center;">لايوجد</td>'
    
            else:
                html_output += f'<td style="text-align: center;">{getattr(item, field.name)}</td>'

        html_output += '</tr>'

    # إغلاق الجدول والصفحة
    html_output += '</tbody></table>'
    
    return html_output


def create_report_table(queryset, model_name, sys_name_id):
    model = get_dynamic_model(model_name)
    model_schema = ModelSchema.objects.get(name=model_name)
    columns = FieldSchema.objects.filter(model_schema=model_schema)

    # إنشاء الجدول
    # html_output = '<table  class="table table-bordered table-striped"><thead>'
    html_output = '<table id="example1" class="table table-bordered table-striped"><thead>'

    # إنشاء الرأس
    html_output += '<tr>'
    html_output += '<th style="text-align: center;">id</th>'

    for field in columns:
        html_output += f'<th style="text-align: center;">{field.kwargs["verbose_name"]}</th>'
    
    # html_output += '<th style="text-align: center;">الحدث</th>'
    html_output += '</tr></thead><tbody>'

    for item in queryset:
        html_output += '<tr>'
        html_output += f'<td style="text-align: center;">{item.id}</td>'

        for field in columns:  # التكرار على الحقول المعرّفة فقط وليس جميع الحقول
            field_name = field.name
            if not hasattr(item, field_name):
                html_output += '<td style="text-align: center;">-</td>'
                continue

            value = getattr(item, field_name)

            # التعامل مع الحقول العلائقية ForeignKey
            if isinstance(model._meta.get_field(field_name), models.ForeignKey):
                try:
                    related_object = value
                    if related_object:
                        related_name = CustomField.objects.get(table=model_name, field_name=field_name).related_name
                        value = getattr(related_object, related_name, "لايوجد")
                    else:
                        value = "لايوجد"
                except CustomField.DoesNotExist:
                    value = "خطأ في الربط"

            # التعامل مع الحقول متعددة القيم (ManyToManyField)
            elif isinstance(model._meta.get_field(field_name), models.ManyToManyField):
                try:
                    # الحصول على الحقل الصحيح من CustomField
                    related_field = CustomField.objects.get(table=model_name, field_name=field.name)
                    related_name = related_field.related_name if related_field.related_name else "name"  # وضع قيمة افتراضية
                    
                    # جلب جميع الكائنات المرتبطة
                    related_objects = getattr(item, field.name).all()
                    if related_objects:
                        related_values = [getattr(obj, related_name, str(obj)) for obj in related_objects]  # استخدام `related_name`
                        html_output += f'<td style="text-align: center;">{", ".join(related_values)}</td>'
                    else:
                        html_output += '<td style="text-align: center;">لايوجد</td>'

                except CustomField.DoesNotExist:
                    html_output += '<td style="text-align: center;">خطأ: الحقل غير موجود</td>'
                continue
            # التعامل مع الحقول من نوع الصورة أو الملفات
            elif isinstance(model._meta.get_field(field_name), (models.ImageField, models.FileField)):
                if value:
                    if hasattr(value, 'url'):
                        value = f'<a href="{value.url}" target="_blank">عرض الملف</a>'
                    else:
                        value = "ملف غير متاح"
                else:
                    value = "لايوجد"

            html_output += f'<td style="text-align: center;">{value}</td>'

        
        html_output += '</tr>'

    html_output += '</tbody></table>'
    return html_output


def custm_report_header_edit(request):
    
    # if not request.user.has_perm('.change_information'):
    #     messages.error(request, 'لايوجد لديك صلاحية')
    #     return redirect('confirm_perm')
    # else:
    try:
        info = CustmReportHeader.objects.all().last()
        if request.method == 'POST':
            form = CustmReportHeaderForm(request.POST, request.FILES,instance = info)
            if form.is_valid():
                form.save()
                messages.success(request, 'تم الحفظ بنجاح')
                return redirect('custm_report_header_edit')
        else:
            form = CustmReportHeaderForm(instance = info)
        return render(request,'addCustmReportHeader.html',{'form':form})
    except:
        return render(request,'addCustmReportHeader.html',{'form':form})


def generate_table1(queryset, model_name, sys_name_id):
    model_name_for_data = 'DynamicModels' + model_name.replace("_", "").capitalize()
    model = get_dynamic_model(model_name)
    model_schema = ModelSchema.objects.get(name=model_name)
    columns = FieldSchema.objects.filter(model_schema=model_schema)
    # إنشاء الجدول
    html_output = '<table id="example1" class="table table-bordered table-striped"><thead>'

    # إنشاء الرأس
    html_output += '<tr>'
    html_output += f'<th style="text-align: center;">id</th>'

    for field in columns:
        html_output += f'<th style="text-align: center;">{ field.kwargs["verbose_name"] }</th>'
        # html_output += f'<th style="text-align: center;">{ field }</th>'
    html_output += '<th style="text-align: center;">الحدث</th>'
    html_output += '</tr></thead><tbody>'
    
    for item in queryset:
        html_output += '<tr>'
        
        for field in model._meta.get_fields():
            if not hasattr(item, field.name):
                # html_output += '<td></td>'
                continue

            # if not field.is_relation or field.many_to_many or field.one_to_one:
            #     continue
            # التعامل مع الحقول من نوع Many-to-Many
            if isinstance(field, models.ManyToManyField):
                try:
                    # الحصول على الحقل الصحيح من CustomField
                    related_field = CustomField.objects.get(table=model_name, field_name=field.name)
                    related_name = related_field.related_name if related_field.related_name else "name"  # وضع قيمة افتراضية
                    
                    # جلب جميع الكائنات المرتبطة
                    related_objects = getattr(item, field.name).all()
                    if related_objects:
                        related_values = [getattr(obj, related_name, str(obj)) for obj in related_objects]  # استخدام `related_name`
                        html_output += f'<td style="text-align: center;">{", ".join(related_values)}</td>'
                    else:
                        html_output += '<td style="text-align: center;">لايوجد</td>'

                except CustomField.DoesNotExist:
                    html_output += '<td style="text-align: center;">خطأ: الحقل غير موجود</td>'
                continue

            # if field.is_relation:
            if isinstance(field, models.ForeignKey):
                field_name = field.name
                related_name = CustomField.objects.get(table=model_name , field_name=field_name)
                related_name2= related_name.related_name
        
                related_object = getattr(item, field.name)
                if related_object:
                    related_field_name = f"{related_name.related_name}"
                    # field_name = f"{field.name}"
                    html_output += f'<td style="text-align: center;">{getattr(related_object, related_field_name)}</td>'
                    # html_output += f'<td style="text-align: center;">{getattr(related_object, field_name)}</td>'
                else:
                    html_output += '<td>لايوجد</td>'

            elif isinstance(field, (models.ImageField, models.FileField)):
                file_value = getattr(item, field.name)
                
                if file_value:
                    # إذا كان الحقل يحتوي على قيمة (صورة أو ملف)
                    if hasattr(file_value, 'url'):
                        # عرض الصورة إذا كان الحقل هو ImageField
                        html_output += f'<td style="text-align: center;"><img src="{file_value.url}" alt="Image" style="max-width: 50px; max-height: 50px;"></td>'
                    else:
                        # عرض رابط التنزيل إذا كان الملف من نوع آخر
                        html_output += f'<td style="text-align: center;"><a href="{file_value.url}" download>Download</a></td>'
                else:
                    # إذا لم يكن هناك ملف
                    html_output += f'<td style="text-align: center;">لايوجد</td>'
    
            else:
                html_output += f'<td style="text-align: center;">{getattr(item, field.name)}</td>'

        
        edit_url = reverse('edit_data', args=[model_name, item.id,sys_name_id])
        show_url = reverse('show_data', args=[model_name, item.id,sys_name_id])
        delete_url = reverse('delete_data', args=[model_name, item.id,sys_name_id])
        # إضافة أيقونات للحذف والتعديل والعرض
        html_output += f'''
        
                  <td class="mailbox-date pull-right no-print">
                    <a href="{edit_url}" class="btn btn-outline-secondary btn-xs"
                      data-toggle="tooltip" title="{ 'trans تعديل  البيانات' }">
                      <i class="fa fa-edit"></i>
                    </a>
                    <a href="{show_url}" class="btn btn-outline-secondary btn-xs"
                      data-toggle="tooltip" title="{ 'trans عرض البيانات  ' }">
                      <i class="fa fa-chart-line"></i>

                    </a>
                    <a href="{delete_url}" class="btn btn-outline-danger btn-xs"
                      data-toggle="tooltip" onclick="return confirm('{   'trans هل تريد الاستمرارفي الحذف' }')"
                      title="{ 'trans حذف البيانات' }">
                      <i class="fa fa-trash"></i>
                    </a>
                  </td>
            
        '''
        html_output += '</tr>'

    # إغلاق الجدول والصفحة
    html_output += '</tbody></table>'
    
    return html_output

# الدالة الصحيحة
def generate_table(queryset, model_name, sys_name_id):
    model = get_dynamic_model(model_name)
    model_schema = ModelSchema.objects.get(name=model_name)
    columns = FieldSchema.objects.filter(model_schema=model_schema)

    # إنشاء الجدول
    html_output = '<table id="example1" class="table table-bordered table-striped"><thead>'

    # إنشاء الرأس
    html_output += '<tr>'
    html_output += '<th style="text-align: center;">id</th>'

    for field in columns:
        html_output += f'<th style="text-align: center;">{field.kwargs["verbose_name"]}</th>'
    
    html_output += '<th style="text-align: center;">الحدث</th>'
    html_output += '</tr></thead><tbody>'

    for item in queryset:
        html_output += '<tr>'
        html_output += f'<td style="text-align: center;">{item.id}</td>'

        for field in columns:  # التكرار على الحقول المعرّفة فقط وليس جميع الحقول
            field_name = field.name
            if not hasattr(item, field_name):
                html_output += '<td style="text-align: center;">-</td>'
                continue

            value = getattr(item, field_name)

            # التعامل مع الحقول العلائقية ForeignKey
            if isinstance(model._meta.get_field(field_name), models.ForeignKey):
                try:
                    related_object = value
                    if related_object:
                        related_name = CustomField.objects.get(table=model_name, field_name=field_name).related_name
                        value = getattr(related_object, related_name, "لايوجد")
                    else:
                        value = "لايوجد"
                except CustomField.DoesNotExist:
                    value = "خطأ في الربط"

            # التعامل مع الحقول متعددة القيم (ManyToManyField)
            elif isinstance(model._meta.get_field(field_name), models.ManyToManyField):
                try:
                    # الحصول على الحقل الصحيح من CustomField
                    related_field = CustomField.objects.get(table=model_name, field_name=field.name)
                    related_name = related_field.related_name if related_field.related_name else "name"  # وضع قيمة افتراضية
                    
                    # جلب جميع الكائنات المرتبطة
                    related_objects = getattr(item, field.name).all()
                    # print(related_objects)
                    if related_objects:
                        related_values = [getattr(obj, related_name, str(obj)) for obj in related_objects]  # استخدام `related_name`
                        html_output += f'<td style="text-align: center;">{", ".join(related_values)}</td>'
                    else:
                        html_output += '<td style="text-align: center;">لايوجد</td>'

                except CustomField.DoesNotExist:
                    html_output += '<td style="text-align: center;">خطأ: الحقل غير موجود</td>'
                continue
            # التعامل مع الحقول من نوع الصورة أو الملفات
            elif isinstance(model._meta.get_field(field_name), (models.ImageField, models.FileField)):
                if value:
                    if hasattr(value, 'url'):
                        value = f'<a href="{value.url}" target="_blank">عرض الملف</a>'
                    else:
                        value = "ملف غير متاح"
                else:
                    value = "لايوجد"

            html_output += f'<td style="text-align: center;">{value}</td>'

        # إضافة الأحداث (تعديل - عرض - حذف)
        edit_url = reverse('edit_data', args=[model_name, item.id, sys_name_id])
        show_url = reverse('show_data', args=[model_name, item.id, sys_name_id])
        delete_url = reverse('delete_data', args=[model_name, item.id, sys_name_id])

        html_output += f'''
        <td class="mailbox-date pull-right no-print">
            <a href="{edit_url}" class="btn btn-outline-secondary btn-xs" title="تعديل البيانات">
                <i class="fa fa-edit"></i>
            </a>
            <a href="{show_url}" class="btn btn-outline-secondary btn-xs" title="عرض البيانات">
                <i class="fa fa-chart-line"></i>
            </a>
            <a href="{delete_url}" class="btn btn-outline-danger btn-xs"
                onclick="return confirm('هل تريد الاستمرار في الحذف؟')" title="حذف البيانات">
                <i class="fa fa-trash"></i>
            </a>
        </td>
        '''
        html_output += '</tr>'

    html_output += '</tbody></table>'
    return html_output


def generate_table2(queryset, model_name, sys_name_id):
    model_name_for_data = 'DynamicModels' + model_name.replace("_", "").capitalize()
    model = get_dynamic_model(model_name)
    model_schema = ModelSchema.objects.get(name=model_name)
    columns = FieldSchema.objects.filter(model_schema=model_schema)

    # إنشاء الجدول
    html_output = '<table id="example1" class="table table-bordered table-striped"><thead>'

    # إنشاء الرأس
    html_output += '<tr>'
    html_output += f'<th style="text-align: center;">id</th>'

    for field in columns:
        html_output += f'<th style="text-align: center;">{ field.kwargs["verbose_name"] }</th>'
    html_output += '<th style="text-align: center;">الحدث</th>'
    html_output += '</tr></thead><tbody>'
    
    for item in queryset:
        html_output += '<tr>'
        html_output += f'<td style="text-align: center;">{item.id}</td>'  # عرض الـ ID
        
        for field in model._meta.get_fields():
            if not hasattr(item, field.name):
                continue

            # التعامل مع الحقول العادية
            if not field.is_relation:
                html_output += f'<td style="text-align: center;">{getattr(item, field.name)}</td>'
                continue

            # التعامل مع الحقول من نوع ForeignKey
            if field.many_to_one:
                related_object = getattr(item, field.name)
                if related_object:
                    related_name = CustomField.objects.get(table=model_name, field_name=field.name).related_name
                    html_output += f'<td style="text-align: center;">{getattr(related_object, related_name)}</td>'
                else:
                    html_output += '<td style="text-align: center;">لايوجد</td>'
                continue

            # التعامل مع الحقول من نوع Many-to-Many
            if field.many_to_many:
                related_objects = getattr(item, field.name).all()
                if related_objects:
                    related_values = [str(obj) for obj in related_objects]  # تحويل الكائنات إلى نص
                    html_output += f'<td style="text-align: center;">{", ".join(related_values)}</td>'
                else:
                    html_output += '<td style="text-align: center;">لايوجد</td>'
                continue

            # التعامل مع الحقول من نوع One-to-One
            if field.one_to_one:
                related_object = getattr(item, field.name)
                if related_object:
                    html_output += f'<td style="text-align: center;">{related_object}</td>'
                else:
                    html_output += '<td style="text-align: center;">لايوجد</td>'
                continue

        # إضافة أيقونات للحذف والتعديل والعرض
        edit_url = reverse('edit_data', args=[model_name, item.id, sys_name_id])
        show_url = reverse('show_data', args=[model_name, item.id, sys_name_id])
        delete_url = reverse('delete_data', args=[model_name, item.id, sys_name_id])
        html_output += f'''
            <td class="mailbox-date pull-right no-print">
                <a href="{edit_url}" class="btn btn-outline-secondary btn-xs"
                    data-toggle="tooltip" title="تعديل البيانات">
                    <i class="fa fa-edit"></i>
                </a>
                <a href="{show_url}" class="btn btn-outline-secondary btn-xs"
                    data-toggle="tooltip" title="عرض البيانات">
                    <i class="fa fa-chart-line"></i>
                </a>
                <a href="{delete_url}" class="btn btn-outline-danger btn-xs"
                    data-toggle="tooltip" onclick="return confirm('هل تريد الاستمرار في الحذف؟')"
                    title="حذف البيانات">
                    <i class="fa fa-trash"></i>
                </a>
            </td>
        '''
        html_output += '</tr>'

    # إغلاق الجدول
    html_output += '</tbody></table>'
    
    return html_output


from django.core.exceptions import ObjectDoesNotExist

def show_data(request,model_name, row_id,sys_name_id):
    table_name = 'DynamicModels' + model_name.capitalize()
    model = apps.get_model(app_label='test2', model_name=table_name)
    dataId = model.objects.get(id=row_id)
    # print(dataId, "ddddddddddddd")
    form_class = create_dynamic_form(model_name)
    # print(request.method, "ennnnnnnnn")
    form = form_class(instance=dataId)
    
    return render(request, 'show_data.html', {'form': form, 'sys_name_id':sys_name_id, 'model_name': model_name})
    # return render(request, 'my_view2.html', {'form': form, 'model_name': model_name})

 
def create_dynamic_form1(table_name):
    model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
    fields = CustomField.objects.filter(table=table_name)
    form_fields = {}
    field_names = [field.field_name for field in fields]
    custom_labels = [field.verbose_name for field in fields]
    related_names = [field.related_name for field in fields]
   
    class DynamicForm(forms.ModelForm):
        class Meta:
            model = apps.get_model(app_label='test2', model_name=model_name)
            fields = field_names
        def __init__(self, *args, **kwargs):
            super(DynamicForm, self).__init__(*args, **kwargs)
            
            def save(self, commit=True):
                instance = super().save(commit=False)
                if commit:
                    instance.save()
                return instance
            # def custom_label_from_instance(obj, field_name):
            #     return getattr(obj, field_name)
            for i, field_name in enumerate(field_names):
                self.fields[field_name].label = custom_labels[i]

                if isinstance(self.Meta.model._meta.get_field(field_name), models.ForeignKey):
                    related_model = self.Meta.model._meta.get_field(field_name).remote_field.model
                    related_name = self.Meta.model._meta.get_field(field_name).remote_field.field_name
                    related_name2 = related_names[i]
                    # print(related_name2, "lllllllllllllllllll")
                    RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)
                    
                    def custom_label_from_instance(RelatedModel, field_name):
                        def label_from_instance(obj):
                            # return getattr(obj, related_name2)
                            return getattr(obj, field_name)
                        form_field = forms.ModelChoiceField(queryset=RelatedModel.objects.all(), to_field_name=related_name)
                        form_field.label_from_instance = label_from_instance
                        form_field.initial = field_name
                        return form_field

                    form_field = custom_label_from_instance(RelatedModel,field_name)
                    self.fields[field_name] = form_field
                self.fields[field_name].label = custom_labels[i]
                
    
    return DynamicForm

from django import forms
from django.db import models
from django.apps import apps
from django.forms import widgets


def search_my_model(request):
    print("ddddddddddddddddddddddd")
    model_name = QueryDict(request.body).get('model_name')
    # field_name = QueryDict(request.body).get('field_name')
    table_name = 'DynamicModels' + model_name.capitalize()
    # table_name = 'DynamicModelsAlaqsam'
    model = apps.get_model(app_label='test2', model_name=table_name)
    # field = model._meta.get_field(field_name)
    # data = model.objects.values_list(field_name, flat=True)
    if request.is_ajax():
        print("enter")
        search_term = request.GET.get('sersh')
        print(search_term, "jjjjjjjjjjjjjj")
        results = model.objects.filter(field_name__icontains=search_term)
        data = [{'id': result.id, 'text': str(result)} for result in results]
        return JsonResponse(data, safe=False)

from django.db import models

def manage_models(request, model_name, sys_name_id):
    if not request.user.has_perm(f'test2.manage_dynamicmodels{model_name}'):
    # if not request.user.has_perm('test2.can_view_dynamicmodels'+model_name):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        # modify_delete_behavior()
        # make_migrations_and_migrate('test2')
        # reload_dynamic_models()

        fields = CustomField.objects.filter(table=model_name)
        # model_schema_instance1 = ModelSchema.objects.get(name=model_name).as_model()
        # print(is_model_related(get_dynamic_model(model_name)))
        # print(model_schema_instance1)
        model_schema_instance = ModelSchema.objects.get(name=model_name)
        field_schema = FieldSchema.objects.filter(model_schema=model_schema_instance)
        model = Modelnames.objects.get(modelname=model_name)
        # print(model)
        return render(request, 'manage_models.html', {'model_name': model_name, 'model': model, 'sys_name_id':sys_name_id, 'fields': fields, 'field_schema':field_schema})


from django import forms


# مع الشروط لاكن لم تجرب
# def create_dynamic_form(model_name):
#     # استرجاع الشروط من قاعدة البيانات
#     conditions = FieldCondition.objects.filter(model_name=model_name)

#     class DynamicForm(forms.ModelForm):
#         class Meta:
#             model = get_model_from_name(model_name)  # دالة لاسترجاع النموذج من اسمه
#             fields = '__all__'

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             for condition in conditions:
#                 field_name = condition.field_name
#                 if field_name in self.fields:
#                     self.fields[field_name].widget.attrs['data-condition'] = condition.condition
#                     self.fields[field_name].widget.attrs['data-action'] = condition.action

#         def clean(self):
#             cleaned_data = super().clean()
#             for condition in conditions:
#                 field_name = condition.field_name
#                 if field_name in cleaned_data:
#                     condition_value = cleaned_data[field_name]
#                     if eval(condition.condition, {'field_name': condition_value}):
#                         # تطبيق الإجراء المحدد
#                         if condition.action.startswith('show'):
#                             field_to_show = condition.action.split(' ')[1]
#                             self.fields[field_to_show].widget.attrs['style'] = 'display: block;'
#                         elif condition.action.startswith('hide'):
#                             field_to_hide = condition.action.split(' ')[1]
#                             self.fields[field_to_hide].widget.attrs['style'] = 'display: none;'
#             return cleaned_data

#     return DynamicForm

from .models import FieldCondition


def get_model_fields(model_name):
    """
    دالة لاسترجاع قائمة الحقول في نموذج معين بناءً على اسم النموذج.
    """
    try:
        # استرجاع النموذج من اسمه
        model = get_dynamic_model(model_name)
        # استرجاع قائمة الحقول
        # fields = [field.name for field in model._meta.get_fields()]
        fields = CustomField.objects.filter(table=model_name)
        # field_names = [field.field_name for field in fields]
        # field_names = [field.verbose_name for field in fields]
        # print(field_names)
        # return field_names
        return fields
    except LookupError:
        # إذا لم يتم العثور على النموذج
        return []

from django.template.loader import render_to_string


def add_condition(request, model_name, sys_name_id):
    form1 =get_selected_field(request)
    print(form1)
    selected_field = request.GET.get('selected_field')
    print(f"🔹 Selected Field from GET: {selected_field}")
    if request.method == 'POST':
        selected_field = request.POST.get('field_name', selected_field)  
        print(f"🔹 Selected Field from POST: {selected_field}")
        form = FieldConditionForm(request.POST, model_name=model_name, selected_field=selected_field)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.restricted_values = form.cleaned_data.get('restricted_values', [])
            instance.save()
            return redirect('condition_list', model_name, sys_name_id)
        else:
            print(f"❌ أخطاء النموذج: {form.errors}")  
    else:
        # print(selected_field,"kkkkkkkkkkkkkkkkkkkkkkkkkk")
        form = FieldConditionForm(model_name=model_name, selected_field=selected_field)

    return render(request, 'add_condition.html', { 'sys_name_id': sys_name_id, 'model_name': model_name, 'form': form, })

from django.http import JsonResponse
from django.template.loader import render_to_string

def get_selected_field(request):
    if request.method == 'POST':
        selected_field = request.POST.get('selected_field', '')
        model_name = request.POST.get('model_name', '')

        # print(f"🔹 الحقل المحدد: {selected_field}")

        # إنشاء النموذج بالقيم الجديدة
        form = FieldConditionForm(model_name=model_name, selected_field=selected_field)

        # استخراج الحقل المطلوب فقط
        restricted_values_html = render_to_string(
            'partial_restricted_values.html',
            {'form': form},
            request=request
        )

        return JsonResponse({'status': 1, 'restricted_values_html': restricted_values_html})

    return JsonResponse({'status': 2, 'message': "طلب غير صالح!"})




from django.http import JsonResponse

def get_restricted_values(request):
    if request.method == 'POST':
        model_name = request.POST.get('model_name')
        selected_field = request.POST.get('selected_field')
        
        if model_name and selected_field:
            model = get_dynamic_model(model_name)
            if model:
                values = model.objects.values_list(selected_field, flat=True).distinct()
                restricted_values = [(str(value), str(value)) for value in values if value is not None]
                return JsonResponse({'status': 1, 'restricted_values': restricted_values})
        
        return JsonResponse({'status': 0, 'error': 'Invalid data'})

def get_field_values(request):
    model_name = request.GET.get("model_name")
    field_name = request.GET.get("field_name")
    print(field_name,"yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    model = get_dynamic_model(model_name)
    if not model:
        return JsonResponse({"error": "النموذج غير موجود"}, status=400)

    try:
        values = model.objects.values_list(field_name, flat=True).distinct()
        return JsonResponse({"values": list(values)})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)




def get_field_values1(request):
    """
    دالة لجلب القيم المتاحة لحقل معين وإرجاعها كـ JSON.
    """
    model_name = request.GET.get('model_name')
    field_name = request.GET.get('field_name')

    if model_name and field_name:
        try:
            model = get_dynamic_model(model_name)
            values = model.objects.values_list(field_name, flat=True).distinct()
            print(f"🟢 القيم المسترجعة من {field_name}: {list(values)}")  # ✅ تحقق من القيم في الكونسول
            return JsonResponse({'values': list(values)})
        except Exception as e:
            print(f"🔴 خطأ أثناء استرجاع القيم: {e}")
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
# مستخدمة ل حقل
def get_field_values2(request):
    """
    دالة لجلب القيم المتاحة لحقل معين وإرجاعها كـ JSON.
    """
    model_name = request.GET.get('model_name')
    field_name = request.GET.get('field_name')

    if model_name and field_name:
        try:
            model = get_dynamic_model(model_name)
            values = model.objects.values_list(field_name, flat=True).distinct()
            print(f"🟢 القيم المسترجعة من {field_name}: {list(values)}")  # ✅ تحقق من القيم في الكونسول
            return JsonResponse({'values': list(values)})
        except Exception as e:
            print(f"🔴 خطأ أثناء استرجاع القيم: {e}")
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def condition_list(request,model_name,sys_name_id):
    conditions = FieldCondition.objects.all()
    return render(request, 'condition_list.html', {'sys_name_id':sys_name_id, 'model_name':model_name, 'conditions': conditions})



def add_data(request, model_name, sys_name_id):
    if not request.user.has_perm(f'test2.add_dynamicmodels{model_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        table_name = Modelnames.objects.get(modelname=model_name).modelnameAr

        form_class = create_dynamic_form(model_name)
        if request.method == 'POST':
            form = form_class(request.POST, request.FILES)
            if form.is_valid():
                # الحصول على البيانات المدخلة في الفورم
                form_data = form.cleaned_data
                details_str = save_user_action(form,form_data,model_name)
                # حفظ البيانات في النموذج
                form.save()

                # تسجيل الحركة في UserAction
                UserAction.objects.create(user=request.user, action="إضافة بيانات", model_name=table_name, details=details_str)
                return redirect('display_data', model_name, sys_name_id)
        else:
            form = form_class()
        
        return render(request, 'add_data.html', {'sys_name_id': sys_name_id, 'form': form, 'model_name': model_name})


def save_user_action(form, form_data, model_name):
    # إنشاء قائمة لتخزين تفاصيل الحقول
    details = []

    for field, value in form_data.items():
        field_instance = form.fields[field]  # الحصول على الحقل نفسه من الـ form
        
        # التعامل مع الحقول التي هي من نوع ManyToManyField
        if isinstance(field_instance, forms.ModelMultipleChoiceField):
            related_field = CustomField.objects.filter(table=model_name, field_name=field).first().related_name
            related_name = related_field
            
            # الحصول على القيم المرتبطة باستخدام related_name
            related_values = [getattr(obj, related_name, str(obj)) for obj in value]
            
            # إضافة القيم إلى details
            if related_values:
                details.append(', '.join(str(val) for val in related_values))
            else:
                details.append("لا يوجد")

        # التعامل مع الحقول التي هي من نوع ForeignKey أو OneToOneField
        elif isinstance(field_instance, forms.ModelChoiceField):
            related_field = CustomField.objects.filter(table=model_name, field_name=field).first().related_name
            related_name = related_field
            related_value = getattr(value, related_name, None)  # الحصول على القيمة باستخدام related_name
            details.append(str(related_value) if related_value else "لا يوجد")

        else:
            # إضافة القيم التي ليست من النوع Relationship (مثل الحقول النصية)
            details.append(str(value))
    
    # تحويل details إلى سلسلة نصية
    details_str = ', '.join(details)

    return details_str

def save_user_action1(form,form_data, model_name):

     # إنشاء قائمة لتخزين تفاصيل الحقول
    details = []

    for field, value in form_data.items():
        field_instance = form.fields[field]  # الحصول على الحقل نفسه من الـ form
        
        # التعامل مع الحقول التي هي من نوع ManyToManyField
        if isinstance(field_instance, forms.ModelMultipleChoiceField):
            related_field = CustomField.objects.filter(table=model_name, field_name=field).first().related_name
            related_name = related_field
            
            related_values = [getattr(obj, related_name, str(obj)) for obj in value]  # استخدام `related_name`
            details.append(str(related_value) if related_value else "لا يوجد")

        # التعامل مع الحقول التي هي من نوع ForeignKey أو OneToOneField
        elif isinstance(field_instance, forms.ModelChoiceField):
            related_field = CustomField.objects.filter(table=model_name, field_name=field).first().related_name
            related_name = related_field
            related_value = getattr(value, related_name, None)  # الحصول على القيمة باستخدام related_name
            details.append(str(related_value) if related_value else "لا يوجد")

        else:
            # إضافة القيم التي ليست من النوع Relationship (مثل الحقول النصية)
            details.append(str(value))
    
    # تحويل details إلى سلسلة نصية
    details_str = ', '.join(details)

    return details_str


def edit_data(request, model_name, row_id,sys_name_id):
    if not request.user.has_perm(f'test2.change_dynamicmodels{model_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        table_nameAr = Modelnames.objects.get(modelname=model_name).modelnameAr
        
        model = get_dynamic_model(model_name)
        data_instance = model.objects.get(id=row_id)
        # احصل على النموذج الديناميكي
        DynamicForm = create_dynamic_form(model_name)
        if request.method == 'POST':
            form = DynamicForm(request.POST, request.FILES, instance=data_instance)
            if form.is_valid():
                form_data = form.cleaned_data
                # نقوم بتحويل form_data إلى قائمة تحتوي على القيم فقط دون أسماء الحقول
                details = save_user_action(form,form_data,model_name)


                form.save()
                UserAction.objects.create(user=request.user,action="تعديل بيانات",model_name=table_nameAr,details=details)
                return redirect('display_data', model_name,sys_name_id)
                # اتمام عملية الحفظ
        else:
            form = DynamicForm(instance=data_instance)

        return render(request, 'edit_data.html', {'form': form,'sys_name_id':sys_name_id, 'model_name': model_name})

from django.forms.models import model_to_dict

def delete_data(request, model_name, row_id,sys_name_id):
    if not request.user.has_perm(f'test2.delete_dynamicmodels{model_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        try:
            # استرجاع اسم الجدول باللغة العربية
            table_nameAr = Modelnames.objects.get(modelname=model_name)
            
            # بناء اسم الجدول بناءً على النموذج
            model =get_dynamic_model(model_name)
            
            # استرجاع العنصر باستخدام row_id
            item = get_object_or_404(model, pk=row_id)
            # تحويل الكائن إلى قاموس من الحقول
            item_dict = model_to_dict(item)

            # إنشاء تفاصيل الحذف باستخدام القاموس
            details = ", ".join([f"{value}" for key, value in item_dict.items()])

            # تسجيل الحذف في سجل الأفعال (UserAction)
            UserAction.objects.create(
                user=request.user,
                action=" حذف بيانات",
                model_name=table_nameAr,  # افترض أنك تستخدم الحقل modelname_ar في Modelnames
                details=details  # بيانات العنصر المحذوف
            )

            # حذف العنصر
            item.delete()

            messages.success(request, "تم عملية الحذف بنجاح")
            return redirect('display_data', model_name,sys_name_id)

        except Exception as e:
            messages.error(request, f"حدث خطأ: {str(e)}")
            return redirect('display_data', model_name,sys_name_id)

def edit_field(request, model_name, field_id, sys_name_id):
    try:
        data_instance = CustomField.objects.get(id=field_id)
    except CustomField.DoesNotExist:
        result = {'status': 2, 'message': "السجل غير موجود"}
        return JsonResponse(result)

    field_name = data_instance.field_name
    model_schema = ModelSchema.objects.get(name=model_name)

    try:
        field_schema = FieldSchema.objects.get(model_schema=model_schema, name=field_name)
    except FieldSchema.DoesNotExist:
        print(f"FieldSchema does not exist for model_schema={model_schema} and field_name={field_name}")
        result = {'status': 2, 'message': "تعذر العثور على مخطط الحقل"}
        return JsonResponse(result)

    print("field_schema.db_column =", field_schema.db_column)  # طباعة خصائص `field_schema`
    print("field_schema.name =", field_schema.name)

    if request.method == 'POST':
        form = CustomFieldForm(request.POST, request.FILES, instance=data_instance)
        if form.is_valid():
            try:
                table_name = model_schema.db_table
                column_name = field_schema.db_column

                if utils.db_field_allows_null(table_name, column_name):
                    result = {'status': 2, 'message': "لا يمكن تعديل هذا الحقل ليكون فارغًا."}
                    return JsonResponse(result)
                    
                field_schema.null = True
                field_schema.save()
                form.save()

                result = {'status': 1, 'message': "تم العملية بنجاح"}
                return redirect('manage_models', model_name, sys_name_id)

            except Exception as e:
                print("Error:", e)
                result = {'status': 2, 'message': "عملية تعديل خطأ"}
                return JsonResponse(result)

    else:
        form = CustomFieldForm(instance=data_instance)

    return render(request, 'edit_field.html', {'form': form, 'model_name': model_name, 'sys_name_id': sys_name_id})

from django.shortcuts import render, get_object_or_404, redirect
from dynamic_models.models import FieldSchema
from dynamic_models.forms import FieldSchemaForm

def edit_field2(request, field_id):
    field = get_object_or_404(FieldSchema, id=field_id)
    
    if request.method == 'POST':
        form = FieldSchemaForm(request.POST, instance=field)
        if form.is_valid():
            form.save()
            return redirect('index')  # إعادة التوجيه إلى صفحة القائمة
    else:
        form = FieldSchemaForm(instance=field)
    
    return render(request, 'edit_field2.html', {'form': form})


def delete_field(request, model_name, field_name, sys_name_id):
    if not request.user.has_perm(f'test2.drop_field_dynamicmodels{model_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    
    try:
        table_nameAr = Modelnames.objects.get(modelname=model_name).modelnameAr
        # الحصول على النموذج الديناميكي
        model = get_dynamic_model(model_name)

        # التحقق إذا كان الحقل يحتوي على بيانات
        if model.objects.filter(**{f"{field_name}__isnull": False}).exists():
            messages.error(request, "عملية حذف خطأ: هذا السجل يحتوي على بيانات")
            return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)
        
        model_schema = get_object_or_404(ModelSchema, name=model_name)
        field_schema = get_object_or_404(FieldSchema, model_schema=model_schema, name=field_name)
        
        # التحقق مما إذا كان الحقل مرتبطًا مع سجلات أخرى
        if not check_field_is_related(model_name, field_name):
            # التحقق من وجود الحقل في الجدول
            table_name = model_schema.db_table
            column_name = field_schema.db_column
            
            if field_schema.class_name == 'django.db.models.ForeignKey':
                column_name = f"{field_name}_id"

            if not utils.db_table_has_field(table_name, column_name):
                messages.error(request, "العمود غير موجود في الجدول")
                return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)

            # حذف الحقل من الجدول
            field_schema.delete()

            # حذف الحقل من CustomField
            custm_field_name = CustomField.objects.filter(table=model_name, field_name=field_name).first()
            if custm_field_name:
                UserAction.objects.create(user=request.user,action="حذف حقل ",model_name=table_nameAr, details=custm_field_name.verbose_name)
                custm_field_name.delete()
            
            modify_delete_behavior()
            make_migrations_and_migrate('test2')

            messages.success(request, "تمت العملية بنجاح")
            return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)

        else:
            messages.error(request, "عملية حذف خطأ: هذا السجل مرتبط بسجل آخر")
            return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)

    except Exception as e:
        # تسجيل الخطأ
        # print(f"Error during field deletion: {e}")
        messages.error(request, f"حدث خطأ أثناء عملية الحذف: {e}")
        return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)



def check_field_is_related2(table_name, field_name):
    is_related = CustomField.objects.filter(table=table_name, field_name=field_name).first()
    if is_related and is_related.is_related:
        return True
    return False


def delete_field1(request, model_name, field_name, sys_name_id):
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    if not request.user.has_perm('test2.delete_field_'+model_name):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        
        model = get_dynamic_model(model_name)
       
        data = model.objects.values_list(field_name, flat=True)
        if data:
            messages.error(request,"عملية حذف خطأ: هذا السجل  يحتوي على بيانات  ")
            
        else:
            model_schema = ModelSchema.objects.get(name=model_name)
            field_schema = FieldSchema.objects.get(model_schema=model_schema, name=field_name)
            # print( check_field_is_related(model_name, field_name))
            if not check_field_is_related(model_name, field_name):
                try:
                    table_name = model_schema.db_table
                    column_name = field_schema.db_column
                    assert utils.db_table_has_field(table_name, column_name)
                    field_schema.delete()
                    assert not utils.db_table_has_field(table_name, column_name)
                    custm_field_name = CustomField.objects.get(table=model_name, field_name=field_name)
                    custm_field_name.delete()
                    modify_delete_behavior()
                    # print(custm_field_name,"ttttttttttt")
                    messages.success(request,"تم العملية بنجاح")
                    return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)
                    
                except Exception as e:
                    messages.error(request,"عملية حذف خطأ: هذا السجل مرتبط بسجل آخر")
                    
            else:
                messages.error(request,"عملية حذف خطأ: هذا السجل مرتبط بسجل آخر")
                return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)
    return redirect('manage_models', model_name=model_name, sys_name_id=sys_name_id)

               
def check_field_is_related(table_name, field_name):
    is_related = CustomField.objects.get(table=table_name, field_name=field_name)
    if is_related.is_related == False:
        return False
        
    else:
        return True

def drop_column(request, model_name):
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    if not request.user.has_perm('test2.delete_field_'+model_name):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        model_name = QueryDict(request.body).get('model_name')
        field_name = QueryDict(request.body).get('field_name')
        # table_name = 'DynamicModels' + model_name.capitalize()
        model = get_dynamic_model(model_name)
        # model = apps.get_model(app_label='test2', model_name=table_name)
        # field = model._meta.get_field(field_name)
        data = model.objects.values_list(field_name, flat=True)
        if data:
            result={'status':2,'message':"عملية حذف خطأ: هذا السجل  يحتوي على بيانات  "}
            return JsonResponse(result)
        else:
            model_schema = ModelSchema.objects.get(name=model_name)
            field_schema = FieldSchema.objects.get(model_schema=model_schema, name=field_name)
            # print( check_field_is_related(model_name, field_name))
            if not check_field_is_related(model_name, field_name):
                try:
                    table_name = model_schema.db_table
                    column_name = field_schema.db_column
                    assert utils.db_table_has_field(table_name, column_name)
                    field_schema.delete()
                    assert not utils.db_table_has_field(table_name, column_name)
                    custm_field_name = CustomField.objects.get(table=model_name, field_name=field_name)
                    custm_field_name.delete()
                    modify_delete_behavior()
                    # print(custm_field_name,"ttttttttttt")
                    result={'status':1,'message':"تم العملية بنجاح"}
                    return JsonResponse(result)

                except Exception as e:
                    result={'status':0,'message':"عملية حذف خطأ: هذا السجل مرتبط بسجل آخر"}
                    return JsonResponse(result)
            else:
                result={'status':0,'message':"عملية حذف خطأ: هذا السجل مرتبط بسجل آخر"}
                return JsonResponse(result)


def is_model_related(related_model):
    """
    تقوم هذه الدالة بإرجاع أسماء النماذج التي تحتوي على حقول ForeignKey 
    تشير إلى النموذج المرسل إليها.

    :param related_model: النموذج المرتبط الذي نبحث عن الحقول التي تشير إليه.
    :return: قائمة بأسماء النماذج التي تحتوي على ForeignKey تشير إلى النموذج المرسل.
    """
    related_models = []
    # print(related_model)
    # الحصول على جميع النماذج في المشروع
    for model in apps.get_models():
        for field in model._meta.get_fields():
            # التحقق من أن الحقل هو ForeignKey وأنه مرتبط بالنموذج المطلوب
            if isinstance(field, models.ForeignKey) and field.related_model == related_model:
                related_models.append(model)
                # related_models.append(model.__name__)
                break  # إذا وجدنا حقلًا مرتبطًا، لا حاجة للاستمرار في البحث في نفس النموذج

    return related_models


def delete_model1(request, model_name, sys_name_id):
    sys_name = TblSystem.objects.get(id=sys_name_id).name
    if not request.user.has_perm(f'dynmic_table.delete_{sys_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')

    try:
        # الحصول على ModelSchema
        model_schema = get_object_or_404(ModelSchema, name=model_name)

        # الحصول على النموذج الديناميكي باستخدام `apps.get_model`
        model = apps.get_model(app_label='test2', model_name='DynamicModels' + model_name.capitalize())

        # التحقق إذا كان النموذج مرتبط بنماذج أخرى
        related_models = is_model_related(model)  # استخدام الدالة التي تحقق من النماذج المرتبطة
        # print(related_models,"lllllllllllllllllllllllllllllllllll")
        if related_models:
            messages.error(request, f"لا يمكن حذف {model_name} لأنه مرتبط بنماذج أخرى: {', '.join([model.__name__ for model in related_models])}.")
            return redirect('subproject_detail', sys_name_id=sys_name_id)

        # التحقق إذا كان هناك بيانات في الجدول
        if model.objects.exists():
            # إذا كانت هناك بيانات في الجدول لا يمكن الحذف
            messages.error(request, "عملية حذف خطأ: هذا السجل يحتوي على بيانات")
        else:
            # التأكد من أن الجدول في قاعدة البيانات موجود
            if utils.db_table_exists(model_schema.db_table):
                # حذف النموذج (النموذج في قاعدة البيانات) 
                model_schema.delete()

                # حذف السجل من `Modelnames`
                table_name = Modelnames.objects.filter(modelname=model_name).first()
                if table_name:
                    UserAction.objects.create(user=request.user, action="حذف جدول", model_name=table_name.sys_name, details=table_name.modelnameAr)
                    table_name.delete()

                # تعديل سلوك الحذف بعد العملية
                modify_delete_behavior()

                # إرسال رسالة نجاح
                messages.success(request, "تمت العملية بنجاح")

                # إعادة التوجيه إلى الصفحة المطلوبة
                return redirect('subproject_detail', sys_name_id=sys_name_id)

            else:
                messages.error(request, "الجدول غير موجود في قاعدة البيانات")

    except Exception as e:
        messages.error(request, "عملية حذف خطأ: هذا الجدول مرتبط بسجل آخر أو حدث خطأ آخر.")

    return redirect('subproject_detail', sys_name_id=sys_name_id)


def delete_model(request, model_name, sys_name_id):
    sys_name = TblSystem.objects.get(id=sys_name_id).name
    if not request.user.has_perm(f'dynmic_table.delete_{sys_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')

    try:
        # الحصول على ModelSchema
        model_schema = get_object_or_404(ModelSchema, name=model_name)

        # الحصول على النموذج الديناميكي باستخدام `apps.get_model`
        model = apps.get_model(app_label='test2', model_name='DynamicModels' + model_name.capitalize())

        # التحقق إذا كان النموذج مرتبط بنماذج أخرى
        related_models = is_model_related(model)  # استخدام الدالة التي تحقق من النماذج المرتبطة
        if related_models:
            messages.error(request, f"لا يمكن حذف {model_name} لأنه مرتبط بنماذج أخرى: {', '.join([model.__name__ for model in related_models])}.")
            return redirect('subproject_detail', sys_name_id=sys_name_id)

        # التحقق إذا كان هناك بيانات في الجدول
        if model.objects.exists():
            # إذا كانت هناك بيانات في الجدول لا يمكن الحذف
            messages.error(request, "عملية حذف خطأ: هذا السجل يحتوي على بيانات")
        else:
            # التأكد من أن الجدول في قاعدة البيانات موجود
            if utils.db_table_exists(model_schema.db_table):
                # حذف الصلاحيات المرتبطة بالنموذج
                content_type = ContentType.objects.get(app_label='test2', model= f'dynamicmodels{model_name.lower()}')
                permissions = Permission.objects.filter(content_type=content_type)

                for permission in permissions:
                    # إزالة الصلاحيات من جميع المجموعات
                    groups = Group.objects.filter(permissions=permission)
                    for group in groups:
                        group.permissions.remove(permission)

                    # إزالة الصلاحيات من جميع المستخدمين
                    users = User.objects.filter(user_permissions=permission)
                    for user in users:
                        user.user_permissions.remove(permission)

                    # حذف الصلاحية نفسها
                    permission.delete()

                # حذف النموذج (النموذج في قاعدة البيانات) 
                model_schema.delete()

                # حذف السجل من `Modelnames`
                table_name = Modelnames.objects.filter(modelname=model_name).first()
                if table_name:
                    UserAction.objects.create(user=request.user, action="حذف جدول", model_name=table_name.sys_name, details=table_name.modelnameAr)
                    table_name.delete()

                # تعديل سلوك الحذف بعد العملية
                modify_delete_behavior()
                make_migrations_and_migrate('test2')
                # إرسال رسالة نجاح
                messages.success(request, "تمت العملية بنجاح")

                # إعادة التوجيه إلى الصفحة المطلوبة
                return redirect('subproject_detail', sys_name_id=sys_name_id)

            else:
                messages.error(request, "الجدول غير موجود في قاعدة البيانات")

    except Exception as e:
        messages.error(request, f"عملية حذف خطأ: {str(e)}")

    return redirect('subproject_detail', sys_name_id=sys_name_id)

def delete_item(request,model_name, item_id):
    if not request.user.has_perm('test2.export_data_dynamicmodels'+model_name):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        item = get_object_or_404(Item, pk=item_id)
        if request.method == 'POST':
            if item.confirm_delete:
                # التحقق من العلاقات المرتبطة والتعامل معها
                item.delete()
                messages.success(request, 'تم حذف العنصر بنجاح.')
                return redirect('success_url')
            else:
                messages.error(request, 'يجب تأكيد الحذف قبل القيام بالعملية.')
        return render(request, 'delete_item.html', {'item': item})

def upload_file(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        table_name = request.GET.get('table', None)
        # قراءة البيانات من ملف Excel
        df = pd.read_excel(excel_file)
        # print(df,"llllllllllllllllllllllllllllllllllllllll")
        # formset_view(request, table_name)
        # تحويل البيانات إلى قائمة من القاموسات
        # records = df.to_dict(orient='records')
        # print(records)
        
        # print("true")
        # return df
        # return render(request, 'index.html')
        # return redirect('formset_view2', table_name)
    # return render(request, 'display_data.html', {'table_html2': table_html2})

        return JsonResponse({'success': True})

    # return JsonResponse({'success': False})

# def upload_file3(request, model_name):
#     if request.method == 'POST' and request.FILES['excel_file']:
#         excel_file = request.FILES['excel_file']

#         # قراءة البيانات من ملف Excel
#         df = pd.read_excel(excel_file)
#         print(df, "uuuuuuuuuuuuu")
#         # تحويل البيانات إلى قائمة من القاموسات
#         records = df.to_dict(orient='records')
#         # print(records)
#         table_html = generate_table1(records, model_name)
#         print(table_html, "ggggggggg")

        
#     return render(request, 'table_editable.html', {'table_html': table_html})
#     # return render(request, 'table_editable.html')

#     #     return JsonResponse({'success': True})

#     # return JsonResponse({'success': False})

# def upload_file2(request):

    return render(request, 'upload_file.html', {})

import pandas as pd
from django.http import HttpResponse
from io import BytesIO
# شغالة ومستخدمة
def export_empty_excel1(request, model_name):

    try:
        # Get the Arabic model name
        model_name_obj = Modelnames.objects.get(modelname=model_name)
        table_name = model_name_obj.modelnameAr
        # print(table_name)

        # Get the fields from the CustomField model based on the table name
        fields = CustomField.objects.filter(table=model_name).values_list('verbose_name', flat=True)

        # Create an empty DataFrame with column names
        df = pd.DataFrame(columns=fields)

        # Create a BytesIO buffer to write the Excel file
        output = BytesIO()

        # Write the DataFrame to the Excel file in the BytesIO buffer
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)

        # Retrieve the content from the BytesIO buffer
        output.seek(0)

        # Prepare the HTTP response to return the file and open it inline
        response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        # Set the filename to the Arabic model name
        response['Content-Disposition'] = f'attachment; filename="{model_name}.xlsx"'
        UserAction.objects.create(user=request.user,action=" تصدير قالب ",model_name=table_name, details=details)
        return response

    except Modelnames.DoesNotExist:
        return HttpResponse("Model name not found")

import urllib.parse

# شغالة ومستخدمة
def export_empty_excel(request, model_name,sys_name_id):
    try:
        # التحقق من صلاحيات المستخدم (يمكن تخصيص هذا بناءً على التطبيق الخاص بك)
        if not request.user.has_perm(f'test2.export_template_{model_name}'):
            messages.error(request, 'لايوجد لديك صلاحية لتصدير القالب')
            return redirect('confirm_perm')

        # الحصول على اسم النموذج بالعربية
        model_name_obj = Modelnames.objects.get(modelname=model_name)
        table_name = model_name_obj.modelnameAr

        # جلب الحقول المرتبطة بالنموذج
        fields = CustomField.objects.filter(table=model_name).values_list('verbose_name', flat=True)

        if not fields:
            messages.warning(request, f"لا توجد حقول مرتبطة بالنموذج {table_name}.")
            return redirect('display_data',model_name,sys_name_id)

        # إنشاء DataFrame فارغ بأسماء الأعمدة
        df = pd.DataFrame(columns=fields)

        # إنشاء استجابة الملف
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        # response['Content-Disposition'] = f'attachment; filename="{table_name}.xlsx"'
        response['Content-Disposition'] = f"attachment; filename*=UTF-8''{urllib.parse.quote(table_name)}.xlsx"

        # كتابة DataFrame إلى ملف Excel
        with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)

        # تسجيل العملية
        UserAction.objects.create(user=request.user, action="تصدير قالب", model_name=table_name, details=f"تم تصدير قالب للنموذج {table_name}.")

        return response

    except Modelnames.DoesNotExist:
        messages.error(request, f"النموذج {table_name} غير موجود.")
        return redirect('display_data',model_name,sys_name_id)
        # return redirect('confirm_perm')
    except Exception as e:
        logging.error(f"خطأ أثناء تصدير القالب للنموذج {table_name}: {e}")
        messages.error(request, f"حدث خطأ أثناء تصدير القالب: {e}")
        return redirect('display_data',model_name,sys_name_id)
        # return redirect('confirm_perm')



# المستخدمة والسليمة
def formset_view1(request, model_name,sys_name_id):
    # print(request.user.get_all_permissions())
    if not request.user.has_perm(f'test2.import_data_dynamicmodels{model_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        form_Upload = ExcelUploadForm()
        if request.method == 'POST':
            form = ExcelUploadForm(request.POST, request.FILES)
            if form.is_valid():
                # excel_file = form.cleaned_data['file']
                excel_file = request.FILES['file']
                # حفظ الملف المحمل مؤقتًا والحصول على المسار
                file_name = excel_file.name  # احصل على اسم الملف
                
                # حفظ الملف المحمل مؤقتًا والحصول على المسار
                temp_file_path = handle_uploaded_file(excel_file, file_name)
                
                # print("Uploaded file:", file_name)  # طباعة اسم الملف
                # print("Temporary file path:", temp_file_path)  # طباعة المسار
                return redirect('import_data', model_name=model_name, excel_data=temp_file_path, sys_name_id=sys_name_id)
        else:
            form_Upload = ExcelUploadForm()
        # return render(request, 'display_data.html', {'form_Upload': form_Upload,  'model_name': model_name})
        return render(request, 'upload_excel.html', { 'sys_name_id':sys_name_id,'form_Upload': form_Upload,  'model_name': model_name})

# المستخدمة والسليمة
def formset_view(request, model_name, sys_name_id):
    if not request.user.has_perm(f'test2.import_data_dynamicmodels{model_name}'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        form_Upload = ExcelUploadForm()
        if request.method == 'POST':
            form = ExcelUploadForm(request.POST, request.FILES)
            if form.is_valid():
                excel_file = request.FILES['file']
                file_name = excel_file.name
                
                # حفظ الملف المحمل مؤقتًا والحصول على المسار
                temp_file_path = handle_uploaded_file(excel_file, file_name)
                
                # قراءة ملف Excel باستخدام pandas
                try:
                    df = pd.read_excel(temp_file_path)
                    if df.empty:
                        messages.error(request, 'الملف لا يحتوي على أي بيانات')
                        return render(request, 'upload_excel.html', {'sys_name_id': sys_name_id, 'form_Upload': form_Upload, 'model_name': model_name})
                except Exception as e:
                    messages.error(request, f'حدث خطأ أثناء قراءة الملف: {str(e)}')
                    return render(request, 'upload_excel.html', {'sys_name_id': sys_name_id, 'form_Upload': form_Upload, 'model_name': model_name})
                
                return redirect('import_data', model_name=model_name, excel_data=temp_file_path, sys_name_id=sys_name_id)
        else:
            form_Upload = ExcelUploadForm()
        
        return render(request, 'upload_excel.html', {'sys_name_id': sys_name_id, 'form_Upload': form_Upload, 'model_name': model_name})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import formset_factory

# def import_data2(request, model_name, excel_data):
#     formset_class, names_match = create_dynamic_formset(model_name, excel_data, request)
    
#     if names_match:
#         DynamicFormSet = formset_factory(create_dynamic_form(model_name), extra=0)
        
#         if request.method == 'POST':
#             formset = DynamicFormSet(request.POST, request.FILES)
            
#             # إذا كانت هناك أخطاء في الفورم، لا نقوم بالحفظ
#             if formset.is_valid():
#                 for form in formset:
#                     instance = form.save(commit=False)
#                     instance.save()
#                 messages.success(request, "تم حفظ البيانات بنجاح!")
#                 return redirect('display_data', model_name)
#             else:
#                 # إذا كانت النماذج تحتوي على أخطاء، عرض رسالة تفيد بذلك
#                 messages.error(request, "يرجى تصحيح الأخطاء في النموذج قبل الحفظ.")
#                 return render(request, 'formset_template.html', {'formset': formset, 'model_name': model_name})
        
#         else:
#             formset = formset_class
        
#         return render(request, 'formset_template.html', {'formset': formset, 'model_name': model_name})
    
#     else:
#         error_message = "أسماء الحقول في ملف الإكسل لا تتطابق مع النموذج المحدد"
#         return render(request, 'upload_excel.html', {'formset': None, 'model_name': model_name, 'error_message': error_message})

# # السليمة
# def create_dynamic_formset1(table_name, excel_file, request):
#     model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
#     fields = CustomField.objects.filter(table=table_name)
#     field_names = [field.field_name for field in fields]
#     custom_labels = [field.verbose_name for field in fields]
#     model = apps.get_model(app_label='test2', model_name=model_name)
    
#     # قراءة بيانات الإكسل
#     df = pd.read_excel(excel_file)
#     print(df)
#     # إنشاء قاموس لربط الأعمدة بين الأسماء المعروضة في نموذج البيانات والأسماء المعرّفة في قاعدة البيانات
#     model_columns = {field.verbose_name: field.field_name for field in fields}
#     model_columns2 = {field.field_name for field in fields}
#     excel_columns = df.columns.tolist()
    
#     # تحويل أسماء الأعمدة في DataFrame لتتطابق مع أسماء الحقول في النموذج
#     for col in excel_columns:
#         if col in model_columns:
#             df.rename(columns={col: model_columns[col]}, inplace=True)
    
#     # استبدال قيم Foreign Key بالمفتاح الرئيسي
#     for field in model._meta.get_fields():
#         if isinstance(field, models.ForeignKey):
#             related_model = field.related_model
#             RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)
#             related_field_name = CustomField.objects.filter(table=table_name,field_name=field.name).first()
#             related_name = related_field_name.related_name
#             # print(related_name,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
#             # related_field_name = field.name
#             # related_name2 = related_names[field]
            
#             try:
#                 # التحقق إذا كان العمود الموجود في DataFrame هو نفسه العمود الموجود في الملف
#                 if field.name not in df.columns:
#                     # استخدام رسالة منبثقة بدلاً من الطباعة
#                     messages.error(request, f"العمود {field.name} غير موجود في ملف الإكسل.")
#                     continue

#                 related_values = df[field.name].dropna()
#                 # related_values = df[field.name].dropna().unique()
                
#                 for idx, related_value in df[field.name].dropna().items():
#                     # print(idx)
#                     if related_value:
#                         related_objects = RelatedModel.objects.filter(**{related_name: related_value})
                        
#                         if related_objects.exists():
#                             for obj in related_objects:
#                                 related_id = obj.id
#                                 df.loc[df[field.name] == related_value, field.name] = related_id
#                         else:
#                             # إضافة رقم الصف إلى رسالة التحذير
#                             messages.warning(request, f"لا توجد قيم مرتبطة للعمود {related_field_name} بقيمة {related_value} في الصف {idx + 1}.")
#                     else:
#                         # إضافة رقم الصف إلى رسالة التحذير
#                         messages.warning(request, f"لا توجد قيم في العمود المرتبط {related_field_name} في الصف {idx + 1}.")
#             except Exception as e:
#                 messages.error(request, f"حدث خطأ غير متوقع في الصف {idx + 1}: {str(e)}")

#     # تحويل DataFrame إلى قائمة من القواميس
#     excel_data = df.to_dict(orient='records')
#     # print(excel_data)
#     # التحقق من مطابقة الأسماء بين الأعمدة
#     names_match = all(column in model_columns2 for column in df.columns.tolist())
#     if names_match:
#         messages.info(request, "أسماء الأعمدة متطابقة بين النموذج وملف الإكسل.")
#     else:
#         messages.warning(request, "يوجد اختلاف في أسماء الأعمدة بين النموذج وملف الإكسل.")

#     # إنشاء الفورم الديناميكي بناءً على النموذج
#     dynamicform = create_dynamic_form(table_name)
#     DynamicFormSet = formset_factory(dynamicform, extra=0)
#     formset = DynamicFormSet(initial=excel_data)
    
#     return formset, names_match

from django.forms import formset_factory, BooleanField



def import_data(request, model_name, excel_data, sys_name_id):
    formset_class, names_match = create_dynamic_formset(model_name, excel_data, request)
    
    if names_match:
        DynamicFormSet = formset_factory(create_dynamic_form_for_formset(model_name), extra=0)
        
        if request.method == 'POST':
            formset = DynamicFormSet(request.POST, request.FILES)
            
            if formset.is_valid():
                # إذا كانت النماذج صحيحة ولا توجد أخطاء، نقوم بالحفظ
                for form in formset:
                    if form.cleaned_data.get('DELETE'):
                        continue  # تجاهل الصفوف التي تم وضع علامة حذف عليها
                    instance = form.save(commit=False)  # حفظ النموذج بدون حفظ العلاقات
                    instance.save()  # حفظ النموذج في قاعدة البيانات
                    
                    # الآن معالجة الحقول ManyToMany بعد حفظ الكائن الأساسي
                    for field in form.instance._meta.get_fields():
                        if isinstance(field, models.ManyToManyField):
                            m2m_field = getattr(instance, field.name)
                            m2m_data = form.cleaned_data.get(field.name)
                            if m2m_data:
                                m2m_field.set(m2m_data)  # ربط الحقول ManyToMany
                    
                    instance.save()  # حفظ التغييرات في العلاقات ManyToMany
                    
                messages.success(request, "تم حفظ البيانات بنجاح!")
                return redirect('display_data', model_name, sys_name_id)
        
        else:
            # عند أول تحميل للنموذج (ليس POST)، يتم عرض الفورم مع البيانات
            formset = formset_class
        
        return render(request, 'formset_template.html', {'sys_name_id': sys_name_id, 'formset': formset, 'model_name': model_name})
    
    else:
        error_message = "أسماء الحقول في ملف الإكسل لا تتطابق مع النموذج المحدد"
        return render(request, 'upload_excel.html', {'sys_name_id': sys_name_id, 'formset': None, 'model_name': model_name, 'error_message': error_message})

# هذه هي دالة create_dynamic_formset المعدلة
# def create_dynamic_formset(table_name, excel_file, request):
#     model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
#     fields = CustomField.objects.filter(table=table_name)
#     field_names = [field.field_name for field in fields]
#     custom_labels = {field.field_name: field.verbose_name for field in fields}
#     model = apps.get_model(app_label='test2', model_name=model_name)
    
#     # قراءة بيانات الإكسل
#     df = pd.read_excel(excel_file)
#     model_columns = {field.verbose_name: field.field_name for field in fields}
#     model_columns2 = {field.field_name for field in fields}
#     excel_columns = df.columns.tolist()
    
#     # إزالة المسافات الزائدة من أسماء الأعمدة
#     df.columns = df.columns.str.strip()

#     # تحويل أسماء الأعمدة لتتطابق مع الحقول في النموذج
#     for col in excel_columns:
#         if col in model_columns:
#             df.rename(columns={col: model_columns[col]}, inplace=True)
    
#     # دالة لمعالجة الحقول المرتبطة (ForeignKey, ManyToMany)
#     def handle_related_field(field, df, model_columns, table_name, request, is_many_to_many=False):
#         try:
#             if field.name not in df.columns:
#                 messages.error(request, f"العمود {field.name} غير موجود في ملف الإكسل.")
#                 return
            
#             related_model = field.related_model
#             RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)
#             related_field_name = CustomField.objects.filter(table=table_name, field_name=field.name).first()
            
#             if related_field_name is None:
#                 messages.error(request, f"لم يتم العثور على حقل مرتبط مع {field.name}.")
#                 return
            
#             related_name = related_field_name.related_name
#             related_values = df[field.name].dropna()

#             for idx, related_value in related_values.items():
#                 if related_value:
#                     if is_many_to_many:
#                         related_values_list = related_value.split(',')  # افتراض أن القيم مفصولة بفواصل
#                         related_objects = RelatedModel.objects.filter(**{related_name + '__in': related_values_list})
                        
#                         if related_objects.exists():
#                             related_ids = [obj.id for obj in related_objects]
#                             df.loc[df[field.name] == related_value, field.name] = ', '.join(map(str, related_ids))
#                         else:
#                             messages.warning(request, f"لا توجد قيم مرتبطة للعمود {related_field_name} بقيمة {related_value} في الصف {idx + 1}.")
#                     else:
#                         related_objects = RelatedModel.objects.filter(**{related_name: related_value})
#                         if related_objects.exists():
#                             for obj in related_objects:
#                                 related_id = obj.id
#                                 df.loc[df[field.name] == related_value, field.name] = related_id
#                         else:
#                             messages.warning(request, f"لا توجد قيم مرتبطة للعمود {related_field_name} بقيمة {related_value} في الصف {idx + 1}.")
#                 else:
#                     messages.warning(request, f"لا توجد قيم في العمود المرتبط {related_field_name} في الصف {idx + 1}.")
#         except Exception as e:
#             messages.error(request, f"حدث خطأ غير متوقع في الصف {idx + 1}: {str(e)}")

#     # معالجة القيم المرتبطة بـ ForeignKey و ManyToMany
#     for field in model._meta.get_fields():
#         if isinstance(field, models.ForeignKey):
#             handle_related_field(field, df, model_columns, table_name, request, is_many_to_many=False)
#         elif isinstance(field, models.ManyToManyField):
#             handle_related_field(field, df, model_columns, table_name, request, is_many_to_many=True)

#     excel_data = df.to_dict(orient='records')
#     names_match = all(column in model_columns2 for column in df.columns.tolist())
    
#     if names_match:
#         messages.info(request, "أسماء الأعمدة متطابقة بين النموذج وملف الإكسل.")
#     else:
#         messages.warning(request, "يوجد اختلاف في أسماء الأعمدة بين النموذج وملف الإكسل.")
    
#     # تعديل النموذج الديناميكي لإضافة حقل DELETE
#     dynamicform = create_dynamic_form_for_formset(table_name)
#     DynamicFormSet = formset_factory(dynamicform, extra=0)
#     formset = DynamicFormSet(initial=excel_data)
    
#     return formset, names_match

# # دالة create_dynamic_form_for_formset المعدلة
# def create_dynamic_form_for_formset(table_name):
#     try:
#         model_instance = ModelSchema.objects.get(name=table_name)
#     except ObjectDoesNotExist:
#         raise ValueError(f"Model {table_name} does not exist.")

#     fields = CustomField.objects.filter(table=table_name)
#     field_names = [field.field_name for field in fields]
#     custom_labels = {field.field_name: field.verbose_name for field in fields}
#     related_names = {field.field_name: field.related_name for field in fields}

#     class DynamicForm(forms.ModelForm):
#         class Meta:
#             model = get_dynamic_model(table_name)
#             fields = field_names

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
            
#             for field_name in field_names:
#                 self.fields[field_name].label = custom_labels.get(field_name, field_name)
#                 field = self.Meta.model._meta.get_field(field_name)

#                 if isinstance(field, models.ForeignKey):
#                     self.handle_foreign_key(field_name, field)

#                 elif isinstance(field, models.ManyToManyField):
#                     self.handle_many_to_many(field_name, field)

#                 elif isinstance(field, (models.DateField, models.DateTimeField)):
#                     self.fields[field_name].widget = forms.DateInput(attrs={'type': 'date'})

#         def handle_foreign_key(self, field_name, field):
#             is_required = self.set_required(field_name)
#             related_model = field.related_model
#             related_name = related_names.get(field_name, field.remote_field.field_name)
            
#             RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

#             field = forms.ModelChoiceField(
#                 queryset=RelatedModel.objects.all(),
#                 required=is_required,
#                 widget=widgets.Select(attrs={'class': 'js-select2'})
#             )

#             field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj)) 
#             field.label = custom_labels.get(field_name, field_name) 
#             self.fields[field_name] = field


#         def handle_many_to_many(self, field_name, field):
#             is_required = self.set_required(field_name)
#             related_model = field.related_model
#             related_name = related_names.get(field_name, field.related_model._meta.pk.name)
#             RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

#             field = forms.ModelMultipleChoiceField(
#                 queryset=RelatedModel.objects.all(),
#                 required=is_required,
#                 widget=widgets.SelectMultiple(attrs={'class': 'js-select2'})
#             )

#             field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj))
#             field.label = custom_labels.get(field_name, field_name) 
#             self.fields[field_name] = field

#         @staticmethod
#         def set_required(field_name):
#             required_fields = ['field_name_that_should_be_required']
#             return field_name in required_fields

#     class CustomDynamicForm(DynamicForm):
#         DELETE = BooleanField(required=False, label="حذف الصف", initial=False)
    
#     return CustomDynamicForm


# مهمات
import os
import tempfile

TEMP_FILE_DIR = tempfile.gettempdir()

# في views.py
def handle_uploaded_file(f, file_name):
    temp_file_path = os.path.join(TEMP_FILE_DIR, file_name)
    
    with open(temp_file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    return temp_file_path

# def formset_view2(request, model_name):
#     # excel_file = 'C:\\Users\\saber\\Desktop\\DYNMAIC_SYSTEM\\empty_excel2.xlsx'
#     excel_file = request.FILES['excel_file']
#     formset_class = create_dynamic_formset(model_name, excel_file)
#     DynamicFormSet = formset_factory(create_dynamic_form(model_name), extra=0)
#     # DynamicFormSet = formset_factory(formset_class)
#     # DynamicFormSet = formset_factory(formset=formset_class)
#     dynamic_form = create_dynamic_form(model_name)
#     print(dynamic_form)
#     form = dynamic_form(request.POST,request.FILES)
#     # print(form, "kkkkkkkkkkkkkk")
#     print("nnnnnnnnnnnnnnnn")
#     if request.method == 'POST':
#         # form = DynamicFormSet(request.POST,request.FILES)
#         formset = DynamicFormSet(request.POST,request.FILES)
#         # print(form, "kkkkkkkkkkkkkk")
#         # formset = formset_class
#         # formset = DynamicFormSet(request.POST, request.FILES)id="id_tqyym
#         # formset = formset_class(request.POST, request.FILES, instances=excel_file)
#         # formset = formset_class(request.POST, None)
#         # formset = formset_class
#         # print(formset)
#         if formset.errors:
#             print("eeeeeeeeeeeeeeeeeeeee")
#             print(formset.errors)
            
#         if formset.is_valid():
#             for form in formset:
#                 instance = form.save(commit=False)  # حفظ النموذج مؤقتًا بدون حفظه في قاعدة البيانات
#                 # قم بتعديل البيانات حسب احتياجاتك هنا
#                 instance.save()  # حفظ النموذج الآن بعد التعديلات اللازمة
#             return redirect('display_data', model_name)

#         # if formset.is_valid():
#         #     print("vvvvvvvvvvvvvvvvv")
#         #     instances = formset.save(commit=False)
#         #     for instance in instances:
#         #         print("sssssssssssssssssss")
#         #         instance.save()
#         #     # formset.save()
#         #     return redirect('display_data', model_name)
#     else:
#         # return redirect('formset_template', model_name, formset)


#         formset = formset_class # تم تحديث هذا السطر
#         # formset = DynamicFormSet # تم تحديث هذا السطر
    
#     return render(request, 'formset_template.html', {'formset': formset, 'model_name': model_name})

# def formset_view24(request, model_name):
#     form = ExcelUploadForm()
#     formset_class = create_dynamic_formset(model_name, excel_data)
#     if request.method == 'POST':
#         form = ExcelUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = form.cleaned_data['file']
#             df = pd.read_excel(excel_file)
#             excel_data = df.to_dict(orient='records')
#             formset_class = create_dynamic_formset(model_name, excel_data)
#             DynamicFormSet = formset_factory(create_dynamic_form(model_name), extra=0)

#             formset = DynamicFormSet(request.POST, request.FILES)
#             if formset.is_valid():
#                 for form in formset:
#                     instance = form.save(commit=False)
#                     instance.save()
#                 return redirect('display_data', model_name)
#     else:
#         form = ExcelUploadForm()
#         # formset = DynamicFormSet(request.POST, request.FILES)
#         formset = formset_class 
#     return render(request, 'formset_template.html', {'formset': formset, 'model_name': model_name})


# def formset_view1(request, model_name):
#     excel_file = request.FILES['excel_file']
#     # excel_file = upload_file(request)
#     formset_class = create_dynamic_formset(model_name, excel_file)
#     DynamicFormSet = formset_factory(create_dynamic_form(model_name), extra=0)
#     print("nnnnnnnnnnnnnnnn")
#     print(excel_file)
#     print(request.method,"ggggggggggggggggggg")
#     if request.method == 'POST' and request.FILES['excel_file']:
#         excel_file = request.FILES['excel_file']
#         df = pd.read_excel(excel_file)
#         excel_data = df.to_dict(orient='records')
#         print(excel_data,"ppppppppppppppppppppppp")
#         return redirect('display_data', model_name)

#     else:
#         # print("nooooooo")
#         formset = formset_class # تم تحديث هذا السطر
    
#     return render(request, 'formset_template.html', {'formset': formset, 'model_name': model_name})
#     # return render(request, 'formset_template.html', { 'model_name': model_name})


import logging


def export_to_excel(request, model_name, sys_name_id):
    try:
        # التحقق من الصلاحيات
        if not request.user.has_perm(f'test2.export_data_dynamicmodels{model_name}'):
            messages.error(request, 'لايوجد لديك صلاحية')
            return redirect('confirm_perm')

        # جلب النموذج الديناميكي
        model = get_dynamic_model(model_name)
        if not model:
            messages.error(request, f"النموذج {table_name} غير موجود.")
            return redirect('display_data', model_name, sys_name_id)

        queryset = model.objects.all()
        model_schema = ModelSchema.objects.get(name=model_name)
        columns = FieldSchema.objects.filter(model_schema=model_schema)
        
        # الحصول على اسم النموذج بالعربية
        model_name_obj = Modelnames.objects.get(modelname=model_name)
        table_name = model_name_obj.modelnameAr

        if not queryset.exists():
            return HttpResponse("لا توجد بيانات لتصديرها.", status=404)

        # إنشاء قائمة لتخزين البيانات
        data = []

        # إنشاء قائمة لأسماء الأعمدة (بدون id)
        headers = []  # تمت إزالة 'id'

        # إضافة أسماء الحقول إلى headers
        for field in columns:
            headers.append(field.kwargs["verbose_name"])

        # جمع البيانات من queryset (بدون id)
        for item in queryset:
            row = []  # تمت إزالة item.id

            for field in model._meta.get_fields():

                if field.name == 'id':  # تخطي حقل id
                    continue

                if not hasattr(item, field.name):
                    continue

                # التعامل مع الحقول المترابطة (ManyToOne, ManyToMany, ForeignKey)
                if field.is_relation:
                    field_name = field.name
                    related_object = getattr(item, field_name)

                    if isinstance(related_object, models.Manager):  # إذا كانت علاقة ManyToMany
                        related_values = [str(related_item) for related_item in related_object.all()]
                        row.append(', '.join(related_values) if related_values else 'لايوجد')
                    elif related_object:  # إذا كانت علاقة ForeignKey
                    
                        related_name = CustomField.objects.get(table=model_name, field_name=field).related_name

                        # related_name = field.related_model._meta.get_field('name')  # للحصول على اسم الحقل المرتبط
                        row.append(getattr(related_object, related_name) if related_object else 'لايوجد')
                    else:
                        row.append('لايوجد')

                # التعامل مع الحقول من نوع الصورة أو الملفات
                elif isinstance(field, (models.ImageField, models.FileField)):
                    file_value = getattr(item, field.name)
                    if file_value:
                        row.append(file_value.url)  # إضافة رابط الملف
                    else:
                        row.append('لايوجد')

                else:
                    row.append(getattr(item, field.name))


            data.append(row)

        # فحص عدد الأعمدة في headers و data
        if len(headers) != len(data[0]):
            return HttpResponse(f"خطأ: عدد الأعمدة في headers ({len(headers)}) لا يتطابق مع عدد الأعمدة في البيانات ({len(data[0])}).", status=500)

        # تحويل البيانات إلى DataFrame
        df = pd.DataFrame(data, columns=headers)

        # إنشاء HttpResponse مع نوع محتوى Excel
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f"attachment; filename*=UTF-8''{urllib.parse.quote(table_name)}.xlsx"

        # تصدير DataFrame إلى Excel
        df.to_excel(response, index=False, engine='openpyxl')

        return response
    except Exception as e:
        # تسجيل الخطأ وإظهار رسالة
        logging.error(f"خطأ أثناء تصدير البيانات للنموذج {table_name}: {e}")
        messages.error(request, f"حدث خطأ أثناء تصدير البيانات: {e}")
        return redirect('display_data', model_name, sys_name_id)     


# views.py
import pandas as pd
from django.shortcuts import render
from .forms import ExcelUploadForm

def upload_excel(request):
    data = None

    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)
            data = df.to_html()  # تحويل البيانات إلى جدول HTML
    else:
        form = ExcelUploadForm()
    
    return render(request, 'upload_excel.html', {'form': form, 'data': data})

# def import_data_from_excel2(request):
#     try:
#         df = pd.read_excel('C:\\Users\\saber\\Desktop\\DYNMAIC_SYSTEM\\empty_excel.xlsx')

#         # تحويل البيانات من DataFrame إلى قائمة من القواميس
#         data = df.to_dict(orient='records')
#         return JsonResponse(data, safe=False)
#         # return render(request, 'table_editable.html', {'data': data})
#     except Exception as e:
#         # يمكنك إدراج رمز الخطأ هنا أو التعامل مع الاستثناء بالطريقة التي تراها مناسبة
#         print("حدث خطأ: ", e)
#         return HttpResponse("حدث خطأ: {}".format(e))

# def api_service(request):

#     return render(request, 'API_Service.html')

# def edit_datas(request, model_name, row_id):
#     table_name = 'DynamicModels' + model_name.capitalize()
#     model = apps.get_model(app_label='test2', model_name=table_name)
#     dataId = model.objects.get(id=row_id)
#     # print(dataId, "ddddddddddddd")
#     form_class = create_dynamic_form(model_name)
#     print(request.method, "ennnnnnnnn")
#     if request.method == 'POST':
#         print("ennnnnnnnn")
#         edit_form = form_class(request.POST, request.FILES, instance=dataId)
#         if edit_form.is_valid():
#             edit_form.save()
#             return redirect('display_data', model_name)
#     else:
#         edit_form = form_class(instance=dataId)

#     return edit_form
    
#     # return render(request, 'display_data.html', {'edit_form': edit_form})

# def show_datas(request,model_name, row_id):
#     table_name = 'DynamicModels' + model_name.capitalize()
#     model = apps.get_model(app_label='test2', model_name=table_name)
#     dataId = model.objects.get(id=row_id)
#     print(dataId, "ddddddddddddd")
#     form_class = create_dynamic_form(model_name)
#     print(request.method, "ennnnnnnnn")
#     if request.method == 'POST':
#         print("ennnnnnnnn")
#         show_form = form_class(request.POST, request.FILES, instance=dataId)
#         if show_form.is_valid():
#             show_form.save()
#             return redirect('display_data', model_name)
#     else:
#         show_form = form_class(instance=dataId)

#     return show_form
#     # return render(request, 'my_view2.html', {'form': form})


# def table_list(request):
#     tables = Table.objects.all()
#     return render(request, 'table_list.html', {'tables': tables})

# def get_table_fields(request):

#     # table_name = request.GET.get('table_name')  # استرداد اسم الجدول من الطلب
#     table_name = 'dynamic_models_table8'
#     print(table_name)
#     db_table_exists(table_name)
#     print(db_table_exists(table_name))
#     # قاموس يحتوي على تعيينات رموز أنواع الحقول
#     type_codes = {
#         16: "bool",
#         17: "bytea",
#         20: "int",
#         21: "int",
#         23: "int",
#         25: "text",
#         700: "float",
#         16384: "relation",
#         # إضافة تعيين للمفاتيح الأجنبية والعلاقات
#         1022: "foreign_key",
#         1028: "foreign_key",
#         1116: "foreign_key",
#         # يمكنك إضافة المزيد من تعيينات الأنواع إذا لزم الأمر
#     }

#     cursor = custm_conncetion()


#     # استعلام SQL لاسترداد حقول الجدول
#     query = "SELECT * FROM dynamic_models_table7"

#     # تنفيذ الاستعلام
#     cursor.execute(query)

#     # استرداد جميع الحقول من مؤشر النتائج
#     # fields = [desc[0] for desc in cursor.description]

#     # # تحويل قائمة الحقول إلى استجابة JSON
#     # fields_json = json.dumps({"fields": fields})

#     # # طباعة استجابة JSON
#     # print(fields_json)
#     # استرداد حقول الجدول وأنواعها
#     fields = []
#     for desc in cursor.description:
#         field_name = desc.name
#         # field_type_code = desc.data_type
#         field_type_code = desc.type_code
#         print(field_type_code, 'typeeeeeeeeeeeeee')
#         # field_type = desc.data_type
#         field_type = type_codes.get(field_type_code, "unknown")
#         fields.append({"name": field_name, "type": field_type})

#     # تحويل قائمة الحقول إلى استجابة JSON
#     fields_json = json.dumps({"fields": fields})

#     # طباعة استجابة JSON
#     print(fields_json)

#     # إغلاق مؤشر النتائج واتصال قاعدة البيانات
#     cursor.close()
#     # conn.close()


#     # استخدام استعلام SQL لاسترداد حقول الجدول
#     try:
#         # connection = connections['default']  # استخدام اسم الاتصال الافتراضي
#         cursor = custm_conncetion()
#         cursor.execute(f"SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'dynamic_models_table8'")
#         print(cursor,"JJJJJJJJJJJJJJJJJJJJJJJJ")

#         fields = [row[0] for row in cursor.fetchall()]
#         cursor.close()
#         print(fields,"mmmmmmmmmmmmmmbv")
#         return JsonResponse({'fields': fields})
#     except Exception as e:
#         return JsonResponse({'error': str(e)})


# def display_model_data(model_name):
#     # ModelClass = apps.get_model(model_name)
#     ModelClass = apps.get_model(app_label='test2', model_name=model_name)

#     if ModelClass is None or not issubclass(ModelClass, Model):
#         return "Invalid model name"

#     fields = ModelClass._meta.fields
#     data = ModelClass.objects.all()
#     print(data)

#     if not data:
#         return "No data available"

#     table_html = "<table>"
#     table_html += "<thead><tr>"
#     for field in fields:
#         table_html += "<th>{}</th>".format(field.verbose_name)
#     table_html += "</tr></thead>"

#     table_html += "<tbody>"
#     for record in data:
#         table_html += "<tr>"
#         for field in fields:
#             table_html += "<td>{}</td>".format(getattr(record, field.name))
#         table_html += "</tr>"
#     table_html += "</tbody>"

#     table_html += "</table>"

#     return format_html(table_html)

# def save_data(request):
#     if request.method == 'POST':
#         # return redirect('display_data', id=t.id)
#      return render(request, 'display_data.html', {'data': data, 'fields': fields})

# def test_model_with_foreign_key(model_schema, another_model_schema):
#         print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
#         print(django.db.models.IntegerField,'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
#         print(django.db.models.ForeignKey,'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
#         FieldSchema.objects.create(
#             name="related",
#             model_schema=model_schema,
#             class_name='django.db.models.fields.related.ForeignKey',
#             kwargs={
#                 "to": another_model_schema,
#                 "on_delete": django.db.models.deletion.CASCADE,
#                 "related_name": "parent_objects",
#             },
#         )
#         print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')

#         related_model = another_model_schema.as_model()
#         print(type(related_model),'dddddddddddddddddddddddddddddddddddddddddd')
#         model = model_schema.as_model()

#         related_instance = related_model.objects.create()
#         model_instance = model.objects.create(related=related_instance)

#         # related objects should be accessible through related managers
#         assert model_instance.related == related_instance
#         assert related_instance.parent_objects.first() == model_instance

#         # CASCADE should work correctly
#         related_instance.delete()
#         with TestCase.assertRaises(model.DoesNotExist):
#             model.objects.get(pk=model_instance.pk)


# def test_table_relationship(model_schema, another_model_schema):
#         # options = [("django.db.models.ForeignKey", models.ForeignKey, {"on_delete": models.CASCADE}),],
#         options = {
#             "on_delete": models.CASCADE,
#             "blank": True,
#             "related_name": "parent_objects",
#             "null": True,
#             "unique": False,
#             }

#         field_schema = FieldSchema(
#             name="field",
#             class_name="django.db.models.ForeignKey",
#             model_schema=model_schema,
#             kwargs={**options, "to": another_model_schema},
#         )
#         field_schema.null = True
#         field = FieldFactory(field_schema).make_field()
#         assert isinstance(field, model_schema)
#         assert field.null is True


# def showObjectLists(request):
#     modelNamesQuerySet = Modelnames.objects.all()
#     modelNames = list()
#     for model in modelNamesQuerySet:
#         modelNames.append(model.modelname)
#     cont_dict = {
#         'modelNames' : modelNames,
#         'get' : True
#     }
#     if request.POST:
#         model = ModelSchema.objects.get(name=request.POST['modelname']).as_model()
#         objList = model.objects.all().values()
#         fieldNames = list()
#         noEntry = False
#         try:
#             for x in objList[0]:
#                 fieldNames.append(x)
#         except Exception as e:
#             noEntry = True
#         cont_dict = {
#             'modelNames' : modelNames,
#             'objects' : objList,
#             'noEntry' : noEntry,
#             'fieldNames' : fieldNames,
#             'objectType' : request.POST['modelname'],
#             'get' : False
#         }
#     return render(request, 'displayObjects.html', context = cont_dict)


def get_tables(request):
    tables = ModelSchema.objects.all()
    
    return render(request, 'index.html', {'tables': tables})
    # return render(request, 'index.html', {'interfaces': interfaces})


from django.db.models import Model
from django.utils.html import format_html

# def create_dynamic_model(request):
#     model_schema = ModelSchema('DynamicMode2')
#     model_schema.add_field(FieldSchema('name', models.CharField, max_length=100))
#     model_schema.add_field(FieldSchema('age', models.IntegerField))
#     # model_schema.add_field(FieldSchema('model_a', models.OneToOneField, to='Field', on_delete=models.CASCADE))
#     model_schema.save()

#     DynamicModel = ModelFactory().create_model(model_schema)

#     # reg_model = model_schema.as_model()
#     # admin.site.register(DynamicModel)
#     # reload(import_module(settings.ROOT_URLCONF))
#     # clear_url_caches()
#     # يمكنك استخدام DynamicModel هنا في العمليات الأخرى

#     # القيام بمهمة أخرى...

#     return HttpResponse('تم إنشاء النموذج الديناميكي بنجاح!')
#     # return render(request, 'index.html')

def dynamic_form(request):
   
    return render(request, 'dynamic_form.html')
    # re

def get_table_names():
    # conn = psycopg2.connect(database="اسم_قاعدة_البيانات", user="اسم_المستخدم", password="كلمة_المرور", host="عنوان_الخادم", port="رقم_المنفذ")
    cursor = custm_conncetion()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    # conn.close()
    return table_names


