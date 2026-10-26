from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from .models import Profile
from django.forms import widgets

from django.contrib.auth.models import Group, ContentType, User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'اسم المستخدم',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,label= 'كلمة المرور',
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'كلمة المرور',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    # remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password']
        # fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class PermissionForm(forms.Form):
    codename = forms.CharField(label='اسم الكود', max_length=100)
    name = forms.CharField(label='اسم الصلاحية', max_length=100)

# class UpdateProfileForm(forms.ModelForm):
#     avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
#     bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

#     class Meta:
#         model = Profile
#         fields = ['avatar', 'bio']


class MyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        for k, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = _('this field is requierd.')
                 
            if 'null' in field.error_messages:
                field.error_messages['null'] = _('this input can\'t be null .')
                 
            if 'blank' in field.error_messages:
                field.error_messages['blank'] = _(' this input can\'t be blank .')
                 
            if 'invalid' in field.error_messages:
                field.error_messages['invalid'] = _(' this value is invalid .')
                 
            if 'invalid_choice' in field.error_messages:
                field.error_messages['invalid_choice'] = _(' this invalid choice .')
                 
            if 'unique' in field.error_messages:
                field.error_messages['unique'] = _('this value must be unique.')
                 
            # if 'unique_for_date' in field.error_messages:
            #     field.error_messages['unique_for_date'] = _('You have to field this.')
                 

class GroupForm(MyForm,forms.ModelForm):
    # error_css_class = 'invalid-feedback'
    class Meta:
        model = Group
        fields = ["name"]
        labels={
            'name':_('اسم المجموعة')
        }
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),

            
        }

class usersForm(MyForm,forms.ModelForm):

    """
    Form for singing Users
    
    """

    password = forms.CharField(
      
        label=_("كلمة المرور"),
        max_length=200,
        widget=forms.PasswordInput(attrs={"placeholder": _("كلمة المرور")}),
    )

    confirm_password = forms.CharField(
        
        label=_("تأكيدكلمةالمرور"),
        max_length=200,
        widget=forms.PasswordInput(attrs={"placeholder": _("تأكيدكلمةالمرور")}),
    )
    username = forms.CharField(
        label=_("username"),
        max_length=200,
        # widget=forms.PasswordInput(attrs={"placeholder": _("Cinfirm Password")}),
    )



    class Meta:
        model = User
        labels = {
            "username":_("اسم المستخدم"),
            "email":_("Email"),
            "first_name":_("الاسم الاول"),
            "last_name":_("الاسم الاخير"),
            "is_superuser":_("مستخدم مدير"),
            "is_staff":_("موظف"),
            "is_active":_("مستخدم نشط"),
            "groups":_("مجموعات"),
        }
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "confirm_password",
            "is_superuser",
            "is_staff",
            "is_active",
            "groups",
        ]
   

            
      
       

    def clean_password(self):
        if len(self.cleaned_data["password"]) < 1:
            raise forms.ValidationError(_("password Must be more than  digit"))
        return self.cleaned_data["password"]

    def clean_confirm_password(self):
        if self.cleaned_data["confirm_password"] != self.cleaned_data.get("password"):
            raise forms.ValidationError(_("password NOT Match"))
        return self.cleaned_data["confirm_password"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(_('Username is already in use.')+' ('+ username+')' )
        elif len(username) < 1:
            raise forms.ValidationError(
                _(" Username is to Small . Must be more than 3 digit please ")
            )

        return username

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='تأكيد كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )
    password = forms.CharField(
        label=' كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password', 'is_superuser', 'is_staff', 'is_active', 'groups']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("كلمات المرور لا تتطابق.")




class usersFormPassword(usersForm):
    class Meta:
        model = User
        fields = ["username","password", "confirm_password"]


class usersFormEdit(usersForm):
    password = None
    confirm_password = None
    class Meta:
        model = User
        labels = {
            "username":_("اسم المستخدم"),
            "email":_("البريد الإلكتروني"),
            "first_name":_("الاسم الاول"),
            "last_name":_("الاسم الاخير"),
            "is_superuser":_("مستخدم مدير"),
            "is_staff":_("موظف"),
            "is_active":_("مستخدم نشط"),
           
        }
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "is_superuser",
            "is_staff",
            "is_active",
            "groups",
        ]

class usersFormGroupEdit(usersForm):
    password = None
    confirm_password = None
    Username = None

    class Meta:
        model = User
        fields = ["username","groups"]

class usersFormGroupEmployee(usersForm):

    username = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
    )

    password = forms.CharField(
        required=False,
        label="Password",
        max_length=200,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
    )
    confirm_password = forms.CharField(
        required=False,
        label="تأكيدكلمةالمرور",
        max_length=200,
        widget=forms.PasswordInput(
            attrs={"placeholder": "تأكيدكلمةالمرور", "class": "form-control"}
        ),
    )
    groups = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Group.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control",}),
    )

    class Meta:
        model = User
        fields = ["username", "password", "confirm_password", "groups"]

# class Meta:
#     permissions = [
#         ("can_restore_database", "يمكن استعادة قاعدة البيانات"),
#     ]


# class UserPasswordForm(forms.ModelForm):
#     confirm_password = forms.CharField(
#         label='تأكيد كلمة المرور',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         required=True
#     )
#     password = forms.CharField(
#         label=' كلمة المرور',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         required=True
#     )

#     class Meta:
#         model = User
#         fields = ['password', 'confirm_password']
#         widgets = {
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(UserPasswordForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs.update({'class': 'form-control'})

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("كلمات المرور لا تتطابق.")

class UserPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='تأكيد كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )
    password = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserPasswordForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # التأكد من تطابق كلمات المرور
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("كلمات المرور لا تتطابق.")
        return cleaned_data

    def save(self, commit=True):
        # التأكد من تشفير كلمة المرور قبل حفظها
        user = super(UserPasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])  # تشفير كلمة المرور
        if commit:
            user.save()
        return user


class UserEditeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'groups']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserEditeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


