from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.db import models
from django.db.utils import DEFAULT_DB_ALIAS
from django.utils.text import slugify

from dynamic_models import compat, config
from dynamic_models.exceptions import InvalidFieldNameError, NullFieldChangedError
from dynamic_models.factory import ModelFactory
from dynamic_models.schema import FieldSchemaEditor, ModelSchemaEditor
from dynamic_models.utils import ModelRegistry
from django.utils.text import slugify
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.apps import apps


from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import ContentType, Permission
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

class ModelBuilder:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_model(self):
        class Meta:
            db_table = self.table_name

        fields = self.get_fields()
        attributes = {
            '__module__': '__main__',
            'Meta': Meta,
            **fields,
        }
        model = type(f"{self.table_name}Model", (models.Model,), attributes)
        return model

    def get_fields(self):
        # قم بإعادة تنفيذ الاستعلام هنا لاسترداد حقول الجدول من قاعدة البيانات
        # وقم بإنشاء الحقول استنادًا إلى حقول الجدول

        fields = {}

        # مثال على إنشاء حقل CharField
        fields['field_name'] = models.CharField(max_length=100)

        # يمكنك إضافة المزيد من الحقول هنا

        return fields

# الاصلي
# class ModelSchema(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     db_name = models.CharField(max_length=32, default=DEFAULT_DB_ALIAS)
#     managed = models.BooleanField(default=True)
#     db_table_name = models.CharField(null=True, max_length=250)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # self._registry = ModelRegistry('test2')
#         self._registry = ModelRegistry(self.app_label)
#         self._initial_name = self.name
#         initial_model = self.get_registered_model()
#         print(initial_model,"initial_model")
#         self._schema_editor = (
#             ModelSchemaEditor(initial_model=initial_model, db_name=self.db_name)
#             if self.managed
#             else None
#         )

#     def save(self, **kwargs):
#         super().save(**kwargs)
#         if self._schema_editor:
#             self._schema_editor.update_table(self._factory.get_model())

#         self._initial_name = self.name

#     def delete(self, **kwargs):
#         if self._schema_editor:
#             self._schema_editor.drop_table(self.as_model())
#         self._factory.destroy_model()
#         super().delete(**kwargs)

#     def get_registered_model(self):
#         # print(self.model_name,"ppppppppppppppppppp")
#         # return self._registry.get_model(self.as_model())
#         return self._registry.get_model(self.model_name)

#     @property
#     def _factory(self):
#         return ModelFactory(self)

#     @property
#     def app_label(self):
#         return config.dynamic_models_app_label()

#     @property
#     def model_name(self):
#         return self.get_model_name(self.name)

#     @property
#     def initial_model_name(self):
#         return self.get_model_name(self._initial_name)

#     @classmethod
#     def get_model_name(cls, name):
#         return name.title().replace(" ", "")

#     @property
#     def db_table(self):
#         return self.db_table_name if self.db_table_name else self._default_db_table_name()

#     def _default_db_table_name(self):
#         safe_name = slugify(self.name).replace("-", "_")
#         return f"{self.app_label}_{safe_name}"

#     def as_model(self):
#         return self._factory.get_model()

#     def __str__(self):
#         return self.name       


from django.db import models



class ModelSchema(models.Model):
    name = models.CharField(max_length=250, unique=True)
    db_name = models.CharField(max_length=32, default=DEFAULT_DB_ALIAS)
    managed = models.BooleanField(default=True)
    db_table_name = models.CharField(null=True, max_length=250)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registry = ModelRegistry(self.app_label)
        self._initial_name = self.name
        initial_model = self.get_registered_model()
        self._schema_editor = (
            ModelSchemaEditor(initial_model=initial_model, db_name=self.db_name)
            if self.managed
            else None
        )

    def save(self, **kwargs):
        super().save(**kwargs)
        if self._schema_editor:
            self._schema_editor.update_table(self._factory.get_model())

        self._initial_name = self.name

    def delete(self, **kwargs):
        if self._schema_editor:
            self._schema_editor.drop_table(self.as_model())
        self._factory.destroy_model()
        super().delete(**kwargs)

    def get_registered_model(self):
        return self._registry.get_model(self.model_name)

    @property
    def _factory(self):
        return ModelFactory(self)

    @property
    def app_label(self):
        return config.dynamic_models_app_label()

    @property
    def model_name(self):
        return self.get_model_name(self.name)

    @property
    def initial_model_name(self):
        return self.get_model_name(self._initial_name)

    @classmethod
    def get_model_name(cls, name):
        return name.title().replace(" ", "")

    @property
    def db_table(self):
        return self.db_table_name if self.db_table_name else self._default_db_table_name()

    def _default_db_table_name(self):
        safe_name = slugify(self.name).replace("-", "_")
        return f"{self.app_label}_{safe_name}"

    def as_model(self):
        return self._factory.get_model()

    def __str__(self):
        return self.name


