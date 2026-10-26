







from django.urls import path
from . import views

from .views import index
from django.contrib.auth import views as auth_views


# from .models import create_custom_permissions

# create_custom_permissions()

urlpatterns = [
    path('index/',views.index, name='index'),
    path('baseApp/', views.base, name='base_app'),
    path('createModels/<int:sys_name_id>/', views.createModels, name='create_models'),
    path('createModels', views.createModels, name='create_models'),
    path('addModelEntries', views.addModelEntries, name='add_entries'),
    # path('showObjectLists', views.showObjectLists, name='show_objects'),
    path('get_tables', views.get_tables, name='get_tables'),
    path('dynamic-form/<str:model_name>/', views.dynamic_form, name='dynamic_form'),
    path('dynamic_form', views.dynamic_form, name='dynamic_form'),
    # path('get_table_fields', views.get_table_fields, name='get_table_fields'),
    path('my_view1', views.my_view1, name='my_view1'),
    path('my_view', views.my_view, name='my_view'),
    path('get_restricted_values/', views.get_restricted_values, name='get_restricted_values'),
    path('get_selected_field', views.get_selected_field, name='get_selected_field'),
    path('my_view2/<str:model_name>/', views.my_view2, name='my_view2'),
    path('get_fields/<str:table_name>/', views.get_fields, name='get_fields'),
    path('get_fields/', views.get_fields, name='get_fields'),
    path('get_field_values/', views.get_field_values, name='get_field_values'),
    path('get_field_values2/', views.get_field_values2, name='get_field_values2'),
    path('add_field/<str:model_name>/<int:sys_name_id>/', views.add_field, name='add_field'),
    path('manage_models/<str:model_name>/<int:sys_name_id>/', views.manage_models, name='manage_models'),
    path('add_related_field2/<str:model_name>/', views.add_related_field2, name='add_related_field2'),
    path('create_subproject/', views.create_subproject, name='create_subproject'),
    path('subproject/<int:sys_name_id>/', views.subproject_detail, name='subproject_detail'),
    path('subprojects_edit/<int:sys_name_id>/', views.subprojects_edit, name='subprojects_edit'),
    path('subprojects_delete/<int:sys_name_id>/', views.subprojects_delete, name='subprojects_delete'),
#     path('subproject/<int:sys_name_id>/create_table/', views.create_table, name='create_table'),
#     # path('create/', views.create_dynamic_model, name='create_dynamic_model'),
    # path('create_table/', views.create_table, name='create_table'),
    # path('create_dynamic_model/', views.create_dynamic_model, name='create_dynamic_model'),
# #     path('edit/<int:id>/', edit, name='edit'),
# #     path('delete/<int:id>/', delete, name='delete'),
# #     path('view_interface/<int:interface_id>/', view_interface, name='view_interface'),
#     path('create_table/', views.create_table, name='create_table'),
# #     path('table_list/', table_list, name='table_list'),
# #     path('table_detail/<int:table_id>/', table_detail, name='table_detail'),
# #     path('table_form_view/<int:table_name>/', table_form_view, name='table_form_view'),
    path('display_data/<str:id>/<int:sys_name_id>/', views.display_data, name='display_data'),
    # path('display_form/<str:model_name>/', views.display_form, name='display_form'),
# #     path('data_form_view/', data_form_view, name='data_form_view'),
    # path('save_data/', views.save_data, name='save_data'),
# #     path('create_new_fields/', views.create_new_fields, name='create_new_fields'),
#     path('data_list/', views.data_list, name='data_list'),
#     # path('display_table/', views.display_table, name='display_table'),
    path('formset/<str:model_name>/<int:sys_name_id>/', views.formset_view, name='formset_view'),
    # path('formset_view2/<str:model_name>/', views.formset_view2, name='formset_view2'),
    # path('formset_view3/<str:model_name>/<file:excel_file>/', views.formset_view3, name='formset_view3'),
    # path('formset_view3/<str:model_name>/<path:excel_file>/', views.formset_view3, name='formset_view3'),
    path('import_data/<str:model_name>/<str:excel_data>/<int:sys_name_id>/', views.import_data, name='import_data'),
    # path('api_service/', views.api_service, name='api_service'),
    # path('upload_file3/<str:model_name>/', views.upload_file3, name='upload_file3'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    # path('upload_file2/', views.upload_file2, name='upload_file2'),
    path('export/<str:model_name>/<int:sys_name_id>/', views.export_empty_excel, name='export_empty_excel'),
    # path('import_data_from_excel/', views.import_data_from_excel, name='import_data_from_excel'),
    # path('import_data_from_excel2/', views.import_data_from_excel2, name='import_data_from_excel2'),
# #     # path('edit_data/<int:pk>/', views.edit_data, name='edit_data'),
    # path('edit_data/<int:id>/', views.edit_data, name='edit_data'),
    path('add_data/<str:model_name>/<int:sys_name_id>/', views.add_data, name='add_data'),
    path('edit_datas/<str:model_name>/<str:row_id>/', views.edit_data, name='edit_data'),
    path('edit_data/<str:model_name>/<str:row_id>/<int:sys_name_id>/', views.edit_data, name='edit_data'),
    path('show_data/<str:model_name>/<str:row_id>/<int:sys_name_id>/', views.show_data, name='show_data'),
    path('delete_data/<str:model_name>/<str:row_id>/<int:sys_name_id>/', views.delete_data, name='delete_data'),
    path('edit_field/<str:model_name>/<str:field_id>/<int:sys_name_id>/', views.edit_field, name='edit_field'),
    path('update_table/<str:model_id>/<int:sys_name_id>/', views.update_table, name='update_table'),
    path('update_field/<str:field_id>/<str:model_name>/<int:sys_name_id>/', views.update_field, name='update_field'),
    path('add_condition/<str:model_name>/<int:sys_name_id>/', views.add_condition, name='add_condition'),
    path('condition_list/<str:model_name>/<int:sys_name_id>/', views.condition_list, name='condition_list'),
    path('delete_field/<str:model_name>/<str:field_name>/<int:sys_name_id>/', views.delete_field, name='delete_field'),
    path('drop_column/<str:model_name>/', views.drop_column, name='drop_column'),
    path('delete_model/<str:model_name>/<int:sys_name_id>/', views.delete_model, name='delete_model'),
    path('search_my_model/', views.search_my_model, name='search_my_model'),
    path('export-excel/<str:model_name>/<int:sys_name_id>/', views.export_to_excel, name='export_to_excel'),
# #     path('edit_data/<str:column_name>/<str:field_value>/<int:id>/', views.edit_data, name='edit_data')

    # path('user_login/', views.user_login, name='user_login'),
    path('add_user/', views.add_user, name='add_user'),
    path('system_manage/', views.system_manage, name='system_manage'),
    path('manage_user/', views.manage_user, name='manage_user'),
    # path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
    path('confirm_perm/',views.confirm_perm , name='confirm_perm'),
    path('subprojects_manage/',views.subprojects_manage , name='subprojects_manage'),
    path('fields/<str:table_name>/', views.display_fields, name='display_fields'),
    path('report_view/<str:table_name>/<int:sys_name_id>/', views.report_view, name='report_view'),
    path('user_action/', views.user_action, name='user_action'),
    path('custm_report_header_edit/', views.custm_report_header_edit, name='custm_report_header_edit'),
    # path('manage_user/<int:user_id>/', CustomUserDetailView.as_view(), name='user_detail'),
    # path('logout1/', auth_views.LogoutView.as_view(next_page='login',template_name='users/login.html'), name='logout1'),
    # path('logout1/',views.logout_view , name='logout1'),
    # path('create_and_apply_permission/', views.create_and_apply_permission,name='create_and_apply_permission'),



]