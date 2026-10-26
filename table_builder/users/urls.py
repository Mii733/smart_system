from django.urls import path
from django.contrib.auth import views as auth_views



from .views import login, roles2,group_premission2,edit_user,get_user,delete_user1,edit_password_user,get_user_password, logout_view,confirm_perm, home,home1, home2, home22,index_operation, index_input,  home3, home4, RegisterView, roles, group_premission, delete_role, roles_edit, users, delete_user, users_edit, users_edit_group, users_edit_password

urlpatterns = [
    # path('',views.index, name='index'),

    path('home/', home, name='home'),
    # path('login/', login, name='login'),
    path('', login, name='login'),
    path('logout/',logout_view , name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('home1', home1, name='home1'),
    path('home2', home2, name='home2'),
    path('home3', home3, name='home3'),
    path('home4', home4, name='home4'),
    path('home22', home22, name='home22'),
    path('index_input', index_input, name='index_input'),
    path('index_operation', index_operation, name='index_operation'),
    # path('profile/', profile, name='users-profile'),
    path('roles/',roles,name='roles'),
    path('roles2/',roles2,name='roles2'),
    path('premission/<int:pk>',group_premission,name='premission'),
    path('premission2/<int:pk>',group_premission2,name='premission2'),
    # path('create_and_apply_permission/', create_and_apply_permission,name='create_and_apply_permission'),
    path('roles/edit/<int:pk>', roles_edit,name='rolesEdit'),
    # path('access_denied', access_denied , name='access_denied'),
    path('delete/role/<int:pk>', delete_role , name='delete_role'),

    path('users/',users , name='users'),
    path('users/confirm_perm/',confirm_perm , name='confirm_perm'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login',template_name='users/login.html'), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('logout/',logout_view , name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login',template_name='users/templates/login.html'), name='logout'),


    path('users/edit/<int:pk>',users_edit,name='users_edit'),
    path('users/edit_group/<int:pk>',users_edit_group,name='users_edit_group'),
    path('users_edit_password/<int:pk>',users_edit_password,name='users_edit_password'),
    path('delete_user/<int:pk>',delete_user,name='delete_user'),


    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),  # لتعريف URL لتحديث بيانات المستخدم
    path('get_user/<int:user_id>/', get_user, name='get_user'),  # تعديل بيانات المستخدم
    path('delete_user1/<int:user_id>/', delete_user1, name='delete_user1'), 

    path('edit_password_user/<int:user_id>/', edit_password_user, name='edit_password_user'),
    path('get_user_password/<int:user_id>/', get_user_password, name='get_user_password'), 




]
