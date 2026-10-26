from django.db import models

# Create your models here.

from django.apps import apps
from django.db import models
from django.contrib.postgres.fields import JSONField
from dynamic_models.models import FieldSchema, ModelSchema


# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models


# from django.db import models
# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType
# from django.apps import apps
# from django.contrib.auth.models import Permission

# def create_custom_permissions():
#     custom_permissions = [
#         {
#             'codename': 'can_import_data',
#             'name': 'Can Import Data',
#         },
#         {
#             'codename': 'can_export_data',
#             'name': 'Can Export Data',
#         },
#         {
#             'codename': 'can_print_data',
#             'name': 'Can Print Data',
#         },
#     ]

#     for permission_data in custom_permissions:
#         permissions = Permission.objects.filter(codename=permission_data['codename'])
        
#         if permissions.exists():
#             for permission in permissions:
#                 # Perform actions with each permission, like updating or deleting
#                 print(f"Permission with codename '{permission.codename}' already exists.")
#         else:
#             # Create new permission if it doesn't exist
#             new_permission = Permission.objects.create(
#                 codename=permission_data['codename'],
#                 name=permission_data['name'],
#             )
#             print(f"Created permission with codename '{new_permission.codename}'.")

# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType
# from django.apps import apps
# from django.core.exceptions import AppRegistryNotReady

# def create_custom_permissions_for_all_models():
#     try:
#         apps.check_models_ready()
#     except AppRegistryNotReady:
#         print("Models aren't loaded yet. Please ensure models are ready before creating permissions.")
#         return

#     all_models = apps.get_models()

#     custom_permissions = [
#         {
#             'codename': 'can_import_data',
#             'name': 'Can Import Data',
#         },
#         {
#             'codename': 'can_export_data',
#             'name': 'Can Export Data',
#         },
#         {
#             'codename': 'can_print_data',
#             'name': 'Can Print Data',
#         },
#     ]

#     for model in all_models:
#         model_content_type = ContentType.objects.get_for_model(model)
        
#         for permission_data in custom_permissions:
#             codename = f"{permission_data['codename']}_{model.__name__.lower()}"
#             name = f"{permission_data['name']} ({model.__name__})"
            
#             # Check if permission already exists
#             permission, created = Permission.objects.get_or_create(
#                 codename=codename,
#                 name=name,
#                 content_type=model_content_type,
#             )
            
#             if created:
#                 print(f"Created permission with codename '{permission.codename}' for model '{model.__name__}'.")
#             else:
#                 print(f"Permission with codename '{codename}' for model '{model.__name__}' already exists.")

# تنفيذ الدالة لإنشاء الصلاحيات المخصصة
# create_custom_permissions_for_all_models()        
        # يمكنك إضافة المزيد من الصلاحيات لكل نموذج هنا

# استدعاء الدالة لإنشاء الصلاحيات
# create_custom_permissions_for_all_models()
# Call the function to create custom permissions
# create_custom_permissions()

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    phone_number = models.CharField(_('phone number'), max_length=15, blank=True, null=True)
    country = models.CharField(_('country'), max_length=100, blank=True)

    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username # يمكنك تغيير هذا حسب ما تريد عرضه


# class TblSystem(models.Model):
#     name = models.CharField(unique=True, max_length=100, verbose_name="إسم النظام")

#     def __str__(self):
#         return self.name   


from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# class TblSystem(models.Model):
#     name = models.CharField(unique=True, max_length=100, verbose_name="إسم النظام")

#     class Meta:
#         permissions = []  # لن نحدد الصلاحيات هنا، سنقوم بإضافتها ديناميكيًا

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         content_type = ContentType.objects.get_for_model(TblSystem)
        
#         # إضافة صلاحيات العرض، التعديل، والحذف
#         permission_names = [
#             ('view', f"Can view {self.name}"),
#             ('add', f"Can view {self.name}"),
#             ('change', f"Can change {self.name}"),
#             ('delete', f"Can delete {self.name}"),
#         ]
        
