






from django import forms

from django.apps import apps
from django.db import models
from django.forms import widgets

from django.forms import formset_factory
import pandas as pd
from django.contrib import messages
from django.forms import formset_factory, BooleanField


# في ملف forms.py

from django import forms
from .models import TblSystem, FieldCondition, CustomField
from django import forms
# from .models import DynamicModel
from dynamic_models.models import FieldSchema, ModelSchema

# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.contrib.auth.models import AbstractUser, Group, Permission, User

from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.utils.translation import ugettext_lazy as _
from .models import CustomUser, CustmReportHeader, UserAction
# from guardian.shortcuts import get_perms

from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

from django import forms
from django.contrib.auth.forms import UserCreationForm
# from guardian.shortcuts import get_perms
# from guardian.utils import get_identity
# from guardian.models import User

from .models import CustomUser


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import Permission

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="البريد الإلكتروني")
    first_name = forms.CharField(label="الاسم الأول")
    last_name = forms.CharField(label="الاسم الأخير")
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput)
    permissions = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'ul'}), label='الصلاحيات')
    groups = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'ul'}), label='الصلاحيات')

    class Meta:
        model = CustomUser
        fields = '__all__'
        labels = {
            'email': 'البريد الإلكتروني',
            'username': 'اسم المستخدم',
            'first_name': 'الاسم الأول',
            'last_name': 'الاسم الأخير',
            'password1': 'كلمة المرور',
            'password2': 'تأكيد كلمة المرور',
            'is_active': 'نشط',
            'phone_number': 'تلفون',
            'country': 'البلد',
            'date_of_birth': 'تاريخ الميلاد',
            'date_joined': 'تاريخ التفعيل',
            'user_permissions': ' صلاحيات المستخدم',
            'last_login': 'اخر دخول',
            'is_Superuser': 'سوبر يوزر',
        }
        help_texts = {
            'email': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_instance = CustomUser.objects.first()
        self.permissions = Permission.objects.all()
        if user_instance:
            self.fields['permissions'].choices = [(perm.id, perm.name) for perm in self.permissions]

    def clean(self):
        cleaned_data = super().clean()
        selected_permissions = cleaned_data.get('permissions')

        if selected_permissions:
            permission_ids = [perm.id for perm in self.permissions]
            cleaned_permissions = [perm_id for perm_id in selected_permissions if perm_id not in permission_ids]
            cleaned_data['permissions'] = cleaned_permissions

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label='اسم المستخدم')
    # email = forms.EmailField(label='ايميل')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput)



class FieldSchemaForm(forms.ModelForm):
    class Meta:
            model = FieldSchema
            fields = '__all__'
            # fields = ['name, class_name, kwargs']
            
class ExcelUploadForm(forms.Form):
    file = forms.FileField(label='اختيار ملف Excel')
# class DynamicForm(forms.ModelForm):
#     class Meta:
#         model = DynamicModel
#         fields = ['dynamic_fields']


class TblSystemForm(forms.ModelForm):
    class Meta:
        model = TblSystem
        fields = ('name',)

    def clean_name(self):
        # الحصول على القيمة الأصلية للحقل
        name = self.cleaned_data.get('name')
        if name:
            # استبدال المسافات بـ "_"
            name = name.replace(' ', '_')
        return name



from django import forms
from .models import CustomField

class CustomFieldForm(forms.ModelForm):
    class Meta:
        model = CustomField
        fields = ['verbose_name', 'null_or_not', 'unique_or_not' ]
        # fields = '__all__'
        labels = {
            'field_name': ' اسم الحقل',
            'field_type': ' نوع الحقل',
            'verbose_name': ' عنوان الحقل',
            # 'max_length': 'طول الحقل',
            'null_or_not': 'يقبل قيمة فارغة',
            # 'blank_or_not': 'Blank',
            'unique_or_not': 'قيمة فريدة ',
            # 'on_delete': 'يسمح بذف البيانات',
            # 'related_name': 'اسم العلاقة',
            # 'related_table': ' الجدول المرتبط بة',
            # 'is_related': 'مرتبط'
        }

    def __init__(self, *args, **kwargs):
        super(CustomFieldForm, self).__init__(*args, **kwargs)
        # Customize ForeignKey field display
        if 'related_table' in self.fields:
            self.fields['related_table'].queryset = CustomField.objects.all()
            self.fields['related_table'].label_from_instance = lambda obj: f"{obj.field_name}"


class PermissionForm(forms.Form):
    codename = forms.CharField(label='اسم الكود', max_length=100)
    name = forms.CharField(label='اسم الصلاحية', max_length=100)