# إشارة لإنشاء الصلاحيات عند إنشاء النموذج
# @receiver(post_save, sender=ModelSchema)
# def create_permissions_for_model(sender, instance, created, **kwargs):
#     if created:
#         try:
#             model = instance.as_model()  # الحصول على النموذج المرتبط
#             model_content_type = ContentType.objects.get_for_model(model)

#             custom_permissions = [
#                 {'codename': 'import_data', 'name': 'Can Import Data'},
#                 {'codename': 'export_data', 'name': 'Can Export Data'},
#                 {'codename': 'print_data', 'name': 'Can Print Data'},
#                 {'codename': 'add_field', 'name': 'Can Add Field'},
#                 {'codename': 'delete_field', 'name': 'Can Delete Field'},
#                 {'codename': 'edit_field', 'name': 'Can Edit Field'},
#                 {'codename': 'delete_model', 'name': 'Can Delete Model'},
#                 {'codename': 'edit_model', 'name': 'Can Edit Model'},
#                 {'codename': 'view_model', 'name': 'Can View Model'},
#             ]

#             for permission_data in custom_permissions:
#                 codename = f"{permission_data['codename']}_{model._meta.model_name}"
#                 name = f"{permission_data['name']} ({model._meta.model_name})"
                
#                 # تحقق إذا كانت الصلاحية موجودة مسبقًا
#                 if not Permission.objects.filter(codename=codename, content_type=model_content_type).exists():
#                     Permission.objects.create(
#                         codename=codename,
#                         name=name,
#                         content_type=model_content_type
#                     )

#         except ObjectDoesNotExist:
#             print(f"لم يتمكن من العثور على ContentType للنموذج {instance.name}.")


# # إشارة لحذف الصلاحيات عند حذف النموذج
# @receiver(post_delete, sender=ModelSchema)
# def delete_permissions_for_model(sender, instance, **kwargs):
#     try:
#         model = instance.as_model()  # الحصول على النموذج المرتبط
#         model_content_type = ContentType.objects.get_for_model(model)

#         # حذف جميع الصلاحيات المرتبطة بهذا النوع من المحتوى
#         Permission.objects.filter(content_type=model_content_type).delete()
#         print(f"تم حذف جميع الصلاحيات المرتبطة بالنموذج {instance.name}.")

#     except ObjectDoesNotExist:
#         print(f"لم يتمكن من العثور على ContentType للنموذج {instance.name}.")


# from django.db import models
# from django.core.exceptions import ValidationError
# from django.db import models

# class FieldKwargsJSON(compat.JSONField):
#     description = "A field that handles storing models.Field kwargs as JSON"

#     def to_python(self, value):
#         raw_value = super().to_python(value)
#         try:
#             return self._convert_on_delete_to_function(raw_value)
#         except AttributeError as err:
#             raise ValidationError("Invalid value for 'on_delete'") from err

#     def get_prep_value(self, value):
#         prep_value = self._convert_on_delete_to_string(value)
#         return super().get_prep_value(prep_value)

#     def _convert_on_delete_to_function(self, raw_value):
#         if raw_value is None or "on_delete" not in raw_value:
#             return raw_value