#         for codename, permission_name in permission_names:
#             Permission.objects.get_or_create(
#                 codename=f"{codename}_{self.name.replace(' ', '_').lower()}",
#                 name=permission_name,
#                 content_type=content_type,
#             )


#     def __str__(self):
#         return self.name

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType

class TblSystem(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name="إسم النظام")

    class Meta:
        permissions = []  # لن نحدد الصلاحيات هنا، سنقوم بإضافتها ديناميكيًا

    def save(self, *args, **kwargs):
        # تحقق مما إذا كان هناك كائن موجود بالفعل في قاعدة البيانات
        if self.pk:  # إذا كان الكائن موجودًا بالفعل
            # جلب الاسم القديم من قاعدة البيانات
            old_name = TblSystem.objects.get(pk=self.pk).name
            if old_name != self.name:  # تحقق إذا كان الاسم قد تغير
                content_type = ContentType.objects.get_for_model(TblSystem)

                # حذف جميع الصلاحيات التي تحمل الاسم القديم
                Permission.objects.filter(
                    codename__startswith=f"{old_name.replace(' ', '_').lower()}_"
                ).delete()

        # حفظ الكائن أولاً
        super().save(*args, **kwargs)

        # إضافة الصلاحيات الجديدة بناءً على الاسم المعدل
        content_type = ContentType.objects.get_for_model(TblSystem)

        permission_names = [
            ('view', f"Can view {self.name}"),
            ('add', f"Can add {self.name}"),
            ('change', f"Can change {self.name}"),
            ('delete', f"Can delete {self.name}"),
        ]

        for codename, permission_name in permission_names:
            Permission.objects.get_or_create(
                codename=f"{self.name.replace(' ', '_').lower()}_{codename}",
                name=permission_name,
                content_type=content_type,
            )

    def delete(self, *args, **kwargs):
        try:
            # جلب نوع المحتوى للنموذج
            content_type = ContentType.objects.get_for_model(TblSystem)
            # جلب جميع الصلاحيات المرتبطة بالكائن
            permissions = Permission.objects.filter(
                codename__startswith=f"{self.name.replace(' ', '_').lower()}_",
                content_type=content_type,
            )

            for permission in permissions:
                # إزالة الصلاحية من جميع المجموعات
                groups = Group.objects.filter(permissions=permission)
                for group in groups:
                    group.permissions.remove(permission)

                # إزالة الصلاحية من جميع المستخدمين
                users = User.objects.filter(user_permissions=permission)
                for user in users:
                    user.user_permissions.remove(permission)

                # حذف الصلاحية
                permission.delete()

        except Exception as e:
            print(f"Error deleting permissions for {self.name}: {e}")

        # حذف الكائن نفسه بعد معالجة الصلاحيات
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


# سليم
# class TblSystem(models.Model):
#     name = models.CharField(unique=True, max_length=100, verbose_name="إسم النظام")

#     class Meta:
#         permissions = []  # لن نحدد الصلاحيات هنا، سنقوم بإضافتها ديناميكيًا

#     def save(self, *args, **kwargs):
#         # تحقق مما إذا كان هناك كائن موجود بالفعل في قاعدة البيانات
#         if self.pk:  # إذا كان الكائن موجودًا بالفعل
#             # جلب الاسم القديم من قاعدة البيانات
#             old_name = TblSystem.objects.get(pk=self.pk).name
#             if old_name != self.name:  # تحقق إذا كان الاسم قد تغير
#                 content_type = ContentType.objects.get_for_model(TblSystem)
                
#                 # حذف جميع الصلاحيات التي تحمل الاسم القديم
#                 Permission.objects.filter(
#                     codename__startswith=f"{old_name.replace(' ', '_').lower()}"
#                 ).delete()

#         # حفظ الكائن أولاً
#         super().save(*args, **kwargs)