class CustmReportHeaderForm(forms.ModelForm):
    
    class Meta:
        model = CustmReportHeader
        fields = '__all__'
        widgets = {

            'field1_right': forms.TextInput(attrs={'class': 'form-control'}),
            'field2_right': forms.TextInput(attrs={'class': 'form-control'}),
            'field3_right': forms.TextInput(attrs={'class': 'form-control'}),
            'field1_left': forms.TextInput(attrs={'class': 'form-control'}),
            'field2_left': forms.TextInput(attrs={'class': 'form-control'}),
            'field3_left': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserActionForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(UserActionForm,self).__init__(*args, **kwargs)
        self.fields["details"] = forms.CharField(
            required = False,
            label = "البيانات",
            widget=forms.Textarea(attrs={"row": "3","column": "2" , "class":'form-field form-control'}),
        )
    class Meta:
        model = UserAction
        fields = '__all__'
        # widgets = {
        #     'details':
        # }



from django.contrib.auth.models import User

class UserActionForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label="المستخدم")
    action = forms.CharField(max_length=255, required=False, label="العملية")
    model_name = forms.CharField(max_length=255, required=False, label="الجدول")
    details = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,  # تحديد عدد الصفوف
            'cols': 20,  # تحديد عدد الأعمدة
            'style': 'width: 100%;'  # لضبط العرض ليكون كاملًا
        }), 
        required=False, 
        label="البيانات"
    )
    timestamp_from = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="من تاريخ")
    timestamp_to = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="إلى تاريخ")

from django import forms
from .models import FieldCondition

# class FieldConditionForm(forms.ModelForm):
#     class Meta:
#         model = FieldCondition
#         fields = '__all__'  # عرض جميع الحقول

from django import forms
from .models import FieldCondition


# def get_model_fields(model_name):
#     """
#     دالة لاسترجاع قائمة الحقول في نموذج معين بناءً على اسم النموذج.
#     """
#     try:
#         # استرجاع النموذج من اسمه
#         model = get_dynamic_model(model_name)
#         # استرجاع قائمة الحقول
#         # fields = [field.name for field in model._meta.get_fields()]
#         fields1 = CustomField.objects.filter(table=model_name)
#         fields = [(field.name, field.verbose_name) for field in model._meta.fields]
       
#         return fields
#     except LookupError:
#         # إذا لم يتم العثور على النموذج
#         return []

def get_model_fields(model_name):
    """
    دالة لاسترجاع قائمة الحقول في نموذج معين بناءً على اسم النموذج.
    """
    try:
        # استرجاع الحقول من CustomField
        fields = CustomField.objects.filter(table=model_name).values_list('field_name', 'verbose_name')
        return fields
    except LookupError:
        # إذا لم يتم العثور على النموذج
        return []


from django import forms
from .models import FieldCondition, CustomField
from django.apps import apps

