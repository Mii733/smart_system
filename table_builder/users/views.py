from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
# from operations.models import Files,Tsk
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date
from .forms import RegisterForm, LoginForm, UpdateUserForm,UserForm, GroupForm, usersForm, usersFormEdit, usersFormPassword, usersFormGroupEdit,usersFormGroupEmployee,UserPasswordForm,UserEditeForm


from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, ContentType, Permission, User
from logs.log import loggingrecord
from django.conf import settings
from django.contrib.auth.hashers import make_password
# from taskapp.models import UserTaskPremission
# from operations.help import  fun_ask_premissio
from datetime import date
from dynmic_table.views import  confirm_perm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse


# @login_required
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        # fiel_count = Files.objects.count()
        
        return render(request, 'index.html', {'user':username})
    else:
        return redirect('login')

# def confirm_perm(request):
#     if messages.error:
#         return render(request, 'confirm_perm.html',{'': ''})
#     else:
#         messages.error(request, 'لايوجد لديك صلاحية')
#         return render(request, 'confirm_perm.html',{'': ''})


def home1(request):
    try:
        if not request.user.has_perm('operations.view_filemulti'):
            messages.error(request, 'لايوجد لديك صلاحية')
            return redirect('confirm_perm')
        else:
            fiel_count = Files.objects.count()
            return render(request, 's.html', {'fiel_count':fiel_count})
    except:
        pass