#         raw_on_delete = raw_value["on_delete"]
#         if isinstance(raw_on_delete, str):
#             if hasattr(models, raw_on_delete):
#                 raw_value["on_delete"] = getattr(models, raw_on_delete)
#             else:
#                 raise AttributeError(f"Invalid value '{raw_on_delete}' for 'on_delete'")

#         return raw_value

#     # def _convert_on_delete_to_function(self, raw_value):
#     #     if raw_value is None or "on_delete" not in raw_value:
#     #         return raw_value

#     #     raw_on_delete = raw_value["on_delete"]
#     #     if isinstance(raw_on_delete, str):
#     #         if hasattr(models, raw_on_delete):
#     #             raw_value["on_delete"] = getattr(models, raw_on_delete)
#     #         else:
#     #             raise AttributeError(f"Invalid value '{raw_on_delete}' for 'on_delete'")
#     #     elif not callable(raw_on_delete):
#     #         raise AttributeError(f"'on_delete' must be callable")

#     #     return raw_value

#     def _convert_on_delete_to_string(self, raw_value):
#         if raw_value is None or "on_delete" not in raw_value:
#             return raw_value

#         raw_on_delete = raw_value["on_delete"]
#         if callable(raw_on_delete):
#             raw_value["on_delete"] = raw_on_delete.__name__

#         return raw_value
#   الكود  الاصل   
class FieldKwargsJSON(compat.JSONField):
    description = "A field that handles storing models.Field kwargs as JSON"

    def to_python(self, value):
        raw_value = super().to_python(value)
        print(f"to_python received value: {value}")
        try:
            return self._convert_on_delete_to_function(raw_value)
        except AttributeError as err:
            raise ValidationError("Invalid value for 'on_delete'") from err

    def from_db_value(self, value, expression, connection):
        # django.contrib.postgres.fields.JSONField does not implement from_db_value
        # for some reason. In that version, value is already a dict
        try:
            db_value = super().from_db_value(value, expression, connection)
        except AttributeError:
            db_value = value
        return self._convert_on_delete_to_function(db_value)

    def get_prep_value(self, value):
        prep_value = self._convert_on_delete_to_string(value)
        return super().get_prep_value(prep_value)

    def _convert_on_delete_to_function(self, raw_value):
        if raw_value is None or "on_delete" not in raw_value:
            return raw_value

        raw_on_delete = raw_value["on_delete"]
        if isinstance(raw_on_delete, str):
            raw_value["on_delete"] = getattr(models, raw_on_delete)

        return raw_value

    def _convert_on_delete_to_string(self, raw_value):
        if raw_value is None or "on_delete" not in raw_value:
            return raw_value

        raw_on_delete = raw_value["on_delete"]
        if callable(raw_on_delete):
            raw_value["on_delete"] = raw_on_delete.__name__

        return raw_value



# class FieldKwargsJSON(compat.JSONField):
#     description = "A field that handles storing models.Field kwargs as JSON"

#     def to_python(self, value):
#         raw_value = super().to_python(value)
#         try:
#             return self._convert_on_delete_to_function(raw_value)
#         except AttributeError as err:
#             raise ValidationError("Invalid value for 'on_delete'") from err

#     def from_db_value(self, value, expression, connection):
#         try:
#             db_value = super().from_db_value(value, expression, connection)
#         except AttributeError:
#             db_value = value
#         return self._convert_on_delete_to_function(db_value)

#     def get_prep_value(self, value):
#         prep_value = self._convert_on_delete_to_string(value)
#         return super().get_prep_value(prep_value)

#     def _convert_on_delete_to_function(self, raw_value):
#         # إذا كان الحقل `on_delete` غير موجود أو ليس دالة، نعيد القيمة كما هي
#         if raw_value is None or "on_delete" not in raw_value:
#             return raw_value

#         raw_on_delete = raw_value["on_delete"]
        
#         # إذا كانت القيمة هي اسم دالة (string)، نحولها إلى الكائن المناسب
#         if isinstance(raw_on_delete, str):
#             raw_value["on_delete"] = getattr(models, raw_on_delete)

#         return raw_value

#     def _convert_on_delete_to_string(self, raw_value):
#         if raw_value is None or "on_delete" not in raw_value:
#             return raw_value