class FieldConditionForm2(forms.ModelForm):
    CONDITION_CHOICES = [
        ("equals", "يساوي"),
        ("not_equals", "لا يساوي"),
        ("contains", "يحتوي على"),
        ("not_contains", "لا يحتوي على"),
    ]
    
    ACTION_CHOICES = [
        ("hide", "إخفاء"),
        ("disable", "تعطيل"),
        ("filter_values", "تصفية القيم"),
    ]

    field_name = forms.ChoiceField(label="اختر الحقل المتأثر", choices=[])  
    dependent_field = forms.ChoiceField(label="اختر الحقل المعتمد عليه", choices=[])  
    condition = forms.ChoiceField(label="اختر الشرط", choices=CONDITION_CHOICES)
    condition_value = forms.ChoiceField(label="القيمة المطلوبة لتنفيذ الشرط", choices=[], required=False)
    action = forms.ChoiceField(label="الإجراء عند تحقق الشرط", choices=ACTION_CHOICES)
    # restricted_values = forms.CharField(
    #     label="القيم المحظورة (للتصفية فقط)",
    #     required=False,
    #     widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'})
    # )
    restricted_values = forms.ChoiceField(
        label="القيم المتاحة",
        required=False,
        choices=[],
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = FieldCondition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        model_name = kwargs.pop('model_name', None)
        field_name_selected = kwargs.pop('field_name_selected', None)  # الحقل المختار لجلب القيم
        super(FieldConditionForm, self).__init__(*args, **kwargs)

        if model_name:
            fields = get_model_fields(model_name)  # جلب الحقول من CustomField
            
            self.fields['field_name'].choices = fields
            self.fields['dependent_field'].choices = fields

            # جلب القيم الخاصة بالحقل المتأثر فقط في حالة تحديده
            if field_name_selected:
                try:
                    model = get_dynamic_model(model_name)
                    values = model.objects.values_list(field_name_selected, flat=True).distinct()
                    print(values,"gggggggggggggggggggggggggggggggggggggggg")
                    self.fields['condition_value'].choices = [(value, value) for value in values if value is not None]
                except Exception as e:
                    print(f"Error fetching field values: {e}")  # تصحيح أي أخطاء محتملة


class FieldConditionForm1(forms.ModelForm):
    CONDITION_CHOICES = [
        ("equals", "يساوي"),
        ("not_equals", "لا يساوي"),
        ("contains", "يحتوي على"),
        ("not_contains", "لا يحتوي على"),
    ]
    
    ACTION_CHOICES = [
        ("hide", "إخفاء"),
        ("disable", "تعطيل"),
        ("filter_values", "تصفية القيم"),
    ]

    field_name = forms.ChoiceField(label="اختر الحقل المتأثر", choices=[])  
    dependent_field = forms.ChoiceField(label="اختر الحقل المعتمد عليه", choices=[])  
    condition = forms.ChoiceField(label="اختر الشرط", choices=CONDITION_CHOICES)
    condition_value = forms.CharField(label="القيمة المطلوبة لتنفيذ الشرط", widget=forms.TextInput(attrs={'class': 'form-control'}))
    action = forms.ChoiceField(label="الإجراء عند تحقق الشرط", choices=ACTION_CHOICES)

    restricted_values = forms.MultipleChoiceField(
        label="القيم المتاحة",
        required=False,  
        choices=[],
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = FieldCondition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        model_name = kwargs.pop('model_name', None)
        selected_field = kwargs.pop('selected_field', None)
        super(FieldConditionForm, self).__init__(*args, **kwargs)

        if model_name:
            fields = get_model_fields(model_name)
            self.fields['field_name'].choices = fields
            self.fields['dependent_field'].choices = fields

        if model_name and selected_field:
            field_values = self.get_field_values(model_name, selected_field)
            self.fields['restricted_values'].choices = field_values
            print(f"✅ قيم restricted_values المحملة: {field_values}")

    def get_field_values(self, model_name, field_name):
        model = get_dynamic_model(model_name)
        if not model:
            print("❌ النموذج غير موجود!")
            return []

        try:
            values = model.objects.values_list(field_name, flat=True).distinct()
            print(f"✅ القيم المسترجعة للحقل '{field_name}': {list(values)}")
            return [(str(value), str(value)) for value in values if value is not None]
        except Exception as e:
            print(f"⚠️ خطأ أثناء استرجاع القيم: {e}")
            return []

    def clean_restricted_values(self):
        """ تحويل القيم المختارة إلى قائمة قبل الحفظ """
        data = self.cleaned_data.get("restricted_values", [])
        print(f"📌 البيانات التي سيتم حفظها في restricted_values: {data}")
        return list(data)  # تأكد أنها قائمة

class FieldConditionForm(forms.ModelForm):
    CONDITION_CHOICES = [
        ("equals", "يساوي"),
        ("not_equals", "لا يساوي"),
        ("contains", "يحتوي على"),
        ("not_contains", "لا يحتوي على"),
    ]
    
    ACTION_CHOICES = [
        ("hide", "إخفاء"),
        ("disable", "تعطيل"),
        ("filter_values", "تصفية القيم"),
    ]

    field_name = forms.ChoiceField(label="اختر الحقل المتأثر", choices=[])
    dependent_field = forms.ChoiceField(label="اختر الحقل المعتمد عليه", choices=[])
    condition = forms.ChoiceField(label="اختر الشرط", choices=CONDITION_CHOICES)
    condition_value = forms.CharField(label="القيمة المطلوبة لتنفيذ الشرط", widget=forms.TextInput(attrs={'class': 'form-control'}))
    action = forms.ChoiceField(label="الإجراء عند تحقق الشرط", choices=ACTION_CHOICES)

    restricted_values = forms.MultipleChoiceField(
        label="القيم المتاحة",
        required=False,
        choices=[],
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = FieldCondition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        model_name = kwargs.pop('model_name', None)
        selected_field = kwargs.pop('selected_field', None)
        super(FieldConditionForm, self).__init__(*args, **kwargs)

        if model_name:
            fields = get_model_fields(model_name)
            self.fields['field_name'].choices = fields
            self.fields['dependent_field'].choices = fields

        if model_name and selected_field:
            self.update_restricted_values(model_name, selected_field)

    def update_restricted_values(self, model_name, field_name):
        field_values = self.get_field_values(model_name, field_name)
        self.fields['restricted_values'].choices = field_values
        print(f"✅ القيم المحددة: {field_values}")

    def get_field_values(self, model_name, field_name):
        model = get_dynamic_model(model_name)
        if not model:
            print("❌ النموذج غير موجود!")
            return []

        try:
            values = model.objects.values_list(field_name, flat=True).distinct()
            print(f"✅ القيم المسترجعة: {list(values)}")
            return [(str(value), str(value)) for value in values if value is not None]
        except Exception as e:
            print(f"⚠️ خطأ أثناء جلب القيم: {e}")
            return []


import os

def get_dynamic_model(model_name):
    # طريقة الاستدعا
    # model_schema = ModelSchema.objects.get(name=model_name)
    #     modelss=[]
    #     for model in model_schema:
    #         modelss.append(model.as_model())
    #     print(modelss)
    app_label = 'test2'
    try:
        # model = apps.get_model('dynamic_models', model_name = model_schema)
        # model = apps.get_model('dynamic_models', model_name = model_name.lower())
        # app_config = apps.get_app_config('test2')
        # app_path = os.path.dirname(app_config.path)

        # # طباعة مسار التطبيق
        # print(f"App path for '{app_label}': {app_path}")
        # model2 = model_name = 'DynamicModels' + model_name.replace(" ", "").capitalize()
        # from  dist.manage._internal.test2.models import model2
        # print(model2,"ooooooooooooooooooooooo")
        model = apps.get_model( 'test2', model_name = 'DynamicModels' + model_name.replace(" ", "").capitalize())
        print(model,"yyyyyyyyyyyyyyyyyyyyyy")
        if model:
            return model
    except LookupError:
        print(f"Model {model_name} not found.")
    return None




def create_dynamic_form11(table_name):
    model_name = ModelSchema.objects.get(name=table_name)
    fields = CustomField.objects.filter(table=table_name)
    field_names = [field.field_name for field in fields]
    custom_labels = [field.verbose_name for field in fields]
    related_names = {field.field_name: field.related_name for field in fields}


    class DynamicForm(forms.ModelForm):
        class Meta:
            model = get_dynamic_model(table_name)
            fields = field_names

        def __init__(self, *args, **kwargs):
            super(DynamicForm, self).__init__(*args, **kwargs)
            for i, field_name in enumerate(field_names):
                self.fields[field_name].label = custom_labels[i]

                field = self.Meta.model._meta.get_field(field_name)

                # إذا كان الحقل من نوع ForeignKey
                if isinstance(field, models.ForeignKey):
                    self.handle_foreign_key(field_name, field)

                elif isinstance(field, models.ManyToManyField):
                    self.handle_many_to_many(field_name, field)

                elif isinstance(field, (models.DateField, models.DateTimeField)):
                    self.fields[field_name].widget = forms.DateInput(attrs={'type': 'date'})

        def handle_foreign_key(self, field_name, field):
            is_required = self.set_required(field_name)
            related_model = field.related_model
            related_name = related_names.get(field_name, field.remote_field.field_name)
            
            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

            field = forms.ModelChoiceField(
                queryset=RelatedModel.objects.all(),
                to_field_name=related_name,
                required=is_required,
                widget=widgets.Select(attrs={'class': 'js-select2'})
            )

            field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj)) 
            self.fields[field_name] = field


        def handle_many_to_many(self, field_name, field):
            is_required = self.set_required(field_name)
            related_model = field.related_model
            related_name = related_names.get(field_name, field.related_model._meta.pk.name)

            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

            field = forms.ModelMultipleChoiceField(
                queryset=RelatedModel.objects.all(),
                to_field_name=related_name,
                required=is_required,
                widget=widgets.SelectMultiple(attrs={'class': 'js-select2'})
            )

            field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj))  
            self.fields[field_name] = field


        @staticmethod
        def set_required(field_name):
            required_fields = ['field_name_that_should_be_required']
            return field_name in required_fields

    return DynamicForm