#         # إضافة الصلاحيات الجديدة بناءً على الاسم المعدل
#         content_type = ContentType.objects.get_for_model(TblSystem)
        
#         permission_names = [
#             ('view', f"Can view {self.name}"),
#             ('add', f"Can add {self.name}"),
#             ('change', f"Can change {self.name}"),
#             ('delete', f"Can delete {self.name}"),
#         ]
        
#         for codename, permission_name in permission_names:
#             Permission.objects.get_or_create(
#                 codename=f"{self.name.replace(' ', '_').lower()}_{codename}",
#                 # codename=f"{codename}_{self.name.replace(' ', '_').lower()}",
#                 name=permission_name,
#                 content_type=content_type,
#             )

#     def delete(self, *args, **kwargs):
#         try:
#             content_type = ContentType.objects.get_for_model(TblSystem)
#             Permission.objects.filter(
#                 codename__startswith=f"{self.name.replace(' ', '_').lower()}_"
#                 # codename__startswith=f"{self.name.replace(' ', '_').lower()}"
#             ).delete()
#         except Exception as e:
#             print(f"Error deleting permissions for {self.name}: {e}")
#         super().delete(*args, **kwargs)


#     # def delete(self, *args, **kwargs):
#     #     # حذف الصلاحيات المرتبطة بالكائن قبل حذفه
#     #     content_type = ContentType.objects.get_for_model(TblSystem)
        
#     #     # حذف جميع الصلاحيات المرتبطة بهذا الكائن بناءً على الاسم
#     #     Permission.objects.filter(
#     #         codename__startswith=f"{self.name.replace(' ', '_').lower()}"
#     #     ).delete()

#     #     # حذف الكائن نفسه بعد حذف الصلاحيات
#     #     super().delete(*args, **kwargs)

#     def __str__(self):
#         return self.name


class Modelnames(models.Model):
    modelname = models.CharField(unique=True, max_length=100)
    modelnameAr = models.CharField(unique=True, max_length=100)
    sys_name = models.ForeignKey(TblSystem, on_delete=models.CASCADE, blank=True, null=True)
    model_type = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = '  اسم النموذج الديناميكي'
        verbose_name_plural = 'أسماء النماذج الديناميكية'

    def __str__(self):
        return self.modelnameAr   


# class DynamicModel(models.Model):
#     dynamic_fields = models.JSONField(default=dict)
    
# class DynamicModel(models.Model):
#     name = models.CharField(max_length=32)
#     related_model = models.CharField(max_length=100)  # اسم النموذج الآخر
#     class Meta:
#         verbose_name = ' النموذج الديناميكي'
#         verbose_name_plural = ' النماذج الديناميكية'

#     def get_related_model(self):
#         return apps.get_model('myapp', self.related_model)


class CustomField(models.Model):
    table = models.CharField(max_length=100)
    field_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100, null=True, blank= True)
    verbose_name = models.CharField(max_length=100, null=True, blank= True)
    max_length = models.IntegerField(null=True, blank= True)
    null_or_not = models.BooleanField(null=True, blank= True)
    blank_or_not = models.BooleanField(null=True, blank= True)
    unique_or_not = models.BooleanField(null=True, blank= True)
    on_delete = models.CharField(max_length=100, null=True, blank= True)
    related_name = models.CharField(max_length=100, null=True, blank= True)
    related_table = models.CharField(max_length=100, null=True, blank= True)
    is_related = models.BooleanField(default=False)

    def __str__(self):
        return self.field_name


