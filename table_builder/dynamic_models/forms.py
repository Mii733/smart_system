from django import forms
from .models import FieldSchema


class FieldSchemaForm1(forms.ModelForm):
    null = forms.BooleanField(required=False, label="Allow Null", initial=False)
    unique = forms.BooleanField(required=False, label="Unique", initial=False)
    max_length = forms.IntegerField(required=False, label="Max Length", initial=255)

    class Meta:
        model = FieldSchema
        fields = ['name', 'model_schema', 'class_name', 'kwargs', 'null', 'unique', 'max_length']  # إضافة الحقول

    def save(self, commit=True):
        # نحدث الـ kwargs بناءً على المدخلات في الـ form
        instance = super().save(commit=False)
        instance.null = self.cleaned_data['null']
        instance.unique = self.cleaned_data['unique']
        instance.max_length = self.cleaned_data['max_length']
        if commit:
            instance.save()
        return instance

from django import forms
from .models import FieldSchema

class FieldSchemaForm(forms.ModelForm):
    null = forms.BooleanField(required=False, label="Allow Null", initial=False)
    unique = forms.BooleanField(required=False, label="Unique", initial=False)
    max_length = forms.IntegerField(required=False, label="Max Length", initial=255)

    # هنا نحدد قائمة من الخيارات لتمثل أنواع الحقول
    FIELD_CHOICES = [
        ('django.db.models.CharField', 'نص'),
        ('django.db.models.IntegerField', 'عدد حقيقي'),
        ('django.db.models.DateField', 'تاريخ'),
        ('django.db.models.BooleanField', 'منطقي'),
        ('django.db.models.FloatField', 'عدد عشري'),
        ('django.db.models.TextField', 'نص طويل'),
        ('django.db.models.DecimalField', 'DecimalField'),
        # أضف هنا المزيد من أنواع الحقول إذا لزم الأمر
    ]
    
    # حقل class_name سيكون عبارة عن قائمة منسدلة
    class_name = forms.ChoiceField(choices=FIELD_CHOICES, label="Field Type", required=True)

    class Meta:
        model = FieldSchema
        fields = ['name', 'model_schema', 'class_name', 'kwargs', 'null', 'unique', 'max_length']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # تخصيص حقل name ليعرض قيمة verbose_name من kwargs في البداية
        if self.instance and self.instance.verbose_name:
            self.fields['name'].initial = self.instance.verbose_name  # يتم تعيين initial بالـ verbose_name

    def save(self, commit=True):
        # نحدث الـ kwargs بناءً على المدخلات في الـ form
        instance = super().save(commit=False)
        instance.null = self.cleaned_data['null']
        instance.unique = self.cleaned_data['unique']
        instance.max_length = self.cleaned_data['max_length']
        
        # تحديث الـ kwargs بناءً على قيمة `class_name` التي تم اختيارها
        instance.kwargs['class_name'] = self.cleaned_data['class_name']
        
        if commit:
            instance.save()
        return instance



class FieldSchemaForm2(forms.ModelForm):
    null = forms.BooleanField(required=False, label="Allow Null", initial=False)
    unique = forms.BooleanField(required=False, label="Unique", initial=False)
    max_length = forms.IntegerField(required=False, label="Max Length", initial=255)

    # هنا نغير حقل name لعرض verbose_name في البداية
    name = forms.CharField(max_length=63, label="Field Name", initial=None)  # سيتم تعديله في `__init__`

    class Meta:
        model = FieldSchema
        fields = ['name', 'model_schema', 'class_name', 'kwargs', 'null', 'unique', 'max_length']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # تخصيص حقل name ليعرض قيمة verbose_name من kwargs في البداية
        if self.instance and self.instance.verbose_name:
            self.fields['name'].initial = self.instance.verbose_name  # يتم تعيين initial بالـ verbose_name
        
    def save(self, commit=True):
        # نحدث الـ kwargs بناءً على المدخلات في الـ form
        instance = super().save(commit=False)
        instance.null = self.cleaned_data['null']
        instance.unique = self.cleaned_data['unique']
        instance.max_length = self.cleaned_data['max_length']
        if commit:
            instance.save()
        return instance



# class FieldSchemaForm(forms.ModelForm):
#     null = forms.BooleanField(required=False, label="Allow Null", initial=False)
#     unique = forms.BooleanField(required=False, label="Unique", initial=False)
#     max_length = forms.IntegerField(required=False, label="Max Length", initial=255)

#     class Meta:
#         model = FieldSchema
#         fields = ['name', 'model_schema', 'class_name', 'kwargs', 'null', 'unique', 'max_length']  # إضافة الحقول

#     def save(self, commit=True):
#         # نحدث الـ kwargs بناءً على المدخلات في الـ form
#         instance = super().save(commit=False)
#         instance.null = self.cleaned_data['null']
#         instance.unique = self.cleaned_data['unique']
#         instance.max_length = self.cleaned_data['max_length']
#         if commit:
#             instance.save()
#         return instance