#         raw_on_delete = raw_value["on_delete"]

#         # إذا كان `raw_on_delete` دالة، نحولها إلى اسمها بدلاً من الدالة نفسها
#         if callable(raw_on_delete):
#             raw_value["on_delete"] = raw_on_delete.__name__

#         return raw_value


# تحت التجربة لحل مشكلة اذا كان فورين كي
from django.db import models
from django.core.exceptions import ValidationError





# class FieldSchema(models.Model):
#     _PROHIBITED_NAMES = ("__module__", "_declared")

#     name = models.CharField(max_length=63)
#     model_schema = models.ForeignKey(ModelSchema, on_delete=models.CASCADE, related_name="fields")
#     class_name = models.TextField()
#     kwargs = FieldKwargsJSON(default=dict)

#     class Meta:
#         unique_together = (("name", "model_schema"),)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._initial_name = self.name
#         self._initial_null = self.null
#         self._initial_field = self.get_registered_model_field()
#         print(self._initial_field,"_initial_field")
#         # print("fffffffffffffffffffffffffff")
#         self._schema_editor = (
#             FieldSchemaEditor(initial_field=self._initial_field, db_name=self.model_schema.db_name)
#             if self.model_schema.managed
#             else None
#         )
    
#     def save(self, **kwargs):
#         self.validate()
#         super().save(**kwargs)
#         model, field = self._get_model_with_field()
#         # print(field,"fieldsssssssssssssssssssssssssssssssssssssssssssssssssss")
#         if self._schema_editor:
#             self._schema_editor.update_column(model, field)


#     def delete(self, **kwargs):
#         model, field = self._get_model_with_field()
#         if self._schema_editor:
#             self._schema_editor.drop_column(model, field)
#         super().delete(**kwargs)

#     def validate(self):
#         if self._initial_null and not self.null:
#             raise NullFieldChangedError(f"Cannot change NULL field '{self.name}' to NOT NULL")

#         if self.name in self.get_prohibited_names():
#             raise InvalidFieldNameError(f"{self.name} is not a valid field name")

#     def get_registered_model_field(self):
#         latest_model = self.model_schema.get_registered_model()
#         if latest_model and self.name:
#             try:
#                 field = latest_model._meta.get_field(self.name)
#                 print(f"Found field: {field}")
#                 return field
#             except FieldDoesNotExist:
#                 pass

#     @classmethod
#     def get_prohibited_names(cls):
#         return cls._PROHIBITED_NAMES

#     @property
#     def db_column(self):
#         return slugify(self.name).replace("-", "_")

#     @property
#     def verbose_name(self):
#         return self.kwargs.get('verbose_name', self.name)

#     @property
#     def unique(self):
#         return self.kwargs.get('unique', False)

#     @property
#     def max_length(self):
#         return self.kwargs.get('max_length', 255)

#     @property
#     def null(self):
#         return self.kwargs.get("null", False)

#     @null.setter
#     def null(self, value):
#         self.kwargs["null"] = value

#     def get_options(self):
#         return self.kwargs.copy()

#     def _get_model_with_field(self):
#         model = self.model_schema.as_model()
#         try:
#             field = model._meta.get_field(self.db_column)
#         except FieldDoesNotExist:
#             field = None
#         return model, field

#     def __str__(self):
#         return self.name

#     def _is_image_or_file_field(self, field):
#         return isinstance(field, (models.ImageField, models.FileField))

#     @property
#     def is_file_field(self):
#         return isinstance(self.get_registered_model_field(), (models.ImageField, models.FileField))

#     @is_file_field.setter
#     def is_file_field(self, value):
#         self.kwargs["upload_to"] = value



from django.db import models
from django.utils.text import slugify
from django.db import models

# class FieldSchema(models.Model):
#     # print("ggggggggggggggggggggggggggg")
#     _PROHIBITED_NAMES = ("__module__", "_declared")

#     name = models.CharField(max_length=63)
#     model_schema = models.ForeignKey(ModelSchema, on_delete=models.CASCADE, related_name="fields")
#     class_name = models.TextField()
#     kwargs = FieldKwargsJSON(default=dict)