class CustmReportHeader(models.Model):
    imge = models.FileField(upload_to='store/', null=True, blank=True, verbose_name="صورة")
    # imge2 = models.ImageField(upload_to='store/', null=True, blank=True, verbose_name="2صورة")
    # imge3 = models.ImageField(null=True, blank=True,upload_to='store/', verbose_name="2صورة")
    field1_right = models.CharField(max_length=200,null=True,blank=True, verbose_name='السطر الاول يمين')
    field2_right = models.CharField(max_length=200,null=True,blank=True, verbose_name='السطر الثاني يمين')
    field3_right = models.CharField(max_length=200,null=True,blank=True, verbose_name='السطر الثالث يمين')
    field1_left = models.CharField(max_length=200,null=True,blank=True, verbose_name='السطر الاول يسار')
    field2_left = models.CharField(max_length=200,null=True,blank=True, verbose_name='السطر الثاني يسار')
    field3_left = models.CharField(max_length=200,null=True,blank=True, verbose_name='السطر الثالث يسار')
    current_user = models.ForeignKey(User,on_delete=models.PROTECT,null=True, blank=True,verbose_name="المستخدم الحالي")
    def __str__(self):
        return self.field1_right




from django.contrib.auth.models import User

class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name="المستخدم")
    action = models.CharField(max_length=255,null=True, blank=True,verbose_name="العملية")
    model_name = models.CharField(max_length=255,null=True, blank=True,verbose_name="الجدول")
    details = models.TextField(null=True, blank=True,verbose_name="البيانات")
    timestamp = models.DateTimeField(auto_now_add=True,null=True, blank=True,verbose_name="التاريخ")

    def __str__(self):
        return f"{self.user.username} performed {self.action} on {self.model_name}  at {self.timestamp}"



# class FieldCondition(models.Model):
#     model_name = models.CharField(max_length=100, null=True, blank= True)  # اسم النموذج
#     field_name = models.CharField(max_length=100, null=True, blank= True)  # اسم الحقل
#     condition = models.CharField(max_length=255, null=True, blank= True)   # الشرط (مثل "if field1 == 'value1'")
#     action = models.CharField(max_length=255, null=True, blank= True)      # الإجراء (مثل "show field2" أو "hide field3")



from django.db import models

class FieldCondition(models.Model):
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

    model_name = models.CharField(max_length=255, null=True, blank= True)  # اسم النموذج
    field_name = models.CharField(max_length=255, null=True, blank= True)  # الحقل الذي سيتم التأثير عليه
    dependent_field = models.CharField(max_length=255, null=True, blank= True)  # الحقل المعتمد عليه
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, null=True, blank= True)  # نوع الشرط
    condition_value = models.CharField(max_length=255, null=True, blank= True)  # القيمة المطلوبة لتنفيذ الشرط
    action = models.CharField(max_length=50, choices=ACTION_CHOICES, null=True, blank= True)  # نوع الإجراء عند تحقق الشرط
    restricted_values = models.JSONField(blank=True, null=True)  # القيم المحظورة (للتصفية)

    def __str__(self):
        return f"{self.model_name}.{self.field_name} يعتمد على {self.dependent_field} ({self.condition} {self.condition_value})"



# model_schema = ModelSchema.objects.all()
    
# for model_name in model_schema:
#     fields = FieldSchema.objects.filter(model_schema=model_name)
#         for field in fields:
#             fields1[field.name]
#         return fields1
#     model_class = type(model_name, (models.Model,), fields1)
#     return model_class


#     class model_name(models.Model):

#         fields = FieldSchema.objects.filter(model_schema=model_name)
#         for field in fields:
#             field.name = field.class_name(field.kwargs)


    

#  CHOICES = [
#     ('text', 'نص '),
#     ('textarea', 'نص طويل '),
#     ('number', 'رقم '),
#     ('email', 'ايميل '),
#     ('password', 'كلمة مرور '),
#     ('checkbox', 'صندوق اختيار '),
#     ('radio', 'راديو '),
#     ('file', 'ملف '),
#     ('search', 'بحث  '),
#     ('hidden', 'حقل مخفي '),
#     ('date', 'تاريخ '),
#     ('datetime', ' تاريخ مع وقت '),
#     ('time', 'وقت فقط '),
#     ('select', 'قائمة منسدلة '),
#     ('ImageField ', 'صورة  '),
    
# ]