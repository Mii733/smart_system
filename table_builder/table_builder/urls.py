"""
URL configuration for table_builder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include
# from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView, login
# from users.forms import LoginForm
from django.contrib.auth import views as auth_views 
from django.urls import include, re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('dynmic_table.urls')),
    path('', include('users.urls')),
    # path('', include('accounts.urls')),

    # path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
    #                                        authentication_form=LoginForm), name='login'),
    
    # path('logout/', auth_views.LogoutView.as_view(next_page='login',template_name='users/login.html'), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login',template_name='users/login.html'), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    # path('password-reset-confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    #      name='password_reset_confirm'),

    # path('password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
    #      name='password_reset_complete'),

    # path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    # url(r'^oauth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







# from django.contrib import admin

# from django.urls import  path, include
# from django.urls import include, re_path as url
# from django.conf import settings
# from django.conf.urls.static import static

# from django.contrib.auth import views as auth_views
# from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView, login

# from users.forms import LoginForm

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('', include('operations.urls')),
#     path('', include('configrate.urls')),
#     path('', include('taskapp.urls')),
#     # path('', include('input.urls')),
#     # path('', include('purchases.urls')),
#     path('', include('users.urls')),

#      # path('login',login,name='login' ),
#     path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
#                                            authentication_form=LoginForm), name='login'),

#     path('logout/', auth_views.LogoutView.as_view(next_page='login',template_name='users/login.html'), name='logout'),

#     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

#     path('password-reset-confirm/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
#          name='password_reset_confirm'),

#     path('password-reset-complete/',
#          auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
#          name='password_reset_complete'),

#     path('password-change/', ChangePasswordView.as_view(), name='password_change'),

#     url(r'^oauth/', include('social_django.urls', namespace='social')),

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls.static import static

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG: #يستخدم هذا التضمين لإظهار الملفات من صور وفيديو في المتصفح من قاعدة البيانات
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)