#     class Meta:
#         unique_together = (("name", "model_schema"),)

#     def __init__(self, *args, **kwargs):
#         # print("wwwwwwwwwwwwwwwwwwwwwwwwwwwww")
#         super().__init__(*args, **kwargs)
#         self._initial_name = self.name
#         self._initial_null = self.null
#         self._initial_field = self.get_registered_model_field()
#         print(self._initial_field)
#         self._schema_editor = (
#             FieldSchemaEditor(initial_field=self._initial_field, db_name=self.model_schema.db_name)
#             if self.model_schema.managed
#             else None
#         )
       
#     def save(self, **kwargs):
#         self.validate()
#         super().save(**kwargs)
#         model, field = self._get_model_with_field()
#         if self._schema_editor:
#             self._schema_editor.update_column(model, field)

#     def delete(self, **kwargs):
#         model, field = self._get_model_with_field()
#         if self._schema_editor:
#             self._schema_editor.drop_column(model, field)
#         super().delete(**kwargs)

#     def validate(self):
#         if self._initial_null and not self.null:
#             raise NullFieldChangedError(f"Cannot change NULL field '{self.name}' to NOT NULL")

#         if self.name in self.get_prohibited_names():
#             raise InvalidFieldNameError(f"{self.name} is not a valid field name")

#     def get_registered_model_field(self):
#         latest_model = self.model_schema.get_registered_model()
#         if latest_model and self.name:
#             try:
#                 field = latest_model._meta.get_field(self.name)
#                 if isinstance(field, (models.ImageField, models.FileField)):
#                     # print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
#                     # إذا كان الحقل من نوع FileField أو ImageField
#                     if "upload_to" in self.kwargs:
#                         field.upload_to = self.kwargs["upload_to"]
#                         # print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
#                 return field
#             except FieldDoesNotExist:
#                 pass

#     @classmethod
#     def get_prohibited_names(cls):
#         return cls._PROHIBITED_NAMES

#     @property
#     def db_column(self):
#         return slugify(self.name).replace("-", "_")

#     @property
#     def verbose_name(self):
#         # الحصول على الـ verbose_name من kwargs
#         return self.kwargs.get('verbose_name', self.name)

#     @property
#     def unique(self):
#         # استرجاع قيمة unique من kwargs
#         return self.kwargs.get('unique', False)

#     @property
#     def max_length(self):
#         # استرجاع قيمة max_length من kwargs
#         return self.kwargs.get('max_length', 255)

#     @property
#     def null(self):
#         return self.kwargs.get("null", False)

#     @null.setter
#     def null(self, value):
#         self.kwargs["null"] = value

#     def get_options(self):
#         return self.kwargs.copy()

#     def _get_model_with_field(self):
#         model = self.model_schema.as_model()
#         try:
#             field = model._meta.get_field(self.db_column)
#         except FieldDoesNotExist:
#             field = None
#         return model, field

#     def __str__(self):
#         return self.name

#     def _is_image_or_file_field(self, field):
#         return isinstance(field, (models.ImageField, models.FileField))

#     @property
#     def is_file_field(self):
#         """تحقق مما إذا كان الحقل هو FileField أو ImageField."""
#         # print("ddddddddddddddddddddddddddddddddddd")
#         return isinstance(self.get_registered_model_field(), (models.ImageField, models.FileField))

#     @is_file_field.setter
#     def is_file_field(self, value):
#         """إعداد الحقل كحقل ملف."""
#         # print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
#         self.kwargs["upload_to"] = value
        
# {"null": true, "blank": true, "upload_to": "media/images/", "verbose_name": "صورة 14"}
# {"null": true, "verbose_name": "صورة 10"}


