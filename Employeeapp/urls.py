from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('register/',views.register),
    path('emp_register/',views.emp_register),
    path('login/',views.login),
    path('logout/',views.logout),


    path('admin_home/',views.admin_home),
    path('admin_view_cmpny/',views.admin_view_cmpny),
    path('admin_view_emp/',views.admin_view_emp),
    path('admin_delete_cmpny/',views.admin_delete_cmpny),
    path('admin_delete_emp/',views.admin_delete_emp),
    path('admin_edit_cmpny/',views.admin_edit_cmpny),
    path('admin_edit_emp/',views.admin_edit_emp),

    path('cmpny_home/',views.cmpny_home),
    path('cmpny_profile/',views.cmpny_profile),
    path('cmpny_employee/',views.cmpny_employee),
    
    path('emp_home/',views.emp_home),
    path('emp_profile/',views.emp_profile),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)