from django import forms
from django.apps import apps
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.forms import widgets

def create_dynamic_form(table_name):
    try:
        model_instance = ModelSchema.objects.get(name=table_name)
    except ObjectDoesNotExist:
        raise ValueError(f"Model {table_name} does not exist.")

    fields = CustomField.objects.filter(table=table_name)
    field_names = [field.field_name for field in fields]
    custom_labels = {field.field_name: field.verbose_name for field in fields}
    related_names = {field.field_name: field.related_name for field in fields}

    class DynamicForm(forms.ModelForm):
        class Meta:
            model = get_dynamic_model(table_name)
            fields = field_names

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for field_name in field_names:
                self.fields[field_name].label = custom_labels.get(field_name, field_name)
                field = self.Meta.model._meta.get_field(field_name)

                if isinstance(field, models.ForeignKey):
                    self.handle_foreign_key(field_name, field)

                elif isinstance(field, models.ManyToManyField):
                    self.handle_many_to_many(field_name, field)

                elif isinstance(field, (models.DateField, models.DateTimeField)):
                    self.fields[field_name].widget = forms.DateInput(attrs={'type': 'date'})

        def handle_foreign_key(self, field_name, field):
            is_required = self.set_required(field_name)
            related_model = field.related_model
            related_name = related_names.get(field_name, field.remote_field.field_name)
            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

            field = forms.ModelChoiceField(
                queryset=RelatedModel.objects.all(),
                to_field_name=related_name,
                required=is_required,
                widget=widgets.Select(attrs={'class': 'js-select2'})
            )

            
            field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj))
            print(field.label_from_instance,"77777777777777777")
            field.label = custom_labels.get(field_name, field_name) 
            self.fields[field_name] = field
          

        def handle_foreign_key2(self, field_name, field):
            is_required = self.set_required(field_name)
            related_model = field.related_model
            related_name = related_names.get(field_name, field.remote_field.field_name)
            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

            # الحصول على القيمة الحالية للحقل
            current_value = getattr(self.instance, field_name, None)
            current_value2 = getattr(current_value, related_name, None) 
            print(current_value2,"tttttttttttttttttttttttttt")
            # إعادة تعريف الحقل
            field = forms.ModelChoiceField(
                queryset=RelatedModel.objects.all(),
                to_field_name=related_name,
                required=is_required,
                widget=widgets.Select(attrs={'class': 'js-select2'})
            )

            field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj)) 
            
            # field.label_from_instance = current_value2
            # field.label_from_instance = getattr(current_value, related_name, None) 
            # field.initial = getattr(current_value, related_name, None) 
            # print(field.initial,"uuuuuuuuuuuuuuuuuuuuuu")
            # field.initial = getattr(current_value, related_name, None)  # استخدام getattr

            field.label = custom_labels.get(field_name, field_name) 
            self.fields[field_name] = field

            # تعيين القيمة الحالية للحقل الجديد
            # if current_value:
            #     field.initial = getattr(current_value, related_name, None)  # استخدام getattr

            # # طباعة القيم الفعلية
            # if current_value:
            #     print(f"Current value for {field_name}: {field.label_from_instance(current_value)}")
            # else:
            #     print(f"No current value for {field_name}")


        def handle_many_to_many(self, field_name, field):
            is_required = self.set_required(field_name)
            related_model = field.related_model
            related_name = related_names.get(field_name, field.related_model._meta.pk.name)

            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

            field = forms.ModelMultipleChoiceField(
                queryset=RelatedModel.objects.all(),
                to_field_name=related_name,
                required=is_required,
                widget=widgets.SelectMultiple(attrs={'class': 'js-select2'})
            )

            field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj))
            field.label = custom_labels.get(field_name, field_name) 
            print(field.label_from_instance,"888888888888888888888888888")
            self.fields[field_name] = field


        @staticmethod
        def set_required(field_name):
            required_fields = ['field_name_that_should_be_required']
            return field_name in required_fields

    return DynamicForm