from django.db import models, connection
# # # سليم خالي من اي مشاكل
class FieldSchema(models.Model):
    _PROHIBITED_NAMES = ("__module__", "_declared")

    name = models.CharField(max_length=63)
    model_schema = models.ForeignKey(ModelSchema, on_delete=models.CASCADE, related_name="fields")
    class_name = models.TextField()
    kwargs = FieldKwargsJSON(default=dict)

    class Meta:
        unique_together = (("name", "model_schema"),)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initial_name = self.name
        self._initial_null = self.null
        self._initial_field = self.get_registered_model_field()
        self._schema_editor = (
            FieldSchemaEditor(initial_field=self._initial_field, db_name=self.model_schema.db_name)
            if self.model_schema.managed
            else None
        )

    # def save(self, **kwargs):
    #     self.validate()
    #     print(f"Saving field: {self.name}, with kwargs: {self.kwargs}")

    #     # إذا كان الحقل ManyToManyField، يجب معالجة العلاقة وإضافة الجدول الوسيط
    #     if self.class_name == "django.db.models.ManyToManyField":
    #         to_model_name = self.kwargs.get("to")
    #         through_table = self.kwargs.get("through")

    #         if not to_model_name or not through_table:
    #             raise ValueError("❌ يجب تحديد `to` و `through` لحقل ManyToManyField")

    #         print(f"🔄 إنشاء علاقة ManyToMany بين {self.model_schema.name} و {to_model_name} عبر {through_table}")

    #         # تحديث العلاقة في `model_schema`
    #         model_class = self.model_schema.as_model()
    #         to_model_class = apps.get_model('test2', to_model_name)

    #         many_to_many_field = models.ManyToManyField(
    #             to_model_class,
    #             through=through_table,
    #             related_name=self.kwargs.get("related_name", None),
    #             verbose_name=self.kwargs.get("verbose_name", None),
    #         )

    #         # إضافة الحقل إلى النموذج الأساسي
    #         model_class.add_to_class(self.name, many_to_many_field)

    #         print(f"✅ تم إنشاء العلاقة ManyToManyField بنجاح بين {self.model_schema.name} و {to_model_name}")

    #     super().save(**kwargs)

    #     # فرض إعادة تحميل النموذج بعد الإضافة
    #     # reload_dynamic_models()

    #     # تحديث المخطط في قاعدة البيانات
    #     # if self._schema_editor:
    #     #     with connection.schema_editor() as schema_editor:
    #     #         schema_editor.alter_db_table(
    #     #             self.model_schema.as_model(),
    #     #             self.model_schema.as_model()._meta.db_table,
    #     #             self.model_schema.as_model()._meta.db_table
    #     #         )


    def save(self, **kwargs):
        self.validate()
        print(f"Saving field: {self.name}, with kwargs: {self.kwargs}")
        super().save(**kwargs)
        model, field = self._get_model_with_field()
        if self._schema_editor:
            self._schema_editor.update_column(model, field)

    def delete(self, **kwargs):
        model, field = self._get_model_with_field()
        if self._schema_editor:
            self._schema_editor.drop_column(model, field)
        super().delete(**kwargs)

    def validate(self):
        if self._initial_null and not self.null:
            raise NullFieldChangedError(f"Cannot change NULL field '{self.name}' to NOT NULL")

        if self.name in self.get_prohibited_names():
            raise InvalidFieldNameError(f"{self.name} is not a valid field name")

    def get_registered_model_field(self):
        latest_model = self.model_schema.get_registered_model()
        if latest_model and self.name:
            try:
                return latest_model._meta.get_field(self.name)
                # print(f"Found field: {latest_model}")
            except FieldDoesNotExist:
                pass

    @classmethod
    def get_prohibited_names(cls):
        # TODO: return prohbited names based on backend
        return cls._PROHIBITED_NAMES

    @property
    def db_column(self):
        return slugify(self.name).replace("-", "_")

    @property
    def null(self):
        return self.kwargs.get("null", False)

    @null.setter
    def null(self, value):
        # print(f"Setting null to {value} for field {self.name}")
        self.kwargs["null"] = value


    def get_options(self):
        return self.kwargs.copy()

    def _get_model_with_field(self):
        model = self.model_schema.as_model()
        try:
            field = model._meta.get_field(self.db_column)
            # print(field,"field")
        except FieldDoesNotExist:
            field = None
        return model, field

    def __str__(self):
        return self.name   
        
        # return self.name, self.model_schema   