def home2(request):
    if not request.user.has_perm('taskapp.view_imagepath'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        fiel_count = Files.objects.count()
        dt = date.today()
        model_data = Tsk.objects.filter(task_status="تم انجازها",send_task_follow='ToManager')
        model_data1 = Tsk.objects.filter(~Q(task_status="تم انجازها") ,date_end__lte= dt)
        model_data_tody = Tsk.objects.filter(date_end = dt)
        count_task = model_data.count()
        count_task_overdue = model_data1.count()
        count_task_today = model_data_tody.count()
        task_premission = fun_ask_premissio(request)
        return render(request, 'index2.html', {'count_task':count_task,'count_task_overdue':count_task_overdue,'count_task_today':count_task_today, "conf_user":request.user.is_superuser,'task_premission':task_premission})

def home22(request):
    if request.user.is_authenticated:
        return render(request, 'index22.html', {'':''})
    else:
        return redirect('login')
def index_input(request):
    if not request.user.has_perm('taskapp.view_emp'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        return render(request, 'indexinput.html', {'':''})
def index_operation(request):
    if request.user.is_authenticated:
        return render(request, 'indexoperation.html', {'':''})
    else:
        return redirect('login')

def home3(request):
    if not request.user.has_perm('auth.view_group'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        return render(request, 'index3.html', {'':''})

def home4(request):
    if not request.user.has_perm('operations.view_task'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        return render(request, 'index4.html', {'':''})



class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'configrate/templates/configrate/users.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})
    

# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm
    # success_url = reverse_lazy('index') 
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


# from django.shortcuts import render
# from .forms import PermissionForm
# from django.http import HttpResponse
# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType
# from django.apps import apps

# def create_and_apply_permission(request):
#     if request.method == 'POST':
#         form = PermissionForm(request.POST)
#         if form.is_valid():
#             permission_content_type = ContentType.objects.get_for_model(Permission)
#             models = apps.get_models()

#             for model in models:
#                 Permission.objects.create(
#                     codename=form.cleaned_data['codename'],
#                     name=form.cleaned_data['name'],
#                     content_type=permission_content_type
#                 )

#             return HttpResponse("تم إنشاء الصلاحية الجديدة وتطبيقها على جميع النماذج بنجاح.")
#     else:
#         form = PermissionForm()

#     return render(request, 'create_and_apply_permission.html', {'form': form})




# fernet = Fernet(settings.SECRET_KEY.encode())

# def get_mac_address():
#     # الحصول على عنوان MAC
#     mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
#     return mac

# def generate_verification_key(device_info, secret_key):
#     # توليد مفتاح تحقق باستخدام HMAC مع SHA-256
#     return hmac.new(secret_key.encode(), device_info.encode(), hashlib.sha256).hexdigest()[:8]

# class CustomLoginView(LoginView):
#     form_class = LoginForm

#     def form_valid(self, form):
#         mac_id = get_mac_address()  # الحصول على عنوان MAC
#         device_id = str(uuid.getnode()) 
#         print("macccccccccccccccccccccccccccccccccc") 
#         print(mac_id)
#         print("iddddddddddddddddddddddddddddddddd") 
#         print(device_id)
#         secret_key = os.getenv('SECRET_KEY', 'default_key') 
#         device_info_str = f"{device_id}"
#         verification_key = generate_verification_key(device_info_str, secret_key)

#         # تحقق من حالة التحقق باستخدام mac_id أو device_id
#         verification_status = NVerificationStatus.objects.filter(
#             mac_id_encrypted=fernet.encrypt(mac_id.encode())
#         ).first() or NVerificationStatus.objects.filter(
#             device_id_encrypted=fernet.encrypt(device_id.encode())
#         ).first()

#         if verification_status is None:
#             # إذا لم تكن حالة التحقق موجودة، نقوم بإنشائها
#             verification_status = NVerificationStatus(mac_id=mac_id, device_id=device_id)
#             verification_status.save()

#         if not verification_status.is_verified:
#             # إذا لم يتم التحقق، إعادة التوجيه إلى شاشة التحقق
#             return redirect('verification_view')  # استبدل 'verification_view' باسم URL الخاص بشاشة التحقق

#         remember_me = form.cleaned_data.get('remember_me')

#         if not remember_me:
#             # تعيين انتهاء صلاحية الجلسة إلى 0 ثوان، بحيث يتم إغلاق الجلسة تلقائيًا بعد إغلاق المتصفح
#             self.request.session.set_expiry(0)
#             self.request.session.modified = True

#         return super(CustomLoginView, self).form_valid(form)



def get_mac_address():
    # الحصول على عنوان MAC
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
    return mac

# def generate_verification_key(device_info, secret_key):
#     # توليد مفتاح تحقق باستخدام HMAC مع SHA-256
#     return hmac.new(secret_key.encode(), device_info.encode(), hashlib.sha256).hexdigest()[:8]

# class CustomLoginView(LoginView):
#     form_class = LoginForm

#     def form_valid(self, form):
#         device_id = str(uuid.uuid4()).replace('-', '')[:8]
#         # device_id = get_mac_address()
#         # device_info_str = f"{device_id} {platform.system()} {platform.release()} {platform.processor()}"
#         device_info_str = f"{device_id}"
#         secret_key = os.getenv('SECRET_KEY', 'default_key') 
#         verification_key = generate_verification_key(device_info_str, secret_key)

#         # تحقق من حالة التحقق
#         verification_status, created = VerificationStatus.objects.get_or_create(device_id=device_id)

#         if not verification_status.is_verified:
#             # إذا لم يتم التحقق، إعادة التوجيه إلى شاشة التحقق
#             return redirect('verification_view')  # استبدل 'verification' باسم URL الخاص بشاشة التحقق

#         remember_me = form.cleaned_data.get('remember_me')

#         if not remember_me:
#             # تعيين انتهاء صلاحية الجلسة إلى 0 ثوان، بحيث يتم إغلاق الجلسة تلقائيًا بعد إغلاق المتصفح
#             self.request.session.set_expiry(0)
#             self.request.session.modified = True

#         return super(CustomLoginView, self).form_valid(form)


# import uuid
# import os
# import hmac
# import hashlib
# # import psutil
# from django.contrib.auth.views import LoginView
# from django.shortcuts import redirect
# # from taskapp.models import LastVerificationStatus




# def generate_verification_key(device_info, secret_key):
#     # توليد مفتاح تحقق باستخدام HMAC مع SHA-256
#     return hmac.new(secret_key.encode(), device_info.encode(), hashlib.sha256).hexdigest()[:8]




# def get_hardware_info():
#     # الحصول على معلومات الهارد
#     hard_disk_info = psutil.disk_usage('/').total / (1024 ** 3)  # إجمالي سعة الهارد بالجيجابايت
#     hard_disk_info = f"{hard_disk_info:.2f} GB"

#     # الحصول على معلومات المعالج
#     cpu_info = psutil.cpu_percent(interval=1)  # نسبة استخدام المعالج
#     cpu_info = f"{cpu_info}%"

#     # الحصول على معلومات الرام
#     ram_info = psutil.virtual_memory().total / (1024 ** 3)  # إجمالي سعة الرام بالجيجابايت
#     ram_info = f"{ram_info:.2f} GB"

#     return hard_disk_info, cpu_info, ram_info
# class CustomLoginView(LoginView):
#     form_class = LoginForm

#     def form_valid(self, form):
#         print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#         # device_id = str(uuid.uuid4()).replace('-', '')[:8]  # أو استخدام get_mac_address()
#         # device_info_str = f"{device_id}"
#         # secret_key = os.getenv('SECRET_KEY', 'default_key') 
#         # verification_key = generate_verification_key(device_info_str, secret_key)
#         device_ip = str(uuid.getnode())[:13]
#         # الحصول على معلومات الجهاز
#         hard_disk_info, cpu_info, ram_info = get_hardware_info()

#         # تحقق من حالة التحقق في جميع السجلات
#         verification_statuses = LastVerificationStatus.objects.all()
#         is_verified = False

#         for verification_status in verification_statuses:
#             if ( verification_status.device_id == device_ip and verification_status.hard_disk_info == hard_disk_info and verification_status.ram_info == ram_info and verification_status.is_verified==True):
#                 is_verified = verification_status.is_verified
#                 break

#         if not is_verified:
#             print("fffffffffffffffffffffffffffff")
#             # إذا لم يتم التحقق، إعادة التوجيه إلى شاشة التحقق
#             return redirect('verification_view')  # استبدل 'verification_view' باسم URL الخاص بشاشة التحقق

#         remember_me = form.cleaned_data.get('remember_me')

#         if not remember_me:
#             # تعيين انتهاء صلاحية الجلسة إلى 0 ثوان، بحيث يتم إغلاق الجلسة تلقائيًا بعد إغلاق المتصفح
#             self.request.session.set_expiry(0)
#             self.request.session.modified = True

#         return super(CustomLoginView, self).form_valid(form)



class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='users-profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})





#............................................





def login2(request):

    """
    Display the login form and handle the login action.
    """
    # username = None
    loggingrecord(request)
    if request.user.is_authenticated:
        username = request.user.username
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method=='POST':
        form=LoginForm(request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login_user(request,user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                messages.error(request, _('Error User Name or Password Please Try Agin'))
                return redirect(settings.LOGOUT_REDIRECT_URL)
        else:
            
            data= {'form' :form, 'username':username}
            return render(request,'login.html',data)
            

    else:
        form=LoginForm()
        
        data= {'form' :form, 'username':username}
        return render(request,'login.html',data)


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid form data. Please correct the errors.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def display_view(request,model_name,form_name,templet_name,title):
    data=model_name.objects.all()[:10]
    form=form_name()
    
    if request.method=="POST":
        form=form_name(request.POST or None)
        if form.is_valid():
            obj= form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            messages.success(request, _(' تم الاضافة بنجاح '))
            return redirect(request.get_full_path())

    context={
        'form':form,
        'data':data,
        'type_title': _(title),
            }
    return render(request,templet_name,context)


# @permission_required('auth.view_permission',raise_exception=True)
@login_required
def roles(request):
    if not request.user.has_perm('auth.view_permission'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        """ ADD group To premission Group 
        """
        request.session["top_menu"] = {"users": "active"}
        request.session["sub_menu"] = {"roles": "active"}

        return display_view(request,Group,GroupForm,'roles.html','Add New')

@login_required
def roles2(request):
    if not request.user.has_perm('auth.view_permission'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        """ ADD group To premission Group 
        """
        request.session["top_menu"] = {"users": "active"}
        request.session["sub_menu"] = {"roles": "active"}

        return display_view(request,Group,GroupForm,'groups.html','Add New')

from dynmic_table.models import TblSystem

from django import template

register = template.Library()


from django.contrib.contenttypes.models import ContentType

from dynmic_table.models import Modelnames
from dynmic_table.views import make_migrations_and_migrate,delete_custom_permissions_for_app,delete_custom_permissions_for_all_models, create_custom_permissions_for_all_models, create_custom_permissions_for_app

# @permission_required('users.view_permission',raise_exception=True)  
def group_premission1(request , pk ):
    if not request.user.has_perm('auth.change_permission'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        """ add and edite premission  Group name """
        # make_migrations_and_migrate('test2')
        # create_custom_permissions_for_app('test2')
        # create_custom_permissions_for_all_models()
        loggingrecord(request)
        group = get_object_or_404(Group, pk=pk)
        group_premission_ids=  group.permissions.all().values_list('id', flat=True)
        data_premission = Permission.objects.all()
        model_premission1 = Modelnames.objects.all()
        # قائمة النماذج التي لا ترغب في عرضها
        excluded_models = [
            'logentry', 'contenttype', 'session', 'compounditemunit', 
            'compounddatail', 'incomeorderdetails', 'rawmaterialsunits', 
            'outgoingorderdetails', 'orderdetail', 'modelschema', 'modelnames',
            'authgroup', 'authgrouppermissions', 'authpermission', 'authuser',
            'authusergroups', 'authuseruserpermissions', 'djangoadminlog',
            'djangocontenttype', 'djangomigrations', 'djangosession', 
            'dynamicmodelsfieldschema', 'dynamicmodelsmodelschema',
            'dynmictablecustomfield', 'dynmictabledynamicmodel',
            'dynmictablemodelnames', 'dynmictabletblsystem', 'fieldschema',
            'dynmictablecustmreportheader', 'dynmictablecustomuser',
            'dynmictablecustomusergroups', 'dynmictablecustomuseruserpermissions',
            'dynmictableuseraction', 'user_groups', 'group_permissions', 
            'customuser', 'customfield', 'user',
        ]

        # استبعاد النماذج باستخدام exclude
        model_premission = ContentType.objects.exclude(model__in=excluded_models)

        # متابعة الكود كما هو لتصنيف الصلاحيات وتوجيه البيانات إلى القالب
        basic_permissions = ['add', 'change', 'delete', 'view']
        categorized_permissions = {}

        for perm in data_premission:
            model_name = perm.content_type.model

            # التحقق إذا كان النموذج في القائمة المستبعدة
            if model_name not in excluded_models:
                if model_name not in categorized_permissions:
                    categorized_permissions[model_name] = {'basic': [], 'additional': []}

                # تصنيف الصلاحية
                for basic_perm in basic_permissions:
                    if perm.codename.startswith(basic_perm):
                        categorized_permissions[model_name]['basic'].append(perm)
                        break
                else:
                    categorized_permissions[model_name]['additional'].append(perm)
        
        if request.method == 'POST':
            if 'premission' not in request.POST.keys():
                group.permissions.clear()
                messages.success(request, _('تم التعديل بنجاح '))
                return HttpResponseRedirect(reverse('roles'))
            else:
                group.permissions.set(dict(request.POST)["premission"])
                messages.success(request, _('تم التعديل بنجاح'))
                return HttpResponseRedirect(reverse('roles'))
        context = {
            'group':group,
            'group_premission_ids':group_premission_ids,
            'data_premission':data_premission,
            'model_premission':model_premission,
            'model_premission1':model_premission1,
            'categorized_permissions': categorized_permissions,
            }
        return render(request, 'groupPremission.html', context)

@login_required 
def group_premission1(request, pk):
    if not request.user.has_perm('auth.change_permission'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        """ Add and edit permissions for a group """
        # make_migrations_and_migrate('test2')
        create_custom_permissions_for_app('test2')
        # delete_custom_permissions_for_all_models()
        # delete_custom_permissions_for_app('test2')
        loggingrecord(request)
        group = get_object_or_404(Group, pk=pk)
        group_premission_ids = group.permissions.all().values_list('id', flat=True)
        data_premission = Permission.objects.all()
        model_premission1 = Modelnames.objects.all()

        # قائمة النماذج التي لا ترغب في عرضها
        excluded_models = [
            'logentry', 'contenttype', 'session', 'compounditemunit', 
            'compounddatail', 'incomeorderdetails', 'rawmaterialsunits', 
            'outgoingorderdetails', 'orderdetail', 'modelschema', 'modelnames',
            'authgroup', 'authgrouppermissions', 'authpermission', 'authuser',
            'authusergroups', 'authuseruserpermissions', 'djangoadminlog',
            'djangocontenttype', 'djangomigrations', 'djangosession', 
            'dynamicmodelsfieldschema', 'dynamicmodelsmodelschema',
            'dynmictablecustomfield', 'dynmictabledynamicmodel',
            'dynmictablemodelnames', 'dynmictabletblsystem', 'fieldschema',
            'dynmictablecustmreportheader', 'dynmictablecustomuser',
            'dynmictablecustomusergroups', 'dynmictablecustomuseruserpermissions',
            'dynmictableuseraction', 'user_groups', 'group_permissions', 
            'customuser', 'customfield', 'user','fieldcondition','dynmictablefieldcondition',
        ]

        # استثناء النماذج الخاصة بتطبيق معين
        excluded_app_label = 'dynamic_models'  # استبدل بـ اسم التطبيق الذي ترغب في استبعاده
        excluded_models_from_app = ContentType.objects.filter(app_label=excluded_app_label).values_list('model', flat=True)

        # استثناء الصلاحيات الديناميكية التي يتم إنشاؤها بواسطة TblSystem
        tblsystem_content_type = ContentType.objects.get_for_model(TblSystem)
        all_permissions_for_tblsystem = Permission.objects.filter(content_type=tblsystem_content_type)

        # استخراج الصلاحيات الديناميكية فقط
        dynamic_permissions = all_permissions_for_tblsystem.exclude(
            codename__in=['add_tblsystem', 'change_tblsystem', 'delete_tblsystem', 'view_tblsystem']
        ).values_list('id', flat=True)

        # تصفية الصلاحيات لاستبعاد النماذج المحددة والنماذج من التطبيق والصلاحيات الديناميكية
        filtered_permissions = data_premission.exclude(
            content_type__model__in=excluded_models
        ).exclude(
            content_type__model__in=excluded_models_from_app
        ).exclude(
            id__in=dynamic_permissions
        )

        # متابعة الكود كما هو لتصنيف الصلاحيات وتوجيه البيانات إلى القالب
        basic_permissions = ['add', 'change', 'delete', 'view']
        categorized_permissions = {}

        for perm in filtered_permissions:
            model_name = perm.content_type.model

            if model_name not in categorized_permissions:
                categorized_permissions[model_name] = {'basic': [], 'additional': []}

            # تصنيف الصلاحية
            for basic_perm in basic_permissions:
                if perm.codename.startswith(basic_perm):
                    categorized_permissions[model_name]['basic'].append(perm)
                    break
            else:
                categorized_permissions[model_name]['additional'].append(perm)


        if request.method == 'POST':
            if 'premission' not in request.POST.keys():
                group.permissions.clear()
                messages.success(request, _('تم التعديل بنجاح '))
                return HttpResponseRedirect(reverse('roles'))
            else:
                group.permissions.set(dict(request.POST)["premission"])
                messages.success(request, _('تم التعديل بنجاح'))
                return HttpResponseRedirect(reverse('roles'))

        context = {
            'group': group,
            'group_premission_ids': group_premission_ids,
            'data_premission': data_premission,
            'model_premission1': model_premission1,
            'categorized_permissions': categorized_permissions,
        }

        return render(request, 'groupPremission.html', context)




@login_required
def group_premission(request, pk):
    if not request.user.has_perm('auth.change_permission'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        """ Add and edit permissions for a group """
        make_migrations_and_migrate('test2')
        create_custom_permissions_for_app('test2')
        loggingrecord(request)
        group = get_object_or_404(Group, pk=pk)
        group_premission_ids = group.permissions.all().values_list('id', flat=True)
        data_premission = Permission.objects.all()
        model_premission1 = Modelnames.objects.all()

        # قائمة النماذج التي لا ترغب في عرضها
        excluded_models = [
            'logentry', 'contenttype', 'session', 'compounditemunit', 
            'compounddatail', 'incomeorderdetails', 'rawmaterialsunits', 
            'outgoingorderdetails', 'orderdetail', 'modelschema', 'modelnames',
            'authgroup', 'authgrouppermissions', 'authpermission', 'authuser',
            'authusergroups', 'authuseruserpermissions', 'djangoadminlog',
            'djangocontenttype', 'djangomigrations', 'djangosession', 
            'dynamicmodelsfieldschema', 'dynamicmodelsmodelschema',
            'dynmictablecustomfield', 'dynmictabledynamicmodel',
            'dynmictablemodelnames', 'dynmictabletblsystem', 'fieldschema',
            'dynmictablecustmreportheader', 'dynmictablecustomuser',
            'dynmictablecustomusergroups', 'dynmictablecustomuseruserpermissions',
            'dynmictableuseraction', 'user_groups', 'group_permissions', 
            'customuser', 'customfield', 'user','fieldcondition','dynmictablefieldcondition',
        ]

        # استثناء النماذج الخاصة بتطبيق معين
        excluded_app_label = 'dynamic_models'
        excluded_models_from_app = ContentType.objects.filter(app_label=excluded_app_label).values_list('model', flat=True)

        # استثناء الصلاحيات الديناميكية التي يتم إنشاؤها بواسطة TblSystem
        # tblsystem_content_type = ContentType.objects.get_for_model(TblSystem)
        # all_permissions_for_tblsystem = Permission.objects.filter(content_type=tblsystem_content_type)

        # # استخراج الصلاحيات الديناميكية فقط
        # dynamic_permissions = all_permissions_for_tblsystem.exclude(
        #     codename__in=['add_tblsystem', 'change_tblsystem', 'delete_tblsystem', 'view_tblsystem']
        # ).values_list('id', flat=True)

        # تصفية الصلاحيات لاستبعاد النماذج المحددة والنماذج من التطبيق والصلاحيات الديناميكية
        filtered_permissions = data_premission.exclude(
            content_type__model__in=excluded_models
        ).exclude(
            content_type__model__in=excluded_models_from_app
        )
        # .exclude(
        #     id__in=dynamic_permissions
        # )

        # تصنيف الصلاحيات
        basic_permissions = ['add', 'change', 'delete', 'view']
        categorized_permissions = {}

        for perm in filtered_permissions:
            model_name = perm.content_type.model

            if model_name not in categorized_permissions:
                categorized_permissions[model_name] = {'basic': [], 'additional': []}

            # تصنيف الصلاحية
            for basic_perm in basic_permissions:
                if perm.codename.startswith(basic_perm):
                    categorized_permissions[model_name]['basic'].append(perm)
                    break
            else:
                categorized_permissions[model_name]['additional'].append(perm)

        if request.method == 'POST':
            if 'premission' not in request.POST.keys():
                messages.success(request, _('تم التعديل بنجاح '))
                return HttpResponseRedirect(reverse('roles'))
            else:
                selected_permissions = set(map(int, dict(request.POST)["premission"]))
                current_permissions = set(group.permissions.values_list('id', flat=True))
                
                # الصلاحيات التي يجب إضافتها
                permissions_to_add = selected_permissions - current_permissions
                
                # الصلاحيات التي يجب إزالتها
                permissions_to_remove = current_permissions - selected_permissions
                
                # تحديث الصلاحيات
                group.permissions.add(*permissions_to_add)
                group.permissions.remove(*permissions_to_remove)
                
                messages.success(request, _('تم التعديل بنجاح'))
                return HttpResponseRedirect(reverse('roles'))

        context = {
            'group': group,
            'group_premission_ids': group_premission_ids,
            'data_premission': data_premission,
            'model_premission1': model_premission1,
            'categorized_permissions': categorized_permissions,
        }

        return render(request, 'groupPremission.html', context)

@login_required
def group_premission2(request, pk):
    if not request.user.has_perm('auth.change_permission'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        group = get_object_or_404(Group, pk=pk)
        tblsystem = ContentType.objects.get_for_model(TblSystem)
        group_permission_ids = group.permissions.all().values_list('id', flat=True)
        data_permission = Permission.objects.filter(content_type=tblsystem)
        systems = TblSystem.objects.all()
        
        if request.method == 'POST':
            selected_permissions = set(map(int, dict(request.POST).get("permission", [])))
            
            # الصلاحيات الحالية المرتبطة بالمجموعة
            current_permissions = set(group.permissions.values_list('id', flat=True))
            
            # الصلاحيات الخاصة بـ TblSystem فقط
            tblsystem_permissions = set(Permission.objects.filter(content_type=tblsystem).values_list('id', flat=True))
            
            # الصلاحيات الحالية الخاصة بـ TblSystem
            current_tblsystem_permissions = current_permissions & tblsystem_permissions
            
            # الصلاحيات التي يجب إضافتها
            permissions_to_add = selected_permissions - current_tblsystem_permissions
            
            # الصلاحيات التي يجب إزالتها (ضمن صلاحيات TblSystem فقط)
            permissions_to_remove = current_tblsystem_permissions - selected_permissions
            
            # تحديث الصلاحيات الخاصة بـ TblSystem فقط
            group.permissions.add(*permissions_to_add)
            group.permissions.remove(*permissions_to_remove)
            
            messages.success(request, _('تم التعديل بنجاح'))
            return HttpResponseRedirect(reverse('roles2'))

        context = {
            'group': group,
            'group_permission_ids': group_permission_ids,
            'data_permission': data_permission,
            'systems': systems,
            'tblsystem': tblsystem,
        }
        return render(request, 'systemspermissions.html', context)


def roles_edit(request , pk ):
    if not request.user.has_perm('auth.change_permission'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        """ Edit premission Group name"""
        request.session["top_menu"] = {"users": "active"}
        request.session["sub_menu"] = {"roles": "active"}
        loggingrecord(request)
        group = get_object_or_404(Group, pk=pk)
        data = Group.objects.all()
        form = GroupForm(request.POST or None, instance=group)
        if request.method =='POST':
            if form.is_valid() :
                form.save()
                messages.success(request, _('تم التعديل بنجاج'))
                return HttpResponseRedirect(reverse('roles'))
            
        context = {'form': form , 'data':data , 'type_title': _('Edit')}
        return render(request, 'roles.html', context)

def delete_role(request , pk):
    if not request.user.has_perm('auth.delete_permission'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        Group.objects.filter(id=pk).delete()
        messages.success(request, _('تم الحذف بنجاح'))
        return HttpResponseRedirect(reverse('roles'))






# @login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # استبدل 'home' بالصفحة التي تريد إعادة التوجيه إليها


# @permission_required('users.view_user',raise_exception=True) 
# @login_required  
# def users(request):
#     if not request.user.has_perm('auth.view_user'):
#         messages.error(request, 'لايوجد لديك صلاحية')
#         return redirect('confirm_perm')
#     else:
#         loggingrecord(request)
#         request.session["top_menu"] = {"users": "active"}
#         request.session["sub_menu"] = {"users": "active"}
#         data=User.objects.all().order_by('-id')
#         form=usersForm()
#         if request.method=="POST":
#             form=usersForm(request.POST or None)
#             if form.is_valid():
#                 obj= form.save(commit=False)
#                 obj.password = make_password(request.POST['password'])
#                 obj.save()
#                 user_id = User.objects.get(id=obj.id)
#                 # UserTaskPremission.objects.create(user_task_prem = user_id)
#                 # user_per_task = UserTaskPremission.objects.create()
#                 # user_id = User.objects.get(id=obj.id)
#                 # user_per_task.user_task_prem = user_id
#                 # user_per_task.save()
#                 if 'groups' in request.POST:
#                     groups = request.POST.getlist('groups')
#                     obj.groups.set(groups)
#                 messages.success(request, _('تم الاضافة بنجاح '))
#                 return redirect(request.get_full_path())

#         all_groups= Group.objects.all()        
#         context={
#             'form':form,
#             'type_title':_('Add New User'),
#             'data':data,
#             'title': _('title'),
#             'all_groups': all_groups
#         }
#         return render(request,'users.html',context)

@login_required  
def users(request):
    if not request.user.has_perm('auth.view_user'):
        messages.error(request, 'لا يوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        loggingrecord(request)
        request.session["top_menu"] = {"users": "active"}
        request.session["sub_menu"] = {"users": "active"}
        
        data = User.objects.all().order_by('-id')
        form = UserForm()
        
        if request.method == "POST":
            form = UserForm(request.POST or None)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.password = make_password(request.POST['password'])
                obj.save()
                user_id = User.objects.get(id=obj.id)
                # UserTaskPremission.objects.create(user_task_prem=user_id)
                
                # تحقق مما إذا كانت هناك مجموعات في POST
                if 'groups' in request.POST:
                    # تحويل مجموعة المجموعات من نص إلى قائمة
                    groups = request.POST.getlist('groups')
                    # ضبط المجموعات للمستخدم
                    obj.groups.set(groups)

                form_data = form.cleaned_data
                # نقوم بتحويل form_data إلى قائمة تحتوي على القيم فقط دون أسماء الحقول
                details = ', '.join(str(value) for value in form_data.values())
                UserAction.objects.create(user=request.user,action="إظافة مستخدم",model_name='المستخدمين', details=details)
                
                messages.success(request, _('تم الإضافة بنجاح '))
                return redirect(request.get_full_path())
        all_groups = Group.objects.all()
        context={

            'form':form,
            'type_title':_('Add New User'),
            'data':data,
            'all_groups': all_groups,
            'title': _('title'),
        }
        return render(request,'users.html',context)




def users_edit_password(request , pk ):
    """ Edit user data"""
    if not request.user.has_perm('auth.change_user'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        loggingrecord(request)
        user_data = get_object_or_404(User, pk=pk)
        data = User.objects.all()
        form = usersFormPassword(request.POST or None, instance=user_data)
        if request.method =='POST':
            if form.is_valid() :
                obj= form.save(commit=False)
                obj.password = make_password(request.POST['password'])
                obj.save()

                form_data = form.cleaned_data
                # نقوم بتحويل form_data إلى قائمة تحتوي على القيم فقط دون أسماء الحقول
                details = ', '.join(str(value) for value in form_data.values())
                UserAction.objects.create(user=request.user,action="تعديل كلمة المرور",model_name='المستخدمين', details=details)
                
                messages.success(request, _('تم التعديل بنجاح'))
                return HttpResponseRedirect(reverse('users'))
            
        context = {'form': form , 'data':data,  'type_title':_('تغيير كلمة المرور'),
                }
        return render(request, 'users_edit_password.html', context)

    
# @permission_required('users.change_user',raise_exception=True) 
def users_edit(request , pk ):
    """ Edit user data"""
    if not request.user.has_perm('auth.change_user'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        loggingrecord(request)
        user_data = get_object_or_404(User, pk=pk)
        data = User.objects.all()
        form = usersFormEdit(request.POST or None, instance=user_data)
        if request.method =='POST':
            if form.is_valid() :
                obj= form.save(commit=False)
                obj.save()
                form_data = form.cleaned_data

                # نقوم بتحويل form_data إلى قائمة تحتوي على القيم فقط دون أسماء الحقول
                details = ', '.join(str(value) for value in form_data.values())
                UserAction.objects.create(user=request.user,action="تعديل مستخدم",model_name='المستخدمين', details=details)
            
                messages.success(request, _('تم التعديل بنجاح'))
                return HttpResponseRedirect(reverse('users'))
            
        context = {'form': form , 'data':data, 'type_title':_('تعيل بيانات المستخدم'),
                        }
        return render(request, 'users1.html', context)


# @permission_required('users.change_group',raise_exception=True) 
def users_edit_group(request , pk ):
    """ Edit user data"""
    if not request.user.has_perm('auth.change_user'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        loggingrecord(request)
        user_data = get_object_or_404(User, pk=pk)
        data = User.objects.all()
        form = usersFormGroupEdit(request.POST or None, instance=user_data)
        if request.method =='POST':
            if form.is_valid() :
                obj= form.save(commit=False)
                if 'groups' in request.POST.keys():
                    obj.groups.set(dict(request.POST)['groups'])
                else:
                    obj.groups.clear()
                obj.save()
                form_data = form.cleaned_data
                # نقوم بتحويل form_data إلى قائمة تحتوي على القيم فقط دون أسماء الحقول
                details = ', '.join(str(value) for value in form_data.values())
                UserAction.objects.create(user=request.user,action="تعديل مجموعة مستخدم",model_name='المستخدمين', details=details)
                
            
                messages.success(request, _('تم التحديث بنجاح '))
                return HttpResponseRedirect(reverse('users'))
            
        context = {'form': form , 'data':data , 'type_title':_('تعديل صلاحيات المستخدم'),
                }
        return render(request, 'edit_group.html', context)
# @permission_required('users.delete_user',raise_exception=True) 
def delete_user(request , pk):
    """ Delete User
    Arguments:
        request , PK
    """
    if not request.user.has_perm('auth.delete_user'):
        messages.error(request, 'لايوجد لديك صلاحية')
        return redirect('confirm_perm')
    else:
        loggingrecord(request)
        try:
            if User.objects.filter(id=pk).exists(): 
                User.objects.filter(id=pk).delete()
                messages.success(request,_("تم الحذف بنجاح"))
                return HttpResponseRedirect(reverse('users'))
        except ProtectedError:
            messages.error(request,_("لايمكن حذفة!!"))
            return HttpResponseRedirect(reverse('users'))


def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = UserEditeForm(instance=user)
    return JsonResponse({'form_html': form.as_p()})

def get_user_password(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = UserPasswordForm(instance=user)
    return JsonResponse({'form1_html': form.as_p()}) 

def edit_user(request, user_id):
    if request.method == "POST":
        # user_id = request.POST.get('user_id')
        if user_id is None:
            messages.error(request, 'لم يتم العثور على معرف المستخدم.')
            return redirect('users')
        user = get_object_or_404(User, id=user_id)
        form = UserEditeForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            # نقوم بتحويل form_data إلى قائمة تحتوي على القيم فقط دون أسماء الحقول
            form_data = form.cleaned_data    
            details = ', '.join(str(value) for value in form_data.values())
            UserAction.objects.create(user=request.user,action="تعديل مستخدم",model_name='المستخدمين', details=details)
            
            messages.success(request, 'تم تعديل المستخدم بنجاح.')
            return redirect('users')
        else:
            messages.error(request, 'حدث خطأ أثناء تحديث المستخدم.')
    return redirect('users')

def edit_password_user(request, user_id):
    if request.method == "POST":
        # user_id = request.POST.get('user_id')
        if user_id is None:
            messages.error(request, 'لم يتم العثور على معرف المستخدم.')
            return redirect('users')
        user = get_object_or_404(User, id=user_id)
        form = UserPasswordForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data
            # نقوم بتحويل form_data إلى قائمة تحتوي على القيم فقط دون أسماء الحقول
            details = ', '.join(str(value) for value in form_data.values())
            UserAction.objects.create(user=request.user,action="تعديل كلمة المرور",model_name='المستخدمين', details=user)
                
            messages.success(request, 'تم تعديل كلمةالمرور بنجاح.')
            return redirect('users')
        else:
            messages.error(request, 'حدث خطأ أثناء تعديل كلمةالمرور .')
    return redirect('users')


from django.forms.models import model_to_dict

from dynmic_table.models import UserAction

def delete_user1(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
   # تحويل الكائن إلى قاموس من الحقول
    item_dict = model_to_dict(user)

    # إنشاء تفاصيل الحذف باستخدام القاموس
    details = ", ".join([f"{value}" for key, value in item_dict.items()])

    form.save()
    UserAction.objects.create(user=request.user,action=" حذف مستخدم",model_name='المستخدمين', details=details)
    messages.success(request, 'تم حذف المستخدم بنجاح.')
    return redirect('users')