def create_dynamic_form_for_seach(table_name):
    try:
        model_instance = ModelSchema.objects.get(name=table_name)
    except ObjectDoesNotExist:
        raise ValueError(f"Model {table_name} does not exist.")

    fields = CustomField.objects.filter(table=table_name)
    field_names = [field.field_name for field in fields]
    custom_labels = {field.field_name: field.verbose_name for field in fields}
    related_names = {field.field_name: field.related_name for field in fields}

    class DynamicForm(forms.ModelForm):
        class Meta:
            model = get_dynamic_model(table_name)
            fields = field_names

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for field_name in field_names:
                self.fields[field_name].label = custom_labels.get(field_name, field_name)
                self.fields[field_name].required = False
                field = self.Meta.model._meta.get_field(field_name)
                # field.required = False  # تعيين الحقل كغير مطلوب
                # print(field.required,"field.required")


                if isinstance(field, models.ForeignKey):
                    self.handle_foreign_key(field_name, field)

                elif isinstance(field, models.ManyToManyField):
                    self.handle_many_to_many(field_name, field)

                elif isinstance(field, (models.DateField, models.DateTimeField)):
                    self.fields[field_name].widget = forms.DateInput(attrs={'type': 'date'})

        def handle_foreign_key(self, field_name, field):
            # is_required = self.set_required(field_name)
            related_model = field.related_model
            related_name = related_names.get(field_name, field.remote_field.field_name)
            
            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

            field = forms.ModelChoiceField(
                queryset=RelatedModel.objects.all(),
                to_field_name=related_name,
                required=False,
                widget=widgets.Select(attrs={'class': 'js-select2'})
            )

            field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj)) 
            field.label = custom_labels.get(field_name, field_name) 
            self.fields[field_name] = field


        def handle_many_to_many(self, field_name, field):
            # is_required = self.set_required(field_name)
            related_model = field.related_model
            related_name = related_names.get(field_name, field.related_model._meta.pk.name)

            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

            field = forms.ModelMultipleChoiceField(
                queryset=RelatedModel.objects.all(),
                to_field_name=related_name,
                required=False,
                widget=widgets.SelectMultiple(attrs={'class': 'js-select2'})
            )

            field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj))
            field.label = custom_labels.get(field_name, field_name) 
            self.fields[field_name] = field

        # @staticmethod
        # def set_required(field_name):
        #     required_fields = ['field_name_that_should_be_required']
        #     return field_name in required_fields

    return DynamicForm


from django import forms
from django.db import models
from django.apps import apps

def create_dynamic_form2(table_name):
    model_name = ModelSchema.objects.get(name=table_name)
    fields = CustomField.objects.filter(table=table_name)
    field_names = [field.field_name for field in fields]
    custom_labels = [field.verbose_name for field in fields]
    related_names = [field.related_name for field in fields]

    class DynamicForm(forms.ModelForm):
        class Meta:
            model = get_dynamic_model(table_name)
            fields = field_names

        def __init__(self, *args, **kwargs):
            super(DynamicForm, self).__init__(*args, **kwargs)
            for i, field_name in enumerate(field_names):
                self.fields[field_name].label = custom_labels[i]

                field = self.Meta.model._meta.get_field(field_name)

                # إذا كان الحقل من نوع ForeignKey
                if isinstance(field, models.ForeignKey):
                    is_required = self.set_required(field_name)
                    related_model = field.related_model
                    related_name = field.remote_field.field_name
                    related_name2 = related_names[i]

                    RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

                    def custom_label_from_instance(obj):
                        return getattr(obj, related_name2)

                    form_field = forms.ModelChoiceField(
                        queryset=RelatedModel.objects.all(),
                        to_field_name=related_name,
                        required=is_required,
                        widget=widgets.Select(attrs={'class': 'js-select2'}),
                    )
                    form_field.label_from_instance = custom_label_from_instance
                    self.fields[field_name] = form_field

                # إذا كان الحقل من نوع ManyToManyField
                elif isinstance(field, models.ManyToManyField):
                    is_required = self.set_required(field_name)
                    related_model = field.related_model
                    related_name2 = related_names[i]

                    RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

                    def custom_label_from_instance(RelatedModel, field_name):
                        def label_from_instance(obj):
                            return getattr(obj, related_name2)
                            # return getattr(obj, field_name)
                            form_field = forms.ModelChoiceField(
                            queryset=RelatedModel.objects.all(), 
                            # to_field_name=related_name2,
                            to_field_name=related_name,
                            required=is_required, 
                            widget=widgets.Select(attrs={'class': 'js-select2'}),
                        )
                        form_field.label_from_instance = label_from_instance
                        form_field.initial = field_name
                        return form_field

                    form_field = custom_label_from_instance(RelatedModel, field_name)
                    self.fields[field_name] = form_field

                # إذا كان الحقل من نوع DateField أو DateTimeField
                elif isinstance(field, models.DateField) or isinstance(field, models.DateTimeField):
                    self.fields[field_name].widget = forms.DateInput(attrs={'type': 'date'})

                self.fields[field_name].label = custom_labels[i]

        def set_required(self, field_name):
            if field_name == 'field_name_that_should_be_required':
                return True
            else:
                return False

    return DynamicForm

# دالة سليمة 100% و المستخدمة
def create_dynamic_form1(table_name):
    model_name = ModelSchema.objects.get(name=table_name)
    # model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
    fields = CustomField.objects.filter(table=table_name)
    # field_names = [field.field_name.replace("_", "") for field in fields]
    field_names = [field.field_name for field in fields]
    custom_labels = [field.verbose_name for field in fields]
    related_names = [field.related_name for field in fields]

    class DynamicForm(forms.ModelForm):
        class Meta:
            model = get_dynamic_model(table_name)
            # model = apps.get_model(app_label='test2', model_name=model_name)
            # fields = '__all__'
            fields = field_names

        def __init__(self, *args, **kwargs):
                super(DynamicForm, self).__init__(*args, **kwargs)
                for i, field_name in enumerate(field_names):
                    self.fields[field_name].label = custom_labels[i]

                    field = self.Meta.model._meta.get_field(field_name)
                    if isinstance(field, models.ForeignKey):
                        is_required = self.set_required(field_name)
                        related_model = field.related_model
                        related_name = field.remote_field.field_name
                        # print(related_name,"333333333333333333333333333333333333")
                        related_name2 = related_names[i]
                        # print(related_name2,"444444444444444444444444444444")
                        
                        # RelatedModel = get_dynamic_model(related_model)
                        RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)
                        
                        def custom_label_from_instance(RelatedModel, field_name):
                            def label_from_instance(obj):
                                return getattr(obj, related_name2)
                                # return getattr(obj, field_name)
                            form_field = forms.ModelChoiceField(
                                queryset=RelatedModel.objects.all(), 
                                # to_field_name=related_name2,
                                to_field_name=related_name,
                                required=is_required, 
                                widget=widgets.Select(attrs={'class': 'js-select2'}),
                            )
                            form_field.label_from_instance = label_from_instance
                            form_field.initial = field_name
                            return form_field

                        form_field = custom_label_from_instance(RelatedModel, field_name)
                        self.fields[field_name] = form_field
                    elif isinstance(field, models.DateField) or isinstance(field, models.DateTimeField):
                        # تخصيص الـ widget للحقول من نوع تاريخ
                        self.fields[field_name].widget = forms.DateInput(attrs={'type': 'date'})
                    
                    self.fields[field_name].label = custom_labels[i]

        def set_required(self, field_name):
            if field_name == 'field_name_that_should_be_required':
                # self.fields[field_name].required = True
                return True
            else:
                # self.fields[field_name].required = False
                return False

    return DynamicForm


# السليمة و المستخدمة
def create_dynamic_form_for_formset1(table_name):
    model_name = ModelSchema.objects.get(name=table_name)
    # model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
    fields = CustomField.objects.filter(table=table_name)
    # field_names = [field.field_name.replace("_", "") for field in fields]
    field_names = [field.field_name for field in fields]
    custom_labels = [field.verbose_name for field in fields]
    related_names = [field.related_name for field in fields]

    class DynamicForm(forms.ModelForm):
        class Meta:
            model = get_dynamic_model(table_name)
            # model = apps.get_model(app_label='test2', model_name=model_name)
            # fields = '__all__'
            fields = field_names

        def __init__(self, *args, **kwargs):
                super(DynamicForm, self).__init__(*args, **kwargs)
                for i, field_name in enumerate(field_names):
                    self.fields[field_name].label = custom_labels[i]

                    field = self.Meta.model._meta.get_field(field_name)
                    if isinstance(field, models.ForeignKey):
                        is_required = self.set_required(field_name)
                        related_model = field.related_model
                        related_name = field.remote_field.field_name
                        # print(related_name,"333333333333333333333333333333333333")
                        related_name2 = related_names[i]
                        # print(related_name2,"444444444444444444444444444444")
                        
                        # RelatedModel = get_dynamic_model(related_model)
                        RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)
                        
                        def custom_label_from_instance(RelatedModel, field_name):
                            def label_from_instance(obj):
                                return getattr(obj, related_name2)
                                # return getattr(obj, field_name)
                            form_field = forms.ModelChoiceField(
                                queryset=RelatedModel.objects.all(), 
                                # to_field_name=related_name2,
                                to_field_name=related_name,
                                required=is_required, 
                                widget=widgets.Select(attrs={'class': 'js-select2'}),
                            )
                            form_field.label_from_instance = label_from_instance
                            form_field.initial = field_name
                            return form_field

                        form_field = custom_label_from_instance(RelatedModel, field_name)
                        self.fields[field_name] = form_field
                    elif isinstance(field, models.DateField) or isinstance(field, models.DateTimeField):
                        # تخصيص الـ widget للحقول من نوع تاريخ
                        self.fields[field_name].widget = forms.DateInput(attrs={'type': 'date'})
                    
                    self.fields[field_name].label = custom_labels[i]

        def set_required(self, field_name):
            if field_name == 'field_name_that_should_be_required':
                # self.fields[field_name].required = True
                return True
            else:
                # self.fields[field_name].required = False
                return False

       
    class CustomDynamicForm(DynamicForm):

        DELETE = BooleanField(required=False, label="حذف الصف", initial=False)
    # form = 
                    
    return CustomDynamicForm
    # return DynamicForm


def create_dynamic_form_for_formset(table_name):
    try:
        model_instance = ModelSchema.objects.get(name=table_name)
    except ObjectDoesNotExist:
        raise ValueError(f"Model {table_name} does not exist.")

    fields = CustomField.objects.filter(table=table_name)
    field_names = [field.field_name for field in fields]
    custom_labels = {field.field_name: field.verbose_name for field in fields}
    related_names = {field.field_name: field.related_name for field in fields}

    class DynamicForm(forms.ModelForm):
        class Meta:
            model = get_dynamic_model(table_name)
            fields = field_names

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for field_name in field_names:
                self.fields[field_name].label = custom_labels.get(field_name, field_name)
                field = self.Meta.model._meta.get_field(field_name)

                if isinstance(field, models.ForeignKey):
                    self.handle_foreign_key(field_name, field)

                elif isinstance(field, models.ManyToManyField):
                    self.handle_many_to_many(field_name, field)

                elif isinstance(field, (models.DateField, models.DateTimeField)):
                    self.fields[field_name].widget = forms.DateInput(attrs={'type': 'date'})

        def handle_foreign_key(self, field_name, field):
            is_required = self.set_required(field_name)
            related_model = field.related_model
            related_name = related_names.get(field_name, field.remote_field.field_name)
            
            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

            field = forms.ModelChoiceField(
                queryset=RelatedModel.objects.all(),
                # to_field_name=related_name,
                required=is_required,
                widget=widgets.Select(attrs={'class': 'js-select2'})
            )

            field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj)) 
            field.label = custom_labels.get(field_name, field_name) 
            self.fields[field_name] = field


        def handle_many_to_many(self, field_name, field):
            is_required = self.set_required(field_name)
            related_model = field.related_model
            related_name = related_names.get(field_name, field.related_model._meta.pk.name)
            # print(related_name,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)

            field = forms.ModelMultipleChoiceField(
                queryset=RelatedModel.objects.all(),
                # to_field_name=related_name,
                required=is_required,
                widget=widgets.SelectMultiple(attrs={'class': 'js-select2'})
            )

            field.label_from_instance = lambda obj: getattr(obj, related_name, str(obj))
            field.label = custom_labels.get(field_name, field_name) 
            self.fields[field_name] = field

        @staticmethod
        def set_required(field_name):
            required_fields = ['field_name_that_should_be_required']
            return field_name in required_fields

    class CustomDynamicForm(DynamicForm):

        DELETE = BooleanField(required=False, label="حذف الصف", initial=False)
    
    return CustomDynamicForm
    # return DynamicForm




# السليمة و المستخدمة
def create_dynamic_formset1(table_name, excel_file, request):
    model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
    fields = CustomField.objects.filter(table=table_name)
    field_names = [field.field_name for field in fields]
    custom_labels = [field.verbose_name for field in fields]
    model = apps.get_model(app_label='test2', model_name=model_name)
    
    # قراءة بيانات الإكسل
    df = pd.read_excel(excel_file)
    model_columns = {field.verbose_name: field.field_name for field in fields}
    model_columns2 = {field.field_name for field in fields}
    excel_columns = df.columns.tolist()
    
    # تحويل أسماء الأعمدة لتتطابق مع الحقول في النموذج
    for col in excel_columns:
        if col in model_columns:
            df.rename(columns={col: model_columns[col]}, inplace=True)
    
    # معالجة القيم المرتبطة بـ ForeignKey
    for field in model._meta.get_fields():
        if isinstance(field, models.ForeignKey):
            related_model = field.related_model
            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)
            related_field_name = CustomField.objects.filter(table=table_name, field_name=field.name).first()
            related_name = related_field_name.related_name
            
            try:
                if field.name not in df.columns:
                    messages.error(request, f"العمود {field.name} غير موجود في ملف الإكسل.")
                    continue

                related_values = df[field.name].dropna()
                
                for idx, related_value in df[field.name].dropna().items():
                    if related_value:
                        related_objects = RelatedModel.objects.filter(**{related_name: related_value})
                        if related_objects.exists():
                            for obj in related_objects:
                                related_id = obj.id
                                df.loc[df[field.name] == related_value, field.name] = related_id
                        else:
                            messages.warning(request, f"لا توجد قيم مرتبطة للعمود {related_field_name} بقيمة {related_value} في الصف {idx + 1}.")
                    else:
                        messages.warning(request, f"لا توجد قيم في العمود المرتبط {related_field_name} في الصف {idx + 1}.")
            except Exception as e:
                messages.error(request, f"حدث خطأ غير متوقع في الصف {idx + 1}: {str(e)}")

    excel_data = df.to_dict(orient='records')
    names_match = all(column in model_columns2 for column in df.columns.tolist())
    if names_match:
        messages.info(request, "أسماء الأعمدة متطابقة بين النموذج وملف الإكسل.")
    else:
        messages.warning(request, "يوجد اختلاف في أسماء الأعمدة بين النموذج وملف الإكسل.")

    # تعديل النموذج الديناميكي لإضافة حقل DELETE
    dynamicform = create_dynamic_form_for_formset(table_name)
    DynamicFormSet = formset_factory(dynamicform, extra=0)
    formset = DynamicFormSet(initial=excel_data)
    
    return formset, names_match

def create_dynamic_formset(table_name, excel_file, request):
    model_name = 'DynamicModels' + table_name.replace("_", "").capitalize()
    fields = CustomField.objects.filter(table=table_name)
    field_names = [field.field_name for field in fields]
    custom_labels = [field.verbose_name for field in fields]
    model = apps.get_model(app_label='test2', model_name=model_name)
    
    # قراءة بيانات الإكسل
    df = pd.read_excel(excel_file)
    model_columns = {field.verbose_name: field.field_name for field in fields}
    model_columns2 = {field.field_name for field in fields}
    excel_columns = df.columns.tolist()
    
    # إزالة المسافات الزائدة من أسماء الأعمدة
    df.columns = df.columns.str.strip()

    # تحويل أسماء الأعمدة لتتطابق مع الحقول في النموذج
    for col in excel_columns:
        if col in model_columns:
            df.rename(columns={col: model_columns[col]}, inplace=True)
    
    # دالة لمعالجة الحقول المرتبطة (ForeignKey, ManyToMany)
    def handle_related_field(field, df, model_columns, table_name, request, is_many_to_many=False):
        try:
            if field.name not in df.columns:
                messages.error(request, f"العمود {field.name} غير موجود في ملف الإكسل.")
                return
            
            related_model = field.related_model
            RelatedModel = apps.get_model(app_label='test2', model_name=related_model._meta.model_name)
            related_field_name = CustomField.objects.filter(table=table_name, field_name=field.name).first()
            
            if related_field_name is None:
                messages.error(request, f"لم يتم العثور على حقل مرتبط مع {field.name}.")
                return
            
            related_name = related_field_name.related_name
            related_values = df[field.name].dropna()

            for idx, related_value in related_values.items():
                if related_value:
                    if is_many_to_many:
                        related_values_list = related_value.split(',')  # افتراض أن القيم مفصولة بفواصل
                        related_objects = RelatedModel.objects.filter(**{related_name + '__in': related_values_list})
                        
                        if related_objects.exists():
                            related_ids = [obj.id for obj in related_objects]
                            df.loc[df[field.name] == related_value, field.name] = ', '.join(map(str, related_ids))
                        else:
                            messages.warning(request, f"لا توجد قيم مرتبطة للعمود {related_field_name} بقيمة {related_value} في الصف {idx + 1}.")
                    else:
                        related_objects = RelatedModel.objects.filter(**{related_name: related_value})
                        if related_objects.exists():
                            for obj in related_objects:
                                related_id = obj.id
                                df.loc[df[field.name] == related_value, field.name] = related_id
                        else:
                            messages.warning(request, f"لا توجد قيم مرتبطة للعمود {related_field_name} بقيمة {related_value} في الصف {idx + 1}.")
                else:
                    messages.warning(request, f"لا توجد قيم في العمود المرتبط {related_field_name} في الصف {idx + 1}.")
        except Exception as e:
            messages.error(request, f"حدث خطأ غير متوقع في الصف {idx + 1}: {str(e)}")

    # معالجة القيم المرتبطة بـ ForeignKey و ManyToMany
    for field in model._meta.get_fields():
        if isinstance(field, models.ForeignKey):
            handle_related_field(field, df, model_columns, table_name, request, is_many_to_many=False)
        elif isinstance(field, models.ManyToManyField):
            handle_related_field(field, df, model_columns, table_name, request, is_many_to_many=True)

    excel_data = df.to_dict(orient='records')
    names_match = all(column in model_columns2 for column in df.columns.tolist())
    
    if names_match:
        messages.info(request, "أسماء الأعمدة متطابقة بين النموذج وملف الإكسل.")
    else:
        messages.warning(request, "يوجد اختلاف في أسماء الأعمدة بين النموذج وملف الإكسل.")
    
    # تعديل النموذج الديناميكي لإضافة حقل DELETE
    dynamicform = create_dynamic_form_for_formset(table_name)
    DynamicFormSet = formset_factory(dynamicform, extra=0)
    formset = DynamicFormSet(initial=excel_data)
    
    return formset, names_match


# class CustomTableForm(forms.ModelForm):
#     class Meta:
#         model = CustomTable
#         fields = ('name',)

# class CustomFieldForm(forms.ModelForm):
#     class Meta:
#         model = CustomField
#         fields = ('field_name', 'field_type', 'related_table')

# class FieldForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     field_type = forms.ChoiceField(choices=[('char', 'CharField'), ('int', 'IntegerField'), ('fk', 'ForeignKey')])
#     related_table = forms.ModelChoiceField(queryset=RelatedTable.objects.all(), required=False)



# class TableForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     fields = forms.ModelMultipleChoiceField(queryset=Field.objects.all())  # استخدم النموذج المناسب هنا

# FieldFormSet = formset_factory(FieldForm, extra=1)

# class TableForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     fields = FieldFormSet